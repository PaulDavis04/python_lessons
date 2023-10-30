#############-----------OBJEKTINIS   PROGRAMAVIMAS-----##########


# class Automobilis:
#     def __init__(self, marke, modelis, metai, variklio_turis, kuro_tipas):
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = metai
#         self.variklio_turis = variklio_turis
#         self.kuro_tipas = kuro_tipas
#         self.rida = 0
#
#
#
#     def automobilio_pavadinimas(self):
#         return f" Automobilis: {self.marke}\n Automobilio marke: {self.modelis}\n Automobilio_pagaminimo_metai: {self.metai}"
#
#     def vaziuoti(self, km):
#         self.rida += km
#         return f"Vaziuojam {km}km. Bendra rida {self.rida}km"
#
# auto1 = Automobilis("Audi","A8",2021,3.0,"Benzinas")
# print(auto1.automobilio_pavadinimas())
# print(auto1.vaziuoti(150))
# print()
# ###METODAS
# # auto1 = Automobilis("Audi","A8",2021)
# # print(auto1.automobilio_pavadinimas())

#####----------------------------------------------------------------

# class Gyvunas(object):
#     def __init__(self, rusis, svoris, amzius, vardas):
#         self.rusis = rusis
#         self.svoris = svoris
#         self.amzius = amzius
#         self.vardas = vardas
#
#     def gyvuno_aprasymas(self):
#         return f" Gyvunas: {self.rusis}\n Svoris: {self.svoris}\n Amzius: {self.amzius}\n Vardas: {self.vardas}"
#
#     def valgyti(self):
#         return f" {self.vardas} valgo"
#
#     def prisistatymas(self):
#         return f" As esu {self.rusis}, ir mano vardas yra {self.vardas}. "
#
# kate = Gyvunas("Rusu Melynasis", 15, 10, "Mikis")
# print(kate.gyvuno_aprasymas())
# print(kate.valgyti())
# print(kate.prisistatymas())
# #####################----------------------------######################
# from colorama import init, Fore

# init()
# class Uzduotis:
#     def __init__(self,pavadinimas, aprasymas):
#         self.pavadinimas = pavadinimas
#         self.aprasymas = aprasymas
#         self.atlikta = False                       #####uzduotie objektas...klase..
#
#     def atlikimas(self):
#         self.atlikta = True
#         print(f"Uzduotis '{self.pavadinimas}' bovo atlikta")
#
#     def info(self):
#         return f"Pavadinimas {self.pavadinimas}\n Aprasymas:{self.aprasymas}"
#
# class TodoSarasas:
#     def __init__(self):
#         self.uzduociu_sarasas = []
#
#     def prideti_uzduoti(self,pavadinimas,aprasymas):
#         uzduotis = Uzduotis(pavadinimas,aprasymas)
#         self.uzduociu_sarasas.append(uzduotis)
#
#     def visos_uzduotys(self):
#         if not self.uzduociu_sarasas:
#             print("Uzduociu_sarasas yra tuscias")
#         for uzduotis in self.uzduociu_sarasas:
#             print(uzduotis.info())
#
#     def pazymeti_kaip_atlikta(self,pavadinimas):
#         for uzduotis in self.uzduociu_sarasas:
#             if uzduotis.pavadinimas == pavadinimas:
#                 uzduotis.atlikimas()
#                 return
#         print(f"Uzduotis pavadinimu: '{pavadinimas}' nerasta")
#
# todo_sarasas = TodoSarasas()
#
# while True:
#     print("\nPasirinkite veiksma:")
#     print("1.Prideti uzduoti:")
#     print("2.Perziureti uzduotis:")
#     print("3.Pazymeti uzduoti kaip atlikta;")
#     print("4.Iseiti is uzduociu saraso")
#     pasirinkimas = input()
#
#     if pasirinkimas == "1":
#         pavadinimas = input("iveskite uzduoties pavadinima_>")
#         aprasymas = input("Iveskite uzduoties aprasyma_>")
#         todo_sarasas.prideti_uzduoti(pavadinimas,aprasymas)
#         print("Uzduotis prideta sekmingai!!!")
#
#     elif pasirinkimas == "2":
#         todo_sarasas.visos_uzduotys()
#     elif pasirinkimas == "3":
#         pavadinimas == input("Iveskite uzduoties pavadinima kuria norite pazymeti kaip atlikta_>")
#         todo_sarasas.pazymeti_kaip_atlikta(pavadinimas)
#     elif pasirinkimas == "4":
#         print("Iseinama..")
#         break
#     else:
#         print("Neteisingas pasirinkimas! Prasome bandyti dar karta!")

#__________________________________________________________________________________
#
# class Saskaita:
#     def __init__(self,vardas,pavarde,pradinis_likutis=0):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pradinis_likutis =pradinis_likutis
#
#     def inesti_pinigus(self, suma):
#         if suma > 0:
#             self.pradinis_likutis +=suma
#         else:
#             print:("Klaida, negalima inesti neigiamos sumos")
#
#     def nusiimti_pinigus(self, suma):
#         if suma > 0:
#             if suma < self.pradinis_likutis:
#                 self.pradinis_likutis -= suma
#                 print(f"Jus sekmingai nusiemete {suma}")
#             else:
#                 print("Jusu likutis nepakankamas")
#         else:
#             print("Negalite nusiimti neigiamos sumos")
#
#     def patikrinti_likuti(self):
#         return f"Jusu {self.vardas} {self.pavarde} saskaitos likutis yra:>> {self.pradinis_likutis}"
#
# numeris_vienas = Saskaita("Petras", "Petraitis")
#
# numeris_vienas.inesti_pinigus(500)
# numeris_vienas.nusiimti_pinigus(200)
# print(numeris_vienas.patikrinti_likuti())

#------------#####----------------------####-----------------

# class Studentas:
#     def __init__(self, vardas, pavarde, amzius, studento_numeris, pazymiai = None):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
#         self.studento_numeris = studento_numeris
#         self.pazymiai = pazymiai if pazymiai else []
#
#     def studento_vidurkis(self):
#         return sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0
#
#     def prideti_pazimi(self,pazymys):
#         self.pazymiai.append(pazymys)
#
#     def studento_informacija(self):
#         return (f"Studento vardas: {self.vardas}, studento pavarde: {self.pavarde}, amzius {self.amzius}, "
#                 f"studento numeris: {self.studento_numeris}, pazymiai: {self.pazymiai}")
#
#     def pasalinti_pazimi(self, pazymys):
#         if 0<= pazymys < len(self.pazymiai):
#             del self.pazymiai[pazymys]
#         else:
#             print("Toks pazymys nerastas")
#
#     def __str__(self):
#         return f"{self.vardas} {self.pavarde} {self.studento_numeris} {self.pazymiai}"
# class StudentuValdymoSistema:
#     def __init__(self):
#         self.studentu_sarasas = []
#
#     def prideti_studenta(self, studentas):
#         self.studentu_sarasas.append(studentas)
#         print("Studentas sekmingai pridetas")
#
#     def pasalinti_studenta(self, studento_numeris):
#         naujas_studentu_sarasas = []
#         for s in self.studentu_sarasas:
#             if s.studento_numeris != studento_numeris:
#                 naujas_studentu_sarasas.append(s)
#         self.studentu_sarasas = naujas_studentu_sarasas
#         # print("Studentas pasalintas")
#
#     def visi_studentai(self):
#         return self.studentu_sarasas
#
#     def __str__(self):
#         return "\n ".join(str(studentas) for studentas in self.studentu_sarasas)
#
#
# studentu_sistema = StudentuValdymoSistema()
# studentas1 = Studentas("Petras", "Petraitis", 21, 565898)
# studentas2 = Studentas("Brunonas", "Bludolas", 20, 458745)
#
# studentas1.prideti_pazimi(7)
# studentas1.prideti_pazimi(9)
# studentas1.prideti_pazimi(8)
# studentas1.prideti_pazimi(4)
#
# studentu_sistema.prideti_studenta(studentas1)
#
#
# studentas1.studento_informacija()
# # studentas1.pasalinti_pazimi()
# studentas1.studento_informacija()
#
# studentas2.studento_informacija()
# # print(studentu_sistema.visi_studentai())
# # print(studentu_sistema.pasalinti_studenta())
#
# for studentas in studentu_sistema.visi_studentai():
#     print(studentas)
#
# print(studentu_sistema)

###---------------##########---------------###########------------###

#+++++Sukurkite Studentas klase kuri reprezentuoja individualų studentą,------
# +++++turintį savo vardą, pavardę, amžių, studento numerį ir pažymių sąrašą.--------

# +++++Antroje klasėje StudentuValdymoSistema - tai klasė, skirta valdyti studentų sąrašą.--


# +++++Sukurkite metoda kuris isves studento vidurki;----S

# +++++sukurkite metoda kad galetumete prideti studenta;----V

# +++++Sukurkite metoda kuris grazins visa studento info;----S

# +++++Sukurkite metoda kuris pasalintu studenta;----V

# +++++Sukurkite metoda kad galetumete prideti pazymi studentui;----S

# +++++Sukurkite metoda kad galetumete pasalinti pazymi;----S

# +++++Sukurkite metoda kad galetumete rikiuoti studentus pagal jų pažymių vidurkį, vardą ar kitą kriterijų.----

# +++++Sukurkite metoda leidžianti filtruoti studentus pagal jų pažymių vidurkį (pvz., visi studentai, ----
# +++++kurių vidurkis didesnis už 8).----