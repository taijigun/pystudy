# Broken Link Detector

# 웹 페이지의 URL을 입력받아 해당 웹 페이지에서 연결이 끊긴 링크 이름과 연결 대상을 출력하는 프로그램을 작성해보자.
# 연습문제의 목적에 따라 urllib.request.urlopen() 으로 URL을 열 때 오류가 발생한다면 링크가 끊긴 것으로 간주한다

from urllib.request import urlopen
from bs4 import BeautifulSoup

print("enter the url")
input(weblink)

try:
 with urllib.request.urlopen(weblink) as doc:
    soup0=BeautifulSoup(doc))
    links = [(link.string, link["href"]) for link in soup0.find_all("a") if link.has_attr("href")]

    for
#  html=doc.read().decode('utf-8')

except:
 print("could not open %s" %doc, file=sys.err)