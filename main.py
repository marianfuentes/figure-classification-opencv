# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:28:05 2020

Main function

@author: Marian Fuentes
"""
import numpy as np
import cv2
from imageShape import *



def main():
    
    #Creat an object of type class imageShape and ask user to give a height and width image dimensions
    myshape = imageShape(input("Enter your height image"),input("Enter your width image"))
    
    #generate random shape
    myshape.generateShape()
    #shows shape for 5 seconds
    myshape.showShape()
    #save figure image and name figure 
    img, namefig = myshape.getShape()
    print("The figure is a" , namefig)
    
    #classifies the saved image according to the shape 
    fig_classified = myshape.whatShape(img)
    print(fig_classified)
    
    #compares if the classification is right
    if namefig == fig_classified:
        print("Correct classification")
    else:
        print("Incorrect classification")
        
main()