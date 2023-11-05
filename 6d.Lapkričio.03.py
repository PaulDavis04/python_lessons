import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
import requests
from bs4 import BeautifulSoup

##
# data = pd.Series([1,2,3,4,5])
# ##grazina pirmus skaicius
# print(data)
# ##grazina paskutinius skaicius
# print(data.tail())
# ##grazina statistine info
# print(data.describe())
# grazina vidurki
# print.(data.mean())
# ##mediana
# print.(data.median())
# ##grazina unikalias reiksmes
# print.(data.unique())
#
# ##grazina reiksmiu pasikartojimo skaiciu
# print(data.value_counts())
##grazina didziausios reiksmes indeksa
# print(data.idxmax())


####-------------------

# knygos = ["Haris Poteris", "Alchemikas", "Mazasis princas", "Mobis Dikas", "Don Kichotas"]
# vertinimas = [4.9, 4.2, 4.3, 3.8, 4.5]
# ##nurodyti reiksmes
#
# data = pd.Series(data=vertinimas, index=knygos)
# # print(data)
# # vidurkis = data.mean().round(2)
# # print(f"vidutinis knygu ivertinimas: {vidurkis}")
# #
# # std_nuokrypis = data.std().round(2)
# #
# # auksciausias_ivertinimas = data.idmax()
# # print(f"auksciausia ivertinima turinti knyga: {auksciausias_ivertinimas}")
#
# # plt.figure(figsize=(20,6))
# # data.plot(kind ="bar", color="skyblue")
# # plt.title("Knygu ivertinimas")
# # plt.xlabel("Knygos")
# # plt.ylabel("Ivertinimai")
# # plt.xticks(rotation=45, ha="right")
# # plt.show()
#
# # labels = "A","B","C","D"
# # sizes = [15,20,35,10]
#
# x = [5, 3, 5, 10, 20, 34]
# y = [15, 20, 35, 10, 21, 45]
#
# plt.scatter(x, y, label= "taskai", color="blue")
# plt.title("sklaidos diagrama")
# plt.xlabel("x asis")
# plt.ylabel("y asis")
# plt.legend()
# plt.show()


# colors = ["gold","yellowgreen", "lightcoral","lightskyblue"]
# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
# plt.title("skrituline diagrama")
# plt.show()

##### -------------------bendra pardavimu suma pagal data

data = pd.read_csv(r"soft_drink_sales.csv")
# print(data)
#
# pardavimai_pagal_data = data.groupby("Purchase Date")["Revenue"].sum().reset_index()
# # print(pardavimai_pagal_data)
#
# pardavimai_pagal_data.to_csv("pardavimai pagal data.csv", index=False)

### pardavimu sumos vidurkis pagal imone

# pardavimu_sumos_vidurkis_pagal_imone = data.groupby("Company")["Revenue"].mean().round(2).reset_index
# pardavimu_sumos_vidurkis_pagal_imone.to_csv("pardavimai pagal data.csv", index=False)

# print(pardavimu_sumos_vidurkis_pagal_imone)

####-- 5 prekes kurios daugiausiai pelno atnesa ir maziausiai pelno atnesa

# maziausiai_pelningas = data.sort_values(by="Profit",ascending=False).head(5)
#
# labiausiai_pelningas = data.sort_values(by="Profit").head(5)
#
# print(labiausiai_pelningas)

###-----pardavimu suma pagal kliento miesta----

# pardavimai_pagal_kliento_miesta = data.groupby("Customer City")["Revenue"].mean().reset_index()
# surusiavimas = pardavimai_pagal_kliento_miesta.sort_values(by="Revenue", ascending=False)


# pardavimai_pagal = data.groupby("Customer City")["Revenue"].mean().sort_values(ascending=False).reset_index()
#
# print(pardavimai_pagal)

# pirkimu skaicius per diena ir atvaizduoti linijineje diagramoje

# pirkimu_skaiciu_per_diena = data.groupby("Purchase Date")["Unit Sold"].sum().reset_index()

####---------------------------
# data["Purchase Day"] = pd.to_datetime(data["Purchase Date"]).dt.day
# pirkimai_pagal_diena = data["Purchase Day"].value_counts()
#
# plt.figure(figsize=(10,6))
# (data.groupby("Purchase Day")["Profit"].sum().\
# plot(kind="line",color=["green" if i>0 else "red" for i in data.groupby("Purchase Day")["Profit"].sum()]))
# plt.title("Pelnas pagal diena")
# plt.xlabel("Pirkimu dienos")
# plt.ylabel("Pelnas")
# plt.xticks(rotation=0, ha="right")
# plt.show()

#######----------------

##-----------rasti pelningumo ir nuostolio santyki

# pelno_nuostolio_sk = [len(data[data["Profit"]>0]), len(data[data["Profit"]<0])]
#
# # print(pelno_nuostolio_sk)
# labels = 'pelningi', 'nuostolingi'
# plt.pie(pelno_nuostolio_sk, labels = labels, autopct="%1.1f%%", startangle=90)
# plt.title("Pyragas")
# plt.show()
####---------------
# Pelno_nuostoliu_sk = [len(data[data["Profit"]>0]), len(data[data["Profit"]<=0])]
#
# labels = 'Pelningi', 'Nuostolingi'
# colors = ["lightskyblue", "green"]
# plt.pie(Pelno_nuostoliu_sk, labels = labels, autopct='%1.1f%%', startangle=90)
# plt.title("Pyragas")
# plt.show()
#
#
#
# print(Pelno_nuostoliu_sk)


###-----------kurie klientai dazniausiai apsipirkinejo

# Pirkeju_top_10 = data.value_counts("Customer Name").sort_values(ascending=False).head(10)
#
# plt.figure(figsize=(10,6))
# Pirkeju_top_10.plot(kind="barh", color="skyblue")
# plt.title("Top 10 Klientu")
# plt.xlabel("kiekis")
# plt.ylabel("vardai")
# plt.xticks(rotation=0, ha="right")
# plt.show()

# print(Pirkeju_top_10)

###------produktu pardavimai pagal kategorija

# p_p_p_k = data.grou("Category")["Revenue"].sum().reset_index()
# pppk = p_p_p_k["Revenue"
# kategorijos = p_p_p_k["Category"]
#
# labels = 'Alkoholis', 'Kava',"Limo","Arbata"
# colors = ["lightskyblue", "green"]
# plt.pie(pppk, labels = kategorijos, autopct='%1.1f%%', startangle=90)
# plt.title("Statistika")
# plt.show()

####________Pirkimai_pagal_metu_laika

# data["Purchase Month"] = pd.to_datetime(data["Purchase Date"]).dt.month
#
# seasons = {
#     12:"Ziema", 1:"Ziema",2:"Ziema",
#     3:"Pavasaris", 4:"Pavasaris",5:"Pavasaris",
#     6:"Vasara", 7:"Vasara",8:"Vasara",
#     9:"Ruduo", 10:"Ruduo",11:"Ruduo",
# }
#
# data["Metu laikai"] = data["Purchase Month"].map(seasons)
# data.groupby("Metu laikai")["Revenue"].sum().reindex(["Ziema", "Pavasaris", "Vasara", "Ruduo"]).\
# plot(kind="pie", autopct= "%1.1f%%", figsize=(10,7))
#
# plt.title("Statistika")
# plt.ylabel("")
# plt.show()

####--------------



