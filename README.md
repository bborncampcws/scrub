Tools for using scrub.cws.net written in python.

Makes it easier to automate certain tasks

getdst.py get destination of domains specified with arguments or in a domains file

e.g. python getdst.py domain.com domain2.com
     python getdst.py (will iterate over domains listed in file 'domains')

chdst.py change mail server destination for a give domain

e.g. python chdst.py domain.com 192.168.0.100
