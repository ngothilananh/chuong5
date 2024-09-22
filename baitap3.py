# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:22:35 2024

@author: DELL
"""

import random
soluongphantu=random.randint(20,30)
danhsach= [0]* soluongphantu
for i in range (soluongphantu):
    sothuc= random.uniform(19, 30)
    danhsach[i]= sothuc**2
print (f"số lượng phần tử: {soluongphantu}")
print("DANH SÁCH BÌNH PHƯƠNG", danhsach)


