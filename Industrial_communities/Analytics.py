#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:24:02 2020

@author: rafael
"""

import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")

import pandas as pd



####DataFrames import
###Australia
##Scenario 0 - No incentives
AUSS_S0 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentives/Model_run_AUS_S0.csv")
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