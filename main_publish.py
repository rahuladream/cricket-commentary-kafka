from fastapi import FastAPI
from publish import publish_router

app = FastAPI()
app.include_router(publish_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)  # Running on port 8001
