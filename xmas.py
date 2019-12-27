#!/usr/bin/python3
import argparse
from phue import Bridge
from time import sleep

parser = argparse.ArgumentParser()

parser.add_argument('--group', '-G', help='Hue Light Group', type=int, default=1)
parser.add_argument('--duration', '-D', help='Duration of color in seconds', type=int, default=2)
parser.add_argument('--brightness', '-B', help='Brightness 0 - 254', type=int, default=254)

args = parser.parse_args()

b = Bridge()

green = [0.1856, 0.6045]
red = [0.5654, 0.3068]
lights = b.get_light_objects('id')
group = b.get_group(args.group,'lights')
i=0

# change colors
def color(color1, color2):
    for l in group:
        lights[int(l)].on = True
        lights[int(l)].brightness = args.brightness
        lights[int(l)].xy = color1 if (int(l) % 2) == 0 else color2
    sleep(args.duration)

# loop endlessly
while True:
    if (i % 2) == 0:
        color(red, green)
    else:
        color(green, red)
    i+=1
