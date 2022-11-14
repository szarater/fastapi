from fastapi import FastAPI
app = FastAPI()
@app.get ("/saludo")

async def root():
    return {"message": "hola mision tic 2022"}

@app.get ("/usuario/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

cursos= [{"cursos": "Fundamentos de Programacion"}, {"cursos": "Programacion Basica"}, {"cursos": "Desarrollo Apps Web"}, {"cursos": "Desarrollo web"}]

@app.get ("/cursos/")
async def read_item(skip: int=0, limit: int=10):
    return cursos[skip: skip + limit] 