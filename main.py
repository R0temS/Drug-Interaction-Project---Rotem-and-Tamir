#17.12 - i created a warning list and a table (there's a problem with the table creation)

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
from updateDB import *





# 04.12 - I added the drug interaction method to the warning button - but I need to define the main and all the arrays (therefore it doesnt work at the moment)
#having trouble with the reviewProfile function import



# deffining functionalities of buttons
druglist = [] # a list of the drugs. item:[drug name, drug rxcui, perWeek, perDay]
drugsInfoDic={} # a dictionary containing information about the drugs. {"druginfo": [{"rxcui": ###, "drugName": ###, "INDICATION AND USAGE": ###, "WARNINGS": ###, "DOSAGE AND ADMINISTRATION": ###},...]}
patientInfo={'Allergies': [], 'Background Dieseases': []} # a dictionary containing information about the patient. {'firstName': ###, 'lastName': ###, 'Age': ###, 'Allergies': [list of allergies], 'Background Dieseases': [list of background dieseases]}
historyDrugs=[] # a list of the history of the used drugs. item:[drug name, drug rxcui, perWeek, perDay]
inteructionWarnings = []  # a list of interuction warnings. item: [drug1Name, drug1Rxcui, drug2Name, drug2Rxcui]
# DB creation

try:
    conn = sqlite3.connect('patient_info.db')
    c = conn.cursor()
    #Create table
    c.execute("""CREATE TABLE info(
                       firstName text,
                       lastName text,
                       age text,
                       bgilnesses text,
                       allergies text
                       )""")
    c.execute("""CREATE TABLE drugList(
                       drugname text,
                       drugrxcui text,
                       perweek text,
                       perday text
                       )""")
    c.execute("""CREATE TABLE drugsInfo(
                       rxcui text, 
                       drugName text, 
                       INDICATION_AND_USAGE text, 
                       WARNINGS text, 
                       DOSAGE_AND_ADMINISTRATION text
                       )""")
    c.execute("""CREATE TABLE historyDrugs(
                       drugname text,
                       drugrxcui text,
                       perweek text,
                       perday text
                       )""")
    c.execute("""CREATE TABLE inteructionWarnings(
                       drugAName text,
                       drugARxcui text,
                       drugBName text,
                       drugBRxcui text
                       )""")

    # # Commit Changes
    conn.commit()
    # # Close connection
    conn.close()

    getPatientInfo(patientInfo, "", "", "", "")

except Exception:
    getInfoFromDB(druglist, drugsInfoDic, patientInfo, historyDrugs, inteructionWarnings)

while True:
    mainMenu(historyDrugs, druglist, drugsInfoDic, patientInfo, inteructionWarnings)
