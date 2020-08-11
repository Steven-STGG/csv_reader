import csv
import sys
import os
import pandas
import re
import shutil

database = os.path.join(os.getcwd(),"Database")

def main():
    if len(sys.argv) !=2:
        sys.exit("Usage: python csv .py CSVfile")
    Data=Getdata(sys.argv[1])
    database(Data)
    
def Data_save(source,database):
    for files in source:





















        
        
def Getdata(directory):

    for files in os.listdir(directory):
        if not files.__contains__("CHINA"):
            continue
        if files.__contains__("PkAv"):
            continue
              
 
        with open (os.path.join(directory,files),"r",encoding="utf-8") as f:
            pd_mode = pandas.read_csv(f,delimiter="\t")
            pd_mode =pd_mode.drop(labels=0)

            if files.__contains__("Average"):
                AverageValue = pd_mode.copy()
            if files.__contains__("Peak"):
                PeakValue = pd_mode.copy()
    return AverageValue, PeakValue
        

def database(Data):
    AverageValue, PeakValue = Data
    

    parent_path=os.getcwd()

    #RE SEARCH
    pattern  = re.compile(r"(.)\.(Average)")

    match = pattern.search()

    new_folder = os.path.join(parent_path,"ccc")
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    AverageValue.to_csv(new_folder+"/"+"www.csv")
    




    # AverageValue.to_csv(os.path.join(os.path.dirname(os.getcwd()),"ccc","cccc.csv"))
    # print(PeakValue)






main()