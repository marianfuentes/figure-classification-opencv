# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:27:02 2020

This file contains definition of class object "imageShape".
It allows to receive from user two values of height and width image.

Methods
generateShape:
    It generates and saves image with height and width received.
    It also draws a centered figure (choosing between triangle, rectangle, rotated square or circle) randomly.
    
showShape:
    shows image with figure drawed.
    If there's no image it shows a black image.

getShape:
    returns figure image and figure name
    
whatShape:
    receives an image with a figure (black background and clear object)
    Classifies the image between triangle, rectangle, square and circle.
    Returns the name of the classified figure.




@author: Marian Fuentes
"""
 

#Libraries


import numpy as np
import cv2


# imageShape creation 

class imageShape:

########  Constructor  #######
    #Receives height and width of an image
    def __init__(self,height,width):
        #saves height and width image
        self.h = height
        self.w = width
        #flag to know that there's no existing image
        self.b = 0
        
####### Methods #########
    def generateShape(self):
        
        #generate random number with uniform distribution between 0 and 3
        #each number corresponds to a geometric figure
        # 0 -> triangle, 1 -> square, 2 -> rectangle, 3 -> circle
        numfig = round(np.random.uniform(0,3))
        
        #Create black image of height and width size and saves it in self
        self.shape = np.zeros((int(self.h), int(self.w), 3), np.uint8)

        # Calculate the center point of image
        x, y = int(self.w) // 2, int(self.h)// 2
        
        #Draw image according to numfig random number
        
        if numfig == 3:
            ######## CIRCLE #################
           
            #figure name
            self.fig = "Circle"
            
            #Draw the centered circle. 
            #Radius: minimun value between height and width divided by 4
            #Circle color: cyan
            #Thickness -1 fills the circle.
            cv2.circle(self.shape, center=(x, y), radius=min(int(self.w),int(self.h))//4, color=(255,255,0), thickness=-1)
            #flag indicates that a figure has been created
            self.b = 1
            
        elif numfig == 2:
       
            ###### RECTANGLE ################
            
            #figure name
            self.fig = "Rectangle"
            
            #Calculate horizontal side length
            horz_side = int(self.w)/2
            #Calculate vertical side length
            vert_side = int(self.h)/2
            
            #Calculate four coordinate points of the rectangle adding the corresponding distance from the center
            x1 = int(round(x - horz_side/2))
            y1 = int(round(y - vert_side/2))
            x2 = int(round(x + horz_side/2))
            y2 = int(round(y + vert_side/2))
            
            #Draw the centered rectangle. 
            #horizontal side: width/2 
            #vertical side: height/2
            #Rectangle color: cyan
            #Thickness -1 fills the rectangle.
            cv2.rectangle(self.shape, (x1,y1), (x2,y2), (255, 255, 0), -1) 

            
        elif numfig == 1:
      
            ####### ROTATED SQUARE #############
            #Square rotated 45°
            #figure name
            self.fig = "Square"
            
            #Calculate side length: minimun value between height and width divided by 2
            side = min(int(self.w),int(self.h))/2
            
            #Calculate four coordinate points of the square adding the corresponding distance from the center
            x1 = int(round(x + side/2))
            y1 = int(round(y))
            x2 = int(round(x))
            y2 = int(round(y - side/2))
            x3 = int(round(x - side/2))
            y3 = int(round(y))     
            x4 = int(round(x))
            y4 = int(round(y + side/2))
            
            #Draw lines between the four points of cyan color.
            cv2.line(self.shape, (x1, y1),(x2,y2),(255, 255, 0), 2)
            cv2.line(self.shape, (x2, y2),(x3,y3), (255, 255, 0), 2)
            cv2.line(self.shape, (x3, y3),(x4,y4),(255, 255, 0), 2)
            cv2.line(self.shape, (x4, y4),(x1,y1),(255, 255, 0), 2)
            
            #fill the square
            cv2.floodFill(self.shape, None, (x, y), (255, 225, 0))
            #flag indicates that a figure has been created
            self.b = 1
            
        elif numfig == 0:
            
            ####### EQUILATERAL TRIANGLE ################
            
            #figure name
            self.fig = "Triangle"
            
            #calculate side length as minimun value between height and width divided by 2
            side = min(int(self.h),int(self.w))/2
            
            #r is the distance from the triangle center to the side  (apothem)
            r = side * (np.sqrt(3)/6)
            
            #R is the distance from the triangle center to the vertex
            R = side * (np.sqrt(3)/3)
            
            #Calculate the 3 coordinate points of each vertex adding the corresponding distance from the center 
            x1 = int(round((x + side/2)))
            y1 = int(round((y + r)))
            x2 = int(x)
            y2 = int(round(y-R))
            x3 = int(round(x - side/2))
            y3 = int(round((y + r)))
            
            #Draw 3 lines to build the triangle color cyan
            cv2.line(self.shape, (x1, y1),(x2,y2),(255, 255, 0), 2)
            cv2.line(self.shape, (x2, y2),(x3,y3), (255, 255, 0), 2)
            cv2.line(self.shape, (x3, y3),(x1,y1),(255, 255, 0), 2)
            
            #Fills the triangle
            cv2.floodFill(self.shape, None, (x, y), (255, 225, 0))
            
            #flag indicates that a figure has been created
            self.b = 1


    def showShape(self):
        
        #if there's no figure created it shows a black image for 5 seconds
        if(self.b == 0):
            self.shape = np.zeros((int(self.h), int(self.w), 3), np.uint8)
            cv2.imshow("shape", self.shape) 
            cv2.waitKey(5000) 
            
            #shows the image for 5 seconds
        else:
            
            cv2.imshow("shape", self.shape) 
            cv2.waitKey(5000) 
    
    def getShape(self):
        #returns image with figure and the figure name
        return (self.shape, self.fig)
    
    def whatShape(self,im):
        
        #save received image and binarize with OTSU Method
        self.img = im
        image_draw = self.img.copy()
        image_gray = cv2.cvtColor(image_draw, cv2.COLOR_BGR2GRAY)
        ret, Ibw_shapes = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        #Find contours
        contours, hierarchy = cv2.findContours(Ibw_shapes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        #for each contour found it calculate the moments and find area
        for cnt in contours:
            
            #Approximates a polygonal curve with specified precision
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            
            #Classifies shape according to number of approximations
            if len(approx)==3:
                return "Triangle"
            
            elif len(approx)==4:
                
                #Calculate size of image
                height, width, channels = self.img.shape
                
                #Calculate square area according to the size specifications
                squarearea = (min(height,width)/2)**2
                
                #Calculate moments and area of shape
                for idx, cont in enumerate(contours):

                    M = cv2.moments(contours[idx])
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    area = M['m00']
                    
                    #In case the image has same height and width it identifies the square from the rectangle calculating the rectangle area
                    #It compares the calculated rectangle area with the area found with the moments
                    if (height == width):
                        recta = (height/2)**2
                        if area < recta:
                            return "Square"
                        else:
                            return "Rectangle"
                    #If height and width image are different it compares the area of shape with square area calculated
                    elif area > squarearea:
                        return "Rectangle"
                    else:
                        return "Square"
            else: 
                return "Circle"
        


