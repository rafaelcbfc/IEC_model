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
import Australia, Brazil, Iran, Japan, NLD, USA


###Number of Communities
##Scenario 0
Aac_S0 = Australia.Ac_S0
Bac_S0 = Brazil.Ac_S0
Iac_S0 = Iran.Ac_S0
Jac_S0 = Japan.Ac_S0
Nac_S0 = NLD.Ac_S0
Uac_S0 = USA.Ac_s0

##Scenario 1
Aac_S1 = Australia.Ac_S1
Bac_S1 = Brazil.Ac_S1
Iac_S1 = Iran.Ac_S1
Jac_S1 = Japan.Ac_S1
Nac_S1 = NLD.Ac_S1
Uac_S1 = USA.Ac_s1
Aac_S11 = Australia.Ac_S11
Bac_S11 = Brazil.Ac_S11
Iac_S11 = Iran.Ac_S11
Jac_S11 = Japan.Ac_S11
Nac_S11 = NLD.Ac_S11
Uac_S11 = USA.Ac_s11
Aac_S12 = Australia.Ac_S12
Bac_S12 = Brazil.Ac_S12
Iac_S12 = Iran.Ac_S12
Jac_S12 = Japan.Ac_S12
Nac_S12 = NLD.Ac_S12
Uac_S12 = USA.Ac_s12
Aac_S13 = Australia.Ac_S13
Bac_S13 = Brazil.Ac_S13
Iac_S13 = Iran.Ac_S13
Jac_S13 = Japan.Ac_S13
Nac_S13 = NLD.Ac_S13
Uac_S13 = USA.Ac_s13

##Scenario 2
Aac_S2 = Australia.Ac_S2
Bac_S2 = Brazil.Ac_S2
Iac_S2 = Iran.Ac_S2
Jac_S2 = Japan.Ac_S2
Nac_S2 = NLD.Ac_S2
Uac_S2 = USA.Ac_s2
Aac_S21 = Australia.Ac_S21
Bac_S21 = Brazil.Ac_S21
Iac_S21 = Iran.Ac_S21
Jac_S21 = Japan.Ac_S21
Nac_S21 = NLD.Ac_S21
Uac_S21 = USA.Ac_s21
Aac_S22 = Australia.Ac_S22
Bac_S22 = Brazil.Ac_S22
Iac_S22 = Iran.Ac_S22
Jac_S22 = Japan.Ac_S22
Nac_S22 = NLD.Ac_S22
Uac_S22 = USA.Ac_s22
Aac_S23 = Australia.Ac_S23
Bac_S23 = Brazil.Ac_S23
Iac_S23 = Iran.Ac_S23
Jac_S23 = Japan.Ac_S23
Nac_S23 = NLD.Ac_S23
Uac_S23 = USA.Ac_s23

##Scenario 3
Aac_S3 = Australia.Ac_S3
Bac_S3 = Brazil.Ac_S3
Iac_S3 = Iran.Ac_S3
Jac_S3 = Japan.Ac_S3
Nac_S3 = NLD.Ac_S3
Uac_S3 = USA.Ac_s3
Aac_S31 = Australia.Ac_S31
Bac_S31 = Brazil.Ac_S31
Iac_S31 = Iran.Ac_S31
Jac_S31 = Japan.Ac_S31
Nac_S31 = NLD.Ac_S31
Uac_S31 = USA.Ac_s31
Aac_S32 = Australia.Ac_S32
Bac_S32 = Brazil.Ac_S32
Iac_S32 = Iran.Ac_S32
Jac_S32 = Japan.Ac_S32
Nac_S32 = NLD.Ac_S32
Uac_S32 = USA.Ac_s32
Aac_S33 = Australia.Ac_S33
Bac_S33 = Brazil.Ac_S33
Iac_S33 = Iran.Ac_S33
Jac_S33 = Japan.Ac_S33
Nac_S33 = NLD.Ac_S33
Uac_S33 = USA.Ac_s33


###Members of Communities
##Scenario 0
Am_S0 = Australia.M_S0
Bm_S0 = Brazil.M_S0
Im_S0 = Iran.M_S0
Jm_S0 = Japan.M_S0
Nm_S0 = NLD.M_S0
Um_S0 = USA.M_s0

##Scenario 1
Am_S1 = Australia.M_S1
Bm_S1 = Brazil.M_S1
Im_S1 = Iran.M_S1
Jm_S1 = Japan.M_S1
Nm_S1 = NLD.M_S1
Um_S1 = USA.M_s1

Am_S11 = Australia.M_S11
Bm_S11 = Brazil.M_S11
Im_S11 = Iran.M_S11
Jm_S11 = Japan.M_S11
Nm_S11 = NLD.M_S11
Um_S11 = USA.M_s11

Am_S12 = Australia.M_S12
Bm_S12 = Brazil.M_S12
Im_S12 = Iran.M_S12
Jm_S12 = Japan.M_S12
Nm_S12 = NLD.M_S12
Um_S12 = USA.M_s12

Am_S13 = Australia.M_S13
Bm_S13 = Brazil.M_S13
Im_S13 = Iran.M_S13
Jm_S13 = Japan.M_S13
Nm_S13 = NLD.M_S13
Um_S13 = USA.M_s13






###Graph building
#dirty_graph_pdi = df["pdi"]
#g_pdi = pd.DataFrame([x for x in dirty_graph_pdi if str(x) != 'nan'])
#m_pdi, s_pdi = stats.norm.fit(g_pdi)  


###Plotting
#fig, ax = plt.subplots()
#g_pdi.plot.hist(density=True, ax=ax, color="#66b3ff")
#g_pdi.plot.kde(ax=ax, legend=False, title='Power Distance Distribution', color = 'orange')
#plt.axvline(m_pdi, color='k', linestyle='dashed', linewidth=1)
#plt.xlabel('Power Distance Index')
#plt.legend(["Distribution function", "mean", "Power Distance freq"])
#plt.show()