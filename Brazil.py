#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
##BRAZIL
#Scenario 0 - No incentives
B00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_BRA_S0.csv")
#Scenario 1 - FIT
B11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-01.csv")
B12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-02.csv")
B13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-03.csv")
#Scenario 2 - TAX
B21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-01.csv")
B22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-02.csv")
B23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-03.csv")
#Scenario 3 - TGC
B31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-01.csv")
B32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-02.csv")
B33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-03.csv")


#### Datacube creation
###Scenario 0 - Data Frame
##Collectio
B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
#tick1
for i in ticks[1::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B1.append(z)
#tick2
for i in ticks[2::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B2.append(z)
#tick3
for i in ticks[3::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B3.append(z)
#tick4
for i in ticks[4::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B4.append(z)
#tick5
for i in ticks[5::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B5.append(z)
#tick6
for i in ticks[6::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B6.append(z)
#tick7
for i in ticks[7::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B7.append(z)
#tick8
for i in ticks[8::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B8.append(z)
#tick9
for i in ticks[9::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B9.append(z)
#tick10
for i in ticks[10::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B10.append(z)
#tick11
for i in ticks[11::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B11.append(z)
#tick12
for i in ticks[12::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B12.append(z)
#tick13
for i in ticks[13::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B13.append(z)
#tick14
for i in ticks[14::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B14.append(z)
#tick15
for i in ticks[15::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B15.append(z)
#tick16
for i in ticks[16::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B16.append(z)
#tick17
for i in ticks[17::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B17.append(z)
#tick18
for i in ticks[18::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B18.append(z)
#tick19
for i in ticks[19::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B19.append(z)
#tick0
for i in ticks[0::20]: 
    z = B00["ActiveCommunities"].iloc[i]
    B0.append(z)




































