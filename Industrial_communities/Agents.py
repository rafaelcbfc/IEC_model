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
gridtariff = Data.gridtariff
decision_style = Data.decision_style 
decision_rule = Data.decision_rule


## Interaction functions
def askforInvestment(com, member): #for project execution ask for investment to shareholders
    com.wealth += com.request
    member.invested += com.request
    member.loyalty -= 1
 
       
def voting(com, member): #Voting process during meetings
    com.voting_result = 0
    if com.strategy == 0:
        if com.project_tariff < gridtariff and com.business_plan == "Feasible":
            member.vote = 1
        else: member.vote = 0
    
    elif com.strategy == 1:
        if com.project_margin >= member.expected_return and com.business_plan == "Feasible":
            member.vote = 1
        else: member.vote = 0
    
    com.voting_result +=  member.vote
    member.community_vote = com.voting_result / len(com.members)   

    
##Industry
class Industry(Agent): #Industry agent propoerties
    def __init__(self, name, pos, model):
        super().__init__(name, model)
        self.aff = []
        self.cba_lvl = 0
        self.cba_lvlc = 0
        self.cba_lvlp = 0
        self.com_premium = 0
        self.community_vote = 0
        self.decision_style = random.choice(decision_style)
        self.decision_rule = random.choice(decision_rule)
        self.energy = 0
        self.energy_time_check = list(range(0,240,12))
        self.eng_lvl = 0
        self.expected_return = random.uniform(0,5) # -------> Check value
        self.friends = []
        self.id = name 
        self.invested = 0
        self.LCOE = 0
        self.loyalty = 0
        self.max_re = 0
        self.payment = 0
        self.period = 0
        self.pos = pos
        self.ROI = 0
        self.retrn = 0
        self.energy_rtn = 0
        self.smallworld = []
        self.strategy = random.randrange(0,2) #0 - "energy generation" / 1 - "profit increase"
        self.threshold = 12
        self.vote = 0
        self.which_community = 0 
       
        
#Industry functions
#tick actions 
    def step(self): #Action per tick
        self.energy = 0
        self.LCOE = 0
        self.updateNeighbors()
        self.energyLevel()
        self.engagementLevel()
        self.createCommunity()
        self.returnofInvestment()
        self.leaveCommunity()
        self.period = self.period + 1
        #print("ID " + str(self.id) + ' style ' + str(self.decision_style) + ' rule ' + str(self.decision_rule))
        #print("ID " + str(self.id) + ' cba_lvl ' + str(self.cba_lvl) + ' cba_lvlp ' + str(self.cba_lvlp) + ' cba_lvlc ' + str(self.cba_lvlc) + ' eng_lvl ' + str(self.eng_lvl))
        #print("ID " + str(self.id) +  ' LCOE ' + str(self.LCOE) + ' com ' + str(self.which_community))
        
 
    def updateNeighbors(self): #create a list of nglobal c_neighbors, i_neighbors
        self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=20)
        self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
        self.c_neighbors = [x for x in self.neighbors if type(x) is Community]
        self.i_neighbors = [x for x in self.neighbors if type(x) is Industry]      
        
    
    def energyLevel(self):  #value in KWh from a distribution between 200KWh and 30MWh
        if self.period in self.energy_time_check:
            self.energy = np.random.choice(uniform.rvs(size=10000, loc = 200, scale=30000))     

    
    def engagementLevel(self): #Define engagement level of each industry
        if self.period in self.energy_time_check and self.eng_lvl not in [5, 10, 98, 99]:
                Data.cbaCalc(self)
                if self.cba_lvl in [1, 2, 3]:
                    if self.cba_lvl == 1:
                        self.eng_lvl = 1
                    if self.cba_lvl in [2,3]:
                            for community in self.c_neighbors: #Search for a community to join
                                if community.active == "Yes":
                                    Data.cbaCalcCom(self, community)
                                    if self.cba_lvlc == 1:
                                        self.eng_lvl = 10
                                        self.which_community = community.name
                                        community.members.append(self)
                                        self.joinCommunity()
                                        break
                                    
                    if self.eng_lvl not in [1, 10, 98, 99]:
                            for neighbor in self.i_neighbors: #If no communities exists, look for industries
                                Data.cbaCalcPeer(self, neighbor)
                                if self.cba_lvlp == 1:
                                        self.eng_lvl = 2
                                if self.cba_lvlp == 2:
                                        self.eng_lvl = 5
                                        neighbor.eng_lvl = 5
                                        self.strategy = 0
                                        neighbor.strategy = 0
                                        break
                                if self.cba_lvlp == 3:
                                        self.eng_lvl = 5
                                        neighbor.eng_lvl = 5
                                        self.strategy = 1
                                        neighbor.strategy = 1
                                        break
        else:
            pass
        
            
    def createCommunity(self): #create a community
        if self.period in self.energy_time_check and self.eng_lvl == 5:
            self.industryNetwork()
            if self.eng_lvl == 99 and self.which_community == 0: 
                for community in [x for x in self.c_neighbors if x.active == "No"]: break
                self.which_community = community.name
                community.members.append(self)
                community.strategy = self.strategy
                community.active = "Yes"
                for f in self.smallworld:
                    if f.eng_lvl == 98:
                       f.which_community = community.name
                       community.members.append(f)
    
               
    def industryNetwork(self): #Creates the strong network
        self.smallworld = []    
        neighbors = [agent for agent in self.i_neighbors if type(agent) == Industry]
        vicinity = list(self.model.G.neighbors(self.id))
        self.smallworld = [agent for agent in neighbors if agent.id in vicinity]
        for f in self.smallworld:
            if f.eng_lvl == 5:
                self.friends.append(f.id)
            if f.eng_lvl == 10:
                self.aff.append(f.id)
        if len(self.friends) > 0 and len(self.friends + self.aff)/len(self.smallworld) >= 0.5: 
            self.eng_lvl = 99
            for f in self.smallworld:
                if f.id in self.friends:
                    f.eng_lvl = 98
    
        
    def joinCommunity(self):
        print('id ' + str(self.id) + ' invested ' + str(self.invested))
        if self.invested == 0 or self.com_premium == 0:
            self.invested = self.energy * gridtariff
        else:
            self.invested += self.energy + self.com_premium
        print('ID ' + str(self.id) +  ' invested ' + str(self.invested))
        
              
    def returnofInvestment(self): #Return of Investment function used on voting
        
        if self.which_community != 0:
            print('ID ' + str(self.id) + ' com ' + str(self.which_community) + ' premium ' + str(self.com_premium))
            if self.com_premium == 0: pass
            else: self.ROI = self.retrn / self.invested 
            print('ROI ' + str(self.ROI))
           
        else: pass
 
    
    def decisionStyle(self): #community voted how I believe?
        ratio = self.community_vote
        if self.decision_style <= 33: #Unanimity
            if ratio >=0.8:
                self.loyalty += 1
            if ratio <= 0.3:
                self.loyalty += -1
        elif self.decision_style > 33 and self.decision_style <= 66: #Majority
            if ratio >= 0.5:
                self.loyalty += 1
            if ratio < 0.5:
                self.loyalty += -1
        elif self.decision_style > 66:#Hierarchy
            if ratio < 0.5:
                self.loyalty += 1
            if ratio > 0.5:
                self.loyalty += -1
     
        
    def decisionRule(self): #Was my option chosen?
        if self.decision_rule <= 33: #confrontation
            if self.vote == 1 and self.community_vote > 0: 
                self.loyalty += 1
            else:
                self.loyalty += -1
        if self.decision_rule > 33 and self.decision_rule <=66: #bargaining
            self.threshold = 24 #longer slack for tolerance
            if self.vote == 1 and self.community_vote > 0: 
                self.loyalty += 1
            else:
                self.loyalty += -1
        if self.decision_rule > 66:
            if self.vote ==1 and self.community_vote > 0:
                self.loyalty += 1
            else:
                self.loyalty += 0


    def leaveCommunity(self): #leaving the community ---> Add decision style here
        self.decisionStyle()
        self.decisionRule()
        if self.loyalty >= self.threshold:
                if self.ROI < 0.1:# -----> To be defined
                    self.which_community = 0

##Community
class Community(Agent):
    def __init__(self, name, pos, activity, model):
        super().__init__(name, model)
        self.active = activity
        self.business_plan = 0 
        self.costs = 0
        self.energy = 0
        self.energy_solar = 0
        self.energy_wind = 0
        self.energy_total = 0
        self.energy_total_solar = 0
        self.energy_total_wind = 0
        self.gov_fit = 0
        self.gov_tax = 0
        self.incentive_fit = 0
        self.incentive_tax = 0
        self.investment = 0
        self.meeting_time = list(range(0,240,12))
        self.members = []
        self.name = name
        self.period = 0
        self.pos = pos
        self.policy_entrepreneur = 0
        self.premium = 0
        self.project_cost = 0 
        self.project_margin = 0
        self.project_tariff0 = 0
        self.project_tariff1 = 0
        self.project_time = list(range(1,240,12))
        self.plan_execution = "" 
        self.request = 0
        self.revenue = 0
        self.sale0 = 0
        self.sale1 = 0
        self.strategy = 0
        self.voting_result = 0
        self.wealth = 0    
        
        
        
#Community functions   
    def step(self):
        self.energy = 0
        self.plan_execution = 0
        self.request = 0
        self.sale = 0
        if self.active == 'Yes':
           self.energyDemand()
           self.initialInvestment()
           self.projectDefinition()
           self.meetings()
           self.planExecution()
           self.policyEntrepeneur()
           self.newMemberFee()
           self.rtnFunc()
           self.period = self.period + 1 
        
        if self.active == 'No':
           pass
        print('Com ID ' + str(self.name) + ' Active ' + str(self.active) + ' wealth ' + str(self.wealth))
        
        
    def energyDemand(self): #update the member list
        if len(self.members) == 0:
            self.active = 'No' 
        else:
            if self.period in self.meeting_time:
                for member in self.members:
                   self.energy = self.energy + member.energy    
                
        
    def initialInvestment(self):#Initial investment by founders
        if self.active == 'Yes' and self.period == 0:
            Data.projectSelector(self)
            invested_capital = (self.project_cost * 1.2)/len(self.members) 
            self.wealth += invested_capital * len(self.members)
            for member in self.members:
                member.invested = invested_capital
    
    
    def projectDefinition(self): #Choose what type of project to be done: All solar, All wind or mixed
        Data.projectSelector(self)
        if self.project_margin <= 0:
            self.business_plan = "Unfeasible" 
            pass
        elif self.project_margin > 0:
            self.business_plan = "Feasible"   
            if self.project_cost >= self.wealth:
                self.policy_entrepreneur += -1    
                self.investment = self.project_cost - self.wealth
                self.request = self.investment / len(self.members)
                for member in self.members:
                   askforInvestment(self, member)
            else:
                None
    
    
    def meetings(self): #Schedule a meeting with members
        for member in self.members:
             voting(self, member)
        if self.voting_result > len(self.members)/2:
            self.plan_execution = "Approved"
        else:
            self.plan_execution = "Rejected"
                
        
    def planExecution(self): #For approved plans, execute and revenue
        if self.period in self.project_time:
            if self.plan_execution == "Approved":
                self.wealth = self.wealth - self.project_cost #Pay for project
                self.energy_total += (self.energy_solar + self.energy_wind) #Increase generation park
                self.sale0 = ((self.energy_solar + self.energy_wind)) * self.project_tariff0 #Produce energy
                self.sale1 = self.project_tariff1 * (self.energy_solar + self.energy_wind)
                
                #Cummulative measures
                if self.strategy == 0:
                    self.wealth += self.sale0
                    self.revenue += self.sale0
                if self.strategy == 1:
                    self.wealth += self.sale1
                    self.revenue += self.sale1
                    
                self.costs += self.project_cost 
                self.energy_total_solar += self.energy_solar
                self.energy_total_total += self.energy_wind
                self.gov_fit += self.incentive_fit
                self.gov_tax += self.incentive_tax
            
            if self.plan_execution == "Rejected":
                self.wealth -= (self.energy * Data.gridtariff)
                self.costs += (self.energy * Data.gridtariff)
                for member in self.members:
                    member.loyalty += -1
        else:
            pass

        
    def newMemberFee(self): #Calculate how much does it cost to a new member to join
        try:
            ratios = self.energy_solar_total/self.energy_total
            ratiow = self.energy_wind_total/self.energy_total
        except:
            ratios = 0.5
            ratiow = 0.5
        try:
            LCOE_wind = (self.costs * ratiow)/(self.energy_wind_total)
        except:
            LCOE_wind = 0
        try:
            LCOE_solar = (self.costs * ratios)/(self.energy_solar_total)
        except: 
            LCOE_solar = 0
        
        self.premium = (LCOE_solar * ratios) + (LCOE_wind * ratiow) 
        for member in self.members:
            member.com_premium = self.premium
        
    
    def rtnFunc(self): #Financial return if strategy = 1
        if self.period in self.meeting_time: 
            delta =  Data.gridtariff - self.premium
            for member in self.members:
                if self.strategy == 0:
                    member.retrn += delta * member.energy
                    pass
                elif self.strategy == 1:
                    member.retrn += ((self.sale1 - self.project_cost) * 0.7)/len(self.members)
                    pass
        else:
            pass 
    
    
    def policyEntrepeneur(self): #reportt how each period was compared to the past one
            #Able to generate projects
            if self.plan_execution == "Approved":
                self.policy_entrepreneur += 1
            elif self.plan_execution == "Rejeceted":
                self.policy_entrepreneur += - 1     
            #Profitable
            if self.revenue/self.costs > 1:
                self.policy_entrepreneur += 1   
            elif self.revenue/self.costs <= 1:
                self.policy_entrepreneur += -1
            

        
        
        
        

   
        
        
        
        
        
        
        