import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def loguearse():
    token = ""
    url_get = "https://extranet.osocna.com.ar/Backend/token"
    usr = {"UserName":"ScienzaWSuser", "Password":"kj2342dfh$", "grant_type": "password"}
    hdr = {"Content-Type":"application/x-www-form-urlencoded"}

    r = requests.get(url_get, headers=hdr, data=usr, verify=False) ## pasar usr como headers para autenticar
    # print(r.json())
    if r.status_code == 200:
        content_json = r.json()
        pretoken = content_json['access_token']
        token = "Bearer " + pretoken 
    return token




    
