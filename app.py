from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import JSONResponse
app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root(text: str="IDK"):
    if text == "hello":
        return "Hello from salt lake city"
    if text =="test":
        return JSONResponse
    else:
        return "Hello"

