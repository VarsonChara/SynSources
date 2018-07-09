# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f = open("files/file.txt","r")
tab=[]
for i in f.readlines():
    #i.split("\t")
    i=i[:-1]
    tab.append(i.split("\t"))
    print (tab)
    print ("---------------")
f.close()
