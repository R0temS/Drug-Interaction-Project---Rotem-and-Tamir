import os
import requests as req
from getInfofun import *
from searchDrugfun import *
from drugInteractionfun import *
from menu import *
from getPatientInfo import *
from checkallergyandbrd import *

druglist = [] # a list of the drugs. item:[drug name, drug rxcui]
drugsInfoDic={} # a dictionary containing information about the drugs. {"druginfo": [["rxcui": ###, "drugName": ###, "INDICATION AND USAGE": ###, "WARNINGS": ###, "DOSAGE AND ADMINISTRATION": ###],...]}
patientInfo={} # a dictionary containing information about the patient. {'Name': ###, 'Age': ###, 'Allergies': [list of allergies], 'Background Dieseases': [list of background dieseases]}
if len(patientInfo)==0:
    getPatientInfo(patientInfo)
while(True): 
    menu()
    try:
        choice = int(input(""))
    except Exception:
        print("Only a number!")
        continue
    os.system('cls')
    if choice == 1: #Add drugs to the druglist
        searchDrug(druglist)
        print("UPDATING THE DRUG LIST...")
        updatedrugsinfodic(drugsInfoDic, druglist)
        os.system('cls')
        
    elif choice == 2: #Show the druglist
        showDrugList(druglist)
    elif choice == 3: #Show the drug interactions
        if(len(druglist)!=0):
            print("-----DRUGS INTERACTIONS-----\n")
            drugInteraction(druglist)
        else:
            print("\nInsert drugs first!")
    elif choice == 4: #Shows info of specific drug
        if(len(druglist)!=0):
            showDrugList(druglist)
            try:
                drugforinfo = int(input("Info of which drug?\n"))-1
            except Exception:
                print("Only a number!")
                continue
            if(drugforinfo>=0 and drugforinfo< len(druglist)):
                print("-----DRUG INFO-----\n")
                getInfo(druglist[drugforinfo][1], "p", drugsInfoDic,druglist[drugforinfo][0], 0)
            else:
                print("Choice out of range")
        else:
            print("\nInsert drugs first!")
    elif choice == 5: #Delete a specific drug from the druglist
        if(len(druglist)!=0):
            print("-----DELETE A DRUG-----")
            showDrugList(druglist)
            try:
                drugfordelete = int(input("Delete line number  "))-1
            except Exception:
                print("Only a number!")
                continue
            if(drugfordelete>=0 and drugfordelete< len(druglist)):
                drugfordelete1 = findLocationInDrugsInfoDic(druglist, drugsInfoDic, drugfordelete)
                druglist.pop(drugfordelete)
                if drugfordelete1!=-1:
                    drugsInfoDic['druginfo'].pop(drugfordelete1)

            else:
                print("Choice out of range")
        else:
            print("\nInsert drugs first!")
    elif choice == 6: #Enter or show patient information
        try:
            innerchoice = int(input("1. Enter info\n2. Show info\n"))
        except Exception:
            print("Only a number!")
            continue
        if innerchoice == 1:
            patientInfo={}
            getPatientInfo(patientInfo)
        elif innerchoice == 2:
            showPatientInfo(patientInfo)
    elif choice == 7: #Show drug information that relevant for the patient allergies
        if(len(druglist)!=0):
            print("-----RELEVENT ALLERGIES INFO-----")
            checkAllergy(drugsInfoDic, patientInfo)
        else:
            print("\nInsert drugs first!")  

    elif choice==8: #exit the program
        print("BYE!")
        break

    
