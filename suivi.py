# Algo suiveur de lignes

#/////////////////////////////////////////////////////////////////////////////
from threading import Timer
import cv2
import numpy as np
#import matplotlib.pylab as plt
import colorsys
from wheel import free_wheel

#Global variables
COLOR = 0
print("COLOR = ", COLOR)
GREEN = 0
TIME = 1
lastcenter = 160

#Initialisation
cap = cv2.VideoCapture(-1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
cap.set(3, 320)
cap.set(4, 180)

#/////////////////////Functions

#Green

def timeout():
    global TIME
    TIME = 1

def pixel_is_green(threevalues):
    h,s,v = threevalues
    if (h>0.24 and h<0.32 and s>0.65):
        return True
    return False

def green_bar_is_detected(src):#Gérer la saturation


    h,w = src.shape[0],src.shape[1]

    total = 0
    for i in range(h):
        for j in range(w):
            rgb = src[i][j]
            if pixel_is_green(colorsys.rgb_to_hsv(rgb[0]/255,rgb[1]/255,rgb[2]/255)):
                total+=1
    res = total/(h*w)
    if (res>0.4):
        return True
    return False

def green_processing(frame):
    global TIME
    global COLOR
    if (green_bar_is_detected(frame) and (TIME==1)) :
        COLOR+=1
        print("COLOR = ", COLOR)
        TIME = 0
        t = Timer(10.0, timeout)
        t.start()

#Following lines

# Function: K Means
# -------------
def kmeans(dataSet, k, MAX_ITERATIONS=2):

    centroids = getRandomCentroids(dataSet, k)
    iterations = 0
    oldCentroids = None

    while not shouldStop(oldCentroids, centroids, iterations, MAX_ITERATIONS):
        oldCentroids = centroids
        iterations += 1
        labels = getLabels(dataSet, centroids)
        centroids = getCentroids(dataSet, labels, k)

    return centroids#, labels

# Function: getRandomCentroids
# -------------
# Initialize centroids by choosing randomly k points from the dataset
def getRandomCentroids(dataSet, numClusters):
    numPoints, _ = dataSet.shape
    centroids = dataSet[np.random.randint(numPoints, size =  numClusters), :]
    return centroids

# Function: shouldStop
# -------------
# Returns True or False if k-means if the maximum number of iterations is reached
# or if the centroids do not change anymore
def shouldStop(oldCentroids, centroids, iterations, MAX_ITERATIONS):
    return iterations == MAX_ITERATIONS
    #centroids == oldCentroids or

# Function: getLabels
# -------------
# Returns the label for each point in the dataSet. The label is the one of the closest centroid
def getLabels(dataSet, centroids):
    dataSet_row = dataSet.shape[0]
    centroids_row = centroids.shape[0]
    labels = np.zeros(dataSet_row)
    for i in range (dataSet_row):
        min_range = np.linalg.norm(dataSet[i]-centroids[0])
        labels[i] = 0
        for k in range (1,centroids_row):
            if (np.linalg.norm(dataSet[i]-centroids[k]) < min_range):
                min_range = np.linalg.norm(dataSet[i]-centroids[k])
                labels[i] = k
    return labels

# Function: getCentroids
# -------------
# Returns the centroids of the clusters. Each centroid is the geometric mean of the points that
# have that centroid's label. Important: If a centroid is empty (no points have
# that centroid's label) you should randomly re-initialize it.
def getCentroids(dataSet, labels, k):
    dataSet_col = dataSet.shape[1]
    labels_row = labels.shape[0]
    centroids = np.zeros((k,dataSet_col))
    for i in range (k):
        for h in range (dataSet_col):
            list = []
            for j in range (labels_row):
                if (labels[j] == i):
                    list.append(dataSet[j][h])
            if (len(list) == 0):
                centroids[i][h]=-1
            else:
                centroids[i][h] = sum(list)/len(list)
    return centroids

#Pixels

def color_pixel_coord(frame):
    global COLOR
    h,w = frame.shape[0]//2,frame.shape[1]//2
    L = []
    if (COLOR == 0):
        for i in range(0, h, 2):
            for j in range(0, w, 2):
                rgb = frame[i][j]
                hvalue,s,v = colorsys.rgb_to_hsv(rgb[0]/255,rgb[1]/255,rgb[2]/255)
                if ((hvalue<0.56) and (hvalue>0.50) and (s>0.7)):
                    L.append([i,j])
    if (COLOR == 1):
        for i in range(0, h, 2):
            for j in range(0, w, 2):
                rgb = frame[i][j]
                hvalue,s,v = colorsys.rgb_to_hsv(rgb[0]/255,rgb[1]/255,rgb[2]/255)
                if ((hvalue<0.10) and (hvalue>0.04) and (s>0.7)):
                    L.append([i,j])
    if (COLOR == 2):
        for i in range(0, h, 2):
            for j in range(0, w, 2):
                rgb = frame[i][j]
                hvalue,s,v = colorsys.rgb_to_hsv(rgb[0]/255,rgb[1]/255,rgb[2]/255)
                if ((hvalue<0.68) and (hvalue>0.64) and (s>0.7)):
                    L.append([i,j])
    return np.array(L)

#Behavior

def behavior(centers,lastcenter):
    destination = 0
    distance = abs(centers[0][1]-centers[1][1])
    if (distance>80):
        if (abs(centers[0][1]-lastcenter) < abs(centers[1][1]-lastcenter)):
            destination = centers[0][1]
        else:
            destination = centers[1][1]
    else:
        destination = (centers[0][1] + centers[1][1])/2
#Test
    print("Destination: ",destination,"\n")
    if (destination>160):
        print("Tourner à droite")
    else:
        print("Tourner à gauche")
#EO Test
    return destination

def get_current_color():
    return COLOR

def get_distance_suivi():
    global lastcenter

    ret, frame = cap.read()
    frame = frame[160:]
    green_processing(frame)
    dataset = color_pixel_coord(frame)

    if (len(dataset)>0):
        centers = kmeans(dataset,2)
        lastcenter = behavior(centers,lastcenter)
#Testing
       # cv2.circle(frame,(int(centers[0][1]),int(centers[0][0])),1,(255,0,255),3)
       # cv2.circle(frame,(int(centers[1][1]),int(centers[1][0])),1,(255,0,255),3)
    #print("COLOR = ",COLOR,"\n")
    #cv2.imshow("Frame", frame)

    return lastcenter
#EO Testing

        # key = cv2.waitKey(1)
        # if key==50:
            
        #     break

#///////////////////Run
# while True:
#     ret, frame = cap.read()
#     src = frame[160:]
#     green_processing(frame)
#     dataset = color_pixel_coord(frame)

#     if (len(dataset)>0):
#         centers = kmeans(dataset,2)
#         lastcenter = behavior(centers,lastcenter)

# #Testing
#         cv2.circle(src,(int(centers[0][1]),int(centers[0][0])),1,(255,0,255),3)
#         cv2.circle(src,(int(centers[1][1]),int(centers[1][0])),1,(255,0,255),3)
#     print("COLOR = ",COLOR,"\n")
#     cv2.imshow("Frame", src)
# #EO Testing

#     key = cv2.waitKey(1)
#     if key==50:
#         break

# #Ending
def end_camera():
    free_wheel()
    cap.release()
    cv2.destroyAllWindows()
