import requests
import webbrowser
#import googletrans 오작동하여 패스.
urlsci = 'https://www.sci.news/archive'
urlnysci = 'https://www.nytimes.com/section/science'#현재 구현은 안됨.
urlDAsci = 'https://m.dongascience.com/news.php'#'https://www.dongascience.com/news.php'

def tryint():
    try : 
        a = int(input("번호 입력 : \n"))
        if (1<=a<=3):
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

response = requests.get(urlsci)
np1 = response.text
'''
response = requests.get(urlnysci)
np2 = response.text
'''
response = requests.get(urlDAsci)
np3 = response.text
#print(np3)

'''
translator = googletrans.Translator()

str2 = "I like burger."
result2 = translator.translate(str2, dest='ko', src='en' )
print(result2)
'''
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
