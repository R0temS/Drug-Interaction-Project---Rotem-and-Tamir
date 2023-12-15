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
   
    patientInfo.update({'Allergies': [], 'Background Dieseases': []})
    for firstName in firstName:
        if str(firstName)[1:-2] != "None":
            patientInfo.update({'firstName': str(firstName)[2:-3]})

    for lastName in lastName:
        if str(lastName)[1:-2] != "None":
            patientInfo.update({'lastName': str(lastName)[2:-3]})

    for age in age:
        if str(age)[1:-2] != "None":
            patientInfo.update({'Age': str(age)[2:-3]})

    for bgilnesses in bgilnesses:
        if str(bgilnesses)[1:-2] != "None":
            patientInfo['Background Dieseases'].append(str(bgilnesses)[2:-3])

    for allergies in allergies:
        if str(allergies)[1:-2] != "None":
            patientInfo['Allergies'].append(str(allergies)[2:-3])


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
        drugsInfoDic['druginfo'].append({"rxcui": str(rxcui)[2:-3], "drugName": str(drugName)[2:-3], "INDICATION AND USAGE": str(INDICATION_AND_USAGE)[2:-3], "WARNINGS": str(WARNINGS)[2:-3], "DOSAGE AND ADMINISTRATION": str(DOSAGE_AND_ADMINISTRATION)[2:-3]})
    
    conn.close()
    

def updateDB(druglist, drugsInfoDic, patientInfo, historyDrugs, mode):
        conn = sqlite3.connect('patient_info.db')
        c = conn.cursor()
       
        if mode == "druglist":
            c.execute('DELETE FROM druglist') #initializing the table values
            
            if len(druglist)!=0:
                for drugname, drugrxcui, perday, perweek in druglist:
                        c.execute('INSERT INTO drugList (drugname, drugrxcui, perweek, perday) VALUES (?, ?, ?, ?)', (drugname, drugrxcui, perweek, perday))

        if mode == "drughistory":
            c.execute('DELETE FROM historyDrugs') #initializing the table values

            if len(historyDrugs)!=0:
                for drugname, drugrxcui, perday, perweek in historyDrugs:
                        c.execute('INSERT INTO historyDrugs (drugname, drugrxcui, perweek, perday) VALUES (?, ?, ?, ?)', (drugname, drugrxcui, perweek, perday))
        
        if mode == "patientinfo":
            c.execute('DELETE FROM info') #initializing the table values
            c.execute('INSERT INTO info (firstName, lastName, age) VALUES (?, ?, ?)', ( patientInfo['firstName'], patientInfo['lastName'], patientInfo['Age']))
            if len(patientInfo['Allergies'])!=0:
                for allergy in patientInfo['Allergies']:
                    c.execute('INSERT INTO info (allergies) VALUES (?)', (allergy, ))
           
            
            if len(patientInfo['Background Dieseases'])!=0:
                for bgilnesses in patientInfo['Background Dieseases']:
                    c.execute('INSERT INTO info (bgilnesses) VALUES (?)', (bgilnesses, ))
            
            
         
        if mode == "druginfo":
            c.execute('DELETE FROM drugsInfo') #initializing the table values
            if len(drugsInfoDic['druginfo'])!=0:
                for item in drugsInfoDic['druginfo']:
                    
                  try:
                        c.execute('INSERT INTO drugsInfo (rxcui, drugName, INDICATION_AND_USAGE, WARNINGS, DOSAGE_AND_ADMINISTRATION) VALUES (?, ?, ?, ?, ?)', (item['rxcui'], item['drugName'], item['INDICATION AND USAGE'], item['WARNINGS'], item['DOSAGE AND ADMINISTRATION']))
                  except Exception :
                      pass
            
        conn.commit()           
        conn.close()
