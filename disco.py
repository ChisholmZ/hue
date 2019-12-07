#!/usr/bin/python
import argparse, random
from phue import Bridge
from time import sleep

parser = argparse.ArgumentParser()

parser.add_argument('--group', '-G', help='Hue Light Group', type=int, default=1)
parser.add_argument('--duration', '-D', help='Duration of color in seconds', type=int, default=2)

args = parser.parse_args()

b = Bridge()

lights = b.get_light_objects('id')
group = b.get_group(args.group,'lights')
i=0

# change colors
def color():
    for l in group:
        lights[int(l)].xy = [random.random(),random.random()]
    sleep(args.duration)

# loop endlessly
while True:
    color()
