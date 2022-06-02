"""
Buzzer-HID to OSC (buzzerhid2osc)
Copyright 2022, Eric Kirchheim

Description:
Converts HID keypresses of "Buzzersystem Quattro"
to OSC-Commands for two Servers

Version 1.2

Config-VAR: buzzthru -> rebuild locking-logic in script or pass thru Buzzer 1-4
"""


from pynput import keyboard
from pythonosc.udp_client import SimpleUDPClient

# configuration for OSC-Client (sending only)
# QLab
ip1 = "192.168.10.102"  # IP of server 1
port1 = 53000  # Listening-Port of server 1
client1 = SimpleUDPClient(ip1, port1)  # Create client 1

# CasparCG
ip2 = "127.0.0.1"  # IP of server 2
port2 = 53000  # Listening-Port of server 2
client2 = SimpleUDPClient(ip2, port2)  # Create client 2

# Config-VAR: Rebuild logic in script or pass thru
buzzthru = False


# rebuild buzzer state
locked = False
lastbuzz = 0


# method for keypress
def on_press(key):
    global locked
    global lastbuzz
    global buzzthru
    try:
        if key.char == '1':
            print("Buzzer 1")
            if not locked:
                client1.send_message("/cue/buzz1/start", "1")
                client2.send_message("/control/buzz1/play", "1")
                if not buzzthru:
                    locked = True
                    print("Locking on Buzzer 1")
                lastbuzz = 1
                print("Processed Buzz 1")
            else:
                print("Locked by Buzzer " + str(lastbuzz))
        elif key.char == '2':
            print("Buzzer 2")
            if not locked:
                client1.send_message("/cue/buzz2/start", "1")
                client2.send_message("/control/buzz2/play", "1")
                if not buzzthru:
                    locked = True
                    print("Locking on Buzzer 2")
                lastbuzz = 2
                print("Processed Buzz 2")
            else:
                print("Locked by Buzzer " + str(lastbuzz))
        elif key.char == '3':
            print("Buzzer 3")
            if not locked:
                client1.send_message("/cue/buzz3/start", "1")
                client2.send_message("/control/buzz3/play", "1")
                if not buzzthru:
                    locked = True
                    print("Locking on Buzzer 3")
                lastbuzz = 3
                print("Processed Buzz 3")
            else:
                print("Locked by Buzzer " + str(lastbuzz))
        elif key.char == '4':
            print("Buzzer 4")
            if not locked:
                client1.send_message("/cue/buzz4/start", "1")
                client2.send_message("/control/buzz4/play", "1")
                if not buzzthru:
                    locked = True
                    print("Locking on Buzzer 4")
                lastbuzz = 4
                print("Processed Buzz 4")
            else:
                print("Locked by Buzzer " + str(lastbuzz))
        elif key.char == '5':
            print("Reset")
            client1.send_message("/cue/buzzreset/start", "1")
            client2.send_message("/ccontrol/buzzreset/play", "1")
            locked = False
            print("Processed Reset")
        elif key.char == '6':
            print("lock")
            client1.send_message("/cue/buzzlock/start", "1")
            client2.send_message("/control/buzzlock/play", "1")
            print("Processed Global buzz by system's logic")
    except AttributeError:
        print('No valid alphanumeric key: {0}'.format(key.char))


# Collect events
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
