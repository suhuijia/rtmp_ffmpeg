import cv2 

## 读取rtsp视频流并显示
# cap = cv2.VideoCapture("rtmp://192.168.46.159:2016/hls_alic/film")
cap = cv2.VideoCapture("rtmp://192.168.46.111:1935/live")
# cap = cv2.VideoCapture("rtsp://192.168.46.120:8554/live1.h264")
## 读取usb-camera 0（/dev/video0） 
#cap = cv2.VideoCapture(0)
while True:
    if (cap.isOpened):
        print("Open RTMP")
        break
    else:
        print("Fail to Open RTMP!")
        continue

while cap.isOpened():
    ret,frame = cap.read()
    print (frame.shape[0], frame.shape[1], frame.shape[2])
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyWindow("frame")
cap.release()


# ffmpeg -f dshow -i video="SEMIC Camera" -vcodec libx264 -acodec copy -preset:v ultrafast -tune:v zerolatency -f flv rtmp://192.168.46.111:1935/live
# ffmpeg -f dshow -i video="SEMIC Camera" -vcodec copy -acodec copy -f flv rtmp://192.168.46.111:1935/live
# ffmpeg -f dshow -i video="SEMIC Camera" -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv rtmp://192.168.46.111:1935/live
# ffmpeg -r 25 -f dshow -s 640×480 -i video="SEMIC Camera" -vcodec libx264 -b 600k -vpre slow -acodec libfaac -f flv rtmp://192.168.46.111:1935/live

# ffmpeg -list_devices true -f dshow -i dummy
# https://blog.csdn.net/leixiaohua1020/article/details/38284961

# 简单的抓屏
# ffmpeg -f gdigrab -i desktop out.avi  (抓取整张桌面)
# ffmpeg -f gdigrab -framerate 5 -offset_x 10 -offset_y 20 -video_size 640x480 -i desktop out.avi (从屏幕上(10, 20)的点开始抓取640x480的屏幕大小)

# ffmpeg -f gdigrab -i title={MobaXterm} out.avi