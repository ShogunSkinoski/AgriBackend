from fastapi import FastAPI
from modules.detection.app.flies import fly_router
from modules.detection.app.color import color_router
from modules.base.app.management import management_router
app = FastAPI()
app.include_router(management_router, prefix="/management", tags=["management"])
app.include_router(fly_router, prefix="/fly", tags=["fly"])
app.include_router(color_router, prefix="/color", tags=["color"])


#TODO: admin sector detayı alabilmeli 
#TODO: admin sector güncelleyebilmeli

@app.get("")
async def root():
    return {"message": "Hello World"}

def main():
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, workers=1)

if __name__ == "__main__":
    main()