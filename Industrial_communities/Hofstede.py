#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:57:29 2019

@author: rafael
"""

import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import pandas as pd
import numpy as np
import statistics
import random
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
AUS_gridtariff = uniform.rvs(size=1000, loc = 0.0519, scale=0.0116) # From 0.0519 to 0.0635 - usd/kwh 2018 Average National USDAUD = 1.41 - https://www.aer.gov.au/wholesale-markets/wholesale-statistics/annual-volume-weighted-average-spot-prices-regions
AUS_solarCosts = uniform.rvs(size=1000, loc = 800, scale=1200) #From 800 to 2000 usd/kw 2018 National https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
AUS_windCosts = uniform.rvs(size=1000, loc = 1300, scale=700) #From 1300 to 2000 - usd/kw - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
AUS_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) # from 0.2 to 0.25 in % pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
AUS_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) #from 0.02 to 0.03 usd/kwh pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
AUS_discount_rate = 0.07 ## http://www.economia.gov.br/acesso-a-informacao/participacao-social/consultas-publicas/arquivos/TDTaxaSocialdeDesconto.pdf
AUS_sunshine = 2270.2 #Sydney - Mean Annual hours of sunshine http://data.un.org/Data.aspx?q=sunshine&d=CLINO&f=ElementCode%3a15
AUS_wind_dist = 2525.8 #Sydney - Hours of high/medium wind speed http://windfinder.com 

#Brazil
BRADecision_style_mean = statistics.mean([float(dt.iloc[0,1]), float(dt.iloc[4,1]), float(dt.iloc[5,1])]) #PDI, LTO, IVR
BRADecision_rule_mean = statistics.mean([float(dt.iloc[1,1]), float(dt.iloc[2,1]), float(dt.iloc[3,1])]) #PDI, LTO, IVR
BRADS = np.random.normal(loc = BRADecision_style_mean, scale = decision_style_std, size=200)
BRA_Decision_style = [x for x in BRADS if float(x) > 0 and float(x) < 100]
BRADR = np.random.normal(loc = BRADecision_rule_mean, scale = decision_rule_std, size=200)
BRA_Decision_rule = [x for x in BRADR if float(x) > 0 and float(x) < 100]
BRA_gridtariff = uniform.rvs(size=1000, loc = 0.09612, scale=0.02136) # From 0.09612 to 0.11748 - USD/kwh 2019 SP state average USDBRL = 3.87 (31/12/18 - https://www.bcb.gov.br/conversao) - https://www.aneel.gov.br/dados/tarifas
BRA_solarCosts = uniform.rvs(size=1000, loc = 800, scale=1200) # From 800 to 2000  - 2018 usd/kwh National USD https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
BRA_windCosts = uniform.rvs(size=1000, loc = 1200, scale=1200) #From 1200 to 2500 - 2018 USD/kWh  National USD/kwh https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
BRA_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) #in % pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
BRA_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) #usd/kwh pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
BRA_discount_rate = 0.1 #http://www.economia.gov.br/acesso-a-informacao/participacao-social/consultas-publicas/arquivos/TDTaxaSocialdeDesconto.pdf
BRA_sunshine = 1732.7 #São Paulo - Mean Annual hours of sunshine http://data.un.org/Data.aspx?q=sunshine&d=CLINO&f=ElementCode%3a15
BRA_wind_dist = 1673.16 #São Paulo - Hours of high/medium wind speed http://windfinder.com 

#Iran
IRADecision_style_mean = statistics.mean([float(dt.iloc[0,2]), float(dt.iloc[4,2]), float(dt.iloc[5,2])]) #PDI, LTO, IVR
IRADecision_rule_mean = statistics.mean([float(dt.iloc[1,2]), float(dt.iloc[2,2]), float(dt.iloc[3,2])]) #PDI, LTO, IVR
IRADS = np.random.normal(loc = IRADecision_style_mean, scale = decision_style_std, size=200)
IRA_Decision_style = [x for x in IRADS if float(x) > 0 and float(x) < 100]
IRADR = np.random.normal(loc = IRADecision_rule_mean, scale = decision_rule_std, size=200)
IRA_Decision_rule = [x for x in IRADR if float(x) > 0 and float(x) < 100]
IRA_gridtariff = uniform.rvs(size=1000, loc = 0.0468, scale=0.0752) #From 0.0468 to 0.0752 - usd/kwh https://www.doingbusiness.org/content/dam/doingBusiness/country/i/iran/IRN.pdf
IRA_solarCosts = uniform.rvs(size=1000, loc = 800, scale=500) # From 800 to 1300 - usd/kwh peered from saudi arabia- https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
IRA_windCosts = uniform.rvs(size=1000, loc = 1100, scale=1000) #From 1100 to 2100 - usd/kw - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
IRA_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) #in % pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
IRA_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) #usd/kwh pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
IRA_discount_rate = 0.058 #https://journalofeconomicstructures.springeropen.com/articles/10.1186/s40008-018-0127-x
IRA_sunshine = 2951.8 #Arak - Mean Annual hours of sunshine http://data.un.org/Data.aspx?q=sunshine&d=CLINO&f=ElementCode%3a15
IRA_wind_dist = 2760.86 #Arak - Hours of high/medium wind speed http://windfinder.com

#Japan
JPNDecision_style_mean = statistics.mean([float(dt.iloc[0,3]), float(dt.iloc[4,3]), float(dt.iloc[5,3])]) #PDI, LTO, IVR
JPNDecision_rule_mean = statistics.mean([float(dt.iloc[1,3]), float(dt.iloc[2,3]), float(dt.iloc[3,3])]) #PDI, LTO, IVR
JPNDS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
JPN_Decision_style = [x for x in JPNDS if float(x) > 0 and float(x) < 100]
JPNDR = np.random.normal(loc = JPNDecision_rule_mean, scale = decision_rule_std, size=200)
JPN_Decision_rule = [x for x in JPNDR if float(x) > 0 and float(x) < 100]
JPN_gridtariff = uniform.rvs(size=1000, loc = 0.1084, scale=0.0241) #From 0.1084 to 0.1325 - USD/kwh Average https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/834368/table_531.xlsx
JPN_solarCosts = uniform.rvs(size=1000, loc = 1400, scale=700) #From 1400 to 2100  - usd/kwh 2018 National USD https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
JPN_windCosts = uniform.rvs(size=1000, loc = 1600, scale=1000) #From 1600 to 2600 - usd/kwh 2018 pg35  https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
JPN_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) #in % pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
JPN_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) #usd/kwh pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
JPN_discount_rate = 0.04 #http://press-files.anu.edu.au/downloads/press/p345233/pdf/app04.pdf
JPN_sunshine = 1773.29 #Kyoto - Mean Annual hours of sunshine http://data.un.org/Data.aspx?q=sunshine&d=CLINO&f=ElementCode%3a15
JPN_wind_dist = 979.66 #Kyoto - Hours of high/medium wind speed http://windfinder.com

#Netherlands
NLDDecision_style_mean = statistics.mean([float(dt.iloc[0,4]), float(dt.iloc[4,4]), float(dt.iloc[5,4])]) #PDI, LTO, IVR
NLDDecision_rule_mean = statistics.mean([float(dt.iloc[1,4]), float(dt.iloc[2,4]), float(dt.iloc[3,4])]) #PDI, LTO, IVR
NLDDS = np.random.normal(loc = NLDDecision_style_mean, scale = decision_style_std, size=200)
NLD_Decision_style = [x for x in NLDDS if float(x) > 0 and float(x) < 100]
NLDDR = np.random.normal(loc = NLDDecision_rule_mean, scale = decision_rule_std, size=200)
NLD_Decision_rule = [x for x in NLDDR if float(x) > 0 and float(x) < 100]
NLD_gridtariff = uniform.rvs(size=1000, loc = 0.06786, scale=0.011508) # From 0.06786 to 0.08294 - usd/kwh Average USDEUR=0.874 - /kwh https://appsso.eurostat.ec.europa.eu/nui/submitViewTableAction.do
NLD_solarCosts = uniform.rvs(size=1000, loc = 900, scale=2590) # From 900 to 3490 -  usd/kw USDEUR=0.874 - 2014  page 3 http://spinlab.vu.nl/wp-content/uploads/2016/09/Economic_Feasibility_of_roof_top_solar_panels_in_Amsterdam-Michel_Paardekooper.pdf
NLD_windCosts = uniform.rvs(size=1000, loc = 1000, scale=2100) #From 1000 to 3100 - usd/kw USDEUR=0.874 - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
NLD_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) #in % pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
NLD_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) #usd/kwh pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
NLD_discount_rate = 0.03 #http://www.economia.gov.br/acesso-a-informacao/participacao-social/consultas-publicas/arquivos/TDTaxaSocialdeDesconto.pdf
NLD_sunshine = 1542.3  #Rotterdam - Mean Annual hours of sunshine http://data.un.org/Data.aspx?q=sunshine&d=CLINO&f=ElementCode%3a15
NLD_wind_dist = 3749.28 #Rotterdam - Hours of high/medium wind speed http://windfinder.com

#USA
USADecision_style_mean = statistics.mean([float(dt.iloc[0,5]), float(dt.iloc[4,5]), float(dt.iloc[5,5])]) #PDI, LTO, IVR
USADecision_rule_mean = statistics.mean([float(dt.iloc[1,5]), float(dt.iloc[2,5]), float(dt.iloc[3,5])]) #PDI, LTO, IVR
USADS = np.random.normal(loc = USADecision_style_mean, scale = decision_style_std, size=200)
USA_Decision_style = [x for x in USADS if float(x) > 0 and float(x) < 100]
USADR = np.random.normal(loc = USADecision_rule_mean, scale = decision_rule_std, size=200)
USA_Decision_rule  = [x for x in USADR if float(x) > 0 and float(x) < 100]
USA_gridtariff = uniform.rvs(size=1000, loc = 0.0717, scale=0.0159)  # From 0.0717 to 0.0876 - usd/kwh Oct/2019 national https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_06_a
USA_solarCosts = uniform.rvs(size=1000, loc = 800, scale=1200) #From 800 to 2000  -  usd/kw 2018 National https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
USA_windCosts = uniform.rvs(size=1000, loc = 1200, scale=1300) # From 1200 to 2500 - usd/kw 2018 National USD/kwh https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
USA_solar_OM = uniform.rvs(size=1000, loc = 0.2, scale=0.05) #in % pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
USA_wind_OM = uniform.rvs(size=1000, loc = 0.02, scale=0.03) #usd/kwh pg 82 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
USA_discount_rate = 0.03 ##http://www.economia.gov.br/acesso-a-informacao/participacao-social/consultas-publicas/arquivos/TDTaxaSocialdeDesconto.pdf
USA_sunshine = 3254.2 #Los Angeles - Mean Annual hours of sunshine http://data.un.org/Data.aspx?q=sunshine&d=CLINO&f=ElementCode%3a15
USA_wind_dist = 2562.38 #Los Angeles - Hours of high/medium wind speed http://windfinder.com

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

