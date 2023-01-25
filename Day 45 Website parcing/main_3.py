import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
movies = response.text
soup = BeautifulSoup(movies, "html.parser")


all_titles = soup.find_all(name="h3", class_="title")

all_movies = [movie.getText() for movie in all_titles]

for movie in all_movies[::-1]:
    with open("movies.txt", "a", encoding="UTF-8") as file:
        file.write(movie + "\n")
