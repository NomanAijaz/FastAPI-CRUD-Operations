from fastapi import FastAPI
from database.connection import engine
from routes.route import router
import models.model as models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(router)
