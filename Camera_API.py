from requests import get 
import json
import pprint
from picamera import camera
from time import sleep

clima = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'
my_log = -22.007805
my_lat = -47.898677
my_clima = get(clima).json()['items']
pprint.pprint(my_clima)

#Controle da câmera

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/sel/max.jpg')
camera.stop_preview()