from fastapi import FastAPI
from modules.detection.app.flies import fly

app = FastAPI()

app.include_router(fly, prefix="/fly", tags=["fly"])

@app.get("")
async def root():
    return {"message": "Hello World"}

def main():
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, workers=1)

if __name__ == "__main__":
    main()