#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rafael
"""

####Australia
###Imports
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import pandas as pd
import numpy as np


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
ticks0 = list(range(0,20000))
ticksS = list(range(0,10000))


###Datasets import
#Scenario 0 - No incentives
D00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_AUS_s0.csv")
#Scenario 1 - FIT
D11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-01.csv")
D12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-02.csv")
D13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-03.csv")
#Scenario 2 - TAX
D21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-01.csv")
D22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-02.csv")
D23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-03.csv")
#Scenario 3 - TGC
D31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-01.csv")
D32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-02.csv")
D33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-03.csv")

#### Datacube creation
###Active Communities
d00, d11, d12, d13, d21, d22, d23, d31, d32, d33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
##Scenario 0 - Baseline
for i in range(20):
    y = []
    t = ticks0[i::20]
    for x in t:
        y.append(D00["ActiveCommunities"].iloc[x])
    d00["tick_{0}".format(i)]= y

##Scenario 1.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D11["ActiveCommunities"].iloc[x])
    d11["tick_{0}".format(i)]= y
##Scenario 1.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D12["ActiveCommunities"].iloc[x])
    d12["tick_{0}".format(i)]= y
##Scenario 1.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D13["ActiveCommunities"].iloc[x])
    d13["tick_{0}".format(i)]= y

##Scenario 2.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D21["ActiveCommunities"].iloc[x])
    d21["tick_{0}".format(i)]= y
##Scenario 2.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D22["ActiveCommunities"].iloc[x])
    d22["tick_{0}".format(i)]= y
##Scenario 2.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D23["ActiveCommunities"].iloc[x])
    d23["tick_{0}".format(i)]= y

##Scenario 3.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D31["ActiveCommunities"].iloc[x])
    d31["tick_{0}".format(i)]= y
##Scenario 3.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D32["ActiveCommunities"].iloc[x])
    d32["tick_{0}".format(i)]= y
##Scenario 3.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D33["ActiveCommunities"].iloc[x])
    d33["tick_{0}".format(i)]= y
    
Ac_S0 = [sum(v)/1000 for v in d00.values()]
Ac_S11 = [sum(v)/500 for v in d11.values()]
Ac_S12 = [sum(v)/500 for v in d12.values()]
Ac_S13 = [sum(v)/500 for v in d13.values()]
Ac_S1 = np.average((Ac_S11, Ac_S12, Ac_S13), axis=0)
Ac_S21 = [sum(v)/500 for v in d21.values()]
Ac_S22 = [sum(v)/500 for v in d22.values()]
Ac_S23 = [sum(v)/500 for v in d23.values()]
Ac_S2 = np.average((Ac_S21, Ac_S22, Ac_S23), axis=0)
Ac_S31 = [sum(v)/500 for v in d31.values()]
Ac_S32 = [sum(v)/500 for v in d32.values()]
Ac_S33 = [sum(v)/500 for v in d33.values()]
Ac_S3 = np.average((Ac_S31, Ac_S32, Ac_S33), axis=0)


###Member population
d00, d11, d12, d13, d21, d22, d23, d31, d32, d33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
##Scenario 0 - Baseline
for i in range(20):
    y = []
    t = ticks0[i::20]
    for x in t:
        y.append(D00["Community Members"].iloc[x])
    d00["tick_{0}".format(i)]= y

##Scenario 1.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D11["Community Members"].iloc[x])
    d11["tick_{0}".format(i)]= y
##Scenario 1.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D12["Community Members"].iloc[x])
    d12["tick_{0}".format(i)]= y
##Scenario 1.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D13["Community Members"].iloc[x])
    d13["tick_{0}".format(i)]= y

##Scenario 2.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D21["Community Members"].iloc[x])
    d21["tick_{0}".format(i)]= y
##Scenario 2.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D22["Community Members"].iloc[x])
    d22["tick_{0}".format(i)]= y
##Scenario 2.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D23["Community Members"].iloc[x])
    d23["tick_{0}".format(i)]= y

##Scenario 3.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D31["Community Members"].iloc[x])
    d31["tick_{0}".format(i)]= y
##Scenario 3.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D32["Community Members"].iloc[x])
    d32["tick_{0}".format(i)]= y
##Scenario 3.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D33["Community Members"].iloc[x])
    d33["tick_{0}".format(i)]= y
    
M_S00 = [sum(v)/1000 for v in d00.values()]
M_S11 = [sum(v)/500 for v in d11.values()]
M_S12 = [sum(v)/500 for v in d12.values()]
M_S13 = [sum(v)/500 for v in d13.values()]
M_S1 = np.average((M_S11, M_S12, M_S13), axis=0)
M_S21 = [sum(v)/500 for v in d21.values()]
M_S22 = [sum(v)/500 for v in d22.values()]
M_S23 = [sum(v)/500 for v in d23.values()]
M_S2 = np.average((M_S21, M_S22, M_S23), axis=0)
M_S31 = [sum(v)/500 for v in d31.values()]
M_S32 = [sum(v)/500 for v in d32.values()]
M_S33 = [sum(v)/500 for v in d33.values()]
M_S3 = np.average((M_S31, M_S32, M_S33), axis=0)


###Solar Energy
d00, d11, d12, d13, d21, d22, d23, d31, d32, d33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
##Scenario 0 - Baseline
for i in range(20):
    y = []
    t = ticks0[i::20]
    for x in t:
        y.append(D00["Community Members"].iloc[x])
    d00["tick_{0}".format(i)]= y

##Scenario 1.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D11["Community Members"].iloc[x])
    d11["tick_{0}".format(i)]= y
##Scenario 1.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D12["Community Members"].iloc[x])
    d12["tick_{0}".format(i)]= y
##Scenario 1.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D13["Community Members"].iloc[x])
    d13["tick_{0}".format(i)]= y

##Scenario 2.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D21["Community Members"].iloc[x])
    d21["tick_{0}".format(i)]= y
##Scenario 2.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D22["Community Members"].iloc[x])
    d22["tick_{0}".format(i)]= y
##Scenario 2.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D23["Community Members"].iloc[x])
    d23["tick_{0}".format(i)]= y

##Scenario 3.1
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D31["Community Members"].iloc[x])
    d31["tick_{0}".format(i)]= y
##Scenario 3.2
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D32["Community Members"].iloc[x])
    d32["tick_{0}".format(i)]= y
##Scenario 3.3
for i in range(20):
    y = []
    t = ticksS[i::20]
    for x in t:
        y.append(D33["Community Members"].iloc[x])
    d33["tick_{0}".format(i)]= y
    
M_S00 = [sum(v)/1000 for v in d00.values()]
M_S11 = [sum(v)/500 for v in d11.values()]
M_S12 = [sum(v)/500 for v in d12.values()]
M_S13 = [sum(v)/500 for v in d13.values()]
M_S1 = np.average((M_S11, M_S12, M_S13), axis=0)
M_S21 = [sum(v)/500 for v in d21.values()]
M_S22 = [sum(v)/500 for v in d22.values()]
M_S23 = [sum(v)/500 for v in d23.values()]
M_S2 = np.average((M_S21, M_S22, M_S23), axis=0)
M_S31 = [sum(v)/500 for v in d31.values()]
M_S32 = [sum(v)/500 for v in d32.values()]
M_S33 = [sum(v)/500 for v in d33.values()]
M_S3 = np.average((M_S31, M_S32, M_S33), axis=0)
