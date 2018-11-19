# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:50:15 2018

@author: neilp
"""

import csv, random

with open("data.csv", "w", newline = "") as csvfile:
    #Make writer as our csv writer
    writer = csv.writer(csvfile, delimiter=',')
    
    #We make 10000 data for our test
    testSize = 10000
    writer.writerow(["X", "Y", "output"])
    
    for count in range(0,testSize):
        #x, y and b are a random number from 1 to 100
        x = random.randint(1,100)
        y = random.randint(1,100)
        b = random.randint(-3,+3)
        #The ans = X^2 + 4*y, we have a bias with random number b
        #Here we set the ans to 7 class as the remainder of ans
        #ans = int((x*x + 4*y + b)/5000)
        ans = x*x + 4*y + b
        if ans >= 5000:
            ans = 1
        else:
            ans = 0
        writer.writerow([x, y, ans])
