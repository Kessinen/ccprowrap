from subprocess import run
from argparse import ArgumentParser

def getCPUTemp():
    #TODO Add logic
    return 0

def changeFanSpeed(fans, speed):
    for fan in fans:
        #FIXME Check if fans is a integer array and speed is integer between 0 and 100
        if not 0 <= speed <= 100:
            #TODO Add logger
            print("ERROR: invalid speed. Must be between 1 - 100")
        cmd = f'liquidctl set fan{fan} speed {speed}'
    #TODO Add logic
    pass

def listFans():
    return None

argparser = ArgumentParser(description="Spin that fan!\nHelper for liquidctl")
argparser.add_argument("fanspeed",help="Set fan speed as percent (0-100)", type=int)

args = argparser.parse_args()