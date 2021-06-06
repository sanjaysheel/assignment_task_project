# cv2.rectangle(opencvImage,(71,67),(155,78),(0,0,255),3)
# cv2.putText(opencvImage, 'GALARETKA',(71,67),cv2.FONT_HERSHEY_COMPLEX,0.5,(50,50,255),1)

# r=requests.post( "http://127.0.0.1:8000/ocr",files={"file":open("C:\Users\cis\Downloads\Image_Project\Image_Project\ss.png","rb")})

# curl -X 'POST' 'http://localhost:8000/ocr' -F "C:\\Users\\cis\\Downloads\\Release\\images\\download (1).png"
import  requests 
import  json 
import  cv2  
print("===============================================================")
r=requests.post("http://127.0.0.1:8000/ocr/",files={"file":open("C:\\Users\\cis\\Downloads\\Release\\images\\download (1).png","rb")})

img = cv2.imread('C:\\Users\\cis\\Downloads\\Release\\images\\download (1).png')
print("This is a josn file@@@@@@@@",r.json())
print("===============================================================")
for b in r.json()['file']:
    img  =  cv2.rectangle(img ,(b['left'],b['top']),(b['right'],b['bottom']),(0,0,255),2)
    ing  =  cv2.putText(img ,b['text'],(b['left'],b['top']),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
cv2.imshow('img',img)
cv2.waitKey(0) 
