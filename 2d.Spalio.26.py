#for raktas in seka
#print(raktas)

# for i in range(5):
#     print("skaicius", i)
#
#
# skaiciai =[1,2,3,4,5]
#
# for skaicius in skaiciai:
#     print("mano saraso skaicius", skaicius)
#
#     --------------------------------------------------------------

# tekstas = "Python data science"
# for raide in tekstas:
#     print(raide)

# ------------------------------------------------------------------

# zodynas = {"a":1, "b":2, "c":3}
#
# for raktas in zodynas:
#     print(raktas, zodynas[raktas])

# ---------------------------------------------------------
# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         #break                           #nutraukia cikla
#         #continue                        #pratesia cikla ismestdamas 3
#     print(skaicius)

#---------------------------------------------------------

# skaiciai = [10,20,30,40,50]
#
#
# suma = sum(skaiciai)
#
# vidurkis = suma /len(skaiciai)
# #print("Gautas vidurkis", vidurkis)
#
# for skaiciai in skaiciai:
#     if skaicius > vidurkis:
#         print(skaicius)

#--------------------------------------------------------------

# sarasas = ["Benas", "Darius", "Onas", "Juozas"]
# print('\n'.join(sarasas))
#
# # for vardas in sarasas:
# #     print(vardas)
#
# # for vardas in sarasas:
# #     print(vardas+'\n')

#--------------------------------------------------------------

# tekstas_1 = "Python"
# tekstas_2 = ""
# for raide in tekstas_1:
#     tekstas_2 = raide+tekstas_2
#     print(tekstas_2)

#--------------------------------------------------------------

        # daugybos_lentele = 10
#
# for i in range(1,daugybos_lentele+ 1):
#     for j in range(1,daugybos_lentele+ 1):
#         print(i*j, end='\t')                   #\t-raide duoda tarpa... #\n-new line...
#     print()

#--------------------------------------------------------------
#
        #sujungti teksta i vientisa.

# sarasas = ["Labas", "rytas", "mieli", "studentai"]
# sarasas_2 = ""
# for zodis in sarasas:
#     sarasas_2 += zodis+" "   #
# sujungtas_sakinys = sarasas_2.rstrip(sarasas_2)     #rstrip-gale pasalina tarpus(space)
# print(sarasas_2)
#___
# sarasas = ["labas", "rytas", "suraitytas", "skanios", "kavytes"]
# for i in sarasas:
#     print(i, end=" ") #-end= zodzius atskiria su" " pagalba

#-------------------------------------------------------------
#
#####------------WHILE____________________####------------------WHILE


# skaicius  = 10
#
# while skaicius <= 20:      #iki False reiksmes
#     print(skaicius)
#     skaicius +=            #prideda po ___

#-------------------------------------------------
# ivestis = int(input("Iveskite teigiama skaiciu_>"))
#
# while ivestis<0:
#     print("Jusu skaicius neigiamas")
#     ivestis = int(input("Bandykite dar karta_>"))
# print("Ivedete teigiama skaiciu")

#-------------------------------------------------
      #zaidimas#

# atsakymas = 5
# spejimas = int(input("Spekite skaiciu nuo 1 iki 10_>"))
#
# while spejimas != atsakymas:
#     spejimas = int(input("Neteisingas atsakymas! Bandykite dar karta_>"))
#
# print("Sveikiname, atspejote!")

#-------------------------------------------------

                  #meniu#

# ar_veikia = True
# while ar_veikia:
# # while True:#                 ----#Leidzia paleisti is naujo
#     print("___----Meniu----___")
#     print("1.Atspausdinti pasisveikinima")
#     print("2.Iveskite nauja varda")
#     print("3.Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3_>")
#     if pasirinkimas == "1":
#         print(f'Labas!')
#     elif pasirinkimas == "2":                    #elifai tikrins viena pasirinkima, grizta iki pirmo if tikrintis
#         vardas = input("Iveskite nauja varda_>")
#
#         print("Sekmingai ivesdete nauja varda")
#         print(f'Jusu vardas pakeistas i {vardas}')
#     elif pasirinkimas == "3":
#         print("Aciu, kad naudojate programa. IKI")
#         ar_veikia = False
#         # break#                   -----# Leidzia paleisti is naujo
#     else:
#         print:("Neteisingas pasirinkimas! Bandykite dar karta")
##
##
#---------------------------

#parasyti programa kurioje nurodytas paslaptingas zodis kuri turi atspeti,

##___

# paslaptingas_zodis = "akis"
# spejimas = input("Spekite paslaptingaji zodi__>>")
#
# while spejimas != paslaptingas_zodis:
#     spejimas = input("spekite paslaptingaji zodi DAR KARTA_>")
#     print("Norime pasveikinti, Jus ATSPEJOTE!!!!")

###-----------------------------------------------------------------------

####programa, kurioje irasau skaiciu, ismeta to skaiciaus daugybos lentele ir parodo atsakyma####

# pasirinkimas = int(input("Pasirinkite skaiciu nuo 1 iki 10 ->>>"))
# max_skaicius = 1
# while max_skaicius <= 10:
#     rezultatas = max_skaicius*pasirinkimas
#     print(f'{pasirinkimas} x {max_skaicius}')
#     max_skaicius += 1
####-----------------------------------------------------------------------
#--------------------------------------------------------------------------
#                    funkcija

# sintakse funkcijose: def funkcijosPavadinimas(argumentai):
#Jusu kodas

# def pasisveikinti(vardas):   #funkcijos sukurimas
#     print(f"Labas{Vardas}")
#
# pasisveikinti("Paulius")

#-------------------------------------------------------------------------


# def suma(a,b):
#     return a+b             #returnas grazina reiksme, naudojamas su skaiciais
#
# atsakymas = suma(5,3)
# print(atsakymas)            #atsakymo ispausdinimui

#------------------------------------------------------------------------

#------------PROJEKTELIS____________________________________________

#knygu valdymo sistema

# def rodyti_meniu():
#     print("------MENIU------")
#     print("1.Prideti knyga")
#     print("2.Perziureti visas knygas")
#     print("3.Ieskoti knygos pagal pavadinima")
#     print("4.Iseiti")
#
# def prideti_knyga(knygu_sarasas):
#     pavadinimas = input("Iveskite knygos pavadinima->>")
#     autorius = int("Iveskite knygos autoriu->>")
#     knygu_sarasas.append({"pavadinimas": pavadinimas, "autorius": autorius})
#     print(f"Knyga'{pavadinimas}' prideta!!!")
#
# def perziureti_knygas(knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#
# def ieskoti_knygos(knygu_sarasas):
#     ieskomas_pavadinimas = input("Iveskite knygos pavadinima kurios ieskote->>")
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga['pavadinimas'].lower()]
#
#     if rasti_knygas:
#         for knyga in rasti_knygas:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#
#     else:
#         print(f" Knyga su pavadinimu: '{ieskomas_pavadinimas}' nerasta")
#
#
# def main():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma(1-4)->>")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "3":
#             ieskoti_knygos(knygu_sarasas)
#         elif pasirinkimas == "4":
#             print("Iki greito!!!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinki nuo 1 iki 4 !!!")
# if __name__ == "__main__":
#     main()

#-------------------------------------------
#########Programele.   bankine sistema#######

####MANO### MANO####
# banko_saskaitos = {}
#
#
# def rodyti_meniu():
#     print("\n----Bankas------")
#     print("1.Atidaryt nauja saskaita")
#     print("2.Inesti pinigus")
#     print("3.Nusiimti pinigus")
#     print("4.Perziureti saskaitos likuti")
#     print("5.Uzdaryti saskaita")
#     print("6.Iseiti")
#
#
# def prideti_saskaita(paslaugos):
#     saskaitos_turetojas = input("Iveskite Varda->>")
#     pradinis_likutis = int(input("Iveskite savo pradini pinigu likuti->>"))
#     saskaitos_nr = len(banko_saskaitos) + 1
#     banko_saskaitos[saskaitos_nr] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis":pradinis_likutis}
#     print(f"Nauja saskaita '{saskaitos_nr}'  Sekmingai prideta!")
#
#
# def inesti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Iveskite saskaitos nr->>"))
#     suma = int(input("Iveskite inesamu pinigu suma->>"))
#     banko_saskaitos[saskaitos_nr]["pradinis_likutis"] += suma
#
#     print(f"I saskaita nr.: '{saskaitos_nr}' sekmingai inesta '{suma}'")
#
#
#
# def nusiimti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Iveskite saskaitos nr->>"))
#     suma = int(input("Iveskite nusiimamu pinigu suma->>"))
#     if suma <= banko_saskaitos[saskaitos_nr]["pradinis_likutis"]:
#         banko_saskaitos[saskaitos_nr]["pradinis_likutis"] -= suma
#         print(f"Is saskaitos nr.: '{saskaitos_nr}' sekmingai nusiimta '{suma}'")
#     else:
#         print("Nepakanka lesu.Likutis->>'{banko_saskaitos[saskaitos_nr]['pradinis_likutis']}")
#
# def perziureti_likuti(paslaugos):
#     saskaitos_nr = int(input("Iveskite saskaitos nr._>>"))
#     likutis = banko_saskaitos[saskaitos_nr]["pradinis_likutis"]
#     print(f"saskaitos nr.: '{saskaitos_nr}' likutis yra '{likutis}'")
#
# def istrinti_saskaita(paslaugos):
#     saskaitos_nr = int(input("Iveskite saskaitos nr:->>"))
#     del banko_saskaitos[saskaitos_nr]
#     print(f"Banko saskaita nr.:'{saskaitos_nr}' buvo istrinta")
#
# def main():
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite operacijos numeri (1-6):->>")
#         if pasirinkimas == "1":
#             prideti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "2":
#             inesti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "3":
#             nusiimti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "4":
#             perziureti_likuti(banko_saskaitos)
#         elif pasirinkimas == "5":
#             istrinti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "6":
#             break
#         else:
#             print("nuo 1 iki 6 ->>")
# main()
#


#-----------------------#MARTYNO#__________________##

# banko_saskaitos = {
#
#
# }
# def rodyti_meniu():                                 #sukuria funkcija su def ir ()
#     print("\n=== Mini Banko sistema ===")
#     print("1. Atidaryti naują saskaitą")
#     print("2. Įnešti pinigus")
#     print("3. Nusiimti pinigus")
#     print("4. Peržiūrėti sąskaitos likutį")
#     print("5. Uždaryti sąskaitą")
#     print("6. Išeiti")
#
# def prideti_saskaita(paslaugos):                  #sukuria funkcija su def
#     saskaitos_turetojas = input("Iveskite vardą: ")
#     pradinis_likutis = int(input("Įveskite pradinį pinigų likutį: "))
#     saskaitos_nr = len(banko_saskaitos) + 1
#     banko_saskaitos[saskaitos_nr] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
#     print(f"Nauja sąskaita '{saskaitos_nr}' sekmingai prideta!")
#
# def inesti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
#     suma = int(input("Įveskite įnešamų pinigų sumą: "))
#     banko_saskaitos[saskaitos_nr]["pradinis_likutis"] += suma
#     print(f"Į sąskaitą nr.: '{saskaitos_nr}' sėkmingai įnešta '{suma}' eurai")
#
# def nusiimti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
#     suma = int(input("Įveskite nusiimamų pinigų sumą: "))
#     if suma <= banko_saskaitos[saskaitos_nr]["pradinis_likutis"]:
#         banko_saskaitos[saskaitos_nr]["pradinis_likutis"] -= suma
#         print(f"Iš sąskaitos nr.: '{saskaitos_nr}' sėkmingai nusiimta '{suma}' eurai")
#     else:
#       print(f"Jūsų pradinis likutis yra per mazas. Jis yra: '{banko_saskaitos[saskaitos_nr]['pradinis_likutis']}' eurai")
#
# def perziureti_likuti(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
#     likutis = banko_saskaitos[saskaitos_nr]["pradinis_likutis"]
#     print(f"Sąskaitos nr.: '{saskaitos_nr}' likutis yra '{likutis}' eurai")
#
# def istrinti_saskaita(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
#     del banko_saskaitos[saskaitos_nr]
#     print(f"Banko sąskaita nr.: '{saskaitos_nr}' buvo ištrinta")
#
#
# def main():
#     paslaugos = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksmą(1-4): ")
#         if pasirinkimas == "1":
#             prideti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "2":
#             inesti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "3":
#             nusiimti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "4":
#             perziureti_likuti(banko_saskaitos)
#         elif pasirinkimas == "5":
#             istrinti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "6":
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 6")
#
# main()
# ##################

#-----------------------------------------------------------------------------------------

#####Sukurkite funkciją pvm_skaiciuokle(), kuri priimtų kainą be PVM ir grąžintų kainą su 21% PVM.
###_______________VISU_______
# def pvm_skaiciuokle (kaina):
#     pvm_tarifas = 0.21
#     kaina_su_pvm = kaina + kaina * pvm_tarifas
#     print('Kaina su pvm:',kaina_su_pvm)
# kaina_be_pvm = int(input("Iveskite kaina be PVM:->> "))
# pvm_skaiciuokle(kaina_be_pvm)
# #--------------------------- ROSVALDO-----------------------
# def be_pvm(kaina):
#     return kaina * 1.21
#
# kaina_su_pvm = be_pvm(int(input("Iveskite kaina be PVM: ")))
# print("Kaina su PVM", + kaina_su_pvm)

####_______________________DIENOS GALAS____________________________



