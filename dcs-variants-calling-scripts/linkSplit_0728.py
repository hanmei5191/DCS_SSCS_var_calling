#!usr/bin/python 
from itertools import combinations 
target = open ("linkage_twoSites.txt","w")
with open ("linkage_sort.txt", "r") as f: 
  lines = f.readlines()
  for line in lines: 
    line_split = line.split() 
    variants = line_split[0].split("_")
    for i,j in list (combinations(variants, r=2)): 
      target.write ("%s\t%s\t%s\t%s\t%s\n" %("_".join((i,j)),line_split[1],line_split[2],line_split[3],line_split[4]))
      