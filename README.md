# XO-tools is a collection of python based tools created for me to learn cybersecurity fundamentals. 

# Network Analyzer 
This Python script uses the Scapy library to capture and analyze network packets. It provides functionality to monitor network traffic, extract packet information, and generate statistics about the protocols used.

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

# System Information and CVE Vulnerability Search
This script gathers system information using the `platform` module and searches for CVE vulnerabilities related to the Linux kernel using the CIRCL CVE database API.

## Usage

1. Make sure you have Python installed on your system.
2. Install the `requests` module if you haven't already:
    ```bash
    pip install requests
    ```
3. Copy the code from `system_info_cve_search.py` into a Python file on your system.
4. Run the Python script:
    ```bash
    python your_script_name.py
    ```

## Description

The script does the following:

- Gathers system information such as OS, release, version, machine, and processor using the `platform` module.
- Searches for CVE vulnerabilities related to the Linux kernel using the CIRCL CVE database API.


## Features

- **Packet Capture:** The script captures network packets in real-time using the Scapy library.
- **Packet Analysis:** It parses captured packets to extract information such as source and destination IP addresses, protocol type, packet length, TTL, and flags.
- **Protocol Distribution:** The script generates a bar chart showing the distribution of protocols in the captured packets.

## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)
- pycvesearch (`pip install pycvesearch`)
- platform (`pip install platform`)
- requests (`pip install requests`)

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Scapy library for packet manipulation and analysis.
- Matplotlib for generating the protocol distribution chart.

## Authors

- XObash
