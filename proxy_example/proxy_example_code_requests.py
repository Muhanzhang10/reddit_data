import requests 

proxy_address = "http://dhqpgqic-rotate:9216y6ag38p4@p.webshare.io:80/"

def fetch_html_content(url, proxy_address, timeout=2):
    headers = {
        "User-Agent": UserAgent().random,
        "Content-Type": "text/html; charset=UTF-8",
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            proxies={
                "http": proxy_address,
                "https": proxy_address,
            },
            timeout=timeout,
        )
        if response.status_code == 200:
            return response.text
        else:
            return ""
    except requests.Timeout:
        print(f"The request timed out when processing {url}")
        return ""
    except Exception as e:
        print(f"The request error when processing {url}")
        print(e)
        return ""