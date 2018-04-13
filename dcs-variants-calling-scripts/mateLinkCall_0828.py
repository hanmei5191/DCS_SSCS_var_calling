#!usr/bin/python 

import re 

def callVariants (mate1_seq,mate1_start,mate2_seq,mate2_start): 
  a = [(m.start() + mate1_start, m.group(0)) for m in re.finditer(r'[ATCG]', mate1_seq)] 
  b = [(n.start() + mate2_start, n.group(0)) for n in re.finditer(r'[ATCG]', mate2_seq)] 
  if len(a) > 0 and len(b) > 0:
    return([a,b])

target = open ("linkage_mates.txt","w")

with open ("mate_aligned.txt", "r") as f: 
  fam={}
  fam_mate={}
  lines = f.readlines()
  for line in lines: 
    line_split = line.split("\t", 1)
    try: 
      fam[line_split[0]]
      fam[line_split[0]].append(line_split[1])
    except KeyError: 
      fam[line_split[0]] = []
      fam[line_split[0]].append(line_split[1])
  
  for key1 in fam: 
    try: 
      if int(fam[key1][0].split("\t")[2]) > int(fam[key1][1].split("\t")[2]):
        fam[key1][0] , fam[key1][1] = fam[key1][1] , fam[key1][0]
    except IndexError: 
      pass 

  for key2 in fam: 
    if len(fam[key2]) == 2: 
      mate1_match = re.sub(r'[ATCGN]*$','',re.sub(r'^[ATCGN]*','', fam[key2][0].split()[8]))
      mate2_match = re.sub(r'[ATCGN]*$','',re.sub(r'^[ATCGN]*','', fam[key2][1].split()[8]))
      mate1_start = int(fam[key2][0].split()[2])
      mate2_start = int(fam[key2][0].split()[6])
      overlapping = mate1_start + len (mate1_match) - mate2_start
      if overlapping >= 0: 
        mate2_start_chunked = mate2_start + overlapping
        mate2_match_chunked = mate2_match[mate2_start_chunked-mate2_start:]
        #find matches separately in mate1_match and mate2_match_chunked
        link=callVariants (mate1_match, mate1_start, mate2_match_chunked, mate2_start_chunked)
        if link is not None:
          tmp1 = [(x,y) for x in link[0] for y in link[1]] 
          for key3 in tmp1: 
            target.write ("%s-%s_%s-%s\t%s\n" %(key3[0][0], key3[0][1], key3[1][0], key3[1][1], key2))

      else:
        #find matches separately in mate1_match and mate2_match 
        link=callVariants (mate1_match, mate1_start, mate2_match, mate2_start)
        if link is not None:
          tmp1 = [(x,y) for x in link[0] for y in link[1]] 
          for key3 in tmp1: 
            target.write ("%s-%s_%s-%s\t%s\n" %(key3[0][0], key3[0][1], key3[1][0], key3[1][1], key2))
    else: 
      pass 

