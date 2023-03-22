# Pcap-Analyser
This GitHub repository contains a set of Python programs that are designed to analyze PCAP files for potential security threats. The repository consists of Four programs, each of which is designed to perform a specific task related to analyzing PCAP files.
PCAP File Analysis Tool
This is a set of Python programs designed to analyze PCAP files for potential security threats. The repository consists of six programs, each of which is designed to perform a specific task related to analyzing PCAP files.

Program Overview
The globalheader.py program is designed to analyze the global header of the PCAP file and provide information such as the length of the global header, the magic number and the endianness of the PCAP file, the major and minor version numbers of the file format, the SnapLength, and the data link type.

The dhcpframe.py program is designed to analyze the first protocol frame captured in the PCAP file, which is a DHCP frame. The program provides information such as the timestamp indicating when this packet was captured, the actual GMT time corresponding to this timestamp, the length of this DHCP frame, the source and destination MAC addresses of the captured communication, the source and destination IP addresses of the captured communication, and the name of the host PC.

The domain.py program is designed to find suspected websites whose domain name ends with ".top". The program achieves this by using Regular Expression in Python to search for URLs in the PCAP file and matching them with a list of known ".top" domains.

The Searchengine.py program is designed to find out which search engine and which keywords the user used to search for information before getting infected or attacked. The program also identifies the website that the search engine recommended and the user actually accessed. The program achieves this by using Regular Expression in Python to search for URLs in the PCAP file and matching them with a list of known search engines.

PCAP File Header Analysis Tool
This is a Python program designed to analyze the global header of a PCAP file and provide information such as the length of the global header, the magic number and the endianness of the PCAP file, the major and minor version numbers of the file format, the SnapLength, and the data link type.

Usage for pcapheader.py
To use this program, simply run the Python script and provide the file path of the PCAP file as an input when prompted. For example:

javascript
Copy code
$ python pcapheader.py
Naitik Mehta PCAP
Enter the file path: /path/to/pcap/file.pcap
The program will then analyze the PCAP file and provide the requested information.

Program Overview
This program uses the Python struct module to read the binary data of the global header of the PCAP file. The program then extracts the required information from the binary data using the unpack function and the correct format string.

The program checks the magic number to determine the endianness of the PCAP file, and then prints out the required information to the console.
