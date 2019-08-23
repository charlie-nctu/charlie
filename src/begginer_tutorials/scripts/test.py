#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist

velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
PI = 3.1415926535897

def decide(goal):
    rospy.init_node('robot_cleaner', anonymous=True)

    if goal == 0:
	rotate(90)
        move(2)
        rotate(90)
        move(2)
        rotate(90)
        move(1)
        rotate(90)
        move(2)
        rotate(90)
        move(1)
    elif goal == 1:
        rotate(90)
        move(2)
    elif goal == 2:
        move(1)
        rotate(-90)
        move(1)
        rotate(-90)
        move(1)
        rotate(90)
        move(1)
        rotate(90)
        move(1)
    elif goal == 3:
        move(1)
        rotate(-90)
        move(1)
        rotate(-90)
        move(1)
        rotate(180)
        move(1)
        rotate(-90)
        move(1)
        rotate(-90)
        move(1)
    elif goal == 4:
        rotate(-90)
        move(1)
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(180)
        move(2)
    elif goal == 5:
        rotate(180)
        move(1)
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(-90)
        move(1)
        rotate(-90)
        move(1)
    elif goal == 6:
        rotate(180)
        move(1)
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(-90)
        move(1)
        rotate(-90)
        move(1)
        rotate(-90)
        move(1)
    elif goal == 7:
        move(1)
        rotate(-90)
        move(2)
    elif goal == 8:
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(-90)
        move(1)
        rotate(-90)
        move(1)
        rotate(-90)
        move(1)
    elif goal == 9:
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(90)
        move(1)
        rotate(-90)
        move(1)
        
def rotate(num):

    vel_msg = Twist()
    

    angular_speed = 15*2*PI/360
    relative_angle = abs(num*2*PI/360)

    if num > 0:
        vel_msg.angular.z = abs(angular_speed)
    else:
        vel_msg.angular.z = -abs(angular_speed)


    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0


    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

    vel_msg.angular.z = 0

def move(distance):

    vel_msg = Twist()

    vel_msg.linear.x = 0.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0



    t0 = rospy.Time.now().to_sec()
    current_distance = 0


    while(current_distance < distance):

        velocity_publisher.publish(vel_msg)

        t1=rospy.Time.now().to_sec()
 
        current_distance= 0.5*(t1-t0)

    vel_msg.linear.x = 0


if __name__ == '__main__':
    try:
	num = int(sys.argv[1])
        decide(num)
    except rospy.ROSInterruptException:
        pass
