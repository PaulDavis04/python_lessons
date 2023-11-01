# age = 20
# age = 25.11
# first_name = "Groch"
# is_online = False
# print (age)

# name = input("Koks tavo vardas? ")
# print("Labas " + name)
# #  input("Koks tavo vardas? ")

# --------------

# a=5
# b=25
# c=88
#
# a-=c
# print(a)
# ------------------

# a=79
# b=14
# print(a==b)
# ----------------

# x = 'Labas babas'
# y = {1:'ab', 2:'cd'}
#
# print('L' in x)
#--------
# print("Sveiki, Atvyke pas mus")
# #
# vardas = input("Koks, Jusu vardas?\n")
# #
# print("Sveikiname prisijungus " + vardas + " prie musu!!!\nKuo galetume jums padeteti?")
# ###-----------
#
# meniu = "----MENIU----\n1. Pienas\n2. Kefyras\n3. Batonas\n4. Duona"
#
#
# print(vardas+", Gal kazko is musu meniu?\nStai ka galime pasiulyti?\n" + meniu)
#
# uzsakymas = input()
#
# print("Puikus pasirinkimas " + vardas +", jusu " + uzsakymas+"bus tuoj paruostas issinesti." )
#-----------------------------------
#-----------
#
# print('labas')
#
# vardas = input("koks vardas?->>")
#
# if vardas == "Paul":
#     print("aloha")
# else:
#     print("Labas "+ vardas + ", bukite pasveikinti!!!")

##-----------

# flats_data = []
# def create_and_insert_flats():
#     #kuriam connectiona prie duomenu bezes:
#     connection = psycopg2.connect(
#         host = "localhost",
#         port = 5432,
#         database = "Autogidas",
#         user="postgres",
#         password = "Litovic"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS autogidas_hyundai(
#             id SERIAL primary key,
#             flat_title VARCHAR(300),
#             flat_price DECIMAL(10,2)
#         )
#     """
#
#     cursor.execute(create_table_query)
#     print("Lentele sukurta!")
#
#
#     url = "https://autogidas.lt/skelbimai/automobiliai/?f_41=2018&f_265=Kair%C4%97je&ac_1=1&s=1542417340&f_1%5B0%5D=Hyundai&f_model_14%5B0%5D=/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content,"html.parser")
#     content_block = soup.select('div. items-container container-section div')
#
#
#
#     for content in content_block:
#         try:
#             flat_title = content.find("h2", class_="item-title").text.strip()
#             flat_price = content.find("div", class_="item-price").text.strip()\
#                 .replace(" ", "").replace("€", "")
#             cursor.execute("select 1 from autogidas_hyundai where flat_title = %s and flat_price = %s",
#                         (flat_title, float(flat_price)))
#             exists = cursor.fetchone()
#             if not exists:
#                 cursor.execute("INSERT INTO autogidas_hyundai (flat_title, flat_price) VALUES (%s, %s)",
#                             (flat_title, float(flat_price)))
#             # print(flat_title, flat_price)
#             # flats_data.append((flat_title, flat_price))
#
#             # insert_query =
#
#
#         except AttributeError:
#             continue
#
#     print("Flats ikelta sekmingai!")
#     print(len(flats_data))
#
#     connection.commit()
#
# create_and_insert_flats()





