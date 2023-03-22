# Pcap-Analyser
This GitHub repository contains a set of Python programs that are designed to analyze PCAP files for potential security threats. The repository consists of Four programs, each of which is designed to perform a specific task related to analyzing PCAP files.
PCAP File Analysis Tool
This is a set of Python programs designed to analyze PCAP files for potential security threats. The repository consists of six programs, each of which is designed to perform a specific task related to analyzing PCAP files.

Program Overview
The globalheader.py program is designed to analyze the global header of the PCAP file and provide information such as the length of the global header, the magic number and the endianness of the PCAP file, the major and minor version numbers of the file format, the SnapLength, and the data link type.

The dhcpframe.py program is designed to analyze the first protocol frame captured in the PCAP file, which is a DHCP frame. The program provides information such as the timestamp indicating when this packet was captured, the actual GMT time corresponding to this timestamp, the length of this DHCP frame, the source and destination MAC addresses of the captured communication, the source and destination IP addresses of the captured communication, and the name of the host PC.

The domain.py program is designed to find suspected websites whose domain name ends with All domain Extensions. The program achieves this by using Regular Expression in Python to search for URLs in the PCAP file and matching them with a list of known ".top,.com,.edu,,etc." domains.

The Searchengine.py program is designed to find out which search engine and which keywords the user used to search for information before getting infected or attacked. The program also identifies the website that the search engine recommended and the user actually accessed. The program achieves this by using Regular Expression in Python to search for URLs in the PCAP file and matching them with a list of known search engines.

<details>
<summary><b>PCAP File Header Analysis Tool</b></summary>
This is a Python program designed to analyze the global header of a PCAP file and provide information such as the length of the global header, the magic number and the endianness of the PCAP file, the major and minor version numbers of the file format, the SnapLength, and the data link type.

<b>Usage</b>

To use this program, simply run the Python script and provide the file path of the PCAP file as an input when prompted. For example:

```python
  python globalheader.py  
```
The program will then analyze the PCAP file and provide the requested information.

<b>Program Overview</b>

This program uses the Python struct module to read the binary data of the global header of the PCAP file. The program then extracts the required information from the binary data using the unpack function and the correct format string.

The program checks the magic number to determine the endianness of the PCAP file, and then prints out the required information to the console.

</details>
<details>
<summary><b>Pcap File Parser</b></summary>
This is a simple Python script that extracts and prints information from a PCAP file.

<b>Parameters</b>

The script uses the following parameter:

file_path: The path of the input PCAP file.
<b>Usage</b>

Clone or download the repository. Run the script with the following command:

```python
python dhcpframe.py
```
Enter the path of the input PCAP file when prompted.

</details>
<details>
<summary><b>PCAP URL Extractor</b></summary>
This is a Python script that extracts website URLs from a PCAP file based on a specified domain extension.

<b>Parameters</b>

The script uses the following parameters:

pcap_file_path: The path of the input PCAP file.
url_pattern: The regular expression pattern to search for website URLs.
<b>Usage</b>

Clone or download the repository. Run the script with the following command:

```python
python domain.py
```
Enter the path of the input PCAP file when prompted. Enter "1" to search for URLs with a specific domain extension. Enter the domain extension to search for when prompted (e.g. ".com", ".org", ".edu"). The script will print out a list of website URLs that match the specified domain extension.

</details>
<details>
<summary><b>PCAP Search Engine Keyword Extractor</b></summary>
This is a Python script that extracts search engine keywords from a PCAP file.

<b>Parameters</b>

The script uses the following parameter:

pcap_file_path: The path of the input PCAP file.
<b>Usage</b>

Clone or download the repository. Run the script with the following command:

```python
python Searchengine.py
```
Enter the path of the input PCAP file when prompted. The script will print out a list of search engine keywords used in the PCAP file, grouped by search engine.

</details>
