from fastapi import FastAPI

app = FastAPI(title="Multimodal Recommendation System API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Multimodal Recommendation System API"}

@app.get("/recommend")
def recommend(query: str):
    return {
        "input": query,
        "recommended": ["item1", "item2", "item3"]
    }
