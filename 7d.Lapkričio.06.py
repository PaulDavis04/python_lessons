import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimage
###

# masyvas = np.array([1,2,3,4,5])
# masyvas2 = np.array([6,7,8,9,10])
# # suma = np.sum(masyvas)
# sujungtas_masyvas = np.concatenate((masyvas,masyvas2))
# print(sujungtas_masyvas)

# atsitiktiniai_skaiciai = np.random.randint(0,10, size=5)
# print(atsitiktiniai_skaiciai)

# masyvas = np.array([10,20,30,40,50])
# atsitiktiniai_elementai = np.random.choice(masyvas, size=3)
# print(atsitiktiniai_elementai)

# masyvas = np.arange(0,10,2) #(nuo,iki,zingsniai)
# print(masyvas)

# masyvas = np.array([1,3,5])
# masyvas2 = np.array([2,3,4])
# lyginimas = masyvas > masyvas2
# print(lyginimas)

# masyvas = np.array([1,2,3,4,5,6,7,8,9,10]) #masyvas
# filtered_array = masyvas[masyvas > 5]
# print(filtered_array)

# masyvas = np.array([1,2,3,4,5,6])
# split_array = np.split(masyvas,2)
# print(split_array)

# array = np.array(np.arange(1,21)).reshape(5,4)
# # print(array)
# df = pd.DataFrame(array, columns=["A","B","C","D"])
#
# # second_column = df["B"]
# # print(df)
# # print(second_column)
# suma = df.groupby("A")["B"] #sumavimas
# second_column = np.sum(array[:,1]) #nuo,iki
# print(second_column)

# trimate_matrica = np.array([[1,2,3],[4,5,6], [7,8,9]])
# eiluciu_sumas = np.sum(trimate_matrica, axis=1)
# print(eiluciu_sumas)
# stulpeliu_suma = np.sum(trimate_matrica, axis=0)
# print(stulpeliu_suma)
# stulpelio_suma = np.sum(trimate_matrica [1]) #eilute kurios reikia
# print(stulpelio_suma)

# masyvas = np.array([0,1,2,3,4,5,6,7,8,9,])
# # skaiciai_nuo_1_iki_5 = masyvas[2:6] # parodo pagal indeksa
# # print(skaiciai_nuo_1_iki_5)
#
# # masyvas = np.array([1,2,3,4,5,6,7,8,9,10]) #masyvas
# filtered_array = masyvas[(masyvas < 5) & (masyvas >2)]
# print(filtered_array)

# df = pd.DataFrame(np.random.randn(100, 3), columns=["A", "B", "C"])# atsitiktiniai
# didesni_uz_0 = df[df["1"] > 0]      ###     didesni uz 0 #filtruoja neigiamas reiksmes
# print(didesni_uz_0)
###-------------------
# df = pd.DataFrame({
#     "x" :np.arange(1,6),
#     "y" :np.arange(1,6)
# })
#
# df["x,y-suma"] = df["x"] + df["y"]
# print(df)

# df = pd.DataFrame({   #
#     "Pirmas stulp":[1,np.nan,3],
#     "Antras stulp":[4,5,np.nan]
#
# })
# # df.fillna(0, inplace=True)  #NAN keicia i 0 vieta
# df.replace(np.nan, 0, inplace=True)  ## irgi keicia
# print(df)

# vienmatis masyvas iki 10
# ideti i data frame
###----------
# df = pd.DataFrame(columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
# atsitiktiniai_skaiciai_iki_10 = np.random.rand(10) #rand  ima
# df.loc[len(df)]= atsitiktiniai_skaiciai_iki_10  #loc len ideda reikalinga skaiciu
# print(atsitiktiniai_skaiciai_iki_10)

# df.loc["Nauja Eilute"] = ["Reiksmes"]  #loc sintakse

# data = {
#     "Amzius":[25,44],
#     "Miestas":["Kaunas", "Vilnius"]
# }
# df = pd.DataFrame(data, index=["Antanas", "Petras"])
# df.loc["Juozas"] = [33,"Panevezys"]
# # print(df)
#
# df.loc[df["Amzius"] >30, "Miestas"] = "Klaipeda"
# # print(df)
#
# df["Miestas"][df["Amzius"]>30] = "Klaipeda"
# print(df)

# Vienetuku_matrica = np.zeros((5,5))
# Krastu_matrica = np.pad(Vienetuku_matrica, pad_width=3, mode="constant", constant_values=1)
# print(Krastu_matrica)

# matrica1 = np.array([[1, 2], [3, 4]])
# matrica2 = np.array([[5,6], [7,8]])
# # c = np.add(matrica1, matrica2)
# daugyba = np.matmul(matrica1, matrica2)
# print(daugyba)
##

# kainos = np.random.normal(100, 10, 100)
# print(kainos)
# def slankusis_vidurkis(duomenys, langas):
#     sv_filtrai = np.cumsum(duomenys, dtype=float)  #kumuliacine suma
#     sv_filtrai[langas:]=sv_filtrai[langas:]-sv_filtrai[:-langas]
#     return sv_filtrai[langas-1:]/langas
#
# langas = 5
# sv_kainos = slankusis_vidurkis(kainos, langas)
# plt.plot(kainos, label= "Originalios Kainos")
# plt.plot(np.arange(langas-1, len(kainos)), sv_kainos, label="Slankusis Vidurkis", color="red")
# plt.legend()
# plt.title("Finansiniu Duomenu Isgryninimas Slankiojo Vidurkio Filtru")
# plt.show()
##########-----------------------------------------------
# akciju_kainos = pd.read_csv("all_stocks_5yr.csv")
# # print(df)
# kainos = np.array(akciju_kainos["close"])
# # print(kainos)
#
#
# kainos_vidurkis = np.mean(akciju_kainos["close"])
#
# kainos_mediana = np.median((akciju_kainos["close"]))
#
# kainos_stand = np.std((akciju_kainos["close"]))
#
# # print(kainos_vidurkis)
# # print(kainos_mediana)
# # print(kainos_stand)
#
#
# plt.figure(figsize=(14,5))
# plt.subplot(1, 4, 1)
# plt.plot(kainos, label="Akciju kainos")
# plt.legend()
# plt.title("Akciju kainos")
#
#
# plt.subplot(1, 4, 2)
# plt.plot([kainos_vidurkis]*len(kainos), label="Kainos vidurkis")
# plt.legend()
# plt.title("Kainos vidurkis")
#
#
# plt.subplot(1, 4, 3)
# plt.plot([kainos_mediana]*len(kainos), label="Kainos mediana")
# plt.legend()
# plt.title("Kainos mediana")
#
#
# plt.subplot(1, 4, 4)
# plt.plot([kainos_stand]*len(kainos), label="Kainos stand. nuokrypis")
# plt.legend()
# plt.title("Kainos stand. nuokrypis")
#
#
# plt.show()

#######----------------------
###---------3d------------
# zingsniu_skaicius = 1000
#
# x_zingsnis = np.random.choice([-1,1], size=zingsniu_skaicius)
# y_zingsnis = np.random.choice([-1,1], size=zingsniu_skaicius)
# z_zingsnis = np.random.choice([-1,1], size=zingsniu_skaicius)
#
# x_trajektorija = np.cumsum(x_zingsnis)
# y_trajektorija = np.cumsum(y_zingsnis)
# z_trajektorija = np.cumsum(z_zingsnis)
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection= "3d")
# ax.plot(x_trajektorija, y_trajektorija, z_trajektorija)
# ax.view_init(elev=40,azim=45)
# ax.set_title("Atsitiktinis trajektorija daleles judejimo erdveje")
# plt.show()
####-----------------------------
# ###################### nuotraukos keitimas----------
# originalus_vaizdas = mpimage.imread("joshua-rawson-harris-TYdYrjdpSZ8-unsplash.jpg")
# veidrodis = np.fliplr(originalus_vaizdas)
# # pasuktas_vaizdas = np.rot90(originalus_vaizdas, k=-2)
# invertuotas_vaizdas = 255-veidrodis
# # invertuotas_vaizdas = 255-pasuktas_vaizdas
# # invertuotas_vaizdas = 255-originalus_vaizdas
#
# fig, ax = plt.subplots(1, 2)
# ax[0].imshow(originalus_vaizdas)
# ax[0].set_title("Originalus vaizdas")
# ax[0].axis("off")
# ax[1].imshow(invertuotas_vaizdas)
# ax[1].set_title("Invertuotas vaizdas")
# ax[1].axis("off")
# plt.show()
# ##########--------------------------


