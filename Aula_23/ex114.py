import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.globo.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Deu certo')
    print(site.read())
