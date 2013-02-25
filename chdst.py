import xmlrpclib
import sys
from getpass import getpass

password=getpass('password for spam filter')

domain=sys.argv[1]
target=sys.argv[2]

url="http://63.164.138.3:80/cgi-mod/api.cgi?password="+password;
cuda=xmlrpclib.Server(url)
try:
  response=cuda.config.set({'type':'domain','path':domain,'mta_relay_advanced_host':target})
  print domain,target,response
except xmlrpclib.Fault:
  print domain,'none'


