import glob
import re
from collections import Counter

flist = glob.glob("*")

with open(flist[0],mode="r") as f:
    fread = f.read()
    sresult = re.split(r'\W+',fread)
# need sort and kill duplication
    flist1=[flist[0] for i in range(len(sresult))]

    myzip = zip(sresult,flist1)
    mydict = dict(myzip)

print(mydict['zip'])


# https://code.tutsplus.com/ko/tutorials/how-to-merge-two-python-dictionaries--cms-26230

#{..., 'aloha':['xxx.txt','xxxx.txt'],...}
