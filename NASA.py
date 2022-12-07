import requests
from urllib.request import urlopen
import cv2
import numpy as np
import webbrowser

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

regex = "\<.*\>|\s-\s.*"
urlNASA = "https://apod.nasa.gov/apod/astropix.html"
response = requests.get(urlNASA)
notice_page = response.text
#JS = response.json()
#json을 사용하고자 하였으나, 해당 페이지에서 받아온 값에 적용이 되지는 않음으로 인해 text로 사용.
#print(notice_page)
imgurl = "https://apod.nasa.gov/apod/"+notice_page.split('IMG SRC="')[1].split('"')[0]
imgtitle = notice_page.split('IMG SRC="')[1].split('<center>')[1].split("Image Credit")[0]
imgtitle = imgtitle[5:-16]
imgtitle = imgtitle.replace(":","").replace("\/","")



#print("저장을 원하시면 1을 눌러 주세요.")
print("1. 저장\n2. 이미지를 브라우저에서 열기\n3. 팝업 이미지(시간이 오래 걸릴 수 있습니다.)")

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
input()
