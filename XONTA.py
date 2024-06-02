from scapy.all import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Define global variables for traffic statistics
packet_count = 0
protocols_count = {}

# Packet capture and parsing
def packet_callback(packet):
    global packet_count, protocols_count

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        # Additional packet details
        length = len(packet)
        ttl = packet[IP].ttl
        flags = packet[IP].flags
        
        # Print packet information
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}, Length: {length}, TTL: {ttl}, Flags: {flags}")

        # Increment packet count
        packet_count += 1
        
        # Update protocol count
        if protocol in protocols_count:
            protocols_count[protocol] += 1
        else:
            protocols_count[protocol] = 1

        # Protocol-specific analysis
        if TCP in packet:
            # Analyze TCP packets
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            flags = packet[TCP].flags
            seq_num = packet[TCP].seq
            ack_num = packet[TCP].ack
            print(f"TCP Packet: Source Port: {src_port}, Destination Port: {dst_port}, Flags: {flags}, Seq: {seq_num}, Ack: {ack_num}")

            # Add detection rules for suspicious TCP activity (e.g., port scanning, SYN floods, etc.)

        if UDP in packet:
            # Analyze UDP packets
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"UDP Packet: Source Port: {src_port}, Destination Port: {dst_port}")

            # Add detection rules for suspicious UDP activity

        # Add analysis for other protocols as needed

# Sniff packets and call the callback function for each packet
sniff(prn=packet_callback, filter="ip", count=10)

# Generate protocol distribution chart
def generate_protocol_chart():
    labels = [str(protocol) for protocol in protocols_count.keys()]
    counts = list(protocols_count.values())
    plt.bar(labels, counts)
    plt.xlabel('Protocol')
    plt.ylabel('Packet Count')
    plt.title('Protocol Distribution')
    plt.show()

# Generate and display protocol distribution chart
generate_protocol_chart()