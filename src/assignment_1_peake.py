#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_a =  pd.read_csv("../data/groupA.txt", header=None, names = ["cost", "weight", "type"])
df_b =  pd.read_csv("../data/groupB.txt", header=None, names = ["cost", "weight", "type"])
df_c =  pd.read_csv("../data/groupC.txt", header=None, names = ["cost", "weight", "type"])

normalized_df_a = df_a.copy()
normalized_df_b = df_b.copy()
normalized_df_c = df_c.copy()

normalized_df_a['cost'] = (df_a['cost']-df_a['cost'].min())/(df_a['cost'].max()-df_a['cost'].min())
normalized_df_a['weight'] = (df_a['weight']-df_a['weight'].min())/(df_a['weight'].max()-df_a['weight'].min())

normalized_df_b['cost'] = (df_b['cost']-df_b['cost'].min())/(df_b['cost'].max()-df_b['cost'].min())
normalized_df_b['weight'] = (df_b['weight']-df_b['weight'].min())/(df_b['weight'].max()-df_b['weight'].min())

normalized_df_c['cost'] = (df_c['cost']-df_c['cost'].min())/(df_c['cost'].max()-df_c['cost'].min())
normalized_df_c['weight'] = (df_c['weight']-df_c['weight'].min())/(df_c['weight'].max()-df_c['weight'].min())

plt.figure()
plt.scatter(normalized_df_a['cost'],normalized_df_a['weight'],c=df_a['type'])
plt.xlabel('cost (USD)')
plt.ylabel('weight') 
plt.title('Weight vs Cost A')
plt.savefig('../plots/plot_a.png')

plt.figure()
plt.scatter(normalized_df_b['cost'],normalized_df_c['weight'],c=df_b['type'])
plt.xlabel('cost (USD)')
plt.ylabel('weight')
plt.title('Weight vs Cost B')
plt.savefig('../plots/plot_b.png')

plt.figure()
plt.scatter(normalized_df_c['cost'],normalized_df_c['weight'],c=df_b['type'])
plt.xlabel('cost (USD)')
plt.ylabel('weight')
plt.title('Weight vs Cost C')
plt.savefig('../plots/plot_c.png')
plt.show()  