#importer une image avec opencv
import cv2

#lire image
image=cv2.imread("image.jpg")


#couleur
#cv2.imshow("Image",image)

#noir et blanc
gray=cv2.imread("image.jpg",0)
cv2.imshow("BW", gray)

cv2.waitKey()
cv2.destroyAllWindows()

#save image
cv2.imwrite("image.jpg", gray)