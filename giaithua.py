# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:58:38 2024

@author: DELL
"""

n=int(input("nhập số nguyên dương:"))
giaithua=1
if n<0 :
    print("vui lòng nhập số nguyên dương")
else:
    for i in range(2, n+1):
        giaithua= giaithua*i
    print("ket qua la:", giaithua)