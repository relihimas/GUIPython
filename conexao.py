import requests
import time

url = 'https://www.google.com/'
timeout = 5

def conexao(url, timeout):
    contwhile = 0

    while contwhile == 0:
        try:
            request = requests.get(url, timeout=timeout)
            status = request.status_code
            time.sleep(5)
        except (requests.ConnectionError, requests.Timeout) as exception:
            contwhile = contwhile + 1
            status = request.status_code
            time.sleep(5)

    return status


