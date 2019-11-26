data='''
# Recommended minimum configuration:
#

#Default: debug_options ALL,1
#more    : debug_options ALL,1 33,2 28,9
debug_options ALL,1 28,3

refresh_pattern -i (/cgi-bin/|\?) 0 0% 0
refresh_pattern .            0 20% 4320
maximum_object_size 8192 KB
cache_dir ufs /var/spool/squid 8192 16 128
cache_log none
cache_store_log none
cache_mem 512 MB

#####################################################################################

# Example rule allowing access from your local networks.

 

# Adapt to list your (internal) IP networks from where browsing
# should be allowed
acl localnet src 10.0.0.0/8    # RFC1918 possible internal network
#acl localnet src 172.16.0.0/12    # RFC1918 possible internal network
acl localnet src 192.168.0.0/16    # RFC1918 possible internal network
#acl localnet src fc00::/7       # RFC 4193 local private network range
#acl localnet src fe80::/10      # RFC 4291 link-local (directly plugged) machines

acl SSL_ports port 443 563 445 8080 10443 27443 28443
#acl SSL_ports port 443
acl Safe_ports port 80        # http
acl Safe_ports port 21        # ftp
acl Safe_ports port 22        # telnet
acl Safe_ports port 443    563 445 # https
acl Safe_ports port 70        # gopher
acl Safe_ports port 210        # wais
acl Safe_ports port 1025-65535    # unregistered ports
acl Safe_ports port 280        # http-mgmt
acl Safe_ports port 488        # gss-http
acl Safe_ports port 591        # filemaker
acl Safe_ports port 777        # multiling http
acl CONNECT method CONNECT

#
# Recommended minimum Access Permission configuration:
#
# Deny requests to certain unsafe ports
http_access deny !Safe_ports

# Deny CONNECT to other than secure SSL ports
#http_access deny CONNECT !SSL_ports

#
# INSERT YOUR OWN RULE(S) HERE TO ALLOW ACCESS FROM YOUR CLIENTS
#
##################################################################


# one who can access services on "localhost" is a local user
http_access deny to_localhost

# Example rule allowing access from your local networks.
# Adapt localnet in the ACL section to list your (internal) IP networks
# from where browsing should be allowed
http_access allow localnet
http_access allow localhost

# And finally deny all other access to this proxy
http_access allow all

# Squid normally listens to port 3128
http_port 3128

# Uncomment and adjust the following to add a disk cache directory.
#cache_dir ufs /var/spool/squid 100 16 256

# Leave coredumps in the first cache dir
coredump_dir /var/spool/squid

#
# Add any of your own refresh_pattern entries above these.
#
refresh_pattern ^ftp:        1440    20%    10080
refresh_pattern ^gopher:    1440    0%    1440
refresh_pattern -i (/cgi-bin/|\?) 0    0%    0
refresh_pattern .        0    20%    4320

'''

import os
os.system('sudo apt update')
os.system('sudo apt upgrade')
os.system('sudo apt install squid -y')

try:
	with open('/etc/squid/squid.conf','w') as f:
		f.write(data)
except:
	print('something went wrong')

os.system('sudo service squid restart')
