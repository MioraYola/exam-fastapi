from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()

@app.get("/")
def root():
    with open("welcome.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, media_type="text/html")

@app.get("/{full_path:path}")
def catch_all(full_path: str):
    with open("404.html", "r", encoding="utf-8") as file:
        html_404 = file.read()
    return Response(content=html_404, status_code=404, media_type="text/html")

