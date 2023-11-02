import pandas as pd

import matplotlib.pyplot as plt
import psycopg2
import requests
from bs4 import BeautifulSoup
#---- 2023-10-31------
# df = pd.read_csv(r"C:\Users\pauli\PycharmProjects\SQLProject\COINBASE231031.csv")
# df = df.rename(columns={"Trade":"Volume (24)", "Volume (24)":"Supply", "Suply":"Trade"})
# df = df.drop(columns= ["Charts", "Change", "Trade"])
# df["Name"] = df["Name"].str.lstrip("")
# df["Price"] = df["Price"].str.lstrip("€")
# df["Market cap"] = df["Market cap"].str.lstrip("€")
# df["Volume (24)"] = df["Volume (24)"].str.lstrip("€")
#-------
# df31 = pd.read_csv(r"C:\Users\pauli\PycharmProjects\SQLProject\ok-COINBASE231031.csv")
# df31 = df31.drop_duplicates(subset="Name")
# df31["Name"] = df31["Name"].str.lstrip("0x ")
# df31 = df31.sort_values("Name")
# df31.to_csv("ok1-COINBASE231031.csv", index=False)
# print(df31)

#-----2023-11-01-------


# df = pd.read_csv(r"C:\Users\pauli\PycharmProjects\SQLProject\COINBASE231101.csv")
#
# df = df.rename(columns={"Suply":"Supply"})
#
# df = df.drop(columns= ["Charts", "Change", "Trade"])
# df["Name"] = df["Name"].str.lstrip("")
# df["Price"] = df["Price"].str.lstrip("€")
# df["Market cap"] = df["Market cap"].str.lstrip("€")
# df["Volume (24)"] = df["Volume (24)"].str.lstrip("€")
#
# df.to_csv("ok-COINBASE231101.csv", index=False)
#----------

# df01 = pd.read_csv(r"C:\Users\pauli\PycharmProjects\SQLProject\ok-COINBASE231101.csv")
# df01 = df01.drop_duplicates(subset="Name")
# df01["Name"] = df01["Name"].str.lstrip("0x ")
# df01 = df01.sort_values("Name")
# df01.to_csv("ok1-COINBASE231101.csv", index=False)
# print(df01)



# #------2023-11-02--------
#
#
# df = pd.read_csv(r"C:\Users\pauli\PycharmProjects\SQLProject\COINBASE231102.csv")
#
# df = df.rename(columns={"Suply":"Supply"})
#
# df = df.drop(columns= ["Charts", "Change", "Trade"])
# df["Name"] = df["Name"].str.lstrip("")
# df["Price"] = df["Price"].str.lstrip("€")
# df["Market cap"] = df["Market cap"].str.lstrip("€")
# df["Volume (24)"] = df["Volume (24)"].str.lstrip("€")
#
# df.to_csv("ok-COINBASE231102.csv", index=False)
###-----------------
# df02 = pd.read_csv(r"C:\Users\pauli\PycharmProjects\SQLProject\ok-COINBASE231102.csv")
# df02 = df02.drop_duplicates(subset="Name")
# df02["Name"] = df02["Name"].str.lstrip("0x ")
# df02 = df02.sort_values("Name")
# df02.to_csv("ok1-COINBASE231102.csv", index=False)
# print(df02)

##-------------------------




