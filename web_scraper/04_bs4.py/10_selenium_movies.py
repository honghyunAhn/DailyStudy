import requests
from bs4 import BeautifulSoup

URL = "https://play.google.com/store/movies/collection/cluster?clp=6gIkIiIKHHByb21vdGlvbl9tb3ZpZXNfbmV3X3JlbGVhc2UQPxgE:S:ANO1ljIv2Z0&gsr=CifqAiQiIgoccHJvbW90aW9uX21vdmllc19uZXdfcmVsZWFzZRA_GAQ%3D:S:ANO1ljJ_5l0&hl=ko&gl=US"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    "Accept-Language" : "ko-KR, ko"
}

res = requests.get(URL, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

