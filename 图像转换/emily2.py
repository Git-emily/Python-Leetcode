import cv2
import numpy as np

if __name__ == '__main__':
    fn="emily1.png"
   
   # print ('load %s as ...') % fn
    img = cv2.imread(fn)
    sp = img.shape
    print (sp)
    sz1 = sp[0]#height(rows) of image
    sz2 = sp[1]#width(colums) of image
    sz3 = sp[2]#the pixels value is made up of three primary colors
   # print ('width: %d \nheight: %d \nnumber: %d')%(sz1,sz2,sz3)
