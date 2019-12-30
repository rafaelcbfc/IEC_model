#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:20:17 2019

@author: rafael
"""
import random

i = 0
CBAi = 0
gridtariff = 0.06011 
solar_implement_Costs = random.uniform(0.8, 2) 
wind_implement_Costs = random.uniform(1.2, 2.5) 
discount_rate = 0.1 
demand = 21000 ##anual demand
wind_threshold = 5000
financial_investment = 0 #"tax-incentive"
strategy = 0
depreciation_period = 20
pareto = 0.8
margin = 0.1
solar_OM = random.uniform(0.2, 0.25) 
wind_OM = random.uniform(0.02, 0.03)

#Baseline
NPV_baseline = 0
for i in range(depreciation_period):
    NPV_baseline = NPV_baseline + ((demand * gridtariff)/(1+discount_rate)**(i*12))

#renewable energy 
coef = demand/wind_threshold
#Scenario 1 = Strategy 0, solar energy
if coef < 1:
    wind_energy_s1 = 0
    wind_tariff_s1 = 0
    wind_OM_s1 = 0
    
    solar_energy_s1 = demand
    investment_solar_s1 = solar_energy_s1 * solar_implement_Costs
    
    if financial_investment == "tax-incentive":
        solar_implement_Costs = solar_implement_Costs * 0.6
        wind_implement_Costs = wind_implement_Costs * 0.6
   
    solar_tariff_s1 = investment_solar_s1/(solar_energy_s1 * depreciation_period)
    solar_OM_s1 = solar_OM * solar_tariff_s1
   
    NPV_investment = 0
    for i in range(depreciation_period):
        NPV_investment = NPV_investment + ((wind_energy_s1 * (wind_tariff_s1) - wind_OM_s1) + 
                                             (solar_energy_s1 * (solar_tariff_s1 - solar_OM_s1))) /((1+discount_rate)**(i*12))

#Scenario 2 = Strategy 0, mixed energy
if coef > 1:
    wind_energy_s2 = int(demand/wind_threshold)*wind_threshold
    investment_wind_s2 = wind_energy_s2 * wind_implement_Costs
    
    solar_energy_s2 = demand % wind_threshold
    investment_solar_s2 = solar_energy_s2 * solar_implement_Costs 
    
    if financial_investment == "tax-incentive":
        solar_implement_Costs = solar_implement_Costs * 0.6
        wind_implement_Costs = wind_implement_Costs * 0.6
    
    wind_tariff_s2 = (investment_wind_s2/(wind_energy_s2 * depreciation_period))
    solar_tariff_s2 =  (investment_solar_s2/(solar_energy_s2 * depreciation_period))
    wind_OM_s2 = wind_OM * wind_energy_s2
    solar_OM_s2 = solar_OM * solar_tariff_s2
    
    NPV_investment = -(solar_implement_Costs + wind_implement_Costs)
    for i in range(depreciation_period):
        NPV_investment = NPV_investment + ((wind_energy_s2 * (wind_tariff_s2) - wind_OM_s2) + 
                                             (solar_energy_s2 * (solar_tariff_s2 - solar_OM_s2))) /((1+discount_rate)**(i*12))
    
   
print(NPV_baseline / NPV_investment)
if (NPV_baseline / NPV_investment) > 1:
    CBAi = "favorable"
elif (NPV_baseline / NPV_investment) < 1:
    CBAi = "unfavorable"



print(CBAi)

