#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:24:02 2020

@author: rafael
"""
###Imports
import sys
sys.path.append("/Users/rafaelcosta/Documents/GitHub/InCES_model/Industrial_communities")
import pandas as pd, numpy as np, statistics, matplotlib.pylab as plt, Data
from scipy import stats
from scipy.stats import uniform
from itertools import cycle, islice


###Definitions
##Variables
Active_communities = pd.DataFrame()
Communities_members = pd.DataFrame()
Total_solar_energy = pd.DataFrame()
Total_wind_energy = pd.DataFrame()
Total_renewable_energy = pd.DataFrame()
Exit_members = pd.DataFrame()
Invested_capital = pd.DataFrame()
LCOE = pd.DataFrame()
Policy_indicator = pd.DataFrame()
Governmental_expenditure = pd.DataFrame() 

##Tick set
ticks = list(range(0,20000))


country = Data.country

###Datasets import
##Alpha
#Scenario 0 - No incentives
A00 = pd.read_csv(r"/Users/rafaelcosta/Documents/GitHub/InCES_model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_AUS_s0.csv")
#Scenario 1 - FIT
#A11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-01.csv")
#A12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-02.csv")
#A13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-03.csv")
#Scenario 2 - TAX
#A21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-01.csv")
#A22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-02.csv")
#A23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-03.csv")
#Scenario 3 - TGC
#A31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-01.csv")
#A32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-02.csv")
#A33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-03.csv")



##Gamma
#Scenario 0 - No incentives
I00 = pd.read_csv(r"/Users/rafaelcosta/Documents/GitHub/InCES_model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_IRA_S0.csv")
#Scenario 1 - FIT
#I11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_IRA_S1-01.csv")
#I12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_IRA_S1-02.csv")
#I13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_IRA_S1-03.csv")
#Scenario 2 - TAX
#I21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_IRA_S2-01.csv")
#I22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-02.csv")
#I23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-03.csv")
#Scenario 3 - TGC
#I31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_IRA_S3-01.csv")
#I32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_IRA_S3-02.csv")
#I33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_IRA_S3-03.csv")

##Delta
#Scenario 0 - No incentives
J00 = pd.read_csv(r"/Users/rafaelcosta/Documents/GitHub/InCES_model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_JPN_S0.csv")
#Scenario 1 - FIT
#J11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-01.csv")
#J12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-02.csv")
#J13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-03.csv")
#Scenario 2 - TAX
#J21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-01.csv")
#J22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-02.csv")
#J23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-03.csv")
#Scenario 3 - TGC
#J31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-01.csv")
#J32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-02.csv")
#J33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-03.csv")

##Epsilon
#Scenario 0 - No incentives
N00 = pd.read_csv(r"/Users/rafaelcosta/Documents/GitHub/InCES_model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_NLD_S0.csv")
#Scenario 1 - FIT
#N11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_NLD_S1-01.csv")
#N12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_NLD_S1-02.csv")
#N13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_NLD_S1-03.csv")
#Scenario 2 - TAX
#N21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_NLD_S2-01.csv")
#N22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_NLD_S2-02.csv")
#N23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_NLD_S2-03.csv")
#Scenario 3 - TGC
#N31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_NLD_S3-01.csv")
#N32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_NLD_S3-02.csv")
#N33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_NLD_S3-03.csv")

##Zeta
#Scenario 0 - No incentives
U00 = pd.read_csv(r"/Users/rafaelcosta/Documents/GitHub/InCES_model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_USA_S0.csv")
#Scenario 1 - FIT
#U11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-01.csv")
#U12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-02.csv")
#U13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-03.csv")
#Scenario 2 - TAX
#U21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-01.csv")
#U22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-02.csv")
#U23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-03.csv")
#Scenario 3 - TGC
#U31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-01.csv")
#U32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-02.csv")
#U33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-03.csv")


#### Datacube creation
###Scenario 0 - Data Frame
##Collectio
A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
#tick1
for i in ticks[1::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A1.append(z)
#tick2
for i in ticks[2::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A2.append(z)
#tick3
for i in ticks[3::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A3.append(z)
#tick4
for i in ticks[4::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A4.append(z)
#tick5
for i in ticks[5::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A5.append(z)
#tick6
for i in ticks[6::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A6.append(z)
#tick7
for i in ticks[7::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A7.append(z)
#tick8
for i in ticks[8::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A8.append(z)
#tick9
for i in ticks[9::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A9.append(z)
#tick10
for i in ticks[10::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A10.append(z)
#tick11
for i in ticks[11::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A11.append(z)
#tick12
for i in ticks[12::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A12.append(z)
#tick13
for i in ticks[13::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A13.append(z)
#tick14
for i in ticks[14::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A14.append(z)
#tick15
for i in ticks[15::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A15.append(z)
#tick16
for i in ticks[16::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    A16.append(z)
#tick17
for i in ticks[17::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    B17.append(z)
#tick18
for i in ticks[18::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    B18.append(z)
#tick19
for i in ticks[19::20]: 
    z = A00["ActiveCommunities"].iloc[i]
    B19.append(z)
#tick0
for i in ticks[0::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B0.append(z)

###Graph building
#dirty_graph_pdi = df["pdi"]
#g_pdi = pd.DataFrame([x for x in dirty_graph_pdi if str(x) != 'nan'])
#m_pdi, s_pdi = stats.norm.fit(g_pdi)  


###Plotting
#fig, ax = plt.subplots()
#g_pdi.plot.hist(density=True, ax=ax, color="#66b3ff")
#g_pdi.plot.kde(ax=ax, legend=False, title='Power Distance Distribution', color = 'orange')
#plt.axvline(m_pdi, color='k', linestyle='dashed', linewidth=1)
#plt.xlabel('Power Distance Index')
#plt.legend(["Distribution function", "mean", "Power Distance freq"])
#plt.show()
