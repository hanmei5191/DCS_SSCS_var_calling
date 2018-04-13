# Duplex

This file describes the workflow calling variants and looking into linkage in two steps. 
1). bash readsCallVariants_0811.sh w/ famSizeConcaNote_0725.py linkageCalling_0726.py linkSplit_0728.py 
-> 
call variants w/ family size and linkage in reads 

# In SSCS, linkage_MAF.txt is filter by strand bias. 

2). bash bamMateLinkCall_0828.sh w/ mateLinkCall_0828.py 
-> 
call linkage in mates, -F 2060 is used in extracting mapped reads 

# In SSCS, linkage_mates_MAF_famSize.txt is filter by strand bias.   