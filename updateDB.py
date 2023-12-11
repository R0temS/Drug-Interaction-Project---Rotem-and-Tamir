import sqlite3

#this function receives the information from the DB and updates the variables  
def getInfoFromDB(druglist, drugsInfoDic, patientInfo, historyDrugs):
    conn = sqlite3.connect('patient_info.db')
    c = conn.cursor()

    #druglist
    c.execute('SELECT drugname FROM drugList')
    drugname = c.fetchall()
    c.execute('SELECT drugrxcui FROM drugList')
    drugrxcui = c.fetchall()
    c.execute('SELECT perweek FROM drugList')
    perweek = c.fetchall()
    c.execute('SELECT perday FROM drugList')
    perday = c.fetchall()

    for drugname, drugrxcui, perweek, perday in zip (drugname, drugrxcui, perweek, perday):
        druglist.append([str(drugname)[2:-3], str(drugrxcui)[2:-3], str(perweek)[2:-3], str(perday)[2:-3]])

    #history
    c.execute('SELECT drugname FROM historyDrugs')
    drugname = c.fetchall()
    c.execute('SELECT drugrxcui FROM historyDrugs')
    drugrxcui = c.fetchall()
    c.execute('SELECT perweek FROM historyDrugs')
    perweek = c.fetchall()
    c.execute('SELECT perday FROM historyDrugs')
    perday = c.fetchall()

    for drugname, drugrxcui, perweek, perday in zip (drugname, drugrxcui, perweek, perday):
        historyDrugs.append([str(drugname)[2:-3], str(drugrxcui)[2:-3], str(perweek)[2:-3], str(perday)[2:-3]])

    #patient info
    c.execute('SELECT firstName FROM info')
    firstName = c.fetchall()
    c.execute('SELECT lastName FROM info')
    lastName = c.fetchall()
    c.execute('SELECT age FROM info')
    age = c.fetchall()
    c.execute('SELECT bgilnesses FROM info')
    bgilnesses = c.fetchall()
    c.execute('SELECT allergies FROM info')
    allergies = c.fetchall()
   
    patientInfo.update({'firstName': str(firstName)[3:-4], 'lastName': str(lastName)[3:-4], 'Age': str(age)[3:-4], 'Allergies': [], 'Background Dieseases': []})
    for bgilnesses in bgilnesses:
        patientInfo['Background Dieseases'].append(bgilnesses)

    for allergies in allergies:
        patientInfo['Allergies'].append(allergies)


    #drugs information dic
    
    c.execute('SELECT rxcui FROM drugsInfo')
    rxcui = c.fetchall()
    c.execute('SELECT drugName FROM drugsInfo')
    drugName = c.fetchall()
    c.execute('SELECT INDICATION_AND_USAGE FROM drugsInfo')
    INDICATION_AND_USAGE = c.fetchall()
    c.execute('SELECT WARNINGS FROM drugsInfo')
    WARNINGS = c.fetchall()
    c.execute('SELECT DOSAGE_AND_ADMINISTRATION FROM drugsInfo')
    DOSAGE_AND_ADMINISTRATION = c.fetchall()

    drugsInfoDic.update({"druginfo": []})
    for rxcui, drugName, INDICATION_AND_USAGE, WARNINGS, DOSAGE_AND_ADMINISTRATION in zip (rxcui, drugName, INDICATION_AND_USAGE, WARNINGS, DOSAGE_AND_ADMINISTRATION):
        drugsInfoDic['druginfo'].append({"rxcui": rxcui, "drugName": drugName, "INDICATION_AND_USAGE": INDICATION_AND_USAGE, "WARNINGS": WARNINGS, "DOSAGE_AND_ADMINISTRATION": DOSAGE_AND_ADMINISTRATION})
    
    conn.close()
    

def updateDB(druglist, drugsInfoDic, patientInfo, historyDrugs, mode):
        conn = sqlite3.connect('patient_info.db')
        c = conn.cursor()
       
        if mode == "druglist":
            c.execute('UPDATE druglist SET drugname = NULL, drugrxcui = NULL, perweek = NULL, perday = NULL')  #initializing the table values

            for drugname, drugrxcui, perweek, perday in druglist:
                    c.execute('INSERT INTO drugList (drugname, drugrxcui, perweek, perday) VALUES (?, ?, ?, ?)', (drugname, drugrxcui, perweek, perday))

        if mode == "drughistory":
            c.execute('UPDATE historyDrugs SET drugname = NULL, drugrxcui = NULL, perweek = NULL, perday = NULL')  #initializing the table values

            for drugname, drugrxcui, perweek, perday in historyDrugs:
                    c.execute('INSERT INTO historyDrugs (drugname, drugrxcui, perweek, perday) VALUES (?, ?, ?, ?)', (drugname, drugrxcui, perweek, perday))
        
        if mode == "patientinfo":
            c.execute('UPDATE info SET firstName = NULL, lastName = NULL, age = NULL, bgilnesses = NULL, allergies = NULL')  #initializing the table values
            c.execute('INSERT INTO info (firstName, lastName, age) VALUES (?, ?, ?)', ( patientInfo['firstName'], patientInfo['lastName'], patientInfo['Age']))
            for allergy in patientInfo['Allergies']:
                c.execute('INSERT INTO info (allergies) VALUES (?)', (allergy))

            for bgilnesses in patientInfo['Background Dieseases']:
                c.execute('INSERT INTO info (bgilnesses) VALUES (?)', (bgilnesses))
            
         
        if mode == "druginfo":
            c.execute('UPDATE drugsInfo SET rxcui = NULL, drugName = NULL, INDICATION_AND_USAGE = NULL, WARNINGS = NULL, DOSAGE_AND_ADMINISTRATION = NULL')  #initializing the table values
            for item in drugsInfoDic['druginfo']:
                c.execute('INSERT INTO drugsInfo (rxcui, drugName, INDICATION_AND_USAGE, WARNINGS, DOSAGE_AND_ADMINISTRATION) VALUES (?, ?, ?, ?, ?)', (item['rxcui'], item['drugName'], item['INDICATION AND USAGE'], item['WARNINGS'], item['DOSAGE AND ADMINISTRATION']))
            
        conn.commit()           
        conn.close()