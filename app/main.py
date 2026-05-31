from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse(content=jsonable_encoder({"message": "Hello Bigger Applications!"}))


