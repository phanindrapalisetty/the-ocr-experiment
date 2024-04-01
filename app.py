#%%
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
import uvicorn 
from services import ocr_manager, result_manager
import json

app = FastAPI() 

@app.get('/health')
async def get_health_status():
    return {
        "statuscode": 200
    }

@app.get('/{userId}')
async def get_userId(userId: int):
    return {
        "userId": userId
    }

@app.post('/uploadfile/')
async def upload_file(file: UploadFile = File(...)):
    try:
        localPrefix = "DataDump"
        contents = await file.read()
        with open(f"{localPrefix}/"+file.filename, "wb") as f:
            f.write(contents)
        return {
            "status": 200,
            "filepath": f"{localPrefix}/"+file.filename
        }
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post('/getOCR/paddle/')
async def get_paddle_ocr_all_text(file_: UploadFile = File(...)):
    try:
        upload_file_res = await upload_file(file_)
        print(upload_file_res)
        if upload_file_res['status'] != 200:
            raise HTTPException(status_code=400, detail=upload_file_res['error'])
        ocr_result = ocr_manager.get_ocr_results(upload_file_res['filepath'], ocr_type='paddle')
        text_reuslt = result_manager.get_all_text_page_wise(ocr_result)

        return {"status": 200, "textResult": text_reuslt}
    except Exception as e:
        return {"status": 400, "error": str(e)}
# %%

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
# %%
