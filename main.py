from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "به سرور من خوش آمدید"}
