from subprocess import run
from argparse import ArgumentParser
import logging

#TODO check fanlist
allFans = [1,2,3,4,5,6]

def getCPUTemp():
    #TODO Add logic
    return 0

def changeFanSpeed(fans, speed):
    
    if len(fans) == 0:
        return False
    logging.info(f'Trying to set the speed of fans {str(fans)}')
    for fan in fans:
        if not 0 <= int(speed) <= 100:
            #TODO Add logger
            logging.error("invalid speed. Must be between 1 - 100")
            return False
        cmd = f'liquidctl set fan{str(fan)} speed {speed}'.split(" ")
        try:
            run(cmd)
        except FileNotFoundError:
            logging.critical("liquidctl not found. Is it installed?")
            exit(1)

def listFans():
    #TODO Add logic
    return None

argparser = ArgumentParser(description="Spin that fan!\nHelper for liquidctl")
argparser.add_argument("-f", "--fanspeed", metavar="int", help="Set fan speed as percent (0-100)", type=int, required=True)
argparser.add_argument("-v", "--verbose", action='store_true')

args = argparser.parse_args()

loglevel = logging.INFO if args.verbose else logging.WARNING
logging.basicConfig(level=loglevel)

try:
    logging.info("Trying to initialize liquidctl")
    run('liquidctl initialize all'.split(" "))
except FileNotFoundError:
    logging.critical("liquidctl not found. Is it installed?")
    exit(1)
    
changeFanSpeed(allFans, args.fanspeed)