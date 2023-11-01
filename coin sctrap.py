import pandas as pd

import matplotlib.pyplot as plt
import psycopg2
import requests
from bs4 import BeautifulSoup
#---- 2023-10-31------
# df = pd.read_csv(r"C:\Users\pauli\PycharmProjects\SQLProject\COINBASE231031.csv")
# # df = df.rename(columns={"Trade":"Volume (24)", "Volume (24)":"Supply", "Suply":"Trade"})
#
# df = df.drop(columns= ["Charts", "Change", "Trade"])
# df["Name"] = df["Name"].str.lstrip("")
# df["Price"] = df["Price"].str.lstrip("€")
# df["Market cap"] = df["Market cap"].str.lstrip("€")
# df["Volume (24)"] = df["Volume (24)"].str.lstrip("€")
#
# df.to_csv("ok-COINBASE231031.csv", index=False)

#-----2023-11-01-------


df = pd.read_csv(r"C:\Users\pauli\PycharmProjects\SQLProject\COINBASE231101.csv")

df = df.drop(columns= ["Charts", "Change", "Trade"])
df["Name"] = df["Name"].str.lstrip("")
df["Price"] = df["Price"].str.lstrip("€")
df["Market cap"] = df["Market cap"].str.lstrip("€")
df["Volume (24)"] = df["Volume (24)"].str.lstrip("€")

df.to_csv("ok-COINBASE231101.csv", index=False)

print(df)