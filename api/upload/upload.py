from fastapi import APIRouter, Depends, File, UploadFile, Response

from security import permission
import helper
from datetime import datetime
import shutil
import os
import uuid
from deta import Drive

upload_router = APIRouter()

drive = Drive("photos")

@upload_router.post("")
async def upload_file(file: UploadFile = File(...)):
    file_extension = os.path.splitext(file.filename)[1]
    new_filename = f"{str(uuid.uuid4()).replace('-', '')}{file_extension}"
    # file_path = os.path.join("public", new_filename)
    # print(file_path)

    file_data = await file.read()

    drive.put(new_filename, file_data)

    # with open(file_path, "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)

    return {"filename": new_filename}


@upload_router.get("/file/{file_name}")
async def upload_file(file_name: str):
    data = drive.get(file_name)
    content = data.read()

    return Response(content, media_type="application/octet-stream")
