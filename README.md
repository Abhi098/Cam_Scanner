# Cam_Scanner
Cam scanner can be defined as document management solution. It is the space management solution to all the paperwork in the world any documents you see in real world can be digitized and saved right away.

The program is divided into two programs:
1. top_view.py
  It contains two functions:
      (a)order_points:
                      The function orders the points according to the sum and difference between x and y. The pts contains 4 points                       i.e x & ycoordinates. The top-left point would have the least sum whereas botom-right would have the largest                       sum. Similarly the top-right would have the least difference and bottom-left would have the maximum                                 difference.You can check by simply plotting an rectangle on a graph. 
      (b)four_point_transform:
                             The function defines the width and height of the rectangle contour.Top_view of the image is formed by                              the perspective transform function. Rest of details about perspective transform can be found on " https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html " 
                             
2. cam_scanner.py
   The image is first preprocessed 
   (a) resized according to image ratio
   (b) converted to grayscale
   (c) remove noise bu gaussian blur
   (d) Edges of the contours (canny)
   The edged copy is subjected find contours function which provides all the contours. Those contours are sorted according the contour area and the largest contour coordinates are applied to top_view.py. The contour is reshaped and multiplied by the ratio as edge detection and contour detection are performed on resized image whereas top_view of document is done on the original image.
