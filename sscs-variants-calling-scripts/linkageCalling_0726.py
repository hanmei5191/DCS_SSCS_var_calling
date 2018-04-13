#!/usr/bin/python 

import re 

target = open ("../linkage.txt","a+")
with open ("tmp1.txt", "r") as f: 
  lines = f.readlines()
  for line in lines: 
    variants=[]
    array=line.split()
    replaced_1 = re.sub(r'^[ATCGN]*', '', array[6])
    replaced_2 = re.sub(r'[ATCGN]*$', '', replaced_1)
    
    pattern = re.compile (r'[ATCG]')
    if (len(pattern.findall (replaced_2))) > 1: 
      for i in pattern.finditer(replaced_2): 
        variants.append("-".join(( str(int(array[5]) + i.start()), i.group() )))
      target.write("%s\t%s\t%s\t%s\t%s\n" %("_".join(variants), array[3],array[4],array[5],array[6]))
