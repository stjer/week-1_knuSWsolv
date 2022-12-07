import requests
urlNATE = "https://news.nate.com/"
response = requests.get(urlNATE)
notice_page = response.text
key = notice_page.split('<meta name="nate:description" content="')[1].split('" />')[0]
print("키워드 : ")
kkey = key.split('#')
for i in range(1,4):
    print(kkey[i])

input()
