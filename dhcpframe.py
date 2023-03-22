import struct

print("Naitik Mehta Pcap")


file_path = input("Enter the file path for the PCAP file: ")

with open(file_path, 'rb') as pcap_file:

    global_header = pcap_file.read(24)

    packet_header = pcap_file.read(16)

    timestamp = struct.unpack('I', packet_header[0:4])[0]
    capture_time = timestamp + (struct.unpack('I', packet_header[4:8])[0] / 1000000)

    import datetime
    utc_time = datetime.datetime.utcfromtimestamp(capture_time)
    utc_time_str = utc_time.strftime('%Y-%m-%d %H:%M:%S.%f UTC')

    packet_length = struct.unpack('I', packet_header[8:12])[0]

    packet_data = pcap_file.read(packet_length)


    source_mac = ':'.join([format(b, '02x') for b in packet_data[6:12]])
    destination_mac = ':'.join([format(b, '02x') for b in packet_data[0:6]])

    source_ip = '.'.join([str(b) for b in packet_data[26:30]])
    destination_ip = '.'.join([str(b) for b in packet_data[30:34]])

    hostname = packet_data[34:].decode(errors='ignore').split('\x00')[0]

    print('Timestamp: {}'.format(capture_time))
    print('UTC time: {}'.format(utc_time_str))
    print('Packet length: {}'.format(packet_length))
    print('Source MAC address: {}'.format(source_mac))
    print('Destination MAC address: {}'.format(destination_mac))
    print('Source IP address: {}'.format(source_ip))
    print('Destination IP address: {}'.format(destination_ip))
    print('Hostname: {}'.format(hostname))