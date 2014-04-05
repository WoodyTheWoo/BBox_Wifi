import urllib3
import re
import clize
import sys

@clize.clize()
def main(active=0):
	"""Activate or deactivate bBox wifi.

    activate: 0 or 1 (0 by default)
    	0 = deactivate
    	1 = activate
    """
	if(active in (0,1)):
		pass
	else:
		print("active must be 0 or 1")
		sys.exit()

	connexion = urllib3.PoolManager()

	r = connexion.request('GET', 'http://192.168.1.254/novice/index.htm')

	token = re.search(r'\w{8}', re.search(r"var token = eval\(\\'\( \"\w{8}\" \)\\'\);", str(r.data)).group()).group()

	values = {'token': token, 'write': 'WLANConfig_RadioEnable:' + str(active)}

	p = connexion.request('POST', 'http://192.168.1.254/cgi-bin/generic.cgi', fields=values)
 
if __name__ == "__main__":
    clize.run(main)