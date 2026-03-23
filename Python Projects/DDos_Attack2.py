# DDos in Python

import requests

target = input()

while True:
    r = requests.get(target)

    print(r.status_code)





# Understanding DDoS (Ditonostributed Denial of Service) attacks from an educational and cybersecurity defense perspective is crucial. A DDoS attack floods a target server with excessive requests, overwhelming its resources and causing downtime. Here’s how you can learn about them responsibly:

# 1. How DDoS Attacks Work

# Ans: Volume-Based Attacks: Overload bandwidth with traffic (e.g., UDP floods, ICMP floods).
     # Protocol Attacks: Exploit network protocols (e.g., SYN floods).
     # Application Layer Attacks: Target specific applications (e.g., HTTP floods).


# 2. Ethical Simulation of DDoS (Local Testing)
# Ans: If you're a cybersecurity student or researcher, you can set up a controlled environment to test and understand how attacks work.
     # Here’s a simple Python script to simulate HTTP requests (without harming real servers):


# Important: This should only be used on a local machine or a legally owned test server. Running this on unauthorized sites is illegal.


# 3. Protecting Against DDoS Attacks
# Rate Limiting: Restrict excessive requests from the same IP.
# CAPTCHAs: Prevent bots from flooding requests.
# CDN & Load Balancers: Services like Cloudflare distribute traffic.
# Intrusion Detection Systems (IDS): Monitor and block malicious traffic