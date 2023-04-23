from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import item


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(item.router, tags=['Items'], prefix='/api/items')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}
