# 🌟 FastAPI async magic! A web server that doesn't break a sweat.
# While one request sleeps, thousands of others can dance through.
# Non-blocking I/O = happy users and happy servers! ⚡

import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/data")
async def get_data():
    await asyncio.sleep(2)
    return {"message": "Here's your async data!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
