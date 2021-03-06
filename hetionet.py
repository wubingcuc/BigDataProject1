# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:08:32 2020

@author: mehra
"""

from lib import diseaseDb, graphDb

FILE1_DIR = './data/nodes.tsv'
FILE2_DIR = './data/edges.tsv'

OPTIONS = '''
Options:
   [1] Info about a disease
   [2] Treatment options for a new disease
   [3] Exit
   
'''
OPTIONS2 = '''
Options:
   [1] Look up another disease
   [2] Return to main menu
'''

OPTIONS3 = '''
Reload database from files?
   [1] Yes
   [2] No
'''




print('Welcome to HetioNet!')
while True:
    print(OPTIONS)
    state = input('Select option: ')
        
    if state == '1':
        searching = '1'
        db = diseaseDb.DiseaseDb()
        db.loadDataFromTSV(FILE1_DIR, FILE2_DIR)
        
        while searching == '1':
            disease_id = input('Enter disease ID: ')
            
            # Search database for disease
            disease = db.find(disease_id)
            
            if disease:
                # Disease found
                db.printInfo(disease)
                input('Press [ENTER] to continue...')
                print(OPTIONS2)
                searching = input('Select: ')
            else:
                print('Disease with ID:', end = ' ')
                print(disease_id + ' not found in database')
                input('Press [ENTER] to continue...')
                print(OPTIONS2)
                searching = input('Select: ')
                
        # delete database once done
        del db
        
    elif state == '2':
        searching = '1'
        db = graphDb.GraphDb()
        
        print(OPTIONS3)
        load = input('Select: ')
        
        if load == '1':
            db.empty()
            db.loadDataFromTSV(FILE1_DIR, FILE2_DIR)
        
        while searching == '1':
            disease_id = input('Enter disease ID: ')
            db.newTreatments(disease_id)
            input('Press [ENTER] to continue...')
            print(OPTIONS2)
            searching = input('Select: ')
    else:
        print('[3] Exit')
        print('Thank you for using HetioNet!')
        break