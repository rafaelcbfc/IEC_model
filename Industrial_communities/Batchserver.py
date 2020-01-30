#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:47:19 2019

@author: rafael
"""
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
from mesa.datacollection import DataCollector
from Model import Modelrun


##Batchrun
from mesa.batchrunner import BatchRunner
import pandas as pd

#Run parameters 
m_step_data = pd.DataFrame()
n_communities = [25]
n_industries = [25]

model_param = {"n_industries": n_industries, "n_communities": n_communities} #All variables in place - Everything that can be changed enters here

#Batchrun settings      
batch_run = BatchRunner(Modelrun, model_param, iterations = 1, max_steps = 1, model_reporters = {"Data Collector": lambda m: m.datacollector}, display_progress=True)
batch_run.run_all()

#Data generation
m_df = batch_run.get_model_vars_dataframe()
#a_df = batch_run.get_agent_vars_dataframe()
m_step_data = pd.DataFrame()
for i in range(len(m_df["Data Collector"])):
    if isinstance(m_df["Data Collector"][i], DataCollector):
        m_run_data = m_df["Data Collector"][i].get_model_vars_dataframe()
       #a_run_data = a_df["data Collector"][i].get_agent_vars_dataframe()
        m_step_data = m_step_data.append(m_run_data, ignore_index=True)
#m_step_data.to_csv("Model_run.csv")