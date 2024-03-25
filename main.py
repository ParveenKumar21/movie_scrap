from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.content

soup = BeautifulSoup(website_html, "html.parser")

articles = soup.find_all(name="h3",class_="title")
all_movies = [movie.getText() for movie in articles]

year = soup.find_all(class_="description")
tex = [i.findNext(name="strong").text for i in year]

movies = all_movies[::-1]
yr = tex[::-1]
with open("movies.txt",mode="w") as file:
    for movie_name in movies:
        if movie_name == movies[58]:
            pass
        else:
            file.write(f'{movie_name} -{yr[movies.index(movie_name)]}\n ')
