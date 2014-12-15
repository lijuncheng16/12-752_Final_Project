
import csv
import os
import numpy as np
from datetime import datetime as dt
os.getcwd()
os.chdir('D:\\GoogleDrive\\12-752 Final Project\\2009 Microdata')

input_data_09 = np.genfromtxt(r'recs2009_public.csv', delimiter=',',
                           names=True,dtype='float',usecols=(4,14,11,785,140,172,231,610,611,141,173,232,615,614,907,912,918,759,827,659,620,845,861,885,873,897))
data = []
timestamp1 = 2009
for line in input_data_09:
    temp = timestamp1,line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25]
    data.append(temp)

os.chdir('D:\\GoogleDrive\\12-752 Final Project\\2005 Microdata')

input_data_05 = np.genfromtxt(r'RECS05alldata.csv', delimiter=',',
                           names=True,dtype='float',usecols=(0,5,60,81,844,167,252,260,580,581,1,2,3,4,582,1052,1042,1065,826,924,641,6,1026,1028,1030,1032,1034))
for line in input_data_05:
    data.append(line)

os.chdir('D:\\GoogleDrive\\12-752 Final Project\\2001 Microdata')

input_data_01 = np.genfromtxt(r'publicuse2001.csv', delimiter=',',
                           names=True,dtype='float',usecols=(8,58))
input_data_01_08 = np.genfromtxt(r'publicuse82001.csv', delimiter=',',
                           names=True,dtype='float',usecols=(9,45))
input_data_01_11 = np.genfromtxt(r'publicuse112001.csv', delimiter=',',
                           names=True,dtype='float',usecols=(29,12,14,16,18,10))
input_data_01_12 = np.genfromtxt(r'publicuse122001.csv', delimiter=',',
                           names=True,dtype='float',usecols=(24))
length_01 = input_data_01.shape[0]
print length_01
timestamp2 = 2001
for i in range(0,length_01):
    if input_data_01_08[i][1] == 1:
        moneypy = 1.5
    if input_data_01_08[i][1] == 2:
        moneypy = 3.5
    if input_data_01_08[i][1] == 3:
        moneypy = 5
    if input_data_01_08[i][1] == 4:
        moneypy = 6
    if input_data_01_08[i][1] == 5:
        moneypy = 7.5
    if input_data_01_08[i][1] == 6:
        moneypy = 9.5
    if input_data_01_08[i][1] == 7:
        moneypy = 11.5
    if input_data_01_08[i][1] == 8:
        moneypy = 15
    if input_data_01_08[i][1] == 9:
        moneypy = 20
    if input_data_01_08[i][1] == 10:
        moneypy = 23.5
    temp = timestamp2, input_data_01[i][0], input_data_01[i][1], 'N/A', moneypy, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',input_data_01_11[i][0],input_data_01_12[i][0],input_data_01_08[i][0], 'N/A', 'N/A', 'N/A',input_data_01_11[i][1],input_data_01_11[i][2],input_data_01_11[i][3],input_data_01_11[i][4],input_data_01_11[i][5]
    
    data.append(temp)
    
with open('clean_data.csv', 'wb') as outfile:
    
    datawriter = csv.writer(outfile, delimiter=',',
                            quotechar='|')
    datawriter.writerow(['Survey','TYPEHUQ', 'KOWNRENT', 'AIA_Zone', 'MONEYPY','ESFRIG','ESDISHW','ESCWASH',
                         'TYPE GLASS', 'NEW GLASS', 'REPLC FRI', 'REPLC DW', 'REPLC CW', 'INSTL INS', 'ADQ INSUL',
                         'TOTALBTU','TOTALBTUOTH','TOTALDOLOTH',
                         'N HSLD MEM', 'TOT SQFT', 'USE SOLAR','INSTL WS','BTU EL', 'BTU NG', 'BTU FO', 'BTU LP', 'BTU KER'])
    datawriter.writerows(data)
print 'New data file generated!'

