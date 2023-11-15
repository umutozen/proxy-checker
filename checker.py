 # Coding by Umut Özen
 # 15.11.2023
import requests

def get_proxies():
    url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
    response = requests.get(url)
    proxies = response.text.split('\n')[:-1]
    return proxies

def make_request_using_proxy(proxy):
    url = "http://httpbin.org/get" # Target URL
    proxies = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}",
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        response.raise_for_status()
        print(f"Success using proxy: {proxy}")
    except requests.exceptions.RequestException as e:
        print(f"Failed using proxy: {proxy}")

def main():
    proxies = get_proxies()
    for proxy in proxies:
        make_request_using_proxy(proxy)

if __name__ == "__main__":
    main()
