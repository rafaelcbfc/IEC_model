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


##USA
#Scenario 0 - No incentives
U00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_USA_S0.csv")
#Scenario 1 - FIT
U11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-01.csv")
U12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-02.csv")
U13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-03.csv")
#Scenario 2 - TAX
U21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-01.csv")
U22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-02.csv")
U23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-03.csv")
#Scenario 3 - TGC
U31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-01.csv")
U32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-02.csv")
U33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-03.csv")

#### Datacube creation
###Scenario 0 - Data Frame
##Collectio
U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11, U12, U13, U14, U15, U16, U17, U18, U19 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
#tick1
for i in ticks[1::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U1.append(z)
#tick2
for i in ticks[2::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U2.append(z)
#tick3
for i in ticks[3::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U3.append(z)
#tick4
for i in ticks[4::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U4.append(z)
#tick5
for i in ticks[5::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U5.append(z)
#tick6
for i in ticks[6::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U6.append(z)
#tick7
for i in ticks[7::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U7.append(z)
#tick8
for i in ticks[8::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U8.append(z)
#tick9
for i in ticks[9::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U9.append(z)
#tick10
for i in ticks[10::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U10.append(z)
#tick11
for i in ticks[11::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U11.append(z)
#tick12
for i in ticks[12::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U12.append(z)
#tick13
for i in ticks[13::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U13.append(z)
#tick14
for i in ticks[14::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U14.append(z)
#tick15
for i in ticks[15::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U15.append(z)
#tick16
for i in ticks[16::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U16.append(z)
#tick17
for i in ticks[17::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U17.append(z)
#tick18
for i in ticks[18::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U18.append(z)
#tick19
for i in ticks[19::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U19.append(z)
#tick0
for i in ticks[0::20]: 
    z = U00["ActiveCommunities"].iloc[i]
    U0.append(z)