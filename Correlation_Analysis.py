# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 22:10:29 2021

@author: begum
"""


import random as rnd
import pandas as pd 
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
import seaborn as sns
from sklearn.metrics import matthews_corrcoef

hd = pd.read_csv("HeartDisease.csv")
hd.head()
hd.info()

#target is binary but string.
#convert target values from string to numeric to apply appropriate correlation test for binary variables

to_numeric = {"Disease":1, "Nodisease":0}
hd["target"]=hd["target"].map(to_numeric)
hd.head()

#plot a cross-plot for an eyeball test

sns.pairplot(hd, diag_kind="kde")


cols = np.array(hd.columns)[:-1]
binary = []
cont = []
categorical = []
target = np.array(hd['target'])
cramersV = {1:[]}

for idx in cols:
    if len(pd.unique(hd[idx])) == 2:
        to_numeric = {pd.unique(hd[idx])[0]:0, pd.unique(hd[idx])[1]:1}
        hd[idx]=hd[idx].map(to_numeric)
        print(idx,"is a BINARY variable so we need to apply Phi coefficient method to detect correlation")
        phi = matthews_corrcoef(np.array(hd[idx]), target)
        print("phi value is",round(phi,3))
        if abs(phi) < 0.1:
            print(idx,"has no correlation with target\n")
        elif abs(phi) < 0.3:
            print(idx,"has weak correlation with target\n")
        elif abs(phi) < 0.5:
            print(idx,"has moderate correlation with target\n")
        else:
            print(idx,"has strong correlation with target\n")
        binary.append(idx)
    elif hd[idx].dtype in ['int64','float64']:
        c,p = stats.pointbiserialr(hd[idx],target)
        print(idx,"is a CONTINIOUS variable so we need to apply Point-Biserial Correlation method to detect correlation")
        print("p value is",round(p,3))
        if p < 0.05:
            print("p value is smaller than 0.05")
            print(idx,"has significant correlation between target\n")
        else:
            print("p value is greater than 0.05")
            print(idx,"has insignificant correlation between target\n")  
        
        cont.append(idx)
    else:
        print(idx,"is a CATEGORICAL variable so we need to apply Point-Biserial Correlation method to detect correlation")
        ct = pd.crosstab(np.array(hd[idx]),target)
        #Chi-squared test statistic, sample size, and minimum of rows and columns
        X2 = stats.chi2_contingency(ct, correction=False)[0]
        n = ct.values.sum()
        minDim = min(ct.shape)-1
        #calculate Cramer's V 
        V = np.sqrt((X2/n) / minDim)
        #display Cramer's V
        print("Cramer's V value is",V)
        if V < 0.1:
            print(idx,"has small correlation with target\n")
        elif V < 0.3:
            print(idx,"has medium correlation with target\n")
        else:
            print(idx,"has large correlation with target\n")
            
        categorical.append(idx)