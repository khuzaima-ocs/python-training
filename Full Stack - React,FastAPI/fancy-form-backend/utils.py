import os, time, shutil

BASE_PATH = os.path.dirname(__file__)
UPLOAD_PATH = os.path.join(BASE_PATH, 'uploads')
timestr = time.strftime("%Y%m%d-%H%M%S")

async def save_image(file):
    try:
        print(file)
        if not file:
            print("No FIle")
        old_filename, file_ext = file.filename.split('.')
        new_filename = f"{old_filename}_{timestr}.{file_ext}"
        upload_file_path = os.path.join(UPLOAD_PATH, new_filename)

        with file.file as source_file:
            with open(upload_file_path, 'wb') as target_file:
                shutil.copyfileobj(source_file, target_file)

        return upload_file_path

    except Exception as e:
        print(str(e))
        return None