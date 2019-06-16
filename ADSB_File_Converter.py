# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:31:24 2019

Author: C. Dawson

This is a file converter that convert a selected 
"""
#---------------------------------------------------------
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
#from pandas.plotting import scatter_matrix
#import numpy as np
#----------------------------------------------------------
Data_Path = os.path.join(os.path.expanduser('~'), 'Downloads') #C:/Users/1134092/Documents/SBRD_NCR/aircraft_adsb_sample_data/Input_Data"

files = []

# r=root, d=directories, f = files
files = os.listdir(Data_Path) #for r, d, f in os.walk(Data_Path):
#txtfiles = []
#if i in files:
    
#txtFiles = filter(lambda x: (x == '.txt'), files)
txtFiles = [f for f in os.listdir(Data_Path) if f.endswith('.txt')]
print (files)
print('\n')
print (txtFiles)
print('\n')
print(txtFiles[0])
 
print('\n')
print('Please select the data file to process\n') 
print('(0)  = ', txtFiles[0]) #ADSB_log_dtg_190612_164940.txt')
print('(1)  = ', txtFiles[1]) #ADSB_log_dtg_190612_173118.txt')
print('(2)  = ', txtFiles[2]) #ADSB_log_dtg_190612_175538.txt')
     
InpFile =input(' ')
#makeit = make[makeV]
if InpFile == '0':
    DataFile = Data_Path + '/' + txtFiles[0] 

elif InpFile == '1':
    DataFile = Data_Path + '/' + txtFiles[1]  #'C:/Users/1134092/Documents/SBRD_NCR/aircraft_adsb_sample_data/Input_Data/ADSB_log_dtg_190612_173118.txt'
    
elif InpFile == '2':
    DataFile = Data_Path + '/' + txtFiles[2] #'C:/Users/1134092/Documents/SBRD_NCR/aircraft_adsb_sample_data/Input_Data/ADSB_log_dtg_190612_175538.txt'
    #    return DataFile
print(DataFile)
#DataFile = 'C:/Users/1134092/Documents/SBRD_NCR/aircraft_adsb_sample_data/Input_Data/ADSB_log_dtg_190612_175538.txt'    
#DataInfo('DataFile')
file2_Open = open(DataFile)

#file2_Open = p

#file2_Open = open("C:/Users/1134092/Documents/SBRD_NCR/aircraft_adsb_sample_data/Input_Data/ADSB_log_dtg_190612_164940.txt")
Read_File = file2_Open.readlines()

if InpFile == '0':
    csvOpen =  open(Data_Path +'/' + txtFiles[0] + '.csv', 'w') # "/Users/1134092/Documents/SBRD_NCR/aircraft_adsb_sample_data/Input_data/ADSB_log_dtg_190612_164940_New.csv", "w")
if InpFile == '1':
    csvOpen =  open(Data_Path +'/' + txtFiles[1] + '.csv', 'w')
if InpFile == '2':
    csvOpen =  open(Data_Path +'/' + txtFiles[2] + '.csv', 'w')

csvFile = csv.writer(csvOpen, delimiter= ",", quoting = csv.QUOTE_ALL)
csvFile.writerow(['Message_Type', 'TX_Type', 'SessionID', 'AircraftID', 'Aircraft_Mode', 'DB_FlightID','MSG_Gen_Date','MSG_Gen_Time','MSG_Log_Date','MSG_Log_Time'])#,'FlightID','Flight_Altitude','Flight_GND_Speed','Aircraft_Track','Latitude','Longitude','VertRate','Squawk','Squawk_Alert','Emergency','TranspoderID','GND_Squat_SW'])
saveIn =[]
#i = 0
for i in Read_File:
    
    #words = saveIn.append(words)
    #if "," in i:
    words = i.replace(",", " ")
    #words = words.split()
    if " " in words:
        #Sep = words.split(" ")[0]
        Message_Type     = words.split(" ")[0]
        TX_Type          = words.split(" ")[1]
        SessionID        = words.split(" ")[2]
        AircraftID       = words.split(" ")[3]
        Aircraft_Mode    = words.split(" ")[4]
        DB_FlightID      = words.split(" ")[5]
        MSG_Gen_Date     = words.split(" ")[6]
        MSG_Gen_Time     = words.split(" ")[7]
        MSG_Log_Date     = words.split(" ")[8]
        MSG_Log_Time     = words.split(" ")[9]
    csvFile.writerow([Message_Type, TX_Type, SessionID, AircraftID, Aircraft_Mode, DB_FlightID, MSG_Gen_Date, MSG_Gen_Time, MSG_Log_Date, MSG_Log_Time])#, FlightID, Flight_Altitude, Flight_GND_Speed, Aircraft_Track, Latitude, Longitude, VertRate, Squawk, Squawk_Alert, Emergency, TranspoderID, GND_Squat_SW])
"""        FlightID         = words.split(" ")[10]
        Flight_Altitude  = words.split(" ")[11]
        Flight_GND_Speed = words.split(" ")[12]
        Aircraft_Track   = words.split(" ")[13]
        Latitude         = words.split(" ")[14]
        Longitude        = words.split(" ")[15]
        VertRate         = words.split(" ")[16]
        Squawk           = words.split(" ")[17]
        Squawk_Alert     = words.split(" ")[18]
        Emergency        = words.split(" ")[19]
        TranspoderID     = words.split(" ")[20]
        GND_Squat_SW     = words.split(" ")[21]
"""


csvOpen.close()
inpFile = int(InpFile)

csvRead = pd.read_csv(txtFiles[inpFile] + '.csv')
print(csvRead.shape)
print(csvRead.head(5))   #View actual data for 20 rows
print(csvRead.describe()) #statistical summary (description)
hh = (csvRead.groupby('Aircraft_Mode').size()) #Disribution
print(hh)
#plt.figure(1)
#csvRead.plot(kind='box', subplots=True, layout=(4,4), sharex=False, sharey=False)
#plt.show
print(max(hh))

plt.figure(1)
hh.hist()
plt.show

dataArray = csvRead.values
X = dataArray[:, 6] # 
Y = dataArray[:,4]    # 


plt.scatter(X,Y, color='red')
plt.xlabel('Altitude')
plt.ylabel('Flight ID')
plt.title('ADSB FlightID vs. Altitude')
plt.show
