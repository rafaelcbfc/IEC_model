#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:03:06 2020

@author: rafael
"""

import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import Hofstede
import random
import numpy as np
import pandas as pd
from scipy.stats import uniform

A, B, C, D, E, F , G = [], [], [], [], [], [], []

pool_countries = ["AUS", "BRA", "IRA", "JPN", "NLD", "USA"]
country =pool_countries[1]
discount_rate = Hofstede.BRA_discount_rate
gridtariff = Hofstede.BRA_gridtariff
solar_implement_Costs = Hofstede.BRA_solarCosts  
wind_implement_Costs = Hofstede.BRA_windCosts
solar_OM = Hofstede.BRA_solar_OM
wind_OM = Hofstede.BRA_wind_OM
sunshine = Hofstede.BRA_sunshine
wind_dist = Hofstede.BRA_wind_dist
 

wind_threshold = 5000 #in KW, minimum value to make it a possibility for wind energy production - https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
depreciation_period = 20

pool_financial_investments = ["feed-in-tariff", "tax-incentive", "tradable-certificates"]
financial_investment = 0 #pool_financial_investment[1]
if financial_investment == "tax-incentive":
    solar_implement_Costs = solar_implement_Costs * 0.6
    wind_implement_Costs = wind_implement_Costs * 0.6


def cbaCalc(me, peer = None):
    rev00, rev11, rev12, rev21, rev22, rev31, rev32, cos10, cos20, cos30 = [], [], [], [], [], [], [], [], [], []
    annual_demand = me.energy
    if peer != None:
        annual_demand = (me.energy + peer.energy)
    else:
        annual_demand = me.energy 
    
    #Case 0 - Grid energy
    r00 = gridtariff * annual_demand
    
    for i in range(depreciation_period):
        rev00.append(r00)
        
    Baseline_cost = np.npv(discount_rate, rev00)
    
    #Case 1 - All solar
    solar_energy1 = annual_demand
    installation_solar1 = solar_energy1 / sunshine
    investment_solar1 = installation_solar1 * solar_implement_Costs
    OM_solar1 = solar_OM * (investment_solar1/(solar_energy1 * depreciation_period)) * solar_energy1
    LCOE_solar1 = (investment_solar1 + OM_solar1 * depreciation_period)/(solar_energy1 * depreciation_period) 
    
    r11 = (gridtariff - LCOE_solar1) * solar_energy1 * 1.1 #Sell energy
    r12 = gridtariff * solar_energy1                       #Produce energy
    c10=  OM_solar1
    
    for i in range(depreciation_period):
        rev11.append(r11)
        rev12.append(r12)
        cos10.append(c10)

    revenue11 = np.npv(discount_rate, rev11)
    revenue12 = np.npv(discount_rate, rev12)
    costs10 = investment_solar1 + np.npv(discount_rate, cos10)
    
    NPV11 = revenue11-costs10
    NPV12 = revenue12-costs10
    margin11 = ((revenue11 - costs10)/revenue11)*100
    margin12 = ((revenue12 - costs10)/revenue12)*100
    
    #Case 2 - All wind
    wind_energy2 = annual_demand
    installation_wind2 = wind_energy2 / wind_dist
    investment_wind2 = installation_wind2 * wind_implement_Costs
    OM_wind2 = wind_OM * wind_energy2
    LCOE_wind2 = (investment_wind2 + OM_wind2 * depreciation_period)/(wind_energy2 * depreciation_period) 

    r21 = (gridtariff - LCOE_wind2) * wind_energy2 * 1.1 #Sell energy
    r22 = gridtariff * wind_energy2                      #Produce energy
    c20 =  OM_wind2
    
    for i in range(depreciation_period):
        rev21.append(r21)
        rev22.append(r22)
        cos20.append(c20)

    revenue21 = np.npv(discount_rate, rev21)
    revenue22 = np.npv(discount_rate, rev22)
    costs20 = investment_wind2 + np.npv(discount_rate, cos20)
    
    NPV21 = revenue21 - costs20
    NPV22 = revenue22-costs20
    margin21 = ((revenue21 - costs20)/revenue21)*100
    margin22 = ((revenue22 - costs20)/revenue22)*100
    
    
    #Case 3- Mixed sources
    #wind
    wind_energy3 = (int(annual_demand/wind_threshold)*wind_threshold)
    installation_wind3 = wind_energy3 / wind_dist
    investment_wind3 = installation_wind3 * wind_implement_Costs
    OM_wind3 = wind_OM * wind_energy3
    try:
        LCOE_wind3 = (investment_wind3 + OM_wind3 * depreciation_period)/(wind_energy3 * depreciation_period)
    except: 
        LCOE_wind3 = 0
    
    #Solar
    solar_energy3 = annual_demand % wind_threshold
    installation_solar3 = solar_energy3 / sunshine
    investment_solar3 = installation_solar3 * solar_implement_Costs
    OM_solar3 = solar_OM * (investment_solar3/(solar_energy3 * depreciation_period)) * solar_energy3
    try:
        LCOE_solar3 = (investment_solar3 + OM_solar3 * depreciation_period)/(solar_energy3 * depreciation_period) 
    except:
        LCOE_solar3 = 0
        
    r31 = ((gridtariff - LCOE_solar3) * solar_energy3 + (gridtariff - LCOE_wind3) * wind_energy3) * 1.1   # Sell energy
    r32 = gridtariff * annual_demand                                                                      #Produce energy 
    c30 =  OM_wind3 + OM_solar3 
    
    for i in range(depreciation_period):
        rev31.append(r31)
        rev32.append(r32)
        cos30.append(c30)

    revenue31 = np.npv(discount_rate, rev31)
    revenue32 = np.npv(discount_rate, rev32)
    costs30 = (investment_solar3 + investment_wind3) + np.npv(discount_rate, cos30)
    
    NPV31 = revenue31 - costs30
    NPV32 = revenue32-costs30
    margin31 = ((revenue31 - costs30)/revenue31)*100
    margin32 = ((revenue32 - costs30)/revenue32)*100
 
    A.append(NPV11)
    B.append(NPV12)
    C.append(NPV21)
    D.append(NPV22)
    E.append(NPV31)
    F.append(NPV32)
    G.append(Baseline_cost)   

    #1st evaluation => is grid energy more expensive than construct RE?
    costs = [costs10, costs20, costs30]
    for cost in costs:
        if Baseline_cost >= cost:
            print("RE")
    
    #2nd evaluation => I am going for renewable, but is it better to produce to my self or sell?
    produce = [NPV12, NPV22, NPV32]
    sell = [NPV11, NPV21, NPV31]

    if max(produce) > max(sell):
        print("produce")
    
    else:
        print("sell")



NPV = 0

if NPV > 0:
       me.CBA = "favorable"
if NPV <= 0:
    me.CBA = "unfavorable"
if peer == None:
   return me.CBA      
if peer != None:
   me.CBAp = me.CBA
   return me.CBAp









A = pd.Series(A)    
B = pd.Series(B)
C = pd.Series(C)
D = pd.Series(D)
E = pd.Series(E)
F = pd.Series(F)
G = pd.Series(G)

z1 = sum(A)
z2 = sum(B)
z3 = sum(C)
z4 = sum(D)
z5 = sum(E)
z6 = sum(F)
z7 = sum(G)


df = pd.DataFrame()
df = df.append(A, ignore_index=True)
df = df.append(B, ignore_index = True)
df = df.append(C, ignore_index = True)
df = df.append(D, ignore_index = True)
df = df.append(E, ignore_index = True)
df = df.append(F, ignore_index = True)
df = df.T


"""
 
 if NPV_sell < 0:
     print('NPV_sell ' + i)
     print(NPV_sell)
 if NPV_generate < 0:
     print('NPV_generate ' + i)
     print(NPV_generate) 
 if margin_sell < 0: 
     print('margin sell ' + i)
     print(margin_sell)
 if margin_generate < 0:
     print('margin generate ' + i)
     print(margin_generate)  

"""




        
def projectSelector(self): 
        rev = []
        cos = [] 
        self.project_cost = 0
        annual_demand = self.energy *1.1
        
        #wind
        self.wind_energy = (int(annual_demand/wind_threshold)*wind_threshold)
        installation_wind = self.wind_energy / wind_dist
        investment_wind = installation_wind * wind_implement_Costs
        OM_wind = wind_OM * self.wind_energy
        
        #Solar
        self.solar_energy = annual_demand % wind_threshold
        installation_solar = self.solar_energy / sunshine
        investment_solar = installation_solar * solar_implement_Costs
        if self.solar_energy > 0:
            solar_tariff =  (investment_solar/(self.solar_energy * depreciation_period)) 
        if self.solar_energy == 0: 
            solar_tariff = 0
        OM_solar = solar_OM * solar_tariff * self.solar_energy
       
        try:
            self.LCOE_solar = (investment_solar + OM_solar * depreciation_period)/(self.solar_energy * depreciation_period) 
        except:
            self.LCOE_solar = 0
        try:
            self.LCOE_wind = (investment_wind + OM_wind * depreciation_period)/(self.wind_energy * depreciation_period) 
        except:
            self.LCOE_wind = 0
        self.project_tariff = (self.LCOE_solar + self.LCOE_wind) / 2
        
        #margin calculation - strategy 0
        if self.strategy == 0:
            r = annual_demand * gridtariff
            c =  OM_wind + OM_solar + (investment_solar + investment_wind)/depreciation_period
            
        #margin calculation - strategy 1
        if self.strategy == 1:
            r = (self.LCOE_solar * self.solar_energy + self.LCOE_wind * self.wind_energy) * 1.1
            c = OM_wind + OM_solar + (investment_solar + investment_wind)/depreciation_period
            
        for i in range(depreciation_period):
            rev.append(r)
            cos.append(c)
            
        project_revenue = np.npv(discount_rate, rev)
        self.project_cost = np.npv(discount_rate, cos)
        self.project_margin = ((project_revenue-self.project_cost)/project_revenue)*100
        if self.project_cost >= self.wealth:
                self.askRevenue()
        
        
        
       





