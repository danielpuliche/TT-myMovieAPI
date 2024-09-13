from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from movies_list import movies_list

app = FastAPI()
app.title = "My first app about movies - data analysis"
app.version = "0.0.1"


@app.get('/', tags=['Home'])  # Decorator for get request
def message():  # Function for the route
    return HTMLResponse('<h1>Hola mundo</h1>')


@app.get('/movies', tags=['Movies'])  # New route for the movies
def get_movies():
    return movies_list


@app.get('/movies/{id}', tags=["Movies"])
def get_movie_by_id(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []


@app.get('/movies/', tags=["Movies"])
def get_movies_by_category(category: str):
    return [item for item in movies_list if item['category'] == category]


@app.post('/movies', tags=['Movies'])
def add_movie(title: str = Body(),
              overview: str = Body(),
              year: int = Body(),
              rating: float = Body(),
              category: str = Body()
              ):
    new_id = movies_list[-1]["id"] + 1,
    movies_list.append({
        "title": title,
        "id": new_id,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies_list
