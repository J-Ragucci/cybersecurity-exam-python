from scapy.all import IP, UDP
ip = IP(dst="192.168.1.24")
udp = UDP(sport=12345, dport=80)
packet = ip/udp
packet.show()