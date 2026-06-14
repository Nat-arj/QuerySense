from fastapi import FastAPI
from app.api.routes import router
from app.config.cors import configure_cors

app = FastAPI(title="QuerySense Advanced Backend")

configure_cors(app)

app.include_router(router)