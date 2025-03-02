import  webbrowser as obdulia
url = 'https://github.com/password_reset'

def obdulia_url(num : int):
    for _ in range(num):
        obdulia.open(url)



obdulia_url(5)