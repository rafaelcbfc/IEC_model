#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:38:45 2020

@author: rafael
"""

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
 









