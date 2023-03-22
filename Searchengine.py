import re

def extract_search_engine_keywords(pcap_file_path):
    with open(pcap_file_path, 'rb') as pcapfile:
       
        pcap_data = pcapfile.read()
        decoded_pcap_data = pcap_data.decode("iso-8859-1")

        url_pattern = re.compile(r'https?://\S+')

        urls = url_pattern.findall(decoded_pcap_data)

        query_pattern = re.compile(r'[\?&]q=([^&]+)')

        searches = {}

        for url in urls:
         
            match = re.search(r'https?://(www\.)?([a-zA-Z0-9_-]+)\.', url)
            if match:
                search_engine = match.group(2)
            
                if search_engine not in searches:
                    searches[search_engine] = []
            
            match = query_pattern.search(url)
            if match:
                keyword = match.group(1)

                searches[search_engine].append(keyword)

        return searches

def main():
  
    print("Naitik Mehta PCAP")


    pcap_file_path = input("Enter the directory for the PCAP file: ")

    searches = extract_search_engine_keywords(pcap_file_path)

    for engine, keywords in searches.items():
        print(f"Search engine used: {engine}")
        print(f"Keywords used: {keywords}")

if __name__ == '__main__':
    main()