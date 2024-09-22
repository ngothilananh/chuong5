# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:24:35 2024

@author: DELL
"""

str_input= input("nhập chuỗi:")
dodaichuoi= len(str_input)
print("độ dài chuỗi:", dodaichuoi)
kitudacbiec= "!@#$%^&*()_+./"
demdacbiec= 0
for chu in (str_input): 
    if chu in kitudacbiec:
        demdacbiec+= 1
print("đếm kí tự đặc biệc:", demdacbiec)
demchucai=0
for chu in str_input:
    if chu.islower():
        demchucai +=1
print("đếm chữ cái:", demchucai)
demkituso= 0
for chu in str_input:
    if chu.isdigit():
        demkituso +=1
print("đếm kí tự số:", demkituso)
demchuhoa=0
for chu in str_input:
    if chu.isupper():
        demchuhoa+=1
print("số kí tự hoa:", demchuhoa)
# sử dụng is upper, is lower 
#: Kiểm tra xem ký tự có phải là số hay không.

    