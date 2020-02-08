#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:24:02 2020

@author: rafael
"""
###Imports
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import pandas as pd
import numpy as np
import statistics
from scipy import stats
from scipy.stats import uniform
import matplotlib.pylab as plt
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


###Datasets import
##AUSTRALIA
#Scenario 0 - No incentives
A00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_AUS_s0.csv")
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

##BRAZIL
#Scenario 0 - No incentives
B00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_BRA_S0.csv")
#Scenario 1 - FIT
#B11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-01.csv")
#B12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-02.csv")
#B13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-03.csv")
#Scenario 2 - TAX
#B21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-01.csv")
#B22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-02.csv")
#B23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-03.csv")
#Scenario 3 - TGC
#B31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-01.csv")
#B32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-02.csv")
#B33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-03.csv")

##IRAN
#Scenario 0 - No incentives
I00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_IRA_S0.csv")
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

##JAPAN
#Scenario 0 - No incentives
J00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_JPN_S0.csv")
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

##NETHERLANDS
#Scenario 0 - No incentives
N00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_NLD_S0.csv")
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

##USA
#Scenario 0 - No incentives
U00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_USA_S0.csv")
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
A1, A2, B1, B2, I1, I2, J1, J2, N1, N2, U1, U2 = [], [], [], [], [], [], [], [], [], [], [], []

for j in range(2):
    for i in ticks[j::20]: 
        a0 = A00["ActiveCommunities"].iloc[i]
        b0 = B00["ActiveCommunities"].iloc[i]
        i0 = I00["ActiveCommunities"].iloc[i]
        j0 = J00["ActiveCommunities"].iloc[i]
        n0 = N00["ActiveCommunities"].iloc[i]
        u0 = U00["ActiveCommunities"].iloc[i]
        Aj.append(a0)
        Bj.append(b0)
        Ij.append(i0)
        Jj.append(j0)
        Nj.append(n0)
        Uj.append(u0)





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
