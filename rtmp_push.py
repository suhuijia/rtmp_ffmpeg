# coding=utf-8
import cv2
import time
import numpy as np
import subprocess as sp

rtmpUrl = 'rtmp://192.168.46.111:1935/live'

camera = cv2.VideoCapture(0)
if (camera.isOpened()):
    print('Open camera')
else:
    print('Fail to open camera!')

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 2560x1920 2217x2217 2952×1944 1920x1080
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camera.set(cv2.CAP_PROP_FPS, 10)

size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
sizeStr = str(size[0]) + 'x' + str(size[1])
fps = camera.get(cv2.CAP_PROP_FPS)  # 30p/self
hz = int(1000.0 / fps)
print('size:'+ sizeStr + ' fps:' + str(fps) + ' hz:' + str(hz))

command = ['ffmpeg',
    '-y',
    '-f', 'rawvideo',
    '-vcodec','rawvideo',
    '-pix_fmt', 'bgr24',
    '-s', sizeStr,
    '-r', str(fps),
    '-i', '-',
    '-c:v', 'libx264',
    # '-pix_fmt', 'yuv420p',
    '-preset', 'ultrafast',
    '-f', 'flv',
    rtmpUrl]


pipe = sp.Popen(command, stdin=sp.PIPE) #,shell=False

count = 0

while True:
    count = count + 1
    ret, frame = camera.read()
    if not ret:
        break

    # 绘制推送图片帧信息
    fpsshow = "Fps  :" + str(int(fps)) + "  Frame:" + str(count)
    nframe  = "Play :" + str(int(count / fps))
    ntime   = "Time :" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cv2.putText(frame, ntime, (40, 50), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    pipe.stdin.write(frame.tostring())

    pass

camera.release()

print("Over!")

