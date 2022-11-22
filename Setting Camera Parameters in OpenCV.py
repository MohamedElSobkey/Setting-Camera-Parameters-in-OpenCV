import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#set your frame width
cap.set(3,3000)
#set your frame height
cap.set(4,3000)

#get your frame width
print(cap.get(3))
#get your frame height
print(cap.get(4))

#while camera is open
while(cap.isOpened()):
    ret, frame = cap.read()#read frames  
      
    if ret == True: #still there is a frame to process
        
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY ) 
     
     cv2.imshow('frame', gray)    
             
     if cv2.waitKey(1) & 0xFF == ord('q'):#wait key from keyboard 
                
         break   
                  
    else: #if ret=false
         
        break  
    
# to close camera        
cap.release()
#close window
cv2.destroyAllWindows()





