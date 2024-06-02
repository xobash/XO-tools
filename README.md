# XO-tools is a collection of python based tools created for me to learn cybersecurity fundamentals. 

# Network Analyzer 
This Python script uses the Scapy library to capture and analyze network packets. It provides functionality to monitor network traffic, extract packet information, and generate statistics about the protocols used.

## Features

- **Packet Capture:** The script captures network packets in real-time using the Scapy library.
- **Packet Analysis:** It parses captured packets to extract information such as source and destination IP addresses, protocol type, packet length, TTL, and flags.
- **Protocol Distribution:** The script generates a bar chart showing the distribution of protocols in the captured packets.

## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)

## Usage

1. Clone the repository or download the script `XONTA.py`.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Activate the virtual environment (if applicable): `source .venv/bin/activate`.
4. Run the script: `python XONTA.py`.
5. Monitor the console output for packet information.
6. View the generated protocol distribution chart.

## Customization

- **Packet Filtering:** You can customize the packet filtering criteria by modifying the `filter` parameter in the `sniff()` function call.
- **Analysis:** Extend the script to perform additional analysis on captured packets, such as detecting suspicious activity or specific network protocols.

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Scapy library for packet manipulation and analysis.
- Matplotlib for generating the protocol distribution chart.

## Authors

- XObash
