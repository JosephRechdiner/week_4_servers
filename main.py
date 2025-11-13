from fastapi import FastAPI, HTTPException
import uvicorn
from writers.txt_writers import write_to_txt
from ciphers.caesar_cipher import CaeserManager
from schemas import CaesarModel

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
    
@app.post("/caesar")
def caeser_both(data: CaesarModel):
    cur_data = data.dict()
    text_to_manage = cur_data["text"]
    offset = cur_data["offset"]
    mode = cur_data["mode"]

    if mode == "encrypt":
        incrypted_data = CaeserManager.caeser_encrypter(text_to_manage, offset)
        return {"encrypted_text": incrypted_data} 
    elif mode == "decrypt":
        decrypted_data = CaeserManager.caeser_decrypter(text_to_manage, offset)
        return {"decrypted_text": decrypted_data} 
    else:
        raise HTTPException(status_code=404, detail="Not found")