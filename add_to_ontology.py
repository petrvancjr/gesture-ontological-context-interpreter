#!/usr/bin/env python

import sys
import rospy
from knowrob.srv import TellQuery, TellQueryRequest
from knowrob.msg import TripleStatement
import time

def add_triplet(s, p, o):
    q = TellQueryRequest()
    t = TripleStatement()
    t.subject = s
    t.property = p
    t.object = o
    t.startTime = time.time()
    t.endTime = time.time()

    q.statements = [t]
    q.reasoner = 'mongolog1'
    print(f"Requesting {q}")

    rospy.wait_for_service('/rosprolog/tell')
    try:
        add_proxy = rospy.ServiceProxy('/rosprolog/tell', TellQuery)
        resp1 = add_proxy(q)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        resp1 = False
    print(f"Result: {resp1}")


def test():
    add_triplet("http://www.ease-crc.org/ont/ciirc-gestures#PandaRobot", \
                "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent", \
                "http://www.ease-crc.org/ont/ciirc-gestures#PandaGripper")

    add_triplet("http://www.ease-crc.org/ont/ciirc-gestures#Mug", \
                "http://www.ease-crc.org/ont/SOMA.owl#isOntopOf", \
                "http://www.ease-crc.org/ont/ciirc-gestures#Table")
    
    add_triplet("http://www.ease-crc.org/ont/ciirc-gestures#MustardBottle", \
                "http://www.ease-crc.org/ont/SOMA.owl#isOntopOf", \
                "http://www.ease-crc.org/ont/ciirc-gestures#Mug")
    
    add_triplet("http://www.ease-crc.org/ont/ciirc-gestures#Mug", \
                "http://www.ease-crc.org/ont/SOMA.owl#hasColor", \
                "http://www.ease-crc.org/ont/ciirc-gestures#Blue")

    add_triplet("http://www.ease-crc.org/ont/ciirc-gestures#Table", \
                "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasQuality", \
                "http://www.ease-crc.org/ont/ciirc-gestures#LargeSize")



if __name__ == "__main__":
    test()

