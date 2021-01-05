#importer une image avec opencv
import cv2

#lire image
#image=cv2.imread("image.jpg")


#couleur
#cv2.imshow("Image",image)

#noir et blanc
gray=cv2.imread("image.jpg",0)
#cv2.imshow("BW", gray)

hsv = cv2.cvtColor(gray, cv2.COLOR_BGR2HSV)
cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
cv2.imshow('hsv',hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

#save image
cv2.imwrite("image.jpg", gray)
