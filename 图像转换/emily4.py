import cv2
import numpy as np

if __name__=='__main__':
 fn_path = "emily1.png"
 fn=cv2.imread(fn_path)
 #print ("load image as...".format(np.shape(fn)))
 cv2.imshow("img", fn)
