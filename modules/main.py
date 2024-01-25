from fastapi import FastAPI
from flies.app.routes.flies import fly

app = FastAPI()

app.include_router(fly, prefix="/fly", tags=["fly"])

@app.get("")
async def root():
    return {"message": "Hello World"}