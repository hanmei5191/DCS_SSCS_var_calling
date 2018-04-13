#!/usr/bin/python 
target = open ("../famSizeVar.txt","a+")
with open ("tmp1.txt", "r") as f: 
  fam={'A': [], 'C': [], 'G': [], 'T': []}
  array=range(1,4362)
  for idx in array:  
    fam[idx]=[]

  outArray=[]
  #famPos=[]
  #famNeg=[]
  lines = f.readlines()
  for line in lines: 
    pos=line.split()[0]
    fam[line.split()[2]].append(line.split()[4])

    #famPos.append(line.split()[4].split("-")[0])
    #famNeg.append(line.split()[4].split("-")[1])
  
  for key in sorted(fam):
    if key in ('A', 'C', 'G', 'T') and fam[key]:
      outArray.append(':'.join([key,'_'.join(fam[key])]))
    
  target.write("%s\t%s\n" %(pos, ','.join(outArray)))

target.close()

