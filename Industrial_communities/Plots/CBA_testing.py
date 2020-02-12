#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:20:17 2019

@author: rafael
"""
import random
import Data
import numpy as np
from scipy.stats import uniform



result = []
rev = []
cos = []
a = 0
b = 0
gridtariff = random.uniform(0.06786, 0.08294)
solar_implement_Costs = random.uniform(900, 3490) 
wind_implement_Costs = random.uniform(1000, 3100)
discount_rate = 0.03 
annual_demand = np.random.choice(uniform.rvs(size=10000, loc = 20, scale=30000))
wind_threshold = 5000
financial_investment = 0 #"tax-incentive"
depreciation_period = 20
solar_OM = random.uniform(0.2, 0.25) 
wind_OM = random.uniform(0.02, 0.03)

wind_energy = (int(annual_demand/wind_threshold)*wind_threshold)
installation_wind = wind_energy / Data.BRA_wind_dist
investment_wind = installation_wind * wind_implement_Costs

solar_energy = annual_demand % wind_threshold
installation_solar = solar_energy / Data.BRA_sunshine
investment_solar = installation_solar * solar_implement_Costs

try:
    LCOE_wind = (investment_wind/(wind_energy * depreciation_period))
except:
    LCOE_wind = 0

try:
    LCOE_solar =  (investment_solar/(solar_energy * depreciation_period)) 
except: 
    LCOE_solar = 0

wind_OM = wind_OM * wind_energy
solar_OM = solar_OM * LCOE_solar * solar_energy

Revenue = annual_demand * gridtariff
Costs =  wind_OM + solar_OM + (investment_solar + investment_wind)/depreciation_period
for i in range(depreciation_period):
    result.append(Revenue - Costs)
    rev.append(Revenue)
    cos.append(Costs)

NPV = np.npv(discount_rate, result)
r = np.npv(discount_rate, rev)
c = np.npv(discount_rate, cos)

margin = ((r-c)/r) * 100

if(NPV > 0):
    print(NPV)

if(margin > 0):
    print(margin)



