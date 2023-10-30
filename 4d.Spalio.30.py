#---------OPEN-------####

# with open("text.txt", "w") as f:   #adresas kur rasyti
#     content = f.write("Labas pasauli")


# with open("text.txt", "r") as f:  #skaityt
#     content = f.read()
# print(content)

# with open("text.txt", "a") as f:   #prideti
#     content = f.write("\nKaboomi")
# print(content)

###----------------###---------------##


#########----------scrapinimas------------##########

import requests
from bs4 import BeautifulSoup
import psycopg2

#200-ok
#301-302 -file found/ redirect
#403- forbiden
#404 -file not foound
#500-server error

# response = requests.get(url)
# # print(response.status_code) #stebeti
# print(response.content)

# flats_data = []
#
# def create_and_insert_flats():
#
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="Aruodas",
#         user="postgres",
#         password="Litovic"
#         )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS Aruodas_uzsienis (
#             id SERIAL primary key,
#             flat_title VARCHAR (300),
#             flat_price DECIMAL (20,2)
#         )
#     """
#     cursor.execute(create_table_query)
#     print("Table created Successfuly")
#
#     url = "https://www.aruodas.lt/uzsienio-objektai/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     content_block = soup.select("div.project-list-content div")
#     # print(content_block)
#     # flats_data[]
#     for content in content_block:
#         try:
#             flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
#             flat_price = content.find("h3", class_="project-title-full project-min-values ").text.strip()\
#                 .split(sep="Kaina:")[1].replace(" ","").replace("€", "")
#
#
#             # print(flat_title, flat_price)
#             # flats_data.append((flat_title, flat_price))
#             insert_query = "INSERT INTO aruodas_uzsienis(flat_title, flat_price) VALUES (%s, %s)"
#             cursor.execute(insert_query, (flat_title, flat_price))
#
#         except AttributeError:
#             continue
#     print("FLATS INSERTED")
#
#     connection.commit()
#
#     # print(flats_data)
# create_and_insert_flats()




#--kitaip

# if flat_title and flat_price:
#     flats_data.append((flat_title, flat_price))
#     continue...............................
#.....................


# kuriame patys su kitais objektais:

flats_data = []
def create_and_insert_flats():
    #kuriam connectiona prie duomenu bezes:
    connection = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "Aruodas",
        user="postgres",
        password = "Litovic"
    )

    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS aruodas_uzsienis(
            id SERIAL primary key,
            flat_title VARCHAR(300),
            flat_price DECIMAL(10,2)
        )
    """

    cursor.execute(create_table_query)
    print("Table created Successfully!")


    url = "https://www.aruodas.lt/uzsienio-objektai/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    content_block = soup.select('div.project-list-item div')



    for content in content_block:
        try:
            flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
            flat_price = content.find("h3", class_="project-title-full project-min-values").text.strip()\
                .replace(" ", "").replace("€", "").split(sep="Kaina:")[1]
            cursor.execute("select 1 from aruodas_uzsienis where flat_title = %s and flat_price = %s",
                        (flat_title, float(flat_price)))
            exists = cursor.fetchone()
            if not exists:
                cursor.execute("INSERT INTO aruodas_uzsienis (flat_title, flat_price) VALUES (%s, %s)",
                            (flat_title, float(flat_price)))
            # print(flat_title, flat_price)
            # flats_data.append((flat_title, flat_price))

            # insert_query =


        except AttributeError:
            continue

    print("Flats inserted successfully!")
    print(len(flats_data))

    connection.commit()

create_and_insert_flats()

