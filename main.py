from fastapi import FastAPI
app = FastAPI()
app.title = "My first app about movies - data analysis"
app.version = "0.0.1"


@app.get('/', tags=['Home'])  # Decorator for get request
def message():  # Function for the route
    return {'message': 'Hello world!'}

