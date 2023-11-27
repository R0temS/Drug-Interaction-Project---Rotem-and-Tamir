import os
import requests as req
from getInfofun import *
from searchDrugfun import *
from drugInteractionfun import *
from menu import *

druglist = []
while(True): 
    menu()
    try:
        choice = int(input(""))
    except Exception:
        print("Only a number!")
        continue
    os.system('cls')
    if choice == 1:
        searchDrug(druglist)
    elif choice == 2:
        print("-----DRUG LIST-----\n")
        showDrugList(druglist)
    elif choice == 3:
        if(len(druglist)!=0):
            print("-----DRUGS INTERACTIONS-----\n")
            drugInteraction(druglist)
        else:
            print("\nInsert drugs first!")
    elif choice == 4:
        if(len(druglist)!=0):
            showDrugList(druglist)
            try:
                drugforinfo = int(input("Info of which drug?\n"))-1
            except Exception:
                print("Only a number!")
                continue
            if(drugforinfo>=0 and drugforinfo<= len(druglist)):
                print("-----DRUG INFO-----\n")
                getInfo(druglist[drugforinfo][1])
            else:
                print("Choice out of range")
        else:
            print("\nInsert drugs first!")
    elif choice == 5:
        if(len(druglist)!=0):
            print("-----DELETE A DRUG-----\n")
            showDrugList(druglist)
            try:
                drugfordelete = int(input("Delete line number  "))-1
            except Exception:
                print("Only a number!")
                continue
            if(drugfordelete>=0 and drugfordelete<= len(druglist)):
                druglist.pop(drugfordelete)
            else:
                print("Choice out of range")
        else:
            print("\nInsert drugs first!")
    elif choice==6:
        print("BYE!")
        break


