# from cv2 import *
# # initialize the camera
# cam = VideoCapture(0)   # 0 -> index of camera
# s, img = cam.read()
# if s:    # frame captured without any errors
#     namedWindow("cam-test",CV_WINDOW_Normal)
#     imshow("cam-test",img)
#     waitKey(0)
#     destroyWindow("cam-test")
#     imwrite("filename.jpg",img) #save image



# from VideoCapture import Device
# cam = Device()
# cam.saveSnapshot('image.jpg')



# saves images a lot with fps
# import cv2
#
# # Opens the inbuilt camera of laptop to capture video.
# cap = cv2.VideoCapture(0)
# i = 0
#
# while (cap.isOpened()):
#     ret, frame = cap.read()
#
#     # This condition prevents from infinite looping
#     # incase video ends.
#     if ret == False:
#         break
#
#     # Save Frame by Frame into disk using imwrite method
#     cv2.imwrite('Frame' + str(i) + '.jpg', frame)
#     i += 1
#
# cap.release()
# cv2.destroyAllWindows()