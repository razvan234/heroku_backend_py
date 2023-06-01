from fastapi import FastAPI, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configure CORS
origins = ["http://localhost:3000"]  # Replace with your frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_places(query: str):
    url = "https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete"


    querystring = {"query": query}

    headers = {
        "X-RapidAPI-Key": "781275f038msh43ccbf90187c7c5p1fa006jsn7c4ba4888a13",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response_json = response.json()

    if response.status_code == 200:
        return response_json
    else:
        raise HTTPException(status_code=response.status_code, detail=response_json)

