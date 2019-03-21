import av
import cv2

video = av.open('rtmp://192.168.46.111:1935/live', 'r')
# video = av.open('rtmp://192.168.46.159:2016/hls_alic/film', 'r')
print("format:" + video.dumps_format())
print('after open')
index = 0
try:
    for frame in video.decode():
        # Do something with `frame`
        index += 1
        print("frame:{}".format(index))

        img = frame.to_nd_array(format='bgr24')
        cv2.imshow("Test", img)

        #cv2.imwrite("Test{}.jpg".format(index), img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except Exception as e:
    print('fate erro:{}'.format(e))

cv2.destroyAllWindows()
