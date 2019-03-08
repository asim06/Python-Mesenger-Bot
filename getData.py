import requests
from bs4 import BeautifulSoup
#Fırat üniversitesi Adli Bilişim Mühendisliği web sitesi üzerinden duyuruların isimleri ve linklerini çeker

#Site tarafından bloklanmamak için gönderdiğimiz tarayıcı bilgileri
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

print("Duyurular çekiliyor\n")

#isteğin yapılacağı adres
url= "http://ab.tek.firat.edu.tr/duyurular"
istek=requests.get(url,headers)

icerik=istek.content
soup = BeautifulSoup(icerik, "lxml")

print(" LİNKlER VE  HABERLER ŞU ŞEKİLDE:\n ------------------------------")

haberler = soup.find_all("span",{"class": "field-content"})


sayi = 1
say = 1
print(len(haberler))
for i in haberler:


    #print("http://ab.tek.firat.edu.tr" + i.a.get("href"))
    sayi+=1

    if(sayi<13):
        print(sayi, "-)", i.text)
        print("http://ab.tek.firat.edu.tr" + i.a.get("href"))
        print("\n")
        filetoAppend = open("/home/asim/Masaüstü/projectone/duyurular.txt", "w")
        filetoAppend.write(i.text)
        filetoAppend.write("   http://ab.tek.firat.edu.tr" + i.a.get("href"))
        filetoAppend.write("\n")
        # filetoAppend.write
        filetoAppend.close()





filetoRead =open("/home/asim/Masaüstü/projectone/duyurular.txt")

print("\n---**** dosyadan okunan veriler--**")

for i in filetoRead:
    a = i


filetoRead.close()
print(a)
