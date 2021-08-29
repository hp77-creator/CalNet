#!/usr/bin/env python
# coding: utf-8

# In[180]:


import cv2
import numpy as np


# In[181]:


image = cv2.imread(r'C:\Users\Tanya srivastava\Downloads\shapessss.png')
cv2.imshow("Image",image)
img = image
cv2.waitKey()
cv2.destroyAllWindows()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# # Drawing Contours 

# In[182]:


ret,thresh = cv2.threshold(gray,127,225,1)
contours,hi = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


# In[183]:


cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[184]:


len(contours)


# # Identifying shapes and writing their names and number of sides (sorted)

# In[185]:


length=[]
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    length.append(len(approx))
length.sort()
length


# In[186]:


type(len(contours))


# In[187]:


image = cv2.imread(r'C:\Users\Tanya srivastava\Downloads\shapessss.png')
img = image
for i in range(0,5):
    
    for cnt in contours:
        
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        #print(len(approx)

        if len(approx) == length[i]:
            if len(approx) == 3:
                shape_ = 'Triangle-3'
                cv2.drawContours(image,[cnt],0,(250,10,100),-1)
            
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.putText(image, shape_, (cx-40,cy+10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    
            elif len(approx) == 4:
                shape_ = "Rectangle-4"
                cv2.drawContours(image,[cnt],0,(0,155,255),-1)
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.putText(image,shape_,(cx-60, cy+5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)

            
            elif len(approx) == 12:
                shape_ = "Star-12"
                cv2.drawContours(image,[cnt],0,(78,255,78),-1)
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.putText(image, shape_, (cx-50,cy+5), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),1)
        
            elif len(approx) >= 15:
                shape_ = "Circle"
                cv2.drawContours(image,[cnt],0,(0,255,255),-1)
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.putText(image,shape_,(cx-30, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)

            
            elif len(approx) ==6:
                
                shape_ = "Hexagon-6"
                cv2.drawContours(img,[cnt],0,(125,5,255),-1)
                M = cv2.moments(cnt)
                cx = int (M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.putText(image,shape_,(cx-45, cy+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        
            cv2.imshow('identified shapes',image)
            cv2.waitKey(0)
        
cv2.waitKey(0)
cv2.destroyAllWindows()

