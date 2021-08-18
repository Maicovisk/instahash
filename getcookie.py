
def getCookie():
    from datetime import datetime
    import requests, json

    link = 'https://www.instagram.com/accounts/login/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'


    username = 'videos2018pg@gmail.com'
    password = 'maicon2019'


    time = int(datetime.now().timestamp())
    response = requests.get(link)

    csrf = "response.cookies['csrftoken']"

    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = requests.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)




    if json_data["authenticated"]:

        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
    else:
        print("login failed ", login_response.text)


    return {
        'text_cookie' : login_response.cookies,
        'cookie': cookie_jar
    }
