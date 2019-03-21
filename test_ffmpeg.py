import av
# import av.datasets
import cv2



container = av.open('res_mv123.avi')

# Signal that we only want to look at keyframes.
stream = container.streams.video[0]
stream.codec_context.skip_frame = 'NONKEY'

for frame in container.decode(stream):

    print(frame)

    # We use `frame.pts` as `frame.index` won't make must sense with the `skip_frame`.
    # frame.to_image().save('night-sky.{:04d}.jpg'.format(frame.pts), quality=80,)
    image = frame.to_nd_array(format='bgr24')
    cv2.imshow('test', image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()



# open input and find video stream
# input_container = av.open('/dev/video0', 'r')
input_container = av.open("res_mv123.avi", 'r')
# input_container.streams.video[0].thread_type = 'AUTO'
input_stream = input_container.streams.get(video=0)[0]

# open output and add a video stream
# output_container = av.open('rtmp://192.168.46.159:2016/hls_alic/film', 'w', format='flv')
output_container = av.open('rtmp://192.168.46.111:1935/live', 'w', format='flv')
output_stream = output_container.add_stream('libx264', rate=input_stream.rate)


for frame in input_container.decode(input_stream):
    # perform edge detection
    img = frame.to_ndarray(format='bgr24')
    cv2.imshow('img', img)
    cv2.waitKey(1)
    # img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

    # rebuild a VideoFrame, preserving timing information
    new_frame = av.VideoFrame.from_ndarray(img, format='bgr24')
    new_frame.pts = frame.pts
    new_frame.time_base = frame.time_base

    # encode and mux
    for packet in output_stream.encode(new_frame):
       output_container.mux_one(packet)

# flush and close output
# for packet in output_stream.encode(None):
#     output_container.mux(packet)
# output_container.close()

