import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")

res.raise_for_status() # 정상적으로 작동하지 못하면 멈추게 한다

#print("응답코드 :", res.status_code) # 200 이면 정상

'''
if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")
'''

print(len(res.text))
print(res.text) # 웹싸이트의 내용을 가져온다

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text) # 가지고 온 내용을 파일로 만들어준다.
