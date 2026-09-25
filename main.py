from randomfiles import * 
from analysis import *


if __name__ == "__main__":
  
  # Sample code that works with the carinventory files
  # make sure to adjust to work with yours
  data_sizes = [10]
  no_queries = 10

  #no_entries = 10
  #file_name = "rand_file_"+str(no_entries)+".txt"
  #generate_data(file_name, no_entries)
  #patient_inventory_analysis(file_name, 10, no_entries)

  for no_entries in data_sizes:
    file_name = "rand_file_" + str(no_entries) + ".txt"

    generate_patient_data(file_name, no_entries)
    patient_inventory_analysis(file_name, no_queries, no_entries)
    
    print()
