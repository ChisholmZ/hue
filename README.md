## Hue Scripts

first install phue library `pip install phue`

then click the connect button on your hue bridge and run
`connect.py --ip YOUR_HUB_IP_ADDRESS`

this will set up a config file so that the phue library to be able to connect to the hub from here on out.

### Christmas Script

run `xmas.py --group 1 --duration 1`

this will alternate all of the lights in the group 1 between red and green with a duration of 1 second before changing.
