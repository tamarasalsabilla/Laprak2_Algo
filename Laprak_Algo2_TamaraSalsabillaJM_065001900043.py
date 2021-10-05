# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:42:14 2021

@author: TamaraSalsabillaJM
"""

input1 = int(input("Masukkan angka pertama: "))
input2 = int(input("Masukkan angka kedua: "))
input3 = int(input("Masukkan angka ketiga: "))

if (input1 > input2) and (input1 > input3):
    terbesar = input1
elif (input2 > input1) and (input2 > input3):
    terbesar = input2
else:
    terbesar = input3

print("\nAngka terbesar adalah:", terbesar)








