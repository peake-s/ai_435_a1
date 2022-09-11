#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_a =  pd.read_csv("../data/groupA.txt", header=None, names = ["cost", "weight", "type"])
df_b =  pd.read_csv("../data/groupB.txt", header=None, names = ["cost", "weight", "type"])
df_c =  pd.read_csv("../data/groupC.txt", header=None, names = ["cost", "weight", "type"])

normalized_df_a = (df_a-df_a.min())/(df_a.max()-df_a.min())
normalized_df_b = (df_b-df_b.min())/(df_b.max()-df_b.min())
normalized_df_c = (df_a-df_c.min())/(df_c.max()-df_c.min())

#price on x, weight on y
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