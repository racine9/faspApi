from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def read_users():
    return ["Ricky", "mark"]

@app.get("/users")
async def read_users2():
    return ["bean", "elfo"]