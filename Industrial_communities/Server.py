#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:53:56 2019

@author: rafael
"""
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
from Model import Modelrun
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from Agents import Community
import Model

max_ind_size = Model.max_ind_size

#Agent visual element 
def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Layer": 0, "Filled": "true", "r": 0.25, "Color": "blue"}
    if type(agent) is Community:
        if agent.active == "Yes":
            color = "#85e085"
        else:
            color = "#cccccc"
        portrayal["Color"] = color
    return portrayal

#Model Parameters 
model_param = {"n_industries": UserSettableParameter("slider", "Total Industries", 50, 25, max_ind_size, 1),
               "n_communities": UserSettableParameter("slider", "Total Communities", 25,25, max_ind_size, 1)}

#Visual Grid formation 
grid = CanvasGrid(agent_portrayal, 15, 15, 500, 500)
chart = ChartModule([{"Label": "Industries", "Color": "#0055ff"},
                      {"Label": "Communities", "Color": "#cccccc"},
                      {"Label": "Active Communities", "Color": "#85e085"}])
server = ModularServer(Modelrun, [grid, chart], "InCES Model", model_param)
server.launch() 

#"n_communities": UserSettableParameter("slider", "Total Communities", 25,25, max_ind_size, 1)

