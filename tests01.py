import urllib.request
import re
from collections import Counter

#weblink = "http://realestate.daum.net/news/detail/main/20180401064015144"
#weblink = "http://realestate.daum.net/news/detail/main/201804010ddd"
weblink = "https://docs.python.org/3/library/re.html"
try:
 with urllib.request.urlopen(weblink) as doc:
  html=doc.read().decode('utf-8')

except:
 print("could not open %s" %doc, file=sys.err)

#print(html)
result=Counter(re.split(r'\W+', html))
print(result.most_common(10))
