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

def populate():

    princ = [10000]  
    
    rate = [.05, .1]

    time = [5, 10, 20]

    comp = 1

    data_names = []    
    for r in rate:
        dex = rate.index(r)
        data_names.append([])
        for name in time:
            idex = time.index(name)
            data_names[dex].append(str(time[idex])+ " Years @ "+ str(rate[dex]*100)+ "%" )
        
    run_names = ['Low Side', 'High Side']
    
    desc = ['Lowside Test Run','Highside Test Run']

    total = []
    interest = []
    
    # Create empty containers for variables    
    for z in rate:
        total.append([]) 
        interest.append([])
    
    # Calculate Total Value and Interest acrued     
    for x in princ:
        dex = princ.index(x)
        for y in rate:
            idex = rate.index(y)
            for t in time:
                tdex = time.index(t)
                total[idex].append(princ[dex]*(1+(rate[idex]/comp))**(comp*time[tdex]))
                interest[idex].append(total[idex][tdex]-princ[dex])
       
    # Return Data dictionary for QC purposes
    output = {"00 Run": run_names, "01 Cases":data_names,  "02 Principle":princ,
              "03 Interest Rates": rate, "04 Period": time,"05 Compounding": comp,
              "06 Total Return":total, "07 Interest Earned":interest
              }
    
        
    
    
    for dataset in data_names:
        dex = data_names.index(dataset)
        #print(dex)
        add_run(run_names[dex], desc[dex])            
        for case in dataset:
            cdex = dataset.index(case)
            #print(cdex)
            # add if statement to make sure all lists have consistent dimensions
            for p in princ:
                pdex = princ.index(p)  
                run_temp = Run.objects.get(name = run_names[dex])
                #print(run_temp)
                add_data(run_temp, case, p, rate[dex], time[cdex], comp, total[dex][cdex], interest[dex][cdex])
        
    
    for r in Run.objects.all():
        for d in Data.objects.filter(run = r):
            print("- {0} - {1}".format(str(r), str(d))) 
    
    return output               
   
    
    


def add_run(nombre, descrip):
    r = Run.objects.get_or_create(name = nombre, description = descrip)[0]
    r.save()
    return r

def add_data(r_name, nombre, capital, interest_rate, time, compounding, total_return, gain):
    d = Data.objects.get_or_create(name = nombre, run = r_name)[0]
    d.principle = capital 
    d.compoundings = compounding
    d.rate = interest_rate
    d.interest = gain
    d.total = total_return
    d.year = time
    d.save()
    return d

""" Code within a conditional if __name__ == '__main__' statement will only be
 executed when the module is run as a standalone Python script.
 Importing the module will not run this code;
 classes or functions will however be fully accessible to you. """


#Execution ... And Go!
if __name__ == '__main__':
    print("Starting population script...")
    test = populate()
    