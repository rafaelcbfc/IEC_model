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
from scipy import stats
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

##Analytics
decision_style_mean = statistics.mean([m_pdi, m_lto, m_ivr])
decision_style_std = np.sqrt(s_pdi**2 + s_lto**2 + s_ivr**2)
decision_rule_mean = statistics.mean([m_mas, m_uai, m_idv])
decision_style_std = np.sqrt(s_mas**2 + s_uai**2 + s_idv**2)


#Data per country
#Australia
AUSDecision_style_mean = statistics.mean([float(dt.iloc[0,1]), float(dt.iloc[4,1]), float(dt.iloc[5,1])])
AUSDecision_rule_mean = statistics.mean([float(dt.iloc[1,1]), float(dt.iloc[2,1]), float(dt.iloc[3,1])])
AUSDS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
AUS_Decision_style = [x for x in AUSDS if float(x) > 0 and float(x) < 100]
AUSDR = np.random.normal(loc = AUSDecision_rule_mean, scale = decision_style_std, size=200)
AUS_Decision_rule = [x for x in AUSDR if float(x) > 0 and float(x) < 100]
AUS_gridtariff = 0.05773 #usd/kwh 2018 Average National USDAUD = 1.41 - https://www.aer.gov.au/wholesale-markets/wholesale-statistics/annual-volume-weighted-average-spot-prices-regions
solarCosts = range(800, 2000, 50) # usd/kw 2018 National https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
windCosts = range(1300, 2000, 50) #usd/kw - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
AUS_discount_rate = 0.07 ## http://www.economia.gov.br/acesso-a-informacao/participacao-social/consultas-publicas/arquivos/TDTaxaSocialdeDesconto.pdf

#Brazil
BRADecision_style_mean = statistics.mean([float(dt.iloc[0,2]), float(dt.iloc[4,2]), float(dt.iloc[5,2])])
BRADecision_rule_mean = statistics.mean([float(dt.iloc[1,2]), float(dt.iloc[2,2]), float(dt.iloc[3,2])])
BRADS = np.random.normal(loc = BRADecision_style_mean, scale = decision_style_std, size=200)
BRA_Decision_style = [x for x in BRADS if float(x) > 0 and float(x) < 100]
BRADR = np.random.normal(loc = BRADecision_rule_mean, scale = decision_style_std, size=200)
BRA_Decision_rule = [x for x in BRADR if float(x) > 0 and float(x) < 100]
BRA_gridtariff = 0.06011 # USD/kwh 2019 National average USDBRL = 3.87 (31/12/18 - https://www.bcb.gov.br/conversao) -  http://relatorios.aneel.gov.br/_layouts/xlviewer.aspx?id=/RelatoriosSAS/RelSampRegCC.xlsx&Source=http://relatorios.aneel.gov.br/RelatoriosSAS/Forms/AllItems.aspx&DefaultItemOpen=1
BRA_solarCosts = range(800, 2000, 50) #2018 usd/kwh National USD https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
BRA_windCosts = range(1200, 2500, 50) #2018 USD/kWh  National USD/kwh https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
BRA_discount_rate = 0.1 #http://www.economia.gov.br/acesso-a-informacao/participacao-social/consultas-publicas/arquivos/TDTaxaSocialdeDesconto.pdf

#Iran
IRADecision_style_mean = statistics.mean([float(dt.iloc[0,2]), float(dt.iloc[4,2]), float(dt.iloc[5,2])])
IRADecision_rule_mean = statistics.mean([float(dt.iloc[1,2]), float(dt.iloc[2,2]), float(dt.iloc[3,2])])
IRADS = np.random.normal(loc = IRADecision_style_mean, scale = decision_style_std, size=200)
IRA_Decision_style = [x for x in IRADS if float(x) > 0 and float(x) < 100]
IRADR = np.random.normal(loc = IRADecision_rule_mean, scale = decision_style_std, size=200)
IRA_Decision_rule = [x for x in IRADR if float(x) > 0 and float(x) < 100]
IRA_gridtariff = 0.052 #usd/kwh https://www.doingbusiness.org/content/dam/doingBusiness/country/i/iran/IRN.pdf
IRA_solarCosts = range(800, 1300, 50) #usd/kwh peered from saudi arabia- https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
IRA_windCosts = range (1100, 2100,50) #usd/kw - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
IRA_discount_rate = 0.058 #https://journalofeconomicstructures.springeropen.com/articles/10.1186/s40008-018-0127-x

#Japan
JPNDecision_style_mean = statistics.mean([float(dt.iloc[0,3]), float(dt.iloc[4,3]), float(dt.iloc[5,3])])
JPNDecision_rule_mean = statistics.mean([float(dt.iloc[1,3]), float(dt.iloc[2,3]), float(dt.iloc[3,3])])
JPNDS = np.random.normal(loc = AUSDecision_style_mean, scale = decision_style_std, size=200)
JPN_Decision_style = [x for x in JPNDS if float(x) > 0 and float(x) < 100]
JPNDR = np.random.normal(loc = JPNDecision_rule_mean, scale = decision_style_std, size=200)
JPN_Decision_rule = [x for x in JPNDR if float(x) > 0 and float(x) < 100]
JPN_gridtariff = 0.1205 #USD/kwh Average https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/834368/table_531.xlsx
JPN_solarCosts = range(1400, 2100, 50) #usd/kwh 2018 National USD https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
JPN_windCosts = range(1600, 2600, 50) #usd/kwh 2018 pg35  https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
JPN_discount_rate = 0.04 #http://press-files.anu.edu.au/downloads/press/p345233/pdf/app04.pdf

#Netherlands
NLDDecision_style_mean = statistics.mean([float(dt.iloc[0,3]), float(dt.iloc[4,3]), float(dt.iloc[5,3])])
NLDDecision_rule_mean = statistics.mean([float(dt.iloc[1,3]), float(dt.iloc[2,3]), float(dt.iloc[3,3])])
NLDDS = np.random.normal(loc = NLDDecision_style_mean, scale = decision_style_std, size=200)
NLD_Decision_style = [x for x in NLDDS if float(x) > 0 and float(x) < 100]
NLDDR = np.random.normal(loc = NLDDecision_rule_mean, scale = decision_style_std, size=200)
NLD_Decision_rule = [x for x in NLDDR if float(x) > 0 and float(x) < 100]
NLD_gridtariff = 0.0754 #usd/kwh Average USDEUR=0.874 - /kwh https://appsso.eurostat.ec.europa.eu/nui/submitViewTableAction.do
NLD_solarCosts = range(230, 920, 50) # usd/kw USDEUR=0.874 - 2014 http://spinlab.vu.nl/wp-content/uploads/2016/09/Economic_Feasibility_of_roof_top_solar_panels_in_Amsterdam-Michel_Paardekooper.pdf
NLD_windCosts = range(1000, 3100, 50) #usd/kw USDEUR=0.874 - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
NLD_discount_rate = 0.03 #http://www.economia.gov.br/acesso-a-informacao/participacao-social/consultas-publicas/arquivos/TDTaxaSocialdeDesconto.pdf

#USA
USADecision_style_mean = statistics.mean([float(dt.iloc[0,3]), float(dt.iloc[4,3]), float(dt.iloc[5,3])])
USADecision_rule_mean = statistics.mean([float(dt.iloc[1,3]), float(dt.iloc[2,3]), float(dt.iloc[3,3])])
USADS = np.random.normal(loc = USADecision_style_mean, scale = decision_style_std, size=200)
USA_Decision_style = [x for x in USADS if float(x) > 0 and float(x) < 100]
USADR = np.random.normal(loc = USADecision_rule_mean, scale = decision_style_std, size=200)
USA_Decision_rule  = [x for x in USADR if float(x) > 0 and float(x) < 100]
USA_gridtariff = 0.0797  # usd/kwh Oct/2019 national https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_06_a
USA_solarCosts = range(800, 2000, 50) # usd/kw 2018 National https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
USA_windCosts = range(1200, 2500, 50) #usd/kw 2018 National USD/kwh https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
USA_discount_rate = 0.03 ##http://www.economia.gov.br/acesso-a-informacao/participacao-social/consultas-publicas/arquivos/TDTaxaSocialdeDesconto.pdf

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










