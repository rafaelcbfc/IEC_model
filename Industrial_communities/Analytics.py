#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:24:02 2020

@author: rafael
"""

import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import pandas as pd



###DataFrames import
##AUSTRALIA
#Scenario 0 - No incentives
AUS_S0 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_AUS_S0.csv")
#Scenario 1 - FIT
AUS_S1_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-01.csv")
AUS_S1_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-02.csv")
AUS_S1_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_AUS_S1-03.csv")
#Scenario 2 - TAX
AUS_S2_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-01.csv")
AUS_S2_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-02.csv")
AUS_S2_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_AUS_S2-03.csv")
#Scenario 3 - TGC
AUS_S3_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-01.csv")
AUS_S3_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-02.csv")
AUS_S3_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_AUS_S3-03.csv")

##BRAZIL
#Scenario 0 - No incentives
BRA_S0 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_BRA_S0.csv")
#Scenario 1 - FIT
BRA_S1_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-01.csv")
BRA_S1_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-02.csv")
BRA_S1_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_BRA_S1-03.csv")
#Scenario 2 - TAX
BRA_S2_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-01.csv")
BRA_S2_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-02.csv")
BRA_S2_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-03.csv")
#Scenario 3 - TGC
BRA_S3_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-01.csv")
BRA_S3_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-02.csv")
BRA_S3_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_BRA_S3-03.csv")

##IRAN
#Scenario 0 - No incentives
IRA_S0 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_IRA_S0.csv")
#Scenario 1 - FIT
IRA_S1_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_IRA_S1-01.csv")
IRA_S1_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_IRA_S1-02.csv")
IRA_S1_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_IRA_S1-03.csv")
#Scenario 2 - TAX
IRA_S2_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_IRA_S2-01.csv")
IRA_S2_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-02.csv")
IRA_S2_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_BRA_S2-03.csv")
#Scenario 3 - TGC
IRA_S3_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_IRA_S3-01.csv")
IRA_S3_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_IRA_S3-02.csv")
IRA_S3_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_IRA_S3-03.csv")

##JAPAN
#Scenario 0 - No incentives
JPN_S0 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_JPN_S0.csv")
#Scenario 1 - FIT
JPN_S1_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-01.csv")
JPN_S1_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-02.csv")
JPN_S1_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-03.csv")
#Scenario 2 - TAX
JPN_S2_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-01.csv")
JPN_S2_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-02.csv")
JPN_S2_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-03.csv")
#Scenario 3 - TGC
JPN_S3_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-01.csv")
JPN_S3_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-02.csv")
JPN_S3_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-03.csv")

##NETHERLANDS
#Scenario 0 - No incentives
NLD_S0 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_NLD_S0.csv")
#Scenario 1 - FIT
NLD_S1_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_NLD_S1-01.csv")
NLD_S1_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_NLD_S1-02.csv")
NLD_S1_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_NLD_S1-03.csv")
#Scenario 2 - TAX
NLD_S2_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_NLD_S2-01.csv")
NLD_S2_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_NLD_S2-02.csv")
NLD_S2_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_NLD_S2-03.csv")
#Scenario 3 - TGC
NLD_S3_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_NLD_S3-01.csv")
NLD_S3_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_NLD_S3-02.csv")
NLD_S3_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_NLD_S3-03.csv")

##USA
#Scenario 0 - No incentives
USA_S0 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_USA_S0.csv")
#Scenario 1 - FIT
USA_S1_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-01.csv")
USA_S1_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-02.csv")
USA_S1_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_USA_S1-03.csv")
#Scenario 2 - TAX
USA_S2_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-01.csv")
USA_S2_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-02.csv")
USA_S2_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_USA_S2-03.csv")
#Scenario 3 - TGC
#USA_S3_01 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-01.csv")
#USA_S3_02 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-02.csv")
#USA_S3_03 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_USA_S3-03.csv")

