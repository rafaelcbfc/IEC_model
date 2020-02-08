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


###Communities
##Scenario 0
Ac_S0 = Australia.C_S0
Bc_S0 = Brazil.C_S0
Ic_S0 = Iran.C_S0
Jc_S0 = Japan.C_S0
Nc_S0 = NLD.C_S0
Uc_S0 = USA.C_s0
##Scenario 1
Ac_S1 = Australia.C_S1
Bc_S1 = Brazil.C_S1
Ic_S1 = Iran.C_S1
Jc_S1 = Japan.C_S1
Nc_S1 = NLD.C_S1
Uc_S1 = USA.C_s1
Ac_S11 = Australia.C_S11
Bc_S11 = Brazil.C_S11
Ic_S11 = Iran.C_S11
Jc_S11 = Japan.C_S11
Nc_S11 = NLD.C_S11
Uc_S11 = USA.C_s11
Ac_S12 = Australia.C_S12
Bc_S12 = Brazil.C_S12
Ic_S12 = Iran.C_S12
Jc_S12 = Japan.C_S12
Nc_S12 = NLD.C_S12
Uc_S12 = USA.C_s12
Ac_S13 = Australia.C_S13
Bc_S13 = Brazil.C_S13
Ic_S13 = Iran.C_S13
Jc_S13 = Japan.C_S13
Nc_S13 = NLD.C_S13
Uc_S13 = USA.C_s13
##Scenario 2
Ac_S2 = Australia.C_S2
Bc_S2 = Brazil.C_S2
Ic_S2 = Iran.C_S2
Jc_S2 = Japan.C_S2
Nc_S2 = NLD.C_S2
Uc_S2 = USA.C_s2
Ac_S21 = Australia.C_S21
Bc_S21 = Brazil.C_S21
Ic_S21 = Iran.C_S21
Jc_S21 = Japan.C_S21
Nc_S21 = NLD.C_S21
Uc_S21 = USA.C_s21
Ac_S22 = Australia.C_S22
Bc_S22 = Brazil.C_S22
Ic_S22 = Iran.C_S22
Jc_S22 = Japan.C_S22
Nc_S22 = NLD.C_S22
Uc_S22 = USA.C_s22
Ac_S23 = Australia.C_S23
Bc_S23 = Brazil.C_S23
Ic_S23 = Iran.C_S23
Jc_S23 = Japan.C_S23
Nc_S23 = NLD.C_S23
Uc_S23 = USA.C_s23
##Scenario 3
Ac_S3 = Australia.C_S3
Bc_S3 = Brazil.C_S3
Ic_S3 = Iran.C_S3
Jc_S3 = Japan.C_S3
Nc_S3 = NLD.C_S3
Uac_S3 = USA.C_s3
Ac_S31 = Australia.C_S31
Bc_S31 = Brazil.C_S31
Ic_S31 = Iran.C_S31
Jc_S31 = Japan.C_S31
Nc_S31 = NLD.C_S31
Uc_S31 = USA.C_s31
Ac_S32 = Australia.C_S32
Bc_S32 = Brazil.C_S32
Ic_S32 = Iran.C_S32
Jc_S32 = Japan.C_S32
Nc_S32 = NLD.C_S32
Uc_S32 = USA.C_s32
Ac_S33 = Australia.C_S33
Bc_S33 = Brazil.C_S33
Ic_S33 = Iran.C_S33
Jc_S33 = Japan.C_S33
Nc_S33 = NLD.C_S33
Uc_S33 = USA.C_s33

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
##Scenario 2
Am_S2 = Australia.M_S2
Bm_S2 = Brazil.M_S2
Im_S2 = Iran.M_S2
Jm_S2 = Japan.M_S2
Nm_S2 = NLD.M_S2
Um_S2 = USA.M_s2
Am_S21 = Australia.M_S21
Bm_S21 = Brazil.M_S21
Im_S21 = Iran.M_S21
Jm_S21 = Japan.M_S21
Nm_S21 = NLD.M_S21
Um_S21 = USA.M_s21
Am_S22 = Australia.M_S22
Bm_S22 = Brazil.M_S22
Im_S22 = Iran.M_S22
Jm_S22 = Japan.M_S22
Nm_S22 = NLD.M_S22
Um_S22 = USA.M_s22
Am_S23 = Australia.M_S23
Bm_S23 = Brazil.M_S23
Im_S23 = Iran.M_S23
Jm_S23 = Japan.M_S23
Nm_S23 = NLD.M_S23
Um_S23 = USA.M_s23
##Scenario 3
Am_S3 = Australia.M_S3
Bm_S3 = Brazil.M_S3
Im_S3 = Iran.M_S3
Jm_S3 = Japan.M_S3
Nm_S3 = NLD.M_S3
Um_S3 = USA.M_s3
Am_S31 = Australia.M_S31
Bm_S31 = Brazil.M_S31
Im_S31 = Iran.M_S31
Jm_S31 = Japan.M_S31
Nm_S31 = NLD.M_S31
Um_S31 = USA.M_s31
Am_S32 = Australia.M_S32
Bm_S32 = Brazil.M_S32
Im_S32 = Iran.M_S32
Jm_S32 = Japan.M_S32
Nm_S32 = NLD.M_S32
Um_S32 = USA.M_s32
Am_S33 = Australia.M_S33
Bm_S33 = Brazil.M_S33
Im_S33 = Iran.M_S13
Jm_S33 = Japan.M_S33
Nm_S33 = NLD.M_S33
Um_S33 = USA.M_s33



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