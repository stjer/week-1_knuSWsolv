import requests
import datetime
urlBUSAN = "https://www.yr.no/en/forecast/daily-table/2-1838524/Republic%20of%20Korea/Busan/Busan"
urlDAEGU = "https://www.yr.no/en/forecast/daily-table/2-1835329/Republic%20of%20Korea/Daegu/Daegu"

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
            #print("체크")
            if (error==1):
                today += datetime.timedelta(days=1)
                weather(url, today,error)


print("부산 날씨")
weather(urlBUSAN)
print("\n\n대구 날씨")
weather(urlDAEGU)

input()
