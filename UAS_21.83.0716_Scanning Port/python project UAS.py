from scapy.all import *

# IP address yang akan di scan
ip = "192.168.1.1"

# Melakukan skanning port pada jaringan
def scan(ip):
    # Membuat paket TCP
    pkt = IP(dst=ip)/TCP(dport=(1,1024), flags="S")
    # Mengirim dan menerima paket
    res = sr1(pkt, timeout=10, verbose=0)
    # Menampilkan hasil skanning
    if res:
        print(res[TCP].sport, "is open")
    else:
        print("Closed")

# Melakukan skanning pada semua port dari 1-1024
for i in range(1,1025):
    scan(ip)
