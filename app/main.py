from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_main():
    return {"message": "Helo World of FastApi with Traefik!"}


@app.get("/users")
async def get_users():
    return {"user1": "User1", "User2":"User2"}