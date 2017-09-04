# wh01p
Tool to obtain information about IP or domain: Geolocation, network, whois and opened ports.
# Install
Review the python dependencies in requeriments.txt
pip install -r requirements.txt
# Use
<pre>
usage: wh01p.py [-h] [-t TARGET] [-i INPUT]

Tool to obtain information about IP or domain: Geolocation, network, whois and open ports

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        The IP which it wants to search
  -i INPUT, --input INPUT
                        File which contains the domains or IP to obtain a piece of information in format txt or json
 </pre>
                 
# Requirements

Input the API key of Shodan and Censys in the modules sh4d0m and getcensys to work properly.
