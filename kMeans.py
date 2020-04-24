# -*- coding: utf-8 -*-
"""
Author  - Achuth Arun Resmi
Email   - Achuth_ArunResmi2020@isb.edu
Date    - 12/02/2020
Project - Perform k-Means clustering using Euclidean distance from centroid
"""
#%% loading packages

import pandas as pd
import os
import random
import numpy as np

#%% Set path where all files are placed

#Make sure to change single forward slash to double forward slash
path = "C:\\Users\\61920731\\Desktop\\ISB\\Acads\\Term-7\\BADM"
print(path)

#Changing working directory
os.chdir(path)
#os.getcwd()

#%% Loading data

df_Universities = pd.read_excel("Universities_PythonInput.xlsx")

df_BackUp = pd.read_excel("Universities_PythonInput.xlsx")

#%% K-Means

#Normalization using Z-Score
for col in df_Universities.columns:
    if not(isinstance(df_Universities[col][1],str)):
        mean = np.mean(df_Universities[col])
        sd = df_Universities[col].std()
        df_Universities[col] = [((i-mean)/sd) for i in df_Universities[col]]
    else:
        df_Universities = df_Universities.drop(columns = col)

#Set k
k = 3

#Random initialisation of clusters
df_Universities["Cluster"] = [random.randint(1,3) for p in range(len(df_Universities))]

#Counter to keep track of cluster changes. When counter = 0, algorithm ends
counter = 0

#List to keep track of average distance from centroid
avg_dist_iter = []

while counter < 100:
    
    #Counter to keep track of cluster changes. When counter = 0, algorithm ends
    counter = counter + 1
    
    #Intialising list to store centroid
    centroid = []

    #Centroid Calculation
    for cl in range(0, k):
        centroid.append(np.mean(df_Universities[df_Universities["Cluster"] == (cl + 1)], axis = 0).values)
    
    print(centroid)

    #Distance calculation and move to 
    for row in range(0, len(df_Universities)):
        #print("\n", row,"\n")
        best_cluster = int(df_Universities.iloc[row]["Cluster"])
        cluster_distance = np.sqrt(sum((df_Universities.iloc[row] - centroid[best_cluster - 1])**2))
        #print("best_cluster =", best_cluster, "\tcluster_distance = ", cluster_distance)
        for cl in range(0, k):
            #print("cl = ", cl+1, "\t Dist = ", np.sqrt(sum((df_Universities.iloc[row] - centroid[cl])**2)))
            if np.sqrt(sum((df_Universities.iloc[row] - centroid[cl])**2)) < cluster_distance:
                best_cluster = cl + 1
        df_Universities.iloc[row]["Cluster"] = best_cluster
        #print("New Best Cluster = ", best_cluster)
    print("Counter = ", counter, "\n")
    
    avg_dist = 0
    
    for row in range(0, len(df_Universities)):
        print(avg_dist)
        avg_dist = avg_dist + np.sqrt(sum((df_Universities.iloc[row] - centroid[int(df_Universities.iloc[row]["Cluster"]) - 1])**2))
    avg_dist_iter.append(avg_dist/len(df_Universities))
    
    
        
            
    
        



