# https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
from skimage.filters import threshold_local
import top_view
import numpy as np
import imutils
import cv2

image=cv2.imread("bill5.jpeg")
print(image.shape,"shape")
# To retain te original length
ratio=image.shape[0]/500.0
orig=image.copy()
image=imutils.resize(image,height=500)


gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# TO remove noise
gray=cv2.GaussianBlur(gray,(5,5),0)
edged=cv2.Canny(gray,75,200)

cv2.imshow("original",image)
cv2.imshow("Edged",edged)

# To get all contours i.e the edges of object and then sort them acc to area
cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print("cnts",len(cnts))
# print(cnts)

cnts=imutils.grab_contours(cnts)
print(len(cnts),"length")
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
print(len(cnts),"length")
for c in cnts:
	# It return the perimeter
	peri=cv2.arcLength(c,True)
	print("Peri",peri)
	# This approximated the contour shape like if recatngle is not fully complete then it approximates it
	approx=cv2.approxPolyDP(c,0.02*peri,True)
	print("Approx",approx)
	if len(approx)==4:
		screenCnt=approx
		break

cv2.drawContours(image, [screenCnt], -1, (0, 0, 255), 2)
cv2.imshow("Outline", image)


warp=top_view.four_point_transform(orig,screenCnt.reshape(4,2)*ratio)
# cv2.imshow("warp",imutils.resize(warp,height=450))
warp=cv2.cvtColor(warp,cv2.COLOR_BGR2GRAY)
T=threshold_local(warp,11,offset=10,method="gaussian")
warp=(warp>T).astype("uint8")*255 #doubt

# cv2.imshow("T",T)
cv2.imshow("scannned",imutils.resize(warp,height=650))

cv2.waitKey(0)
cv2.destroyAllWindows()



# threshold_local
# skimage.filters.threshold_local(image, block_size, method='gaussian', offset=0, mode='reflect', param=None, cval=0)[source]
# Compute a threshold mask image based on local pixel neighborhood.

# Also known as adaptive or dynamic thresholding. The threshold value is the weighted mean for the local neighborhood of a pixel subtracted by a constant. Alternatively the threshold can be determined dynamically by a given function, using the ‘generic’ method.

# Parameters:	
# image : (N, M) ndarray
# Input image.

# block_size : int
# Odd size of pixel neighborhood which is used to calculate the threshold value (e.g. 3, 5, 7, …, 21, …).

# method : {‘generic’, ‘gaussian’, ‘mean’, ‘median’}, optional
# Method used to determine adaptive threshold for local neighbourhood in weighted mean image.

# ‘generic’: use custom function (see param parameter)
# ‘gaussian’: apply gaussian filter (see param parameter for custom sigma value)
# ‘mean’: apply arithmetic mean filter
# ‘median’: apply median rank filter
# By default the ‘gaussian’ method is used.

# offset : float, optional
# Constant subtracted from weighted mean of neighborhood to calculate the local threshold value. Default offset is 0.

# mode : {‘reflect’, ‘constant’, ‘nearest’, ‘mirror’, ‘wrap’}, optional
# The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to ‘constant’. Default is ‘reflect’.

# param : {int, function}, optional
# Either specify sigma for ‘gaussian’ method or function object for ‘generic’ method. This functions takes the flat array of local neighbourhood as a single argument and returns the calculated threshold for the centre pixel.

# cval : float, optional
# Value to fill past edges of input if mode is ‘constant’.

# Returns:	
# threshold : (N, M) ndarray
# Threshold image. All pixels in the input image higher than the corresponding pixel in the threshold image are considered foreground.