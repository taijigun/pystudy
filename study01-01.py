import glob
import re
from itertools import chain
from collections import defaultdict
import pickle

from collections import Counter

flist = glob.glob("*")

for i in range(len(flist)):
    with open(flist[i],mode="r") as f:
        fread = f.read()
        sresult = re.split(r'\W+',fread)
# need sort and kill duplication
        flist1=[flist[i] for k in range(len(sresult))]

        myzip = zip(sresult,flist1)
        mydict = dict(myzip)

        tempDict = defaultdict(list)
        if (i == 0):
            tempDict = mydict
        else :
            for k,v in chain(mydict.items(), resultDict.items()):
                tempDict[k].append(v)

        resultDict = tempDict

print(resultDict['import'])
print(resultDict['except'])
print(resultDict['duplication'])

with open("myData.pickle","wb") as oFile:
    pickle.dump(object, oFile)

with open("myData.pickle","rb") as iFile:
    object = pickle.load(iFile)



# https://code.tutsplus.com/ko/tutorials/how-to-merge-two-python-dictionaries--cms-26230

#{..., 'aloha':['xxx.txt','xxxx.txt'],...}
