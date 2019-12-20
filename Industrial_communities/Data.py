#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:57:29 2019

@author: rafael
"""

import Hofstede

##Data by Country
#Australia
AUS_Decision_style = Hofstede.AUSDS
AUS_Decision_rule = Hofstede.AUSDR
AUS_gridtariff = 0.05773 #usd/kwh 2018 Average National USDAUD = 1.41 - https://www.aer.gov.au/wholesale-markets/wholesale-statistics/annual-volume-weighted-average-spot-prices-regions
solarCosts = range(800, 2000, 20) # usd/kw 2018 National https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
windCosts = range(1300, 2000, 20) #usd/kw - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D


#Brazil
BRA_Decision_style = Hofstede.BRADS
BRA_Decision_rule = Hofstede.BRADR
BRA_gridtariff = 0.06011 # USD/kwh 2019 National average USDBRL = 3.87 (31/12/18 - https://www.bcb.gov.br/conversao) -  http://relatorios.aneel.gov.br/_layouts/xlviewer.aspx?id=/RelatoriosSAS/RelSampRegCC.xlsx&Source=http://relatorios.aneel.gov.br/RelatoriosSAS/Forms/AllItems.aspx&DefaultItemOpen=1
BRA_solarCosts = range(800, 2000, 20) #2018 usd/kwh National USD https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
BRA_windCosts = range(1200, 2500, 20) #2018 USD/kWh  National USD/kwh https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D


#Iran
IRA_Decision_style = Hofstede.IRADS
IRA_Decision_rule = Hofstede.IRADR
IRA_gridtariff = 0.052 #usd/kwh https://www.doingbusiness.org/content/dam/doingBusiness/country/i/iran/IRN.pdf
IRA_solarCosts = range(800, 1300, 20) #usd/kwh peered from saudi arabia- https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
IRA_windCosts = range (1100, 2100, 20) #usd/kw - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D


#Japan
JPN_Decision_style = Hofstede.JPNDS
JPN_Decision_rule = Hofstede.JPNDR
JPN_gridtariff = 0.1205 #USD/kwh Average https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/834368/table_531.xlsx
JPN_solarCosts = range(1400, 2100, 20) #usd/kwh 2018 National USD https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
JPN_windCosts = range(1600, 2600, 20) #usd/kwh 2018 pg35  https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D


#Netherlands
NLD_Decision_style = Hofstede.NLDDS
NLD_Decision_rule = Hofstede.NLDDR
NLD_gridtariff = 0.0754 #usd/kwh Average USDEUR=0.874 - /kwh https://appsso.eurostat.ec.europa.eu/nui/submitViewTableAction.do
NLD_solarCosts = range(230, 920, 20) # usd/kw USDEUR=0.874 - 2014 http://spinlab.vu.nl/wp-content/uploads/2016/09/Economic_Feasibility_of_roof_top_solar_panels_in_Amsterdam-Michel_Paardekooper.pdf
NLD_windCosts = range(1000, 3100, 20) #usd/kw USDEUR=0.874 - 2018 pg35 https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D


#USA
USA_Decision_style = Hofstede.USADS
USA_Decision_rule = Hofstede.USADR
USA_gridtariff = 0.0797  # usd/kwh Oct/2019 national https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_06_a
USA_solarCosts = range(800, 2000, 20) # usd/kw 2018 National https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
USA_windCosts = range(1200, 2500, 20) #usd/kw 2018 National USD/kwh https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
