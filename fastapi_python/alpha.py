from fastapi import FastAPI, UploadFile, File
import uvicorn
import argparse
import io
import cv2, pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from pytesseract import Output
from starlette.responses import StreamingResponse

app = FastAPI()


# need to work in that part
def new_func(image):
    img_list = []
    img = Image.open(image.file).convert('RGB')
    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    opencvImage = cv2.cvtColor(opencvImage, cv2.COLOR_RGB2GRAY)
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    ty = pytesseract.image_to_string(opencvImage)
    height, width = opencvImage.shape
    boxes = pytesseract.image_to_data(opencvImage)
    for count, i in enumerate(boxes.splitlines()):
        d = {}
        if count!=0:
            i= i.split()
            if len(i)==12:
                x,y,w,h = int(i[6]),int(i[7]),int(i[8]), int(i[9])
                cv2.rectangle(opencvImage,(x,y),(x+w,h+y),(0,0,255),3)
                # x= left, y= top , x+w = right, h+y = bottom
                d['left'] = x
                d['top'] = y
                d['right'] = x+w
                d['bottom'] = h+y
                d['text'] = i[-1] 
                img_list.append(d)
                cv2.putText(opencvImage, i[11],(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(50,50,255),1)
    return img_list
   
    

@app.post("/ocr")
async def image_endpoint(file:UploadFile = File(...)):
    predicted = new_func(file)
    return {"file":predicted}


if __name__ == "__main__":
    #  if we are not using multi processing so workers=NUM or reload = True
    # Also note that in this case, you should put uvicorn.run into if __name__ == '__main__' clause in the main module.
    uvicorn.run('app:app', host='127.0.0.2',reload=False, port=8001, log_level="info")