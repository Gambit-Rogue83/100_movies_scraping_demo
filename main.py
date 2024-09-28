from bs4 import BeautifulSoup
import requests
import json

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]


with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")











# <button ng-click="sleevesctrl.selectCurrentCardType(cardType)" class="sleeve-visualizer__card-dimensions ng-binding" aria-selected="true" ng-attr-title="{{cardType.names.join('; ')}}">63.5 x 88</button>
# <p ng-if="cardType.quantity" class="sleeve-visualizer__card-quantity ng-binding ng-scope">Qty 1091 </p>


sleeve_size_class = "sleeve-visualizer__card-dimensions ng-binding"
sleeve_quantity_class = "sleeve-visualizer__card-quantity ng-binding ng-scope"


