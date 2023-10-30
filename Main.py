
# vardas = "Petras"
# amzius = "30"
# ar_petras_moka_programuot = False
# jo_pirkiniu_krepselio_suma = 95.3
# print(type(ar_petras_moka_programuot))

# print ("Mano pusbrolio vardas yra " + vardas + " jo amzius " + amzius)
#
# print("Mano dragugo vardas yra " + vardas + "jo amzius " ,amzius, ar_petras_moka_programuoti
#listas(array) masyvas = []
# vaisiai = ["obuolys", "bananas", "arbuzaz", "kriause"]
# # ilgis = len(vaisiai)
# # print(vaisiai[:2]) #sliece
#
# # prideti_i_pradzia
# # ")vaisiai.insert(0."melionas                   #pagal nurodyta indeksa
# # pridedame_vaisiu = vaisiai.append("melionas")   #  prideti i sarasa pakeistas kintamas
# # print(vaisiai)
#
# # keiciam_reiksme = vaisiai[1] = "kivis"           #keiciam reiksme#
# # print(vaisiai)
# indeksas = vaisiai.index("arbuzaz")
# # vaisiai.pop(2)                                      #ismeta pagal indexa#
# print(indeksas)

#Zodynas -dictionary structure=my_dict ={key1:value1, key2:value2}

# zodynas = {
#     "vardas": " jonas",
#     "amzius": 30,
#     "miestas": "vilnius"
# }
# # zodynas["ar_studentas"] = True
# del zodynas["miestas"]              #istrina su raktu
# print(zodynas)

#
# sarasas
# studentai = [
#     {
#         "vardas" : "jonas",
#         "amzius": 22,
#         "miesta": "kaunas",
#         "profesija": "jurgelis meistrelis"
#     },
#     {
#         "vardas" : "ona",
#         "amzius": 23,
#         "miestas": "pumpenai",
#         "profesija": "gydytoja",
#
#     },
#     {
#         "vardas" : "antanas",
#         "amzius": 33,
#         "miestas": "vilnius",
#         "profesija": "vairuotojas"
#     }
# ]
#   print(studentai["ona"])


# naujas_studentas = {
#         "vardas" : "tomas",
#         "amzius": 33,
#         "miestas": "vilnius",
#         "profesija": "lakunas"
#
# }
#
# studentai.append(naujas_studentas)                 #prideti  studenta
# print(studentai[0])


#

# if salyga       if salyga: jusu veiksmai;

# amzius = 12
# if amzius < 18:                              #dvitaskis
#     print("asmuo yra pilnametis")
# elif amzius > 18:                             #elif gali but belekiek
#     print("asmuo yra paauglys")
# else:                                            #nera kintamojo, dvitaskis po else
#     print("asmuo nera pilnametis" )           #tarpai nuo krasto!!!!!


# vaisiai = ["bananaz", "kivis", "obuolys"]
#
# if "kivis" in vaisiai:
#     print("vaisius kivis")
# elif not "kivis" in vaisiai:
#     print("vaisius nerastas")
# else:
#     print("vaisius nerastas" )


# vaisiai = []
#
# if not vaisiai:  #True                 IF NOT tikrina ar kas yra--jeigu true
#     print("vaisiu sarasas tuscias")
# elif "kivis" in vaisiai:
#     print("vaisius kivi")
# else:
#     print("vaisius kivis nerastas, taciau sarase yra elementu" )



# age = 18
# has_id = True
#
# if age >= 18:
#     if has_id:
#         print("Gali balsuoti")
#     else:
#         print("Jums reikia asmens tapatybes korteles")
# else:
#     print("Jums dar negalima balsuoti")


# prekiu_kategorijos = ["vaisiai", "mesa", "darzoves"]
#
# prekes = {                                  #Dictionary..
#     "vaisiai":["obuoliai","bananai"],
#     "mesa":["kiauliena", "vistiena"],
#     "darzoves":["bulves", "pomidorai"]
# }
#
# #  norime rasti prekes kategorija "Mesa" ir prekes "vistiena''
#
# norima_kategorija = "mesa"
# norima_preke = "vistiena"
#
# if norima_kategorija in prekiu_kategorijos:
#     if norima_kategorija in prekes[norima_kategorija]:
#         print(f'Parduotuveje yra {norima_preke}')
#     else:
#         print(f'Parduotuveje_nera {norima_preke}')
# else:
#     print(f'Parduotuveje nera prekiu kategorijos: {norima_kategorija}')
#
# 1 dalis. Sukurkite sąrašą su žmonių vardais ir amžiumi:
# 2 dalis. Jūsų užduotis - parašyti kodą, kuris išvestų kiekvieno žmogaus vardą su amžiumi:
# "nepilnametis", "suaugęs" arba "vaikas" (jei amžius yra 18).



# 1.
# zmones = [
# {
#     'vardas' : 'algis',
#     'amzius' : 25,
# },
#     {
#     'vardas' : 'tomas',
#     'amzius' : 44,
# },
#     {
#     'vardas' : 'ilona',
#     'amzius' : 17
# }
# ]
# #2.
#
# zmogus = zmones[0]
#
# if zmogus ['amzius'] > 18:
#     print(f' sis zmogus {zmogus["vardas"]} yra suauges')
# if zmogus['amzius'] == 18:
#     print(f' sis zmogus {zmogus["vardas"]}  yra paauglys')
# if zmogus['amzius'] < 18:
#     print(f' sis zmogus {zmogus["vardas"]}  yra nepilnametis')
# # else:
# #     print(zmogus ['vardas'], 'yra vaikas')
#
#
# 2 užduotis:
# 1 dalis: Sukurkite žodyną su darbuotojo informacija(Vardas, atlyginimas,pareigos);
# 2.dalis: Pagal darbuotojo pareigas (jei jis yra "inžinierius"), padidinkite jo atlyginimą 10%.
# Jei jis nėra "inžinierius", palikite atlyginimą nepakeistą.



# 2.1

# darbuotojas = {
#     "Vardas": "Tomas",
#     "Atlyginimas": 2200,
#     "Pareigos": "Inzinierius"
# }
# if darbuotojas["Pareigos"] == "Inzinierius":
#      # padidinti 10% alyginima
#      #ilgesnis uzrasymas
#    # darbuotojas["Atlyginimas"] = darbuotojas["Atlyginimas"] * 1.10
#
#    #trumpesnis
#      darbuotojas["Atlyginimas"] *=1.10
#
# print(darbuotojas)



# 3 užduotis:
# 1 dalis: Sukurkite sąrašą su knygų informacija(Pavadinimas, išleidimo metai);


#
#
# if knyga["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['Pavadinimas']}")knygos = [
# #     {"Pavadinimas": "Haris Poteris", "isleidimo_metai": 1997},
# #     {"Pavadinimas": "Moby Dick", "isleidimo_metai": 1851},
# #     {"Pavadinimas": "Metai", "isleidimo_metai": 2002}]
# # knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_>"))
# #
# #
# # knyga = knygos[1]

# neveikia?
# ----------------------------------------------------------------------------------------------------------
# knygos = [
#     {"Pavadinimas": "Haris Poteris", "isleidimo_metai": 1997},
#     {"Pavadinimas": "Moby Dick", "isleidimo_metai": 1851},
#     {"Pavadinimas": "Metai", "isleidimo_metai": 2002}]
#
# try:
#     knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))
#
#     if knygos[0]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['Pavadinimas']}")
#     elif knygos[1]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[1]['Pavadinimas']}.")
#     elif knygos[2]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[2]['Pavadinimas']}.")
#     else:
#         print(f"Deja, knygų išleistų {knyga_pagal_ieskomus_metus} metais nėra.")
#
# except ValueError:
#     print("Blogas ivesties formatas")


# ---------------------------------------------------------------------------------------------------------



#importuojamos bibliotekos VISUOMET rasomos pirmose eilutese

# import os
#
# dabartinis_katalogas = os.getcwd()
# # print(dabartinis_katalogas)
#
# # norimas_aplankas = input("Iveskite aplanko pavadinima, kurio turini norite matyti_>")
# naujas_katalogas = input("Prasome nurodyti katalogo lokacija_>")
# # keiciam_kataloga = os.chdir()
#
#
#
# try:
#     keiciam_kataloga = os.chdir(naujas_katalogas)
#     if os.getcwd() == naujas_katalogas:
#         print(f"Dabartinis katalogas sekmingai pakeistas i {naujas_katalogas}")
#     #bandome gauti aplanko turini;
#     turinys = os.listdir(norimas_aplankas)
#     print(", ".join(turinys))
#
# except FileNotFoundError:
#     print(f"Deja aplankas ' {naujas_katalogas}' nerastas")

#------------------------------------------------


# import os
# import shutil
#
#
#
# #snyk
#
# EXTENSION_MAP = {
#     '.jpg' :"Images",
#     '.jpeg' : "Images",
#     '.png' : "Images",
#     '.gif' : "Images",
#     '.pdf' : "Documents",
#     '.txt' : "Documents",
#     '.json' : "Json files"
#
# }
#
# filename = input("Please the name of the file you want to organize_>")
#
# file_extension = os.path.splitext(filename) [1]
#
# try:
#     if os.path.exists(filename) and file_extension in EXTENSION_MAP:
#         directory_name = EXTENSION_MAP[file_extension]
#
#
#         #create the directory if it doesn't exist
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
#
#             #Move to file
#             chutil.move(filename, os.path.join(directory_name, filename))
#             print(f"{filename} has been moved to {directory_name}")
#     else:
#         print("The file does not exist or its extension in not recognized")
# except FileNotFoundError:
#     print(f"Error: {filename} was not found")
# except PermissionError:
#     print(f"Error: You don't have permissions to move '{filename}")

# darbuotojas = {
#     "Zmogus1": {
#     "Vardas": "Tomas",
#     "Atlyginimas": 2200,
#     "Pareigos": "Inzinierius"
# },
# {
#     "Zmogus2"
#     "Vardas": "Olegas",
#     "Atlyginimas": 2000,
#     "Pareigos": "Vairuotojas"
#
# }
# }

# --------

# 1. Sukurkite prekių sąrašą su kainomis ir raskite brangiausią prekę.
###___________________nebaigtas-------------
# prekiu_kaina = [
#     {"Pavadinimas": "Morka", "Kaina": 1.5},
#     {"Pavadinimas": "Kopustas", "Kaina": 3},
#     {"Pavadinimas": "Bulves", "Kaina": 2.2},
#     {"Pavadinimas": "Svogunai", "Kaina": 1.1}
# ]
#
#
# a = prekiu_sarasas[0]
# b = prekiu_sarasas[1]
# c = prekiu_sarasas[2]
# d = prekiu_sarasas[3]
#
# verte = max(a["kaina"],b["kaina"],c["kaina"])
#
# if a["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {a["preke"]}')
# if b["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {b["preke"]}')
# if c["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {c["preke"]}')

######---------------------------------

# 2. Sukurkite žodyną su studento pažymiais ir raskite ar studentas išlaikė egzaminą;

# studentai = {
#     "Darius": {"Matematika": 6, "Anglu kalba": 8, "Lietuviu kalba": 9},
#     "Benas":  {"Matematika": 8, "Anglu kalba": 8, "Lietuviu kalba": 8},
#     "Kristupas": {"Matematika": 5, "Anglu kalba": 8, "Lietuviu kalba": 5},
#     "Anzelmas": {"Matematika": 7, "Anglu kalba": 9, "Lietuviu kalba": 8}
# }





# 3. Sukurkite žodyną su kliento informacija ir patikrinkite
# ar jo sąskaitoje yra pakankamai lėšų tam tikram pirkiniui.

# Klientai = {
#     "Daiva": 1000,
#     "Roberta": 500,
#     "Pranas": 750,
#     "Gintaras": 250
# }
####_______________________LINOS

# Sukurkite žodyną su kliento informacija,
# # ir patikrinkite ar jo sąskaitoje yra pakankamai lėšų tam tikram pirkiniui.
#
# Klientas = {
#     "Vardas": "Jonas",
#     "Amzius": 40,
#     "Miestas": "Vilnius",
#     "Telefonas": "+37063025252",
#     "Sask.likutis": 10000
# }
# # print(Klientas)
#
# Pirkinys = 500
# # 10000 < 500 = False
# if Klientas["Sask.likutis"] < Pirkinys:
#     print("lesu nepakanka")
# else:
#     print("galima pirkti")

#####----------------------
# 4.Pagal nurodytą pajamų sumą, paskaičiuokite mokesčius,
# taikant šias taisykles: pajamoms iki 1000 - 10%, nuo 1001 iki 5000 - 15%, virš 5000 - 20%.


####____________ROSVALDO--------------
# pajamos = -25
#
# if pajamos > 5000:
#     print("Mokesciu suma", + pajamos * 0.2)
# elif pajamos > 1000:
#     print("Mokesciu suma", + pajamos * 0.15)
# elif pajamos > 0:
#     print("Mokesciu suma", + pajamos * 0.1)
# else:
#     print("Pajamu nera")
__________________________________________________________________________________