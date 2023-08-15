import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
from pygame import mixer
import os
from sclib import SoundcloudAPI, Track, Playlist
cap = cv2.VideoCapture(0)


classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

offset = 20
imgSize = 300

counter = 0

labels = ["50% volume", "max", "mute", "previous", "pause/play", "next"]

#initialize
mixer.init()
api = SoundcloudAPI()
dir = './Playlist'
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.85)#0.9)

#empty files in playlist folder
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
    
#ask user for soundcloud playlist link 
user_playlist = input("\n\nenter soundcloud playlist link: \n")

#download playlist into Playlist folder:
print("loading playlist ...")
playlist = api.resolve(user_playlist)
i = 0
for track in playlist.tracks:
    filename = f'./Playlist/{i}.mp3'
    i = i+1
    with open(filename, 'wb+') as file:
        track.write_mp3_to(file)
print("all done!")


#create playlist list (list of the file names)
playList = []
dir = './Playlist'
for f in os.listdir(dir):
    playList.append(f)

#load first song of playlist into player
index = 0
mixer.music.load("./Playlist/" + playList[index])
###########################################################################################

switch = 1

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    var = 0
    
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, indexx = classifier.getPrediction(imgWhite, draw=False)
            print(labels[indexx])



        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, indexx = classifier.getPrediction(imgWhite, draw=False)
            print(labels[indexx])
        
        #play
        if indexx == 4 and switch == 1:
            mixer.music.play()
            switch = 0
            var = 1
            print("play")
            
        elif indexx == 4 and switch == 0:
            mixer.music.pause()
            switch = 1
            var = 1
            print("pause")
                    
        #previous (thumbs up)
        elif indexx == 3:
            var = 1
            if index == 0:
                index = (len(playList)-1)
                mixer.music.load("./Playlist/" + playList[index])
                mixer.music.play()
                #print(playList[index])
                #box(indexx, imgOutput)
                #time.sleep(1)
            else: 
                index = index - 1
                mixer.music.load("./Playlist/" + playList[index])
                mixer.music.play() 
                #print(playList[index])
                #box(indexx, imgOutput)
           
        #next (thumbs down)
        elif indexx == 5:
            var = 1
            if index == (len(playList)-1):
                index = 0
                mixer.music.load("./Playlist/" + playList[index])
                mixer.music.play()
                print(playList[index])

            else: 
                index = index+1
                mixer.music.load("./Playlist/" + playList[index])
                mixer.music.play()
                print(playList[index])

        #mute
        elif indexx == 2:
            var = 1
            mixer.music.set_volume(0)
            #time.sleep(1) 
        #20% volume
        elif indexx == 0:
            var = 1
            mixer.music.set_volume(0.2)
        #max volume
        elif indexx == 1:
            var = 1
            mixer.music.set_volume(1) 
            #time.sleep(1) 


        #box(indexx, imgOutput)
        cv2.rectangle(imgOutput, (x - offset, y - offset-50),
                      (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, labels[indexx], (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x-offset, y-offset),
                      (x + w+offset, y + h+offset), (255, 0, 255), 4)
        cv2.imshow("Image", imgOutput)
        
    cv2.imshow("Image", imgOutput)

    cv2.waitKey(1)

    if var == 1:
        cv2.waitKey(1000)
        
    

    
    

