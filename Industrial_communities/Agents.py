#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rafael

@Address: https://github.com/rafaelcbfc/InCES_model/blob/master/Industrial_communities/Agents.py

"""
###Model agents
##Imports
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import Data
import random
import numpy as np
from mesa import Agent
from scipy.stats import uniform


##Variables
#General variables
park_limit = 15 #Size of the park grid layout (15 x 15 squares)
gridtariff = Data.gridtariff
decision_style = Data.Decision_style 
decision_rule = Data.Decision_rule


## Interaction functions
def askforInvestment(com, member): #for project execution ask for investment to shareholders
    if com.request < member.wealth:
        com.wealth = com.wealth + com.request
        member.invested = member.invested + com.request
        member.wealth = member.wealth - com.request
    else:
        print("investment denied")     
    return com.wealth
        
def voting(com, member): #Voting process during meetings
    if com.strategy == 0:
        if com.project_tariff < gridtariff and com.business_plan == "Feasible":
            member.vote = 1
        else: member.vote = 1
    
    if com.strategy == 1:
        if com.project_margin >= member.ROI and com.business_plan == "Feasible":
            member.vote = 1
        else:
            member.vote = -1
    
    com.voting_result = com.voting_result + member.vote
    #print(str(com.voting_result) + " " + str(member.ROI))

##Industry
class Industry(Agent): #Industry agent propoerties
    def __init__(self, name, pos, model):
        super().__init__(name, model)
        self.CBA = 0
        self.CBAp = 0
        self.community_loyalty = 0
        self.decision_style = random.choice(decision_style)
        self.decision_rule = random.choice(decision_rule)
        self.energy = np.random.choice(uniform.rvs(size=10000, loc = 200, scale=30000)) #value in KWh from a distribution between 200KWh and 30MWh
        self.energy_time_check = list(range(0,240,12))
        self.eng_lvl = 0
        self.id = name 
        self.invested = 0
        self.motivated_friends = 0
        self.friends = []
        self.period = int(0)
        self.pos = pos
        self.ROI = 0
        self.energy_rtn = 0
        self.smallworld = []
        self.strategy = random.randrange(0,2) #0 - "energy generation" / 1 - "profit increase"
        self.vote = 0
        self.wealth = 100000000
        self.which_community = 0 
        
        
#Industry functions
#tick actions 
    def step(self): #Action per tick
        self.updateNeighbors()
        self.engagementLevel()
        self.createCommunity()
        self.joinCommunity()
        if self.eng_lvl == 1 or 2:
            print(" id " + str(self.id) + " eng_lvl " + str(self.CBA))
        self.period = self.period + 1
       
    
    def createCommunity(self): #create a community
        if self.period in self.energy_time_check and self.eng_lvl == 5:
            self.industryNetwork()
            if self.eng_lvl == 99 and self.which_community == 0: 
                for com in [x for x in self.c_neighbors if x.active == "No"]: break
                self.which_community = com.name
                com.members.append(self)
                com.strategy = self.strategy
                com.active = "Yes"
                for f in self.smallworld:
                    if f.id in self.friends:
                        f.which_community = com.name
                        com.members.append(f)
        
    
    def engagementLevel(self): #Define engagement level of each industry
        if self.period in self.energy_time_check:
            self.energy = np.random.choice(uniform.rvs(size=10000, loc = 200, scale=30000))
            if self.eng_lvl in [0, 1, 2, 5]:
                Data.cbaCalc(self)
                if self.CBA == "unfavorable":
                    self.eng_lvl = 1
                elif self.CBA == "favorable":
                        for c in self.c_neighbors:
                            if c.active == "No":
                                pass
                            if c.active == "Yes":
                                if c.strategy == self.strategy:
                                    Data.cbaCalc(self, c)
                                    if self.CBAp == "favorable":
                                        self.eng_lvl = 10
                                        self.which_community == c.name
                                        break
                                    else: 
                                        pass

                        #If no communities exists, look for industries
                        for i in self.i_neighbors:
                            if self.eng_lvl not in [1, 10]:
                                Data.cbaCalc(self, i)
                                if self.CBA == "unfavorable":
                                    self.eng_lvl = 2
                                if self.CBA == "favorable":
                                    self.eng_lvl = 5
        else:
            pass
    

    def joinCommunity(self):
            pass
                #print("3 id2 " + str(self.id) + " eng_lvl " + str(self.eng_lvl) + " com " + str(self.which_community))
            #pay to enter
           
                
            
    def industryNetwork(self): #Creates the strong network
        self.smallworld = []    
        neighbors = [agent for agent in self.i_neighbors if type(agent) == Industry]
        vicinity = list(self.model.G.neighbors(self.id))
        self.smallworld = [agent for agent in neighbors if agent.id in vicinity]
        for f in self.smallworld:
            if f.eng_lvl == 5 or 10:
                self.friends.append(f.id)
        if len(self.friends) > 0 and len(self.friends)/len(self.smallworld) >= 0.5: 
            self.eng_lvl = 99
            for f in self.smallworld:
                if f.id in self.friends:
                    f.eng_lvl = 99


    def leaveCommunity(self):
        pass
              
    def retunofInvestment(self): #Return of Investment function used on voting
        if self.rtn == 0: #if received energy
            energy_return = self.energy * gridtariff
            self.ROI = (energy_return - self.invested)/self.invested
        
        if self.rtn > 0: #if received money
            self.ROI = (self.rtn - self.invested)/self.invested
        
        else:
            pass
    
    def updateNeighbors(self): #create a list of neighbors in the Industrial Park
        global c_neighbors, i_neighbors
        self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=20)
        self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
        self.c_neighbors = [x for x in self.neighbors if type(x) is Community]
        self.i_neighbors = [x for x in self.neighbors if type(x) is Industry]
 

##Community
class Community(Agent):
    def __init__(self, name, pos, activity, model):
        super().__init__(name, model)
        self.active = activity
        self.business_plan = 0 
        self.energy = 0
        self.dividend_time = list(range(0,240,12))
        self.invested_capital = 0
        self.investment = 0
        self.members = []
        self.name = name
        self.period = 0
        self.pos = pos
        self.premium = 0
        self.project_cost= 0 
        self.project_margin = 0
        self.plan_execution = "" 
        self.request = 0
        self.revenue = 0
        self.solar_tariff = 0
        self.strategy = 0
        self.voting_result = 0
        self.wealth = 0 
        self.wind_tariff = 0
        
        
#Community functions   
    def step(self):
         if self.active == "Yes":
            self.communityEnergy()
            self.initialInvestment()
            Data.projectSelector(self)
            self.businessPlan()
            self.meetings()
            self.planExecution()
            self.policyEntrepeneur()
            self.newMemberFee()
            
            self.project_cost = 0 #Add this to a function
            self.period = self.period + 1 
         else:
            None
         
        #print("start com id " + str(self.name) )
        #print("wind energy " + str(self.wind_energy) + " wind tariff " + str(self.LCOE_wind) + " wind OM " + str(wind_OM) + " wind inv " + str(investment_wind))
        #print("solar energy " + str(self.solar_energy) + " solar tariff " + str(self.LCOE_solar) + " solar OM " + str(solar_OM) + " solar inv " + str(investment_solar))
        #print("Project revenue " + str(project_revenue) + " project cost " + str(self.project_cost))
        #print("project margin " + str(self.project_margin))
            
    def newMemberFee(self):
        self.premium = (self.LCOE_solar + self.LCOE_wind)/2
        #print("premium " + str(self.premium))
        #print("")
    
    def communityEnergy(self): #update every tick the member list
        if len(self.members) == 0:
            self.active = "No" 
        else:
            if self.period in self.dividend_time:
                self.energy = 0
                for member in self.members:
                   self.energy = self.energy + member.energy
        
    
    def initialInvestment(self):#Initial investment by founders
        if self.active == 'Yes' and self.period == 0:
            self.projectSelector()
            self.invested_capital = self.project_cost/len(self.members)  
            for member in self.members:
                try:
                    member.wealth = member.wealth - self.invested_capital
                except:
                    print("no cash" + str(member.id))
                self.wealth = self.wealth + self.invested_capital
        #print("wealth " + str(self.wealth))

        
    def businessPlan(self):
        if self.project_margin < 0:
            self.business_plan = "Unfeasible" 
        if self.project_margin > 0:
            self.business_plan = "Feasible"   
            self.investment = self.project_cost - self.wealth
        #print("business plan " + str(self.business_plan))
    
    def askRevenue(self): #Ask for revenue if wealth is below 0
        try:
            self.request = self.investment / len(self.members)
        except:
             print("empty member list " + str(self.name))
        for member in self.members:
           askforInvestment(self, member)
    
        
    def meetings(self): #Schedule a meeting with its members
        self.volting_result = 0 
        for member in self.members:
             voting(self, member)
        if self.voting_result > 0:
            self.plan_execution = "Approved"
        else:
            self.plan_execution = "Rejected"
       
        
    def planExecution(self):
        if self.plan_execution == "Approved":
            self.wealth = self.wealth - self.project_cost
            rvn = self.solar_energy * self.solar_tariff + self.wind_energy * self.wind_tariff
            self.wealth = self.wealth + rvn
            self.invested_capital = self.invested_capital + self.project_cost
            self.revenue =+ rvn
            #print("approved")    
        if self.plan_execution == "Rejected":
            pass
            #print("rejected")
    
    
    def policyEntrepeneur(self): #report to government how each period was compared to the past one
        pass
    

    def rtnFunc(self): #Financial return if strategy = 1
        if self.period in self.dividend_time: 
            for member in self.members:
                if self.strategy == 0:
                    member.rtn == 0 
                    
                if self.strategy == 1:
                    member.rtn = (self.revenue/len(self.members))
        else:
            pass
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        