from pynput import keyboard
from pythonosc.udp_client import SimpleUDPClient

# configuartion for OSC-Client (sending only)
ip1 = "192.168.0.29"  # IP of Server
port1 = 53000  # Listening-Port of server
client1 = SimpleUDPClient(ip1, port1)  # Create client 1

# rebuild buzzer state
locked = False
lastbuzz = 0


# method for keypress
def on_press(key):
    global locked
    global lastbuzz
    try:
        if key.char == '1':
            print("Buzzer 1")
            if not locked:
                client1.send_message("/cue/hid1/start", "1")
                locked = True
                lastbuzz = 1
            else:
                print("Locked by Buzzer " + str(lastbuzz))
        elif key.char == '2':
            print("Buzzer 2")
            if not locked:
                client1.send_message("/cue/hid2/start", "1")
                locked = True
                lastbuzz = 2
            else:
                print("Locked by Buzzer " + str(lastbuzz))
        elif key.char == '3':
            print("Buzzer 3")
            if not locked:
                client1.send_message("/cue/hid3/start", "1")
                locked = True
                lastbuzz = 3
            else:
                print("Locked by Buzzer " + str(lastbuzz))
        elif key.char == '4':
            print("Buzzer 4")
            if not locked:
                client1.send_message("/cue/hid4/start", "1")
                locked = True
                lastbuzz = 4
            else:
                print("Locked by Buzzer " + str(lastbuzz))
        elif key.char == '5':
            print("Reset")
            client1.send_message("/cue/hid5/start", "1")
            locked = False
        elif key.char == '6':
            print("lock")
            client1.send_message("/cue/hid6/start", "1")
        else:
            print('No valid alphanumeric key: {0}'.format(key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))


# Collect events
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
