import os
import argparse
import zmq
import json
import pickle
import sys
import time


addr = 'localhost'
context = zmq.Context()
poller = zmq.Poller()

can = context.socket(zmq.SUB)
can.connect("tcp://localhost:%d" % (8006))
can.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(can, zmq.POLLIN)
carState = context.socket(zmq.SUB)
carState.connect("tcp://localhost:%d" % (8021))
carState.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(carState, zmq.POLLIN)
plan = context.socket(zmq.SUB)
plan.connect("tcp://localhost:%d" % (8024))
plan.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(plan, zmq.POLLIN)
carControl = context.socket(zmq.SUB)
carControl.connect("tcp://localhost:%d" % (8023))
carControl.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(carControl, zmq.POLLIN)
live20 = context.socket(zmq.SUB)
live20.connect("tcp://localhost:%d" % (8012))
live20.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(live20, zmq.POLLIN)
l100 = context.socket(zmq.SUB)
l100.connect("tcp://localhost:%d" % (8007))
l100.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(l100, zmq.POLLIN)
liveCalibration = context.socket(zmq.SUB)
liveCalibration.connect("tcp://localhost:%d" % (8019))
liveCalibration.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(liveCalibration, zmq.POLLIN)
liveTracks = context.socket(zmq.SUB)
liveTracks.connect("tcp://localhost:%d" % (8016))
liveTracks.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(liveTracks, zmq.POLLIN)
model = context.socket(zmq.SUB)
model.connect("tcp://localhost:%d" % (8009))
model.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(model, zmq.POLLIN)
liveMpc = context.socket(zmq.SUB)
liveMpc.connect("tcp://localhost:%d" % (8035))
liveMpc.setsockopt(zmq.SUBSCRIBE, b"")
poller.register(liveMpc, zmq.POLLIN)

while True:
  socks = None
  socks = dict(poller.poll(0.))
  for sock in socks:
    #'''
    if sock is l100:
        temp = json.loads(l100.recv(zmq.NOBLOCK))
        print(temp)
    elif sock is carState:
        #print(" ")
        temp = json.loads(carState.recv(zmq.NOBLOCK))
        print(temp)
    elif sock is plan:
        #print(" ")
        temp = json.loads(plan.recv(zmq.NOBLOCK))
        print(temp)
    elif sock is can:
        #print(" ")
        temp = json.loads(can.recv(zmq.NOBLOCK))
        print(temp)
    elif sock is model:
        #print(" ")
        temp = json.loads(model.recv(zmq.NOBLOCK))
        print(temp)
    elif sock is liveCalibration:
        #print(" ")
        temp = json.loads(liveCalibration.recv(zmq.NOBLOCK))
        print(temp)
    elif sock is carControl:
        #print(" ")
        temp = json.loads(carControl.recv(zmq.NOBLOCK))
        print(temp)
    elif sock is liveTracks:
        #print(" ")
        temp = json.loads(liveTracks.recv(zmq.NOBLOCK))
        print(temp)
    elif sock is liveMpc:
        #print(" ")
        temp = json.loads(liveMpc.recv(zmq.NOBLOCK))
        print(temp)
    else:
      print("skipped")
      time.sleep(0.01)
    '''
    if sock is l100:
        temp = (pickle.loads(l100.recv(zmq.NOBLOCK)))
        print(temp)
    elif sock is carState:
        #print(" ")
        temp = (pickle.loads(carState.recv(zmq.NOBLOCK)))
        print(temp)
    elif sock is plan:
        #print(" ")
        temp = (pickle.loads(plan.recv(zmq.NOBLOCK)))
        print(temp)
    elif sock is can:
        #print(" ")
        temp = (pickle.loads(can.recv(zmq.NOBLOCK)))
        print(temp)
    elif sock is model:
        #print(" ")
        temp = (pickle.loads(model.recv(zmq.NOBLOCK)))
        print(temp)
    elif sock is liveCalibration:
        #print(" ")
        temp = (pickle.loads(liveCalibration.recv(zmq.NOBLOCK)))
        print(temp)
    elif sock is carControl:
        #print(" ")
        temp = (pickle.loads(carControl.recv(zmq.NOBLOCK)))
        print(temp)
    elif sock is liveTracks:
        #print(" ")
        temp = (pickle.loads(liveTracks.recv(zmq.NOBLOCK)))
        print(temp)
    elif sock is liveMpc:
        #print(" ")
        temp = (pickle.loads(liveMpc.recv(zmq.NOBLOCK)))
        print(temp)
    else:
        print("skipped")
        time.sleep(0.01)
    '''
