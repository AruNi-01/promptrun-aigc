import uvicorn
from fastapi import FastAPI

from config import appConf
from iface.prompt import prompt_router

app = FastAPI()
app.include_router(prompt_router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=appConf.app_port, reload=True)
