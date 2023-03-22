import re

def find_website_urls(pcap_file_path, url_pattern):
    with open(pcap_file_path, 'rb') as pcapfile:
        website_pattern = re.compile(url_pattern)
        file_content = pcapfile.read()
        website_urls = website_pattern.findall(file_content)
        return website_urls

def main():
  
    print("Naitik Mehta PCAP")

    task = input("Select a task (1): ")

    pcap_file_path = input("Enter the directory for the PCAP file: ")

    if task == "1":

        domain_extension = input("Enter the domain extension to find (e.g. .com, .org, .edu): ")


        domain_extension_bytes = domain_extension.encode()

        url_pattern = rb"https?://\S+?" + re.escape(domain_extension_bytes) + rb"\b"

        website_urls = find_website_urls(pcap_file_path, url_pattern)

        print(website_urls)

if __name__ == '__main__':
    main()