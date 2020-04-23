#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rafael
"""

####Japan
###Imports
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import pandas as pd
import numpy as np


###Definitions
##Tick set
ticks0 = list(range(0,20000))
ticksS = list(range(0,10000))

###Datasets import
##JAPAN
#Scenario 0 - No incentives
D00 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S0 - No incentive/Model_run_JPN_S0.csv")
#Scenario 1 - FIT
D11 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-01.csv")
D12 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-02.csv")
D13 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S1 - FIT/Model_run_JPN_S1-03.csv")
#Scenario 2 - TAX
D21 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-01.csv")
D22 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-02.csv")
D23 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S2 - TAX/Model_run_JPN_S2-03.csv")
#Scenario 3 - TGC
D31 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-01.csv")
D32 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-02.csv")
D33 = pd.read_csv(r"/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Modelrun/S3 - TGC/Model_run_JPN_S3-03.csv")

####Datacube creation
###Variables
c00, c11, c12, c13, c21, c22, c23, c31, c32, c33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
e00, e11, e12, e13, e21, e22, e23, e31, e32, e33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
g00, g11, g12, g13, g21, g22, g23, g31, g32, g33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
i00, i11, i12, i13, i21, i22, i23, i31, i32, i33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
m00, m11, m12, m13, m21, m22, m23, m31, m32, m33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
p00, p11, p12, p13, p21, p22, p23, p31, p32, p33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
s00, s11, s12, s13, s21, s22, s23, s31, s32, s33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
w00, w11, w12, w13, w21, w22, w23, w31, w32, w33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
x00, x11, x12, x13, x21, x22, x23, x31, x32, x33 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

###Data collection
##Scenario 0 - Baseline
for i in range(20):
    C, E, I, M, P, S, W = [],[], [], [], [], [], []
    for x in ticks0[i::20]:
        C.append(D00["ActiveCommunities"].iloc[x])
        E.append(D00["Member exit"].iloc[x])
        I.append(D00["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D00["Community Members"].iloc[x])
        P.append(D00["Policy Entrepreneur"].iloc[x])
        S.append(D00["Solar Energy"].iloc[x])
        W.append(D00["Wind Energy"].iloc[x])
    c00["tick_{0}".format(i)] = C
    e00["tick_{0}".format(i)] = E
    i00["tick_{0}".format(i)] = I
    m00["tick_{0}".format(i)] = M
    p00["tick_{0}".format(i)] = P
    s00["tick_{0}".format(i)] = S
    w00["tick_{0}".format(i)] = W

##Scenario 1 - FIT  
#Scenario 1.1 - FIT = 2.1
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D11["ActiveCommunities"].iloc[x])
        E.append(D11["Member exit"].iloc[x])
        G.append(D11["Govermental FIT incentive"].loc[x])
        I.append(D11["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D11["Community Members"].iloc[x])
        P.append(D11["Policy Entrepreneur"].iloc[x])
        S.append(D11["Solar Energy"].iloc[x])
        W.append(D11["Wind Energy"].iloc[x])
    c11["tick_{0}".format(i)] = C
    e11["tick_{0}".format(i)] = E
    g11["tick_{0}".format(i)] = G
    i11["tick_{0}".format(i)] = I
    m11["tick_{0}".format(i)] = M
    p11["tick_{0}".format(i)] = P
    s11["tick_{0}".format(i)] = S
    w11["tick_{0}".format(i)] = W
#Scenario 1.2 - FIT = 2.5
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D12["ActiveCommunities"].iloc[x])
        E.append(D12["Member exit"].iloc[x])
        G.append(D12["Govermental FIT incentive"].loc[x])##Change later to Governmental
        I.append(D12["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D12["Community Members"].iloc[x])
        P.append(D12["Policy Entrepreneur"].iloc[x])
        S.append(D12["Solar Energy"].iloc[x])
        W.append(D12["Wind Energy"].iloc[x])
    c12["tick_{0}".format(i)] = C
    e12["tick_{0}".format(i)] = E
    g12["tick_{0}".format(i)] = G
    i12["tick_{0}".format(i)] = I
    m12["tick_{0}".format(i)] = M
    p12["tick_{0}".format(i)] = P
    s12["tick_{0}".format(i)] = S
    w12["tick_{0}".format(i)] = W
#Scenario 1.3 - FIT = 3.0
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D13["ActiveCommunities"].iloc[x])
        E.append(D13["Member exit"].iloc[x])
        G.append(D13["Govermental FIT incentive"].loc[x]) ##Change later to Governmental
        I.append(D13["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D13["Community Members"].iloc[x])
        P.append(D13["Policy Entrepreneur"].iloc[x])
        S.append(D13["Solar Energy"].iloc[x])
        W.append(D13["Wind Energy"].iloc[x])
    c13["tick_{0}".format(i)] = C
    e13["tick_{0}".format(i)] = E
    g13["tick_{0}".format(i)] = G
    i13["tick_{0}".format(i)] = I
    m13["tick_{0}".format(i)] = M
    p13["tick_{0}".format(i)] = P
    s13["tick_{0}".format(i)] = S
    w13["tick_{0}".format(i)] = W

##Scenario 2 - TAX incentive
#Scenario 2.1 - 20%
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D21["ActiveCommunities"].iloc[x])
        E.append(D21["Member exit"].iloc[x])
        G.append(D21["Governmental TAX incentive"].loc[x]) ##Change later to Governmental
        I.append(D21["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D21["Community Members"].iloc[x])
        P.append(D21["Policy Entrepreneur"].iloc[x])
        S.append(D21["Solar Energy"].iloc[x])
        W.append(D21["Wind Energy"].iloc[x])
    c21["tick_{0}".format(i)] = C
    e21["tick_{0}".format(i)] = E
    g21["tick_{0}".format(i)] = G
    i21["tick_{0}".format(i)] = I
    m21["tick_{0}".format(i)] = M
    p21["tick_{0}".format(i)] = P
    s21["tick_{0}".format(i)] = S
    w21["tick_{0}".format(i)] = W
#Scenario 2.2 - 40%
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D22["ActiveCommunities"].iloc[x])
        E.append(D22["Member exit"].iloc[x])
        G.append(D22["Governmental TAX incentive"].loc[x])
        I.append(D22["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D22["Community Members"].iloc[x])
        P.append(D22["Policy Entrepreneur"].iloc[x])
        S.append(D22["Solar Energy"].iloc[x])
        W.append(D22["Wind Energy"].iloc[x])
    c22["tick_{0}".format(i)] = C
    e22["tick_{0}".format(i)] = E
    g22["tick_{0}".format(i)] = G
    i22["tick_{0}".format(i)] = I
    m22["tick_{0}".format(i)] = M
    p22["tick_{0}".format(i)] = P
    s22["tick_{0}".format(i)] = S
    w22["tick_{0}".format(i)] = W
#Scenario 2.3 - 60%
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D23["ActiveCommunities"].iloc[x])
        E.append(D23["Member exit"].iloc[x])
        G.append(D23["Governmental TAX incentive"].loc[x])
        I.append(D23["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D23["Community Members"].iloc[x])
        P.append(D23["Policy Entrepreneur"].iloc[x])
        S.append(D23["Solar Energy"].iloc[x])
        W.append(D23["Wind Energy"].iloc[x])
    c23["tick_{0}".format(i)] = C
    e23["tick_{0}".format(i)] = E
    g23["tick_{0}".format(i)] = G
    i23["tick_{0}".format(i)] = I
    m23["tick_{0}".format(i)] = M
    p23["tick_{0}".format(i)] = P
    s23["tick_{0}".format(i)] = S
    w23["tick_{0}".format(i)] = W
##Scenario 3 - TGC
#Scenario 3.1 - 0.015
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D31["ActiveCommunities"].iloc[x])
        E.append(D31["Member exit"].iloc[x])
        G.append(D31["Governmental TGC incentive"].loc[x])
        I.append(D31["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D31["Community Members"].iloc[x])
        P.append(D31["Policy Entrepreneur"].iloc[x])
        S.append(D31["Solar Energy"].iloc[x])
        W.append(D31["Wind Energy"].iloc[x])
    c31["tick_{0}".format(i)] = C
    e31["tick_{0}".format(i)] = E
    g31["tick_{0}".format(i)] = G
    i31["tick_{0}".format(i)] = I
    m31["tick_{0}".format(i)] = M
    p31["tick_{0}".format(i)] = P
    s31["tick_{0}".format(i)] = S
    w31["tick_{0}".format(i)] = W
#Scenario 3.2 - 0.02
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D32["ActiveCommunities"].iloc[x])
        E.append(D32["Member exit"].iloc[x])
        G.append(D32["Governmental TGC incentive"].loc[x])
        I.append(D32["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D32["Community Members"].iloc[x])
        P.append(D32["Policy Entrepreneur"].iloc[x])
        S.append(D32["Solar Energy"].iloc[x])
        W.append(D32["Wind Energy"].iloc[x])
    c32["tick_{0}".format(i)] = C
    e32["tick_{0}".format(i)] = E
    g32["tick_{0}".format(i)] = G
    i32["tick_{0}".format(i)] = I
    m32["tick_{0}".format(i)] = M
    p32["tick_{0}".format(i)] = P
    s32["tick_{0}".format(i)] = S
    w32["tick_{0}".format(i)] = W
#Scenario 3.3 - 00.025
for i in range(20):
    C, E, G, I, M, P, S, W = [],[], [], [], [], [], [], []
    for x in ticksS[i::20]:
        C.append(D33["ActiveCommunities"].iloc[x])
        E.append(D33["Member exit"].iloc[x])
        G.append(D33["Governmental TGC incentive"].loc[x])
        I.append(D33["Community Costs"].iloc[x]) ##Change later to invested costs
        M.append(D33["Community Members"].iloc[x])
        P.append(D33["Policy Entrepreneur"].iloc[x])
        S.append(D33["Solar Energy"].iloc[x])
        W.append(D33["Wind Energy"].iloc[x])
    c33["tick_{0}".format(i)] = C
    e33["tick_{0}".format(i)] = E
    g33["tick_{0}".format(i)] = G
    i33["tick_{0}".format(i)] = I
    m33["tick_{0}".format(i)] = M
    p33["tick_{0}".format(i)] = P
    s33["tick_{0}".format(i)] = S
    w33["tick_{0}".format(i)] = W
   
###Data sorting
##Active Communities    
C_S0 = [sum(v)/1000 for v in c00.values()]
C_S11 = [sum(v)/500 for v in c11.values()]
C_S12 = [sum(v)/500 for v in c12.values()]
C_S13 = [sum(v)/500 for v in c13.values()]
C_S1 = np.average((C_S11, C_S12, C_S13), axis=0)
C_S21 = [sum(v)/500 for v in c21.values()]
C_S22 = [sum(v)/500 for v in c22.values()]
C_S23 = [sum(v)/500 for v in c23.values()]
C_S2 = np.average((C_S21, C_S22, C_S23), axis=0)
C_S31 = [sum(v)/500 for v in c31.values()]
C_S32 = [sum(v)/500 for v in c32.values()]
C_S33 = [sum(v)/500 for v in c33.values()]
C_S3 = np.average((C_S31, C_S32, C_S33), axis=0)

##Members Exit
E_S0 = [sum(v)/1000 for v in e00.values()]
E_S11 = [sum(v)/500 for v in e11.values()]
E_S12 = [sum(v)/500 for v in e12.values()]
E_S13 = [sum(v)/500 for v in e13.values()]
E_S1 = np.average((E_S11, E_S12, E_S13), axis=0)
E_S21 = [sum(v)/500 for v in e21.values()]
E_S22 = [sum(v)/500 for v in e22.values()]
E_S23 = [sum(v)/500 for v in e23.values()]
E_S2 = np.average((E_S21, E_S22, E_S23), axis=0)
E_S31 = [sum(v)/500 for v in e31.values()]
E_S32 = [sum(v)/500 for v in e32.values()]
E_S33 = [sum(v)/500 for v in e33.values()]
E_S3 = np.average((E_S31, E_S32, E_S33), axis=0)

##Governmental expenditure
G_S11 = [sum(v)/500 for v in g11.values()]
G_S12 = [sum(v)/500 for v in g12.values()]
G_S13 = [sum(v)/500 for v in g13.values()]
G_S1 = np.cumsum(np.average((G_S11, G_S12, G_S13), axis=0))
G_S21 = [sum(v)/500 for v in g21.values()]
G_S22 = [sum(v)/500 for v in g22.values()]
G_S23 = [sum(v)/500 for v in g23.values()]
G_S2 = np.cumsum(np.average((G_S21, G_S22, G_S23), axis=0))
G_S31 = [sum(v)/500 for v in g31.values()]
G_S32 = [sum(v)/500 for v in g32.values()]
G_S33 = [sum(v)/500 for v in g33.values()]
G_S3 = np.cumsum(np.average((G_S31, G_S32, G_S33), axis=0))

##Invested amount
I_S0 = [sum(v)/1000 for v in i00.values()]
I_S11 = [sum(v)/500 for v in i11.values()]
I_S12 = [sum(v)/500 for v in i12.values()]
I_S13 = [sum(v)/500 for v in i13.values()]
I_S1 = np.average((I_S11, I_S12, I_S13), axis=0)
I_S21 = [sum(v)/500 for v in i21.values()]
I_S22 = [sum(v)/500 for v in i22.values()]
I_S23 = [sum(v)/500 for v in i23.values()]
I_S2 = np.average((I_S21, I_S22, I_S23), axis=0)
I_S31 = [sum(v)/500 for v in i31.values()]
I_S32 = [sum(v)/500 for v in i32.values()]
I_S33 = [sum(v)/500 for v in i33.values()]
I_S3 = np.average((I_S31, I_S32, I_S33), axis=0)

##Members population    
M_S0 = [sum(v)/1000 for v in m00.values()]
M_S11 = [sum(v)/500 for v in m11.values()]
M_S12 = [sum(v)/500 for v in m12.values()]
M_S13 = [sum(v)/500 for v in m13.values()]
M_S1 = np.average((M_S11, M_S12, M_S13), axis=0)
M_S21 = [sum(v)/500 for v in m21.values()]
M_S22 = [sum(v)/500 for v in m22.values()]
M_S23 = [sum(v)/500 for v in m23.values()]
M_S2 = np.average((M_S21, M_S22, M_S23), axis=0)
M_S31 = [sum(v)/500 for v in m31.values()]
M_S32 = [sum(v)/500 for v in m32.values()]
M_S33 = [sum(v)/500 for v in m33.values()]
M_S3 = np.average((M_S31, M_S32, M_S33), axis=0)

##Policy entrepreneur
P_S0 = [sum(v)/1000 for v in p00.values()]
P_S11 = [sum(v)/500 for v in p11.values()]
P_S12 = [sum(v)/500 for v in p12.values()]
P_S13 = [sum(v)/500 for v in p13.values()]
P_S1 = np.average((P_S11, P_S12, P_S13), axis=0)
P_S21 = [sum(v)/500 for v in p21.values()]
P_S22 = [sum(v)/500 for v in p22.values()]
P_S23 = [sum(v)/500 for v in p23.values()]
P_S2 = np.average((P_S21, P_S22, P_S23), axis=0)
P_S31 = [sum(v)/500 for v in p31.values()]
P_S32 = [sum(v)/500 for v in p32.values()]
P_S33 = [sum(v)/500 for v in p33.values()]
P_S3 = np.average((P_S31, P_S32, P_S33), axis=0)

###Solar Energy
S_S0 = [sum(v)/1000 for v in s00.values()]
S_S11 = [sum(v)/500 for v in s11.values()]
S_S12 = [sum(v)/500 for v in s12.values()]
S_S13 = [sum(v)/500 for v in s13.values()]
S_S1 = np.average((S_S11, S_S12, S_S13), axis=0)
S_S21 = [sum(v)/500 for v in s21.values()]
S_S22 = [sum(v)/500 for v in s22.values()]
S_S23 = [sum(v)/500 for v in s23.values()]
S_S2 = np.average((S_S21, S_S22, S_S23), axis=0)
S_S31 = [sum(v)/500 for v in s31.values()]
S_S32 = [sum(v)/500 for v in s32.values()]
S_S33 = [sum(v)/500 for v in s33.values()]
S_S3 = np.average((S_S31, S_S32, S_S33), axis=0)

###Wind Energy
W_S0 = [sum(v)/1000 for v in w00.values()]
W_S11 = [sum(v)/500 for v in w11.values()]
W_S12 = [sum(v)/500 for v in w12.values()]
W_S13 = [sum(v)/500 for v in w13.values()]
W_S1 = np.average((W_S11, W_S12, W_S13), axis=0)
W_S21 = [sum(v)/500 for v in w21.values()]
W_S22 = [sum(v)/500 for v in w22.values()]
W_S23 = [sum(v)/500 for v in w23.values()]
W_S2 = np.average((W_S21, W_S22, W_S23), axis=0)
W_S31 = [sum(v)/500 for v in w31.values()]
W_S32 = [sum(v)/500 for v in w32.values()]
W_S33 = [sum(v)/500 for v in w33.values()]
W_S3 = np.average((W_S31, W_S32, W_S33), axis=0)

###Ratios
#RFIT2 = sum([sum(x) for x in zip(*[G_S11, G_S12, G_S13, I_S11, I_S12, I_S13])])/sum([sum(x) for x in zip(*[S_S11, S_S12, S_S13, W_S11, W_S12, W_S13])])
#RTAX2 = sum([sum(x) for x in zip(*[G_S21, G_S22, G_S23, I_S21, I_S22, I_S23])])/sum([sum(x) for x in zip(*[S_S21, S_S22, S_S23, W_S21, W_S12, W_S23])])
#RTGC2 = sum([sum(x) for x in zip(*[G_S31, G_S32, G_S33, I_S31, I_S32, I_S33])])/sum([sum(x) for x in zip(*[S_S31, S_S32, S_S33, W_S31, W_S32, W_S33])])


RFITIG = sum([sum(x) for x in zip(*[G_S11, G_S12, G_S13])])/3 
RFITIC = (max(I_S11) + max(I_S12) + max(I_S13))/3
RFIT_I = RFITIG + RFITIC
RFIT_En = sum([sum(x) for x in zip([max(S_S11), max(S_S12), max(S_S13), max(W_S11), max(W_S12), max(W_S13)])])/3

RTAXIG = sum([sum(x) for x in zip(*[G_S21, G_S22, G_S23])])/3 
RTAXIC = (max(I_S21) + max(I_S22) + max(I_S23))/3
RTAX_I =  RTAXIG + RTAXIC
RTAX_En = sum([sum(x) for x in zip([max(S_S21), max(S_S22), max(S_S23), max(W_S21), max(W_S12), max(W_S23)])])/3

RTGCIG = sum([sum(x) for x in zip(*[G_S31, G_S32, G_S33])])/3
RTGCIC = (max(I_S31) + max(I_S32) + max(I_S33))/3
RTGC_I =  RTGCIG + RTGCIC
RTGC_En = sum([sum(x) for x in zip([max(S_S31), max(S_S32), max(S_S33), max(W_S31), max(W_S32), max(W_S33)])])/3


RFIT = RFIT_I/RFIT_En
RTAX = RTAX_I/RTAX_En
RTGC = RTGC_I/RTGC_En
