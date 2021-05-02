'''FYP GUI Demo'''
# pylint: disable=line-too-long,no-member

import random
import subprocess
import sys
from platform import system

import eel

# Initialise eel and specifiy the location of the webroot folder
eel.init('web')

# Run using Chromium if on Linux, use ChromeDriver on Windows
if system() == 'Linux':
    eel.start('index.html', block=False, size=(800, 600), mode='custom',
              cmdline_args=['chromium-browser', '--kiosk', '--incognito', '--disable-pinch',
                            '--overscroll-history-navigation=0', 'http://localhost:8000/index.html'])
else:
    eel.start('index.html', block=False, size=(800, 600),
              cmdline_args=['--kiosk', '--incognito', '--disable-pinch',
                            '--overscroll-history-navigation=0', 'http://localhost:8000/index.html'])


@eel.expose
def get_speed():
    '''Return a random value for Speed'''
    return random.randint(0, 100)


@eel.expose
def get_rpm():
    '''Return a random value for RPM'''
    return random.randint(1800, 3500)


@eel.expose
def close_program():
    '''Method to cleanly exit, exposed via eel so can be called from JS'''
    print('Close python')
    sys.exit(0)


@eel.expose
def pi_power(mode):
    '''Method to handle shutting down or rebooting a Raspberry Pi'''
    accepted = ['shutdown', 'reboot']

    # Only run the command if it is in the above list
    if mode in accepted:
        subprocess.run(["sudo", mode, "now"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        close_program()


# Main Program Loop
while True:
    eel.sleep(0.5)
    # Call the updateGauges function (defined in JS) passing in speed and RPM values
    eel.updateGauges(get_speed(), get_rpm())
