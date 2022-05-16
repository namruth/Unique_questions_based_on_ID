#usage: python3 my-unique-items.py <NUID> <number_of_output_items>

import os
import sys
import hashlib

pcap_list = [
"10k.pcap",
"best_malware_protection.pcap",
"bredolab-sample.pcap",
"emerging-all.pcap",
"evidence03.pcap",
"example.com-3.pcap",
"example.com-4.pcap",
"fake_av.pcap",
"zeus-sample-3.pcap"
]

websites_list = [
"facebook.com",
"instagram.com",
"twitter.com",
"titktok.com",
"pinterest.com",
"reddit.com",
"youtube.com",
"linkedin.com",
"tumblr.com",
"flickr.com"
]

cve_list = [
"CVE-2021-44228",
"CVE-2019-6111",
"CVE-2021-3449",
"CVE-2021-2356"
]

ip_list = [
"8.8.8.8",
"8.8.4.4",
"1.1.1.1",
"9.9.9.9",
"1.0.0.1"
]

nmap_scans_list = [
"Nmap FIN Scan",
"TCP Ping scan",
"Null Scan",
"SYN-FIN Scan",
"XMAS Scans",
"URG Scan"
]

#try:
nuid_raw = sys.argv[1]
print("NUID entered is {}".format(nuid_raw))
n_items = sys.argv[2]
print("Number of output items {}".format(n_items))

op_list = []

#choose the input list from any of the above lists
inp_list = pcap_list
#inp_list = websites_list
#inp_list = ip_list



num_of_samples = len(inp_list)
sha256_hash = hashlib.sha256(nuid_raw.encode())

unique_item_pos = int(sha256_hash.hexdigest(),16) % num_of_samples

if (int(n_items) > num_of_samples):
	print("Enter a value less than the size of the input list")
	exit(0)

for i in range(int(n_items)):
	op_list.append(inp_list[unique_item_pos % num_of_samples])
	#print(unique_item_pos)
	unique_item_pos += 1

print(op_list)

#except:
#	print("Check your NUID or pcap-samples directory")
