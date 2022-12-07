import requests
import datetime
from urllib.request import urlopen
import cv2
import numpy as np
import webbrowser
#import googletrans 오작동하여 패스.

def tryint(num=3):
    try : 
        a = int(input("번호 입력 : \n"))
        if (1<=a<=num):
            return a
        elif a== -1:
            return a
        else:
            print("메뉴에 있는 번호를 선택해 주세요.")
            a = tryint()
            return a
    except: 
        print("숫자를 입력해 주세요.")
        a = tryint()
        return a

def weatherModule():
    urlBUSAN = "https://www.yr.no/en/forecast/daily-table/2-1838524/Republic%20of%20Korea/Busan/Busan"
    urlDAEGU = "https://www.yr.no/en/forecast/daily-table/2-1835329/Republic%20of%20Korea/Daegu/Daegu"
    print("부산 날씨")
    weather(urlBUSAN)
    print("\n\n대구 날씨")
    weather(urlDAEGU)

def weather(url,today = datetime.datetime.today(),error = 0):
    response = requests.get(url)
    notice_page = response.text
    TOD = '"'
    TOD2 = [str(today.year), str(today.month), str(today.day)]
    if len(TOD2[2])==1:
        TOD2[2]="0"+TOD2[2]
    TOD += '-'.join(TOD2)
    TOD += '"'
    TIMEng = ['Morning', 'Afternoon', 'Evening', 'Night']
    TIMKo = ['오전','오후','저녁','새벽']
    WEAeng = ['fair','clear sky','partly cloudy','cloudy','rain','heavy rain','light rain','snow']
    WEAko = ['맑음','맑음','구름 조금','흐림','비','폭우','가랑비','눈']
    for i in range(1,5):
        try :
            weatxt = notice_page.split('time dateTime='+TOD)[1].split('alt=')[i].split('width')[0].replace('"',"")
            weatime = TIMKo[TIMEng.index(weatxt.split(': ')[0])]
            weawea = WEAko[WEAeng.index(weatxt.split(': ')[1].strip())]
            error = 0
            print(weatime,' : ',weawea)
        except :
            error +=1
            if (error==1):
                today += datetime.timedelta(days=1)
                weather(url, today,error)

def keywordNate():
    urlNATE = "https://news.nate.com/"
    response = requests.get(urlNATE)
    notice_page = response.text
    key = notice_page.split('<meta name="nate:description" content="')[1].split('" />')[0]
    print("키워드 : ")
    kkey = key.split('#')
    for i in range(1,4):
        print(kkey[i])
        
def save(imgurl, imgtitle):
    with urlopen(imgurl) as f:
        with open('C:/Users/Samsung/AppData/Local/Programs/Python/Python310/images/' + imgtitle +'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    print("이미지 저장 완료")

def url_to_image(url):
  resp = urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype='uint8')
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)

  return image

def nasa():
    regex = "\<.*\>|\s-\s.*"
    urlNASA = "https://apod.nasa.gov/apod/astropix.html"
    response = requests.get(urlNASA)
    notice_page = response.text
    #JS = response.json()
    #json을 사용하고자 하였으나, 해당 페이지에서 받아온 값에 적용이 되지는 않음으로 인해 text로 사용.
    imgurl = "https://apod.nasa.gov/apod/"+notice_page.split('IMG SRC="')[1].split('"')[0]
    imgtitle = notice_page.split('IMG SRC="')[1].split('<center>')[1].split("Image Credit")[0]
    imgtitle = imgtitle[5:-16]
    imgtitle = imgtitle.replace(":","").replace("\/","")

    image = url_to_image(imgurl)
    cv2.imshow(imgtitle,image)

    print("1. 저장(경로가 올바른지 확인해주세요.)\n2. 이미지를 브라우저에서 열기\n3. 팝업 이미지(시간이 오래 걸릴 수 있습니다.)")

    a = input()
    if a=='1':
        save(imgurl, imgtitle)
    elif a=='2':
        #print(imgurl)
        webbrowser.open(imgurl)
    elif a=='3':
        image = url_to_image(imgurl)
        cv2.imshow(imgtitle,image)
    else:
        print('종료')
    

def scinews():
    urlsci = 'https://www.sci.news/archive'
    urlnysci = 'https://www.nytimes.com/section/science'#현재 구현은 안됨.
    urlDAsci = 'https://m.dongascience.com/news.php'#'https://www.dongascience.com/news.php'
    
    response = requests.get(urlsci)
    np1 = response.text
    '''
    response = requests.get(urlnysci)
    np2 = response.text
    '''
    response = requests.get(urlDAsci)
    np3 = response.text
    roughtitle = np1.split('<ul class="bjqs">')[1].split('<!-- end Basic jQuery Slider')[0]
    #print(roughtitle)
    roughtitle = roughtitle.split("<li>")
    HMarticle = len(roughtitle)#8, 0은 빈값, 1~7까지에 값들이 있음.
    tlink=[]
    ttitle = []
    for i in range(1,HMarticle):
        rough = roughtitle[i].split('rel="bookmark">')
       #print(rough[0][10:-2],"\n",rough[1].split('</a>')[0].strip())
       tlink.append(rough[0][10:-2])
       ttitle.append(rough[1].split('</a>')[0].strip())
    tlink3 = []
    ttitle3 = []
    for i in range(1,11):
        tlink3.append("https://m.dongascience.com/news.php?idx="+np3.split('news.php?idx=')[i].split('">')[0])
        ttitle3.append(np3.split('<dt><div class="tit">')[i].split('</div>')[0])

    nextarti = 0
    nextarti3 = 0
    print("1. 다음 기사\n2. 해당 기사 브라우저로 열기\n3. 다른 플랫폼 기사 보기")
    while (nextarti<HMarticle-1):
        print("\n",ttitle[nextarti])
    
        a = tryint()
        if a==1:
            nextarti+=1
        elif a==2:
            webbrowser.open(tlink[nextarti])
        elif a==3:
            nextarti = HMarticle+1
        else:
            nextarti = HMarticle+1
            nextarti3 = 100
    while (nextarti3<10):
        print("\n",ttitle3[nextarti3])
    
        a = tryint()
        if a==1:
            nextarti3+=1
        elif a==2:
            webbrowser.open(tlink3[nextarti3])
        elif a==3:
            nextarti3 = 11
        else:
            nextarti3 = 11
    
    
    
def main():
    #print("1. 날씨\n2. 뉴스 키워드\n3. 이미지\n4. 게임\n(종료 : -1)\n")
    print("1. 날씨\n2. 뉴스 키워드\n3. 이미지\n4. 과학 뉴스\n(종료 : -1)\n")
    a = tryint(4)

    if a==1:
        #print("날씨")
        weatherModule()
    elif a==2:
        #print("뉴스 키워드")
        keywordNate()
    elif a==3:
        nasa()
    elif a==4:
        #print('게임')
    else :
        return a
    print('\n')
    return 1

point = 1
while(point == 1):
    point = main()
    

