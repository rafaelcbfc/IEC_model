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
sunshine = Hofstede.BRA_sunshine
wind_dist = Hofstede.BRA_wind_dist
decision_style = Hofstede.BRA_Decision_style
decision_rule = Hofstede.BRA_Decision_rule
 

wind_threshold = 5000 #in KW, minimum value to make it a possibility for wind energy production - https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
depreciation_period = 20
gridtariff = Hofstede.BRA_gridtariff 

#pool_financial_investments = ["feed-in-tariff", "tax-incentive", "tradable-certificates"]
#financial_investment = 0 #pool_financial_investment[1]
#if financial_investment == "tax-incentive":
#    solar_implement_Costs = solar_implement_Costs * 0.6
#    wind_implement_Costs = wind_implement_Costs * 0.6


def cbaCalc(me): #Individual Cost benefit: Buy from grid, produce or sell energy?
#Variables   
    gridtariff = Hofstede.BRA_gridtariff
    solar_implement_Costs = Hofstede.BRA_solarCosts  
    wind_implement_Costs = Hofstede.BRA_windCosts
    solar_OM = Hofstede.BRA_solar_OM
    wind_OM = Hofstede.BRA_wind_OM
    
    rev0, rev10, rev11, rev20, rev21, rev30, rev31, cos1, cos2, cos3 = [], [], [], [], [], [], [], [], [], []
    annual_demand = me.energy
    
##Case 0 - Grid energy
    r0 = gridtariff * annual_demand
    
    for i in range(depreciation_period):
        rev0.append(r0)
        
    Baseline_cost = np.npv(discount_rate, rev0)
    
##Case 1 - All solar
    solar_energy1 = annual_demand
    installation_solar1 = solar_energy1 / sunshine
    investment_solar1 = installation_solar1 * solar_implement_Costs
    OM_solar1 = solar_OM * (investment_solar1/(solar_energy1 * depreciation_period)) * solar_energy1
    LCOE_solar1 = (investment_solar1 + OM_solar1 * depreciation_period)/(solar_energy1 * depreciation_period) 
    
    r10 = (gridtariff - LCOE_solar1) * solar_energy1 * 1.1 #Sell energy
    r11 = gridtariff * solar_energy1                       #Produce energy
    c1=  OM_solar1
    
    for i in range(depreciation_period):
        rev10.append(r10)
        rev11.append(r11)
        cos1.append(c1)
    
    revenue10 = np.npv(discount_rate, rev10)
    revenue11 = np.npv(discount_rate, rev11)
    costs1 = investment_solar1 + np.npv(discount_rate, cos1)
    
    NPV10 = revenue10-costs1
    NPV11 = revenue11-costs1
    
##Case 2 - All wind 
    if annual_demand > wind_threshold:
        wind_energy2 = annual_demand
        installation_wind2 = wind_energy2 / wind_dist
        investment_wind2 = installation_wind2 * wind_implement_Costs
        OM_wind2 = wind_OM * wind_energy2
        LCOE_wind2 = (investment_wind2 + OM_wind2 * depreciation_period)/(wind_energy2 * depreciation_period) 
        
        r20 = (gridtariff - LCOE_wind2) * wind_energy2 * 1.1 #Sell energy
        r21 = gridtariff * wind_energy2                      #Produce energy
        c2 =  OM_wind2
        
        for i in range(depreciation_period):
            rev20.append(r20)
            rev21.append(r21)
            cos2.append(c2)
        
        revenue20 = np.npv(discount_rate, rev20)
        revenue21 = np.npv(discount_rate, rev21)
        costs2 = investment_wind2 + np.npv(discount_rate, cos2)
        
        NPV20 = revenue20 - costs2
        NPV21 = revenue21-costs2
    else:
        NPV20 = -10000000
        NPV21 = -10000000
    
##Case 3- Mixed sources
  #wind
    energy3_wind = (int(annual_demand/wind_threshold)*wind_threshold)
    installation_wind3 = energy3_wind / wind_dist
    investment_wind3 = installation_wind3 * wind_implement_Costs
    OM_wind3 = wind_OM * energy3_wind
    try:
        LCOE_wind3 = (investment_wind3 + OM_wind3 * depreciation_period)/(energy3_wind * depreciation_period)
    except: 
        LCOE_wind3 = 0
    
  #Solar
    energy3_solar = annual_demand % wind_threshold
    installation_solar3 = energy3_solar / sunshine
    investment_solar3 = installation_solar3 * solar_implement_Costs
    OM_solar3 = solar_OM * (investment_solar3/(energy3_solar * depreciation_period)) * energy3_solar
    try:
        LCOE_solar3 = (investment_solar3 + OM_solar3 * depreciation_period)/(energy3_solar * depreciation_period) 
    except:
        LCOE_solar3 = 0
        
    r30 = ((gridtariff - LCOE_solar3) * energy3_solar + (gridtariff - LCOE_wind3) * energy3_wind) * 1.1   # Sell energy
    r31 = gridtariff * annual_demand                                                                      #Produce energy 
    c3 =  OM_wind3 + OM_solar3 
    
    for i in range(depreciation_period):
        rev30.append(r30)
        rev31.append(r31)
        cos3.append(c3)
    
    revenue30 = np.npv(discount_rate, rev30)
    revenue31 = np.npv(discount_rate, rev31)
    costs3 = (investment_solar3 + investment_wind3) + np.npv(discount_rate, cos3)
    
    NPV30 = revenue30 - costs3
    NPV31 = revenue31-costs3
    
    ratio_solar = energy3_solar/(energy3_wind+energy3_solar)
    ratio_wind = energy3_wind / (energy3_wind+energy3_solar)
    
##Avaliation
  #Variables
    costs = [costs1, costs2, costs3]
    produce = [NPV11, NPV21, NPV31]
    sell = [NPV10, NPV20, NPV30]
    me.max_re = max(produce + sell)
    
  #1st evaluation => is grid energy more expensive than construct RE?
    count = 0
    for cost in costs:
        if Baseline_cost >= cost: #Grid energy expensier
           count =+ 1
        if max(produce) >= 0: #at least one positive NPV for producing
            count =+ 1
        if max(sell) >= 0: #at least one positive NPV for selling
            count =+1
    
    if count == 0:
        me.cba_lvl = 1 #Grid energy is cheaper than RE and no positive NPV
    
  #2nd evaluation => I am going for renewable, but is it better to produce to my self or sell?
    
    if me.cba_lvl != 1:
        if max(produce) > max(sell): 
           me.cba_lvl = 2 #Producing has a higher NPV than selling
           option = produce.index(max(produce))
        else:
           me.cba_lvl = 3 #Selling has a higher NPV than producing
           option = sell.index(max(sell))
        
        #What is the levelized cost of my option  
        if option == 0:
            me.LCOE = LCOE_solar1
        if option == 1:
            me.LCOE = LCOE_wind2
        if option == 2:
            me.LCOE = (LCOE_solar3 * ratio_solar + LCOE_wind3 * ratio_wind)
    
    print(me.id)
    print("CBA-CBA " + str(me.cba_lvl))
    print("CBA - LCOE " + str(me.LCOE))
    return me.cba_lvl
    return me.LCOE

def cbaCalcPeer(me, peer):
#Variables 
    gridtariff = Hofstede.BRA_gridtariff
    solar_implement_Costs = Hofstede.BRA_solarCosts  
    wind_implement_Costs = Hofstede.BRA_windCosts
    solar_OM = Hofstede.BRA_solar_OM
    wind_OM = Hofstede.BRA_wind_OM
    
    rev10, rev11, rev20, rev21, rev30, rev31, cos1, cos2, cos3 = [], [], [], [], [], [], [], [], []
    annual_demand = (me.energy + peer.energy)
    
#Case 1 - All solar
    solar_energy1 = annual_demand
    installation_solar1 = solar_energy1 / sunshine
    investment_solar1 = installation_solar1 * solar_implement_Costs
    OM_solar1 = solar_OM * (investment_solar1/(solar_energy1 * depreciation_period)) * solar_energy1
    LCOE_solar1 = (investment_solar1 + OM_solar1 * depreciation_period)/(solar_energy1 * depreciation_period) 
    
    r10 = (gridtariff - LCOE_solar1) * solar_energy1 * 1.1 #Sell energy
    r11 = gridtariff * solar_energy1                       #Produce energy
    c1=  OM_solar1
    
    for i in range(depreciation_period):
        rev10.append(r10)
        rev11.append(r11)
        cos1.append(c1)
    
    revenue10 = np.npv(discount_rate, rev10)
    revenue11 = np.npv(discount_rate, rev11)
    costs1 = (0.15 * investment_solar1) + (0.7 * investment_solar1) + np.npv(discount_rate, cos1)
    
    NPVp10 = revenue10-costs1
    NPVp11 = revenue11-costs1
   
#Case 2 - All wind
    if annual_demand > wind_threshold:
        wind_energy2 = annual_demand
        installation_wind2 = wind_energy2 / wind_dist
        investment_wind2 = installation_wind2 * wind_implement_Costs
        OM_wind2 = wind_OM * wind_energy2
        LCOE_wind2 = (investment_wind2 + OM_wind2 * depreciation_period)/(wind_energy2 * depreciation_period) 
        
        r20 = (gridtariff - LCOE_wind2) * wind_energy2 * 1.1 #Sell energy
        r21 = gridtariff * wind_energy2                      #Produce energy
        c2 =  OM_wind2
        
        for i in range(depreciation_period):
            rev20.append(r20)
            rev21.append(r21)
            cos2.append(c2)
        
        revenue20 = np.npv(discount_rate, rev20)
        revenue21 = np.npv(discount_rate, rev21)
        costs2 = (0.15 * investment_wind2) + (0.7 * investment_wind2) + np.npv(discount_rate, cos2)
        
        NPVp20 = revenue20 - costs2
        NPVp21 = revenue21-costs2
    else:
        NPVp20 = -10000000
        NPVp21 = -10000000
    
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
        
    r30 = ((gridtariff - LCOE_solar3) * solar_energy3 + (gridtariff - LCOE_wind3) * wind_energy3) * 1.1   # Sell energy
    r31 = gridtariff * annual_demand                                                                      #Produce energy 
    c3 =  OM_wind3 + OM_solar3 
    
    for i in range(depreciation_period):
        rev30.append(r30)
        rev31.append(r31)
        cos3.append(c3)
    
    revenue30 = np.npv(discount_rate, rev30)
    revenue31 = np.npv(discount_rate, rev31)
    costs3 = ((0.15 * investment_solar3) + (0.7 * investment_solar3) + (0.15 * investment_wind3) + (0.7 * investment_wind3)) + np.npv(discount_rate, cos3)
    
    NPVp30 = revenue30 - costs3
    NPVp31 = revenue31-costs3
    
##Avaliation
    produce_p = [NPVp11, NPVp21, NPVp31]
    sell_p = [NPVp10, NPVp20, NPVp30]
    
  #1st evaluation => doing business with peer is more advantageous?
    count2 = 0 
    max_npvp = max(produce_p + sell_p)
    if max_npvp <= 0: #Negative NPV
        count2 =+ 1
    if me.max_re > max_npvp: #Producing individually is cheaper
        count2 =+ 1
    if peer.max_re > max_npvp: #Producing individually is cheaper
        count2 =+ 1
    
    if count2 > 0:
        me.cba_lvlp == 1 #producing individually is cheper than in group
    
  #2nd evaluation => if we are doing business, produce or sell?
    if me.cba_lvlp != 1:
        if max(produce_p) > max(sell_p): 
           me.cba_lvlp = 2 #Producing has a higher NPV than selling
           
        else:
           me.cba_lvlp = 3 #Selling has a higher NPV than selling



def cbaCalcCom(me, peer):
    if me.LCOE < peer.premium:
        me.cba_lvlc = 0
    else:
        me.cba_lvlc = 1
    

        
def projectSelector(me): 
#Variables    
    gridtariff = Hofstede.BRA_gridtariff
    solar_implement_Costs = Hofstede.BRA_solarCosts  
    wind_implement_Costs = Hofstede.BRA_windCosts
    solar_OM = Hofstede.BRA_solar_OM
    wind_OM = Hofstede.BRA_wind_OM
    
    rev10, rev11, rev20, rev21, rev30, rev31, cos1, cos2, cos3 = [], [], [], [], [], [], [], [], []
    me.project_cost = 0
    annual_demand = me.energy *1.1
    
#Case 1 - All solar
    energy1 = annual_demand
    installation_solar1 = energy1 / sunshine
    investment_solar1 = installation_solar1 * solar_implement_Costs
    OM_solar1 = solar_OM * (investment_solar1/(energy1 * depreciation_period)) * energy1
    LCOE_solar1 = (investment_solar1 + OM_solar1 * depreciation_period)/(energy1 * depreciation_period) 
    
    r10 = (gridtariff - LCOE_solar1) * energy1 * 1.1 #Sell energy
    r11 = gridtariff * energy1                       #Produce energy
    c1=  OM_solar1
    
    for i in range(depreciation_period):
        rev10.append(r10)
        rev11.append(r11)
        cos1.append(c1)
    
    revenue10 = np.npv(discount_rate, rev10)
    revenue11 = np.npv(discount_rate, rev11)
    costs1 = (0.15 * investment_solar1) + (0.7 * investment_solar1) + np.npv(discount_rate, cos1)
    
    NPVc10 = revenue10-costs1
    NPVc11 = revenue11-costs1
    marginc10 = (revenue10 - costs1)/(revenue10 *100)
    marginc11 = (revenue11 - costs1)/(revenue11 *100)
   
#Case 2 - All wind
    if annual_demand > wind_threshold:
        energy2 = annual_demand
        installation_wind2 = energy2 / wind_dist
        investment_wind2 = installation_wind2 * wind_implement_Costs
        OM_wind2 = wind_OM * energy2
        LCOE_wind2 = (investment_wind2 + OM_wind2 * depreciation_period)/(energy2 * depreciation_period) 
        
        r20 = (gridtariff - LCOE_wind2) * energy2 * 1.1 #Sell energy
        r21 = gridtariff * energy2                      #Produce energy
        c2 =  OM_wind2
        
        for i in range(depreciation_period):
            rev20.append(r20)
            rev21.append(r21)
            cos2.append(c2)
        
        revenue20 = np.npv(discount_rate, rev20)
        revenue21 = np.npv(discount_rate, rev21)
        costs2 = ((0.3/float(len(me.members))) * investment_wind2) + (0.7 * investment_wind2) + np.npv(discount_rate, cos2)
        
        NPVc20 = revenue20 - costs2
        NPVc21 = revenue21-costs2
        marginc20 = (revenue20 - costs2)/(revenue20 *100)
        marginc21 = (revenue21 - costs2)/(revenue21 *100)
    else:
        NPVc20 = -10000000
        NPVc21 = -10000000
    
#Case 3- Mixed sources
  #wind
    energy3_wind = (int(annual_demand/wind_threshold)*wind_threshold)
    installation_wind3 = energy3_wind / wind_dist
    investment_wind3 = installation_wind3 * wind_implement_Costs
    OM_wind3 = wind_OM * energy3_wind
    try:
        LCOE_wind3 = (investment_wind3 + OM_wind3 * depreciation_period)/(energy3_wind * depreciation_period)
    except: 
        LCOE_wind3 = 0
    
  #Solar
    energy3_solar = annual_demand % wind_threshold
    installation_solar3 = energy3_solar / sunshine
    investment_solar3 = installation_solar3 * solar_implement_Costs
    OM_solar3 = solar_OM * (investment_solar3/(energy3_solar * depreciation_period)) * energy3_solar
    try:
        LCOE_solar3 = (investment_solar3 + OM_solar3 * depreciation_period)/(energy3_solar * depreciation_period) 
    except:
        LCOE_solar3 = 0
        
    r30 = ((gridtariff - LCOE_solar3) * energy3_solar + (gridtariff - LCOE_wind3) * energy3_wind) * 1.1   # Sell energy
    r31 = gridtariff * annual_demand                                                                      #Produce energy 
    c3 =  OM_wind3 + OM_solar3 

    for i in range(depreciation_period):
        rev30.append(r30)
        rev31.append(r31)
        cos3.append(c3)
    
    revenue30 = np.npv(discount_rate, rev30)
    revenue31 = np.npv(discount_rate, rev31)
    costs3 = (((0.3/float(len(me.members))) * investment_solar3) + (0.7 * investment_solar3) + ((0.3/float(len(me.members))) * investment_wind3) + (0.7 * investment_wind3)) + np.npv(discount_rate, cos3)
    
    NPVc30 = revenue30 - costs3
    NPVc31 = revenue31-costs3
    marginc30 = (revenue30 - costs3)/(revenue30 *100)
    marginc31 = (revenue31 - costs3)/(revenue31 *100)
    ratio_solar = energy3_solar/(energy3_wind+energy3_solar)
    ratio_wind = energy3_wind / (energy3_wind+energy3_solar)
   
##Avaliation
    produce_c = [NPVc11, NPVc21, NPVc31]
    sell_c = [NPVc10, NPVc20, NPVc30]
    
  #1st evaluation => doing business with peer is more advantageous?
    count2 = 0 
    max_npvc = max(produce_c + sell_c)
    if max_npvc <= 0: #Negative NPV
        count2 =+ 1
    
    if count2 > 0:
        me.project_cba == 1 #producing individually is cheper than in group
    
  #2nd evaluation => if we are doing business, produce or sell?
    if me.project_cba != 1:
        if max(produce_c) > max(sell_c): 
           me.project_cba = 2 #Producing has a higher NPV than selling
           option = produce_c.index(max(produce_c))
        else:
           me.project_cba = 3 #Selling has a higher NPV than selling       
           option = sell_c.index(max(sell_c))
    
#What is the levelized cost of my option  
    if option == 0:
        me.project_tariff = LCOE_solar1
        me.technology = "Solar"
        me.project_margin = max(marginc10, marginc11)
        me.project_cost = costs1
        me.energy_solar = energy1
        me.energy_wind = 0
    if option == 1:
        me.project_tariff = LCOE_wind2
        me.technology = "wind"
        me.project_margin = max(marginc20, marginc21)
        me.project_cost = costs2
        me.energy_solar = 0
        me.energy_wind = energy2
    if option == 2:
        me.project_tariff = (LCOE_solar3 * ratio_solar + LCOE_wind3 * ratio_wind)
        me.technology = "mixed"
        me.project_margin = max(marginc30, marginc31)
        me.project_cost = costs3
        me.energy_solar = energy3_solar
        me.energy_wind = energy3_wind
        
        
        

    




