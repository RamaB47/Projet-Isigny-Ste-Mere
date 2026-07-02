#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nettoyage des relevés météos pour obtenir uniquement les données des deux stations météo (ENGLEQUEVILLE & STE MARIE DU MONT)
import pandas as pd


# In[2]:


#
dataset_14 = "Meteo_14.csv"
df = pd.read_csv('Meteo_14.csv', delimiter=";", header=0, dtype={'AAAAMM': str})


# In[3]:


df.head(10)
print(df.head(20))  


# In[4]:


print(len(df))  
print(df.index)  


# In[5]:


print(df.columns)  #4 Quelles colonnes existent?


# In[6]:


df.iloc[0].astype(str).str.split(expand=True)


# In[7]:


# ne garder que les lignes qui concernent la stations ENGLESQUEVILLE
df_englesqueville = df[df["NOM_USUEL"] == "ENGLESQUEVILLE"]




# In[8]:


print(df_englesqueville.head(30))


# In[9]:


value = pd.NaT
print(pd.isna(value))


# In[10]:


val_nat = df[df['AAAAMM'].isna()]
print(val_nat.index)


# In[11]:


from datetime import datetime


# In[13]:


# convertir en string
df_englesqueville.iloc[:, 5] =  df_englesqueville.iloc[:, 5].astype(str)


# In[14]:


import numpy as np


# In[16]:


import chardet
with open('Meteo_14.csv', 'rb') as f:
    result = chardet.detect(f.read())
    print(f"Encodage détecté : {result}")


# In[17]:


# Lire et afficher les 10 premières lignes du fichier
with open('Meteo_14.csv', 'r', encoding='ascii') as f:
    for i in range(10):
        line = f.readline()
        print(f"Ligne {i}: {line.strip()}")


# In[18]:


print(df_englesqueville.head())


# In[19]:


date_brute = str(df_englesqueville.iloc[0, 5])


date_nettoyee = date_brute.strip()


date_object = pd.to_datetime(date_nettoyee, format='%Y%m')

print("Succès ! Type :", type(date_object))


# In[20]:


df_englesqueville.to_csv("Meteo14_cleaned", sep=';', header=0)


# In[21]:


df = "Meteo14_cleaned"
df= pd.read_csv("Meteo14_cleaned", delimiter=";", header=0)


# In[22]:


value = pd.NaT
print(pd.isna(value))


# In[23]:


# Puis exporter
df_englesqueville.to_csv("Meteo14_cleaned", index=False)


# In[24]:


#filtrer pour ne garder que les lignes après janvier 2021
filtre_date = df_englesqueville[df_englesqueville["AAAAMM"] > "202012"]

# Pour voir le résultat :
filtre_date.head()



# In[34]:


filtre_date.to_csv('Meteo_14_cleaned2.csv', index=False)

