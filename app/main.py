from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Video Recommendation API"}

@app.get("/recommend")
def get_recommendations():
    return {"videos": ["video1", "video2", "video3"]}
