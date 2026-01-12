from fastapi import FastAPI, HTTPException
import uvicorn
from writers.txt_writers import write_to_txt
from ciphers.caesar_cipher import CaeserManager
from ciphers.fence_cipher import FenceManager
from schemas import CaesarModel, FenceModel

app = FastAPI()

TXT_PATH = "data/names.txt"


# ============================================================================================================
# BASIC VERSION:
# ============================================================================================================


# TESTS

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
    

# CAESER CIPHER

@app.post("/caesar")
def caeser_both_sipher_actions(data: CaesarModel):
    cur_data = data.dict()
    text_to_manage = cur_data["text"]
    offset = cur_data["offset"]
    mode = cur_data["mode"]

    if mode == "encrypt":
        incrypted_data = CaeserManager.encrypter(text_to_manage, offset)
        return {"encrypted_text": incrypted_data} 
    elif mode == "decrypt":
        decrypted_data = CaeserManager.decrypter(text_to_manage, offset)
        return {"decrypted_text": decrypted_data} 
    else:
        raise HTTPException(status_code=404, detail="Not found")
    

# FENCE CIPHER

@app.get("/fence/encrypt")
def fence_encryper(text: str):
    incrypted_data = FenceManager.encrypter(text)
    return {"encrypted_text": incrypted_data}

@app.post("/fence/decrypte")
def fence_decrypter(data: FenceModel):
    cur_data = data.dict()
    text_to_decryped = cur_data["text"]

    decrypted_data = FenceManager.decrypter(text_to_decryped)
    return {"decrypted_text": decrypted_data} 




# ============================================================================================================
# BONUS VERSION:
# ============================================================================================================

# from writers.json_writers import write_to_json, load_from_json, create_first_url_data, updating_url_data_in_json
# import time

# JSON_ENDPOINT_PATH = "data/endpoints_data.json"
# json_data = load_from_json(JSON_ENDPOINT_PATH)

# # CAESER CIPHER


# @app.post("/caesar")
# def caeser_both_sipher_actions(data: CaesarModel):
#     start_time = time.time()

#     cur_data = data.dict()
#     text_to_manage = cur_data["text"]
#     offset = cur_data["offset"]
#     mode = cur_data["mode"]

#     updated_data = None

#     if mode == "encrypt":
#         incrypted_data = CaeserManager.encrypter(text_to_manage, offset)

#         end_time = time.time()
#         updated_data = updating_url_data_in_json("/caesar","POST", start_time - end_time)
#         json_data.append(updated_data)
#         write_to_json(JSON_ENDPOINT_PATH, updated_data)

#         return {"encrypted_text": incrypted_data} 
    
#     elif mode == "decrypt":
#         decrypted_data = CaeserManager.decrypter(text_to_manage, offset)

#         end_time = time.time()
#         updated_data = updating_url_data_in_json("/caesar","POST", time, start_time - end_time)
#         json_data.append(updated_data)
#         write_to_json(JSON_ENDPOINT_PATH, updated_data)

#         return {"decrypted_text": decrypted_data} 
    
#     else:
#         raise HTTPException(status_code=404, detail="Not found")
    
    
# # FENCE CIPHER

# @app.get("/fence/encrypt")
# def fence_encryper(text: str):
#     start_time = time.time()

#     incrypted_data = FenceManager.encrypter(text)

#     end_time = time.time()
#     updated_data = updating_url_data_in_json("/fence/encrypt","Get", start_time - end_time)
#     json_data.append(updated_data)
#     write_to_json(JSON_ENDPOINT_PATH, updated_data)

#     return {"encrypted_text": incrypted_data}

# @app.post("/fence/decrypte")
# def fence_decrypter(data: FenceModel):
#     start_time = time.time()

#     cur_data = data.dict()
#     text_to_decryped = cur_data["text"]
#     decrypted_data = FenceManager.decrypter(text_to_decryped)

#     end_time = time.time()
#     updating_url_data_in_json("/fence/encrypt","Get", start_time - end_time)
#     updated_data = json_data.append(updated_data)
#     write_to_json(JSON_ENDPOINT_PATH, updated_data)

#     return {"decrypted_text": decrypted_data} 
