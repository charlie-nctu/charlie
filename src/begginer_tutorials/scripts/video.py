#!/usr/bin/env python
import rospy
from darknet_ros_msgs.msg import BoundingBoxes

def callback(data):
    for ans in data.bounding_boxes:
        if ans.Class == 'person':
            xcenter = (ans.xmin + ans.xmax)//2
            ycenter = (ans.ymin + ans.ymax)//2
            print (xcenter,ycenter)
    
def get():

    rospy.init_node('me', anonymous=True)

    rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes , callback)

    rospy.spin()

if __name__ == '__main__':
    get()


