import xmlrpclib
from getpass import getpass
import sys

password=getpass('password for spam filter')

if len(sys.argv) < 2:
  domains=open('domains','r').readlines()
  domains=[domain[:-1] for domain in domains]
else:
  domains=[sys.argv[1:]]


for domain in domains:
  url="http://63.164.138.3:80/cgi-mod/api.cgi?password="+password;
  cuda=xmlrpclib.Server(url)
  try:
    dstaddr=cuda.config.get({'type':'domain','path':domain,'variable':'mta_relay_advanced_host'})
    print domain,dstaddr
  except xmlrpclib.Fault:
    print domain,'none'


