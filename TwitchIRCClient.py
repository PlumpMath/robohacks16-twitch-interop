import socket

# Configuration
HOST = "irc.twitch.tv"
NICK = "YOUR NICKNAME"
PORT = 6667
PASS = "YOUR TWITCH OAUTH KEY HERE"
CHAN = "YOUR CHANNEL NAME HERE ex: #general"
readbuffer = ""
MODT = True

# Twitch socket
twitch_socket = socket.socket()
twitch_socket.connect((HOST, PORT))
twitch_socket.send(("PASS " + PASS + "\r\n").encode('utf-8'))
twitch_socket.send(("NICK " + NICK + "\r\n").encode('utf-8'))
twitch_socket.send(("JOIN " + CHAN + "\r\n").encode('utf-8'))

# Raspberry Pi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('YOUR RASPBERRY PI IP ADDRESS', 'THE RASPBERRY PI PORT'))

# Send a command to the pi
def send_to_pi(message):
    sock.send(message.encode())
    print("Command " + message + " has been sent")


# Twitch socket loop
while True:
    readbuffer = readbuffer + (twitch_socket.recv(1024)).decode()
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        if (line[0] == "PING"):
            twitch_socket.send("PONG %s\r\n" % line[1])
        else:
            parts = str.split(line, ":")
            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""

                usernamesplit = str.split(parts[1], "!")
                username = usernamesplit[0]

                if MODT:
                    # Commands for the pi here. You can parse the message the way you want

                    if message.lower() == "stop" or message.lower() == "s":
                        send_to_pi("STOP")

                    if message.lower() == "left" or message.lower() == "l":
                        send_to_pi("LEFT")

                    if message.lower() == "right" or message.lower() == "r":
                        send_to_pi("RIGHT")

                    if message.lower() == "forward" or message.lower() == "f":
                        send_to_pi("FORWARD")

                    if message.lower() == "jump" or message.lower() == "j":
                        send_to_pi("JUMP")

                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True

sock.close()
