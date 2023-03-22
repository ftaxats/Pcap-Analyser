import struct

def main():
 
    print("Global Header PCAP")

  
    file_path = input("Enter the file path: ")

    with open(file_path, 'rb') as f:
        global_header = f.read(24)

        (magic_number, major_version, minor_version, timezone_offset, timestamp_accuracy, snaplen, data_link_type) = struct.unpack('<IHHiIII', global_header)

        if magic_number == 0xa1b2c3d4:
            endianness = 'big'
        elif magic_number == 0xd4c3b2a1:
            endianness = 'little'
        else:
            endianness = 'unknown'

        print('Global Header Length:', len(global_header))
        print('Magic Number:', hex(magic_number))
        print('Endianness:', endianness)
        print('Major Version:', major_version)
        print('Minor Version:', minor_version)
        print('SnapLength:', snaplen)
        print('Data Link Type:', data_link_type)

if __name__ == '__main__':
    main()
