#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import cv2

img = cv2.imread(r'C:\Users\adith\OneDrive\Pictures\Camera Roll\shape.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,127,255,1)

contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
image=img






length=[]
for cnt in contours:
  
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    length.append(len(approx))
length.sort()
length

    
image = cv2.imread(r'C:\Users\adith\OneDrive\Pictures\Camera Roll\shape.png')
img = image
for i in range(0,5):
    
    for cnt in contours:
        
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if len(approx) == length[i]:
            if len(approx) == 3:
                cv2.drawContours(image,[cnt],0,(0,0,255),-1)
                M = cv2.moments(cnt)
                if M['m00'] != 0.0:
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])
                cv2.putText(img, 'Triangle=3', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0., (255, 0, 127), 1)
                
            elif len(approx) == 4:
                cv2.drawContours(image,[cnt],0,(0,255,0),-1)
                M = cv2.moments(cnt)
                if M['m00'] != 0.0:
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])
                cv2.putText(img, 'Quadrilateral=4', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 127), 1)
                
            elif len(approx) == 5:
                cv2.drawContours(image,[cnt],0,(255,0,0),-1)
                M = cv2.moments(cnt)
                if M['m00'] != 0.0:
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])
                cv2.putText(img, 'Pentagon=5', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 127), 1)
                
            elif len(approx) == 6:
                cv2.drawContours(image,[cnt],0,(255,255,0),-1)
                M = cv2.moments(cnt)
                if M['m00'] != 0.0:
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])
                cv2.putText(img, 'Hexagon=6', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 127), 1)
                
            else:
                shape_ = "Circle"
                cv2.drawContours(image,[cnt],0,(0,255,255),-1)
                M = cv2.moments(cnt)
                if M['m00'] != 0.0:
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])
                cv2.putText(image,shape_,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 127), 1)
                
            
            cv2.imshow('Identified shapes',image)
            cv2.waitKey(0)
                        
cv2.waitKey(0)
cv2.destroyAllWindows()

