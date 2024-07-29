from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import json, os, time, shutil

app = FastAPI()

BASE_PATH = os.path.dirname(__file__)
UPLOAD_PATH = os.path.join(BASE_PATH, 'uploads')

timestr = time.strftime("%Y%m%d-%H%M%S")

@app.post('/upload-json-file')
async def upload_json_file(file: UploadFile):
    if not file.filename.endswith('.json'):
        raise HTTPException(status_code=400, detail="Only JSON files are allowed")
    
    data = json.load(file.file)

    old_filename, file_ext = file.filename.split('.')
    new_filename = f"{old_filename}_{timestr}.{file_ext}"

    upload_file_path = os.path.join(UPLOAD_PATH, new_filename)

    with open(upload_file_path, "w") as f:
        json.dump(data, f)

    return JSONResponse(content={
        "status": "success",
        "filename": new_filename,
    }, status_code=201)

@app.post('/upload-file')
async def upload_any_file(file: UploadFile):
    try:
        old_filename, file_ext = file.filename.split('.')
        new_filename = f"{old_filename}_{timestr}.{file_ext}"
        upload_file_path = os.path.join(UPLOAD_PATH, new_filename)

        with file.file as source_file:
            with open(upload_file_path, 'wb') as target_file:
                shutil.copyfileobj(source_file, target_file)

        return JSONResponse(content={"status": "Success"}, status_code=201)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get('/download-file')
async def download_file(filename: str):
    download_file_path = os.path.join(UPLOAD_PATH, filename)

    return FileResponse(path=download_file_path)

