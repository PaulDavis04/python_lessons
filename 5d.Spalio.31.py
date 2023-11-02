#####-----------------PANDA--------------#####
import pandas as pd

import matplotlib.pyplot as plt
import psycopg2
import requests
from bs4 import BeautifulSoup

#
# data = {
#     "Vardas": ["Jonas", "Andrius", "Migle", "Ana"],
#     "Amzius": [25, 28, 29, 19],
#     "Miestas": ["Vilnius", "Klaipeda", "Kaunas", "Rokiskis"]
# }
#
# df = pd.DataFrame(data)

#grupavimas
# vyresni_nei_25 = df[df["Amzius"] >25]
# grupavimas_pagal_miesta = df.groupby("Miestas").size()
# df = df.sort_values(by="Amzius", ascending=False)
# df["Darbo_stazas"] = [3,6,7,1]
# df.drop(columns=["Darbo_stazas"], inplace=True)  #naudoti--INPLACE=___

# eiluciu_sk = df.shape[0]
# stulpeliu_sk = df.shape[1]
#
# print(f"Eiluciu skaicius {eiluciu_sk}, Stulpeliu skaicius {stulpeliu_sk}")

#####------------------------------------------------------

# df = pd.read_csv("Sales_Records.csv")
# df ["Profit"] = df["Total Revenue"] - df["Total Cost"]
# # #
# df["Profit"] = df["Profit"].round(2)
#
# # df.to_csv("Naujas sales_records.csv", index=False)  #suformuoja, sudaro nauja dokumenta
#
# # print("Bendras pelnas", df["Profit"].sum(),df["Total Revenue"].sum(), df["Total Cost"].sum())
#
# df["Order Date"] = pd.to_datetime(df["Order Date"])
# df["Ship Date"] = pd.to_datetime(df["Ship Date"])
# # df["Units Sold"] = df["Units Sold"].astype(int)
#
# df["Dienu skirtumas"] = (df["Ship Date"] - df["Order Date"]).dt.days
#
# # sort_profit = df.sort_values(by="Profit", ascending=False)
# # print(sort_profit)
# # print(df.isnull().sum())             #tikrina tuscius laukus
#
# ####----------
#
# # df["margin on revenue"] = (df["Profit"]/df["Total Revenue"])*100  #pelnas procentais
# # df["margin on revenue"] = df["margin on revenue"].round(2).astype(str) + "$"    # paprastesnis format
# # df["margin on revenue"] = df["margin on revenue"].apply(lambda x : f"{x:.2f}%") # sudetingesnis formatavimas
#
#
#
# # print(df)
#
# # import mathplotlib.pyplot as plt
#
# # plt.figure(figsize=(20,10))
# # plt.hist(df["Profit"], bins=10, edgecolor="black")
# # plt.title("Pelno histograma")
# # plt.xlabel("Pelnas")
# # plt.ylabel("Imones")
# # plt.savefig("Histograma.jpg")  #padaro foto
# # plt.show()
#
# # plt.bar(["Unit Price"], ["Units Sold"], [df["Unit Price"].mean(), df["Units Sold"].mean()])
# # plt.title("Vidutine kaina")
# # plt.ylabel("Kaina")
# # plt.show()
#
# plt.figure(figsize=(6,8))
# plt.hist(df["Dienu skirtumas"], bins=15, edgecolor="black")
# plt.title("Dienu skirtumas")
# plt.xlabel("Dienu skirtumas")
# plt.ylabel("Uzsakymu kiekis")
# plt.show()

###__________________ORAI________________####


# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
#
# weekdays = content.find_all("span", class_= "date")
# temperatures = soup.find_all("span", class_="big up-from-zero")[1::2]
#
#
# filter_weekdays = [weekday.get_text().split(",")[0] for weekday in weekdays]
# day_temperatures = []
# for temperatures in temperatures:
#     temp_text = temperatures.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
# interval = min(len(filter_weekdays), len(day_temperatures))
#
# data = {"weekday":filter_weekdays, "temperatures": day_temperatures}
#
# df = pd.DataFrame(data)
#
# plt.figure(figsize=(10,7))
# plt.bar(df["weekday"], df["temperatures"])
# plt.title("Temperaturos kaita per savaite")
# plt.xlabel("Savaites diena")
# plt.ylabel("Temperatura C")
# plt.show

# print(df)

# Uzdavinys su temperaturomis:
######------------MARTYNO0-----------Orai


# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
#
#
# weekdays = soup.find_all('span', class_= "date")
# temperatures = soup.find_all('span', class_= "big up-from-zero")[1::2]
#
# filter_weekdays = [weekday.get_text().split(",")[0] for weekday in weekdays]
# day_temperatures = []
# for temperature in temperatures:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
# interval = min(len(filter_weekdays), len(day_temperatures))
#
# data = {"weekday": filter_weekdays,
#         "temperatures": day_temperatures
# }
#
# df = pd.DataFrame(data)
#
# plt.figure(figsize=(10,7))
# plt.bar(["Vidutine temperatura"], df["temperatures"].mean())
# plt.title("Temperaturos kaita per savaite")
# plt.ylabel("Temperatura C")
# plt.show()
#
# print(df.["temperatures"].mean().round(2))

#-----------nauja----visos dienos--------
# vidutine dienos temperatura

# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
#
#
# weekdays = soup.find_all('span', class_= "date")
# day = soup.find_all('span', class_= "big up-from-zero")[1::2]
# night = soup.find_all('span', class_= "big up-from-zero")[0::2]
#
# filter_weekdays = [weekday.get_text().split(",")[0] for weekday in weekdays]
# day_temperatures = []
# night_temperatures = []
#
# for temperature in day:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
#
# for temperature in night:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     night_temperatures.append(temp_value)
#
# data = {"weekday": filter_weekdays,
#         "dtemperatures": day,
#         "ntemperatures": night
# }
#
# df = pd.DataFrame(data)
#
# df["Temperaturu vidurkis"] = (df["dtemperatures"] + df["ntemperatures"])/2
# df.drop(columns=["dtemperatures", "ntemperatures"], inplace=True)
# print(df)
#
# #
# #
# plt.figure(figsize=(10,7))
# plt.bar(df["weekday"], df["Temperaturu vidurkis"])
# plt.title("Vidutine dienos temperatura")
# plt.ylabel("Temperatura C")
# plt.show()

# print(night_temperatures)

###______EXPLORE THE CRYPTOECONOMY___________###########

import requests

data = []
for i in range(6):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }
    url = f"https://www.coinbase.com/explore?page={i}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")



    table = soup.find("table", class_="cds-table-top40r1")

    if table:
        rows = table.find_all("tr")
        for row in rows:
            columns = row.find_all("td")
            if len(columns) >= 8:
                player_data = [column.text.strip() for column in columns]
                data.append(player_data)

    columns = ["Name", "Price", "Charts", "Change", "Market cap", "Volume (24)", "Suply", "Trade"]

df = pd.DataFrame(data, columns = columns)

df.to_csv("COINBASE231102.csv", index=False)


print(df)
# print(content_block)
