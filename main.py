import os
import requests as req
from getInfofun import *
from searchDrugfun import *
from drugInteractionfun import *
from menu import mainMenu
from getPatientInfo import *
from checkallergyandbrd import *
import sqlite3 
from tkinter import *
from drugInteractionfun import *
from tkinter import messagebox




# 04.12 - I added the drug interaction method to the warning button - but I need to define the main and all the arrays (therefore it doesnt work at the moment)
#having trouble with the reviewProfile function import



# deffining functionalities of buttons
druglist = [] # a list of the drugs. item:[drug name, drug rxcui]
drugsInfoDic={} # a dictionary containing information about the drugs. {"druginfo": [["rxcui": ###, "drugName": ###, "INDICATION AND USAGE": ###, "WARNINGS": ###, "DOSAGE AND ADMINISTRATION": ###],...]}
patientInfo={} # a dictionary containing information about the patient. {'Name': ###, 'Age': ###, 'Allergies': [list of allergies], 'Background Dieseases': [list of background dieseases]}

getPatientInfo(patientInfo)
mainMenu(druglist, drugsInfoDic, patientInfo)