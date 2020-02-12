#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rafael
"""

import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import pandas as pd
import numpy as np
import statistics
from scipy import stats
from scipy.stats import uniform
import matplotlib.pylab as plt
from itertools import cycle, islice


###Hofstede's Analysis
##Global DataFrames
dt = pd.DataFrame()
df = pd.read_excel(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/6dimensions.xlsx")
df = df.drop("ctr", axis=1)

#Selected countries 
ctr = [pd.DataFrame(df.loc[5,:]).T, pd.DataFrame(df.loc[10,:]).T, pd.DataFrame(df.loc[38,:]).T, pd.DataFrame(df.loc[45,:]).T, pd.DataFrame(df.loc[54,:]).T, 
       pd.DataFrame(df.loc[85,:]).T]
dt = dt.append(ctr)
dt = dt.set_index("country")
dt = dt.T

#PDI
dirty_graph_pdi = df["pdi"]
g_pdi = pd.DataFrame([x for x in dirty_graph_pdi if str(x) != 'nan'])
m_pdi, s_pdi = stats.norm.fit(g_pdi)  

#IDV
dirty_graph_idv = df["idv"]
g_idv = pd.DataFrame([x for x in dirty_graph_idv if str(x) != 'nan'])
m_idv, s_idv = stats.norm.fit(g_idv)  

#MAS
dirty_graph_mas = df["mas"]
g_mas = pd.DataFrame([x for x in dirty_graph_mas if str(x) != 'nan'])
m_mas, s_mas = stats.norm.fit(g_mas)

#UAI
dirty_graph_uai = df["uai"]
g_uai = pd.DataFrame([x for x in dirty_graph_uai if str(x) != 'nan'])
m_uai, s_uai = stats.norm.fit(g_uai)  

#LTO
dirty_graph_lto = df["ltowvs"]
g_lto = pd.DataFrame([x for x in dirty_graph_lto if str(x) != 'nan'])
m_lto, s_lto = stats.norm.fit(g_lto)
   
#IVR
dirty_graph_ivr = df["ivr"]
g_ivr = pd.DataFrame([x for x in dirty_graph_ivr if str(x) != 'nan'])
m_ivr, s_ivr = stats.norm.fit(g_ivr)  

##Analytics - Combination of different dimensions
decision_style_std = np.sqrt(s_pdi**2 + s_lto**2 + s_ivr**2)
decision_rule_std = np.sqrt(s_mas**2 + s_uai**2 + s_idv**2)


#Data per country
#Australia
AUSDecision_style_mean = statistics.mean([float(dt.iloc[0,0]), float(dt.iloc[4,0]), float(dt.iloc[5,0])]) #PDI, LTO, IVR
AUSDecision_rule_mean = statistics.mean([float(dt.iloc[1,0]), float(dt.iloc[2,0]), float(dt.iloc[3,0])]) #IDV, MAS, UAI
AUSDS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
AUS_Decision_style = [x for x in AUSDS if float(x) > 0 and float(x) < 100]
AUSDR = np.random.normal(loc = AUSDecision_rule_mean, scale = decision_rule_std, size=200)
AUS_Decision_rule = [x for x in AUSDR if float(x) > 0 and float(x) < 100]
AUS_gridtariff = uniform.rvs(size=1000, loc = 0.0519, scale=0.0116) 
AUS_solarCosts = uniform.rvs(size=1000, loc = 800, scale=1200) 
AUS_windCosts = uniform.rvs(size=1000, loc = 1300, scale=700)
AUS_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) 
AUS_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) 
AUS_discount_rate = 0.07 
AUS_sunshine = 2270.2 
AUS_wind_dist = 2525.8  

#Brazil
BRADecision_style_mean = statistics.mean([float(dt.iloc[0,1]), float(dt.iloc[4,1]), float(dt.iloc[5,1])]) #PDI, LTO, IVR
BRADecision_rule_mean = statistics.mean([float(dt.iloc[1,1]), float(dt.iloc[2,1]), float(dt.iloc[3,1])]) #PDI, LTO, IVR
BRADS = np.random.normal(loc = BRADecision_style_mean, scale = decision_style_std, size=200)
BRA_Decision_style = [x for x in BRADS if float(x) > 0 and float(x) < 100]
BRADR = np.random.normal(loc = BRADecision_rule_mean, scale = decision_rule_std, size=200)
BRA_Decision_rule = [x for x in BRADR if float(x) > 0 and float(x) < 100]
BRA_gridtariff = uniform.rvs(size=1000, loc = 0.09612, scale=0.02136) 
BRA_solarCosts = uniform.rvs(size=1000, loc = 800, scale=1200) 
BRA_windCosts = uniform.rvs(size=1000, loc = 1200, scale=1200) 
BRA_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) 
BRA_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) 
BRA_discount_rate = 0.1 
BRA_sunshine = 1732.7
BRA_wind_dist = 1673.16 

#Iran
IRADecision_style_mean = statistics.mean([float(dt.iloc[0,2]), float(dt.iloc[4,2]), float(dt.iloc[5,2])]) #PDI, LTO, IVR
IRADecision_rule_mean = statistics.mean([float(dt.iloc[1,2]), float(dt.iloc[2,2]), float(dt.iloc[3,2])]) #PDI, LTO, IVR
IRADS = np.random.normal(loc = IRADecision_style_mean, scale = decision_style_std, size=200)
IRA_Decision_style = [x for x in IRADS if float(x) > 0 and float(x) < 100]
IRADR = np.random.normal(loc = IRADecision_rule_mean, scale = decision_rule_std, size=200)
IRA_Decision_rule = [x for x in IRADR if float(x) > 0 and float(x) < 100]
IRA_gridtariff = uniform.rvs(size=1000, loc = 0.0468, scale=0.0752) 
IRA_solarCosts = uniform.rvs(size=1000, loc = 800, scale=500) 
IRA_windCosts = uniform.rvs(size=1000, loc = 1100, scale=1000) 
IRA_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) 
IRA_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) 
IRA_discount_rate = 0.058 
IRA_sunshine = 2951.8 
IRA_wind_dist = 2760.86

#Japan
JPNDecision_style_mean = statistics.mean([float(dt.iloc[0,3]), float(dt.iloc[4,3]), float(dt.iloc[5,3])]) #PDI, LTO, IVR
JPNDecision_rule_mean = statistics.mean([float(dt.iloc[1,3]), float(dt.iloc[2,3]), float(dt.iloc[3,3])]) #PDI, LTO, IVR
JPNDS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
JPN_Decision_style = [x for x in JPNDS if float(x) > 0 and float(x) < 100]
JPNDR = np.random.normal(loc = JPNDecision_rule_mean, scale = decision_rule_std, size=200)
JPN_Decision_rule = [x for x in JPNDR if float(x) > 0 and float(x) < 100]
JPN_gridtariff = uniform.rvs(size=1000, loc = 0.1084, scale=0.0241) 
JPN_solarCosts = uniform.rvs(size=1000, loc = 1400, scale=700) 
JPN_windCosts = uniform.rvs(size=1000, loc = 1600, scale=1000) 
JPN_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) 
JPN_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) 
JPN_discount_rate = 0.04 
JPN_sunshine = 1773.29
JPN_wind_dist = 979.66 

#Netherlands
NLDDecision_style_mean = statistics.mean([float(dt.iloc[0,4]), float(dt.iloc[4,4]), float(dt.iloc[5,4])]) #PDI, LTO, IVR
NLDDecision_rule_mean = statistics.mean([float(dt.iloc[1,4]), float(dt.iloc[2,4]), float(dt.iloc[3,4])]) #PDI, LTO, IVR
NLDDS = np.random.normal(loc = NLDDecision_style_mean, scale = decision_style_std, size=200)
NLD_Decision_style = [x for x in NLDDS if float(x) > 0 and float(x) < 100]
NLDDR = np.random.normal(loc = NLDDecision_rule_mean, scale = decision_rule_std, size=200)
NLD_Decision_rule = [x for x in NLDDR if float(x) > 0 and float(x) < 100]
NLD_gridtariff = uniform.rvs(size=1000, loc = 0.06786, scale=0.011508) 
NLD_solarCosts = uniform.rvs(size=1000, loc = 900, scale=2590) 
NLD_windCosts = uniform.rvs(size=1000, loc = 1000, scale=2100)
NLD_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) 
NLD_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) 
NLD_discount_rate = 0.03
NLD_sunshine = 1542.3  
NLD_wind_dist = 3749.28 

#USA
USADecision_style_mean = statistics.mean([float(dt.iloc[0,5]), float(dt.iloc[4,5]), float(dt.iloc[5,5])]) #PDI, LTO, IVR
USADecision_rule_mean = statistics.mean([float(dt.iloc[1,5]), float(dt.iloc[2,5]), float(dt.iloc[3,5])]) #PDI, LTO, IVR
USADS = np.random.normal(loc = USADecision_style_mean, scale = decision_style_std, size=200)
USA_Decision_style = [x for x in USADS if float(x) > 0 and float(x) < 100]
USADR = np.random.normal(loc = USADecision_rule_mean, scale = decision_rule_std, size=200)
USA_Decision_rule  = [x for x in USADR if float(x) > 0 and float(x) < 100]
USA_gridtariff = uniform.rvs(size=1000, loc = 0.0717, scale=0.0159)  
USA_solarCosts = uniform.rvs(size=1000, loc = 800, scale=1200) 
USA_windCosts = uniform.rvs(size=1000, loc = 1200, scale=1300) 
USA_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) 
USA_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) 
USA_discount_rate = 0.03 
USA_sunshine = 3254.2 
USA_wind_dist = 2562.38 
##Graphs
#Selected Countries
my_colors = list(islice(cycle(['#66b3ff', '#2F9599', '#355C7d', '#E84A5F', '#474747', '#9DE0AD']), None, len(dt)))
fig = plt.figure()
ax2 = dt.plot(kind="bar", figsize = (12,8), color = my_colors, fontsize =12, grid=True, title = "Hofstede's 6 dimensions for selected countries")
plt.savefig('H - 6D.png')
ax2.grid(axis="x")

#Power Distance
fig, ax = plt.subplots()
g_pdi.plot.hist(density=True, ax=ax, color="#66b3ff")
g_pdi.plot.kde(ax=ax, legend=False, title='Power Distance Distribution', color = 'orange')
plt.axvline(m_pdi, color='k', linestyle='dashed', linewidth=1)
plt.xlabel('Power Distance Index')
plt.legend(["Distribution function", "mean", "Power Distance freq"])
plt.savefig('H - PDI.png')
plt.show()

#Individualism
fig, ax = plt.subplots()
g_idv.plot.kde(ax=ax, legend=False, title='Individualism Distribution', color = '#594F4F')
g_idv.plot.hist(density=True, ax=ax, color="#2F9599")
plt.axvline(m_idv, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Individualism')
plt.legend(["Distribution function", "mean", "Individualism freq"])
plt.savefig('H - IDV.png')
plt.show()

#Masculinity  
fig, ax = plt.subplots()
g_mas.plot.kde(ax=ax, legend=False, title='Assertiveness Distribution', color = '#F8B195')
g_mas.plot.hist(density=True, ax=ax, color="#355C7d")
plt.axvline(m_mas, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Assertiveness')
plt.legend(["Distribution function", "mean", "Assertiveness freq"])
plt.savefig('H - AST.png')
plt.show()

#Uncertainty Avoidance
fig, ax = plt.subplots()
g_uai.plot.kde(ax=ax, legend=False, title='Uncertainty Avoidance Distribution', color = '#99B898')
g_uai.plot.hist(density=True, ax=ax, color="#E84A5F")
plt.axvline(m_uai, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Uncertainty Avoidance')
plt.legend(["Distribution function", "mean", "Uncertainty Avoid. freq"])
plt.savefig('H - UAI.png')
plt.show()

#Long term orientation
fig, ax = plt.subplots()
g_lto.plot.kde(ax=ax, legend=False, title='Long Term Orientation Distribution', color = '#A8A7A7')
g_lto.plot.hist(density=True, ax=ax, color="#474747")
plt.axvline(m_lto, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Long Term Orientation')
plt.legend(["Distribution function", "mean", "Long-term orient. freq"])
plt.savefig('H - LTO.png')
plt.show()

#Indulgene
fig, ax = plt.subplots()
g_ivr.plot.kde(ax=ax, legend=False, title='Indulgence Distribution', color = '#547980')
g_ivr.plot.hist(density=True, ax=ax, color="#9DE0AD")
plt.axvline(m_ivr, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Indulgence')
plt.legend(["Distribution function", "mean", "Indulgence freq"])
plt.savefig('H - IND.png')
plt.show()

