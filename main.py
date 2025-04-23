from fastapi import FastAPI
from fastapi.responses import JSONResponse
from scraper import parse_fighter

app = FastAPI()

@app.get("/fighter/{slug}")
def get_fighter(slug: str):
    url = f"https://www.sherdog.com/fighter/{slug}"
    try:
        data = parse_fighter(url)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
