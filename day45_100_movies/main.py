import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movies_website = response.text

soup = BeautifulSoup(movies_website, "html.parser")

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

rankings = soup.find_all(name="h3", class_="title")
movie_titles = []
for ranking in rankings:
    ranking_text = ranking.getText()
    movie_titles.append(ranking_text)

reversed_list = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in reversed_list:
        file.write(f"{movie}\n")
