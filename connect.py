#!/usr/bin/python3
import random, argparse
from phue import Bridge

parser = argparse.ArgumentParser()

parser.add_argument('--ip', '-IP', help='IP of Hue Bridge', type=str, required=True)

args = parser.parse_args()

b = Bridge(args.ip)

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()
