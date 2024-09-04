from fastapi import FastAPI
from consume import consume_router

app = FastAPI()
app.include_router(consume_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)  # Running on port 8002
