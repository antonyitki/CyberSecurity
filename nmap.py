print("hello")
import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("gateway")
# And you would get your results in json
print(results)