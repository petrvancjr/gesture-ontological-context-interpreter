#!/usr/bin/env python

import sys
import rospy
from knowrob.srv import TellQuery, TellQueryRequest
from knowrob.msg import TripleStatement
import time

def add(q):
    rospy.wait_for_service('/rosprolog/tell')
    try:
        add_proxy = rospy.ServiceProxy('/rosprolog/tell', TellQuery)
        resp1 = add_proxy(q)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def test():
    q = TellQueryRequest()

    t = TripleStatement()
    t.subject =  "http://www.ease-crc.org/ont/ciirc-gestures#PandaRobot"
    t.property = "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent"
    t.object =   "http://www.ease-crc.org/ont/ciirc-gestures#PandaGripper"
    t.startTime = time.time()
    t.endTime = time.time()

    q.statements = [t]
    q.reasoner = 'mongolog1'
    print(f"Requesting {q}")
    print(f"Result: {add(q)}")

if __name__ == "__main__":
    test()

