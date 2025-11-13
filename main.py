from fastapi import FastAPI
import uvicorn
from writers.txt_writers import write_to_txt

app = FastAPI()

TXT_PATH = "data/names.txt"

@app.get("/test")
def get_test():
    return {"msg": "hi from test"}

@app.get("/test/{name}")
def save_name_to_txt(name: str):
    try:
        write_to_txt(TXT_PATH, name)
        return {"msg": "saved user"}
    except Exception:
        return {"msg": "could not write to the file"}
    

