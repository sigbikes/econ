# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:33:41 2016

@author: Sig
"""
import os
import sys


#For Spyder Testing ======COMMENT OUT OR REMOVE AFTER TESTING
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "econ.settings")

from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'econ.settings')

import django

django.setup()

from c_growth.models import Data, Run

def make_run(name, d_name):
    r = Run.objects.get_or_create(name=name, data=d_name)[0]
    return r
    
def make_data(dataset, P, R, C, t, I, T):
    d = Data.objects.get_or_create(name = dataset)[0]
    d.principle = P
    d.compoundings = C
    d.rate = R
    d.interest = I
    d.total = T
    d.year = t  
    return d

def add_run(names, d_names):
    for name in names:  
        ndex = names.index(name) 
        for data in d_names:
            dex = d_names.index(data)
                
        
            r = Run.objects.get_or_create(name=name, data=d_names)[0]
    
    return r

def add_data(names, princ, rates, time, compounding, total, interest):
    
    dat = make_data()
    return dat



""" Code within a conditional if __name__ == '__main__' statement will only be
 executed when the module is run as a standalone Python script.
 Importing the module will not run this code;
 classes or functions will however be fully accessible to you. """


#Execution ... And Go!
if __name__ == '__main__':
    print("Starting population script...")
    nombre = ['test', 'test2']
    data_nombre = [['5% test', '10% test'], ['garbage in', 'garbage out']]      
    solo = 'wildcat'
    datum = Data.objects.get_or_create(name='sea level')[0]
    make_r_test = make_run(solo, datum)
    print(make_r_test, make_r_test.data)