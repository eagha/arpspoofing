import scapy.all as scapy


def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=processsniffed)

def processsniffed(packet):
    print(packet)

sniff("Qualcomm Atheros QCA9377 Wireless Network Adapter")
    
