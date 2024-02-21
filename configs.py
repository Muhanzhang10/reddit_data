# Contains IP pools in case limite number of request set by the website
#PROXY_ADDRESS = "http://dhqpgqic-rotate:9216y6ag38p4@p.webshare.io:80/"

proxy_username = "dhqpgqic-rotate"
proxy_password = "9216y6ag38p4"
proxy_address  = "p.webshare.io:80"

# Configure Selenium Wire to use the proxy
OPTIONS = {
    "proxy": {
        "http": f"http://{proxy_username}:{proxy_password}@{proxy_address}",
        "https": f"https://{proxy_username}:{proxy_password}@{proxy_address}",
        "no_proxy": "localhost,127.0.0.1",  # Exclude local addresses
    }
}