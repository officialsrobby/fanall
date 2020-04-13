import requests
import time
from requests.exceptions import Timeout

a = list(range(210900010,220000000))
    
i=1
for tokens in a:
	try:
		headers={'User-Agent':'Mozilla/5.0','Authorization':'Token 510b152118e524377ef293c3576d26511c2bddbb'}
		response = requests.post('https://id-api.spooncast.net/users/'+str(tokens)+'/follow/',headers=headers,timeout=1)
		print(response)
		print(i)
		i+=1
		print(tokens)
	except Timeout:
		print('ke '+str(tokens)+' gagal')
	except:
		print('ada yang gagal')
	#time.sleep(5)
