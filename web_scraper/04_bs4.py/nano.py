import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=747271&weekday=thu"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class" : "title"})

# 만화 제목 + 링크 가져오기
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))