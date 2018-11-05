import json,requests,base64,random
import time
#from PIL import Image
#from StringIO import StringIO


def proxy():
    dic_proxy = []
    with open('proxy.list','rb') as p_list:
        for proxy in p_list.readlines():
            if proxy:
                dic_proxy.append(proxy.strip()[1:-1-1])
    random.shuffle(dic_proxy)
    return dic_proxy[0]

def get_json():
    p_url = proxy()
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4'}
    url_json = "http://enquete.uol.com.br:443/vote?jsonp=PollVote&format=jsonp&id=48058&answers=IDMODELO"
    req_json = requests.get(url_json,headers=user_agent,proxies=p_url ,timeout=5)
    json_enquete = req_json.text.encode('utf-8')
    json_enquete = json_enquete.replace('PollVote(','').replace(')','')
    json_enquete = json.loads(json_enquete)
    url_image = json_enquete['captcha']['image']
    url_image = url_image.encode('utf-8')
    id_captcha = json_enquete['captcha']['id']
    id_captcha = id_captcha.encode('utf-8')
    print (req_json.text)
    return (url_image,id_captcha)

def save_img(url_image):
    img = requests.get(url_image, stream=True)
    i = Image.open(StringIO(img.content))
    i.save("captchaZIKA.jpg")

def verf_captcha(texto_id):
    valid = 1
    while valid == 1:
        url_zika = "http://api.dbcapi.me/api/captcha/%s" % texto_id
        get_solved = requests.get(url_zika,timeout=5)
        texto_solved = get_solved.text
        texto_solved = texto_solved.encode('utf-8').split('&')[2].split('=')[1]
        if len(texto_solved) > 0:
            return texto_solved
        else:
            pass

def resolv_captcha():
    data = {"username":"USUARIO-DEATHBYCAPTHCA","password":"SENHA"}
    arq = {"captchafile":open("captchaZIKA.jpg","rb")}
    req_captcha = requests.post("http://api.dbcapi.me/api/captcha", files=arq, data=data,timeout=5)
    texto_id = req_captcha.text
    texto_id = texto_id.encode('utf-8').split('&')[1].split('=')[1]
    texto_solved = verf_captcha(texto_id)
    return texto_solved

def vota_nessa_mina():
    p_url = proxy()
    url_image,id_captcha = get_json()
    save_img(url_image)
    texto_solved = resolv_captcha()
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4'}
    url_voto = "http://enquete.uol.com.br:443/vote?jsonp=PollVote&format=jsonp&id=48058&answers=IDMODELO&captcha-value=%s&captcha-id=%s" % (texto_solved,id_captcha)
    req_voto = requests.get(url_voto,headers=user_agent,proxies=p_url,timeout=5)
    print (req_voto.text)

times = [5,10,3,15]
for i in range(1,2):
    try:
        random.shuffle(times)
        time.sleep(times[0])
        vota_nessa_mina()
    except:
        print("Erro!")
        pass