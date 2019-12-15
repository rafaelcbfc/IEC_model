#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:28:56 2019

@author: rafael
"""

import pandas as pd
import numpy as np
import statistics
from scipy import stats
import matplotlib.pylab as plt
from itertools import cycle, islice

###Hofstede's Analysis
##Global DataFrames
dt = pd.DataFrame()
df = pd.read_excel(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Datasets/6dimensions.xlsx")
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

##Analytics
decision_style_mean = statistics.mean([m_pdi, m_lto, m_ivr])
decision_style_std = np.sqrt(s_pdi**2 + s_lto**2 + s_ivr**2)
decision_rule_mean = statistics.mean([m_mas, m_uai, m_idv])
decision_style_std = np.sqrt(s_mas**2 + s_uai**2 + s_idv**2)


#Decision style normal distribuition per country
#Australia
AUSDecision_style_mean = statistics.mean([float(dt.iloc[0,1]), float(dt.iloc[4,1]), float(dt.iloc[5,1])])
AUSDecision_rule_mean = statistics.mean([float(dt.iloc[1,1]), float(dt.iloc[2,1]), float(dt.iloc[3,1])])
AUSDS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
AUSDS = [x for x in AUSDS if float(x) > 0 and float(x) < 100]
AUSDR = np.random.normal(loc = AUSDecision_rule_mean, scale = decision_style_std, size=200)
AUSDR = [x for x in AUSDR if float(x) > 0 and float(x) < 100]

#Brazil
BRADecision_style_mean = statistics.mean([float(dt.iloc[0,2]), float(dt.iloc[4,2]), float(dt.iloc[5,2])])
BRADecision_rule_mean = statistics.mean([float(dt.iloc[1,2]), float(dt.iloc[2,2]), float(dt.iloc[3,2])])
BRADS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
BRADS = [x for x in AUSDS if float(x) > 0 and float(x) < 100]
BRADR = np.random.normal(loc = AUSDecision_rule_mean, scale = decision_style_std, size=200)
BRADR = [x for x in AUSDR if float(x) > 0 and float(x) < 100]

#Iran
IRADecision_style_mean = statistics.mean([float(dt.iloc[0,2]), float(dt.iloc[4,2]), float(dt.iloc[5,2])])
IRADecision_rule_mean = statistics.mean([float(dt.iloc[1,2]), float(dt.iloc[2,2]), float(dt.iloc[3,2])])
IRADS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
IRADS = [x for x in AUSDS if float(x) > 0 and float(x) < 100]
IRADR = np.random.normal(loc = AUSDecision_rule_mean, scale = decision_style_std, size=200)
IRADR = [x for x in AUSDR if float(x) > 0 and float(x) < 100]

#Japan
JPNDecision_style_mean = statistics.mean([float(dt.iloc[0,3]), float(dt.iloc[4,3]), float(dt.iloc[5,3])])
JPNDecision_rule_mean = statistics.mean([float(dt.iloc[1,3]), float(dt.iloc[2,3]), float(dt.iloc[3,3])])
JPNDS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
JPNDS = [x for x in AUSDS if float(x) > 0 and float(x) < 100]
JPNDR = np.random.normal(loc = AUSDecision_rule_mean, scale = decision_style_std, size=200)
JPNDR = [x for x in AUSDR if float(x) > 0 and float(x) < 100]

#Netherlands
NLDDecision_style_mean = statistics.mean([float(dt.iloc[0,3]), float(dt.iloc[4,3]), float(dt.iloc[5,3])])
NLDDecision_rule_mean = statistics.mean([float(dt.iloc[1,3]), float(dt.iloc[2,3]), float(dt.iloc[3,3])])
NLDDS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
NLDDS = [x for x in AUSDS if float(x) > 0 and float(x) < 100]
NLDDR = np.random.normal(loc = AUSDecision_rule_mean, scale = decision_style_std, size=200)
NLDDR = [x for x in AUSDR if float(x) > 0 and float(x) < 100]

#USA
USADecision_style_mean = statistics.mean([float(dt.iloc[0,3]), float(dt.iloc[4,3]), float(dt.iloc[5,3])])
USADecision_rule_mean = statistics.mean([float(dt.iloc[1,3]), float(dt.iloc[2,3]), float(dt.iloc[3,3])])
USADS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
USADS = [x for x in AUSDS if float(x) > 0 and float(x) < 100]
USADR = np.random.normal(loc = AUSDecision_rule_mean, scale = decision_style_std, size=200)
USADR = [x for x in AUSDR if float(x) > 0 and float(x) < 100]
 

##Graphs
#Selected Countries
my_colors = list(islice(cycle(['#66b3ff', '#2F9599', '#355C7d', '#E84A5F', '#474747', '#9DE0AD']), None, len(dt)))
fig = plt.figure()
ax2 = dt.plot(kind="bar", figsize = (12,8), color = my_colors, fontsize =12, grid=True, title = "Hofstede's 6 dimensions for selected countries")
ax2.grid(axis="x")

#Power Distance
fig, ax = plt.subplots()
g_pdi.plot.hist(density=True, ax=ax, color="#66b3ff")
g_pdi.plot.kde(ax=ax, legend=False, title='Power Distance Distribution', color = 'orange')
plt.axvline(m_pdi, color='k', linestyle='dashed', linewidth=1)
plt.xlabel('Power Distance Index')
plt.legend(["Distribution function", "mean", "Power Distance freq"])
plt.show()

#Individualism
fig, ax = plt.subplots()
g_idv.plot.kde(ax=ax, legend=False, title='Individualism Distribution', color = '#594F4F')
g_idv.plot.hist(density=True, ax=ax, color="#2F9599")
plt.axvline(m_idv, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Individualism')
plt.legend(["Distribution function", "mean", "Individualism freq"])
plt.show()

#Masculinity  
fig, ax = plt.subplots()
g_mas.plot.kde(ax=ax, legend=False, title='Masculinity Distribution', color = '#F8B195')
g_mas.plot.hist(density=True, ax=ax, color="#355C7d")
plt.axvline(m_mas, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Masculinity')
plt.legend(["Distribution function", "mean", "Masculinity freq"])
plt.show()

#Uncertainty Avoidance
fig, ax = plt.subplots()
g_uai.plot.kde(ax=ax, legend=False, title='Uncertainty Avoidance Distribution', color = '#99B898')
g_uai.plot.hist(density=True, ax=ax, color="#E84A5F")
plt.axvline(m_uai, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Uncertainty Avoidance')
plt.legend(["Distribution function", "mean", "Uncertainty Avoid. freq"])
plt.show()

#Long term orientation
fig, ax = plt.subplots()
g_lto.plot.kde(ax=ax, legend=False, title='Long Term Orientation Distribution', color = '#A8A7A7')
g_lto.plot.hist(density=True, ax=ax, color="#474747")
plt.axvline(m_lto, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Long Term Orientation')
plt.legend(["Distribution function", "mean", "Long-term orient. freq"])
plt.show()

#Indulgene
fig, ax = plt.subplots()
g_ivr.plot.kde(ax=ax, legend=False, title='Indulgence Distribution', color = '#547980')
g_ivr.plot.hist(density=True, ax=ax, color="#9DE0AD")
plt.axvline(m_ivr, color='k', linestyle='dashed', label="mean", linewidth=1)
plt.xlabel('Indulgence')
plt.legend(["Distribution function", "mean", "Indulgence freq"])
plt.show()



