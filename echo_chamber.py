from scapy.all import rdpcap, ICMP

final_bytes = b""
pcap_file = "echo_chamber.pcap"
packets = rdpcap(pcap_file)

for i, packet in enumerate(packets):
    # As replies are the same as requests...
    if i % 2 == 0:
        continue
    if ICMP in packet:
        final_bytes += bytes(packet[ICMP].payload)[16:17]

with open("output.png", "wb") as outfile:
    outfile.write(final_bytes)
