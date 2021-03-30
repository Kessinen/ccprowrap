from subprocess import run
from argparse import ArgumentParser

#TODO check fanlist
allFans = [1,2,3,4,5,6]

def getCPUTemp():
    #TODO Add logic
    return 0

def changeFanSpeed(fans, speed):
    
    if len(fans) == 0:
        return False
    print(f'Trying to set the speed of fans {str(fans)}')
    for fan in fans:
        if not 0 <= int(speed) <= 100:
            #TODO Add logger
            print("ERROR: invalid speed. Must be between 1 - 100")
            return False
        cmd = f'liquidctl set fan{str(fan)} speed {speed}'.split(" ")
        try:
            run(cmd)
        except FileNotFoundError:
            print("liquidctl not found. Is it installed?")
            exit(1)

def listFans():
    #TODO Add logic
    return None

argparser = ArgumentParser(description="Spin that fan!\nHelper for liquidctl")
argparser.add_argument("fanspeed",help="Set fan speed as percent (0-100)", type=int)

args = argparser.parse_args()
try:
    run('liquidctl initialize all'.split(" "))
except FileNotFoundError:
    print("liquidctl not found. Is it installed?")
    exit(1)
changeFanSpeed(allFans, args.fanspeed)