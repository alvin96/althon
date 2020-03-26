from urllib.error import URLError
from urllib.request import urlopen


def internet_connection():
    try:
        urlopen('https://google.com', timeout = 2)
        return True
    except URLError as err:
        print(f"Checking internet connection failed, status code {err}.")
        return False


print(internet_connection())
