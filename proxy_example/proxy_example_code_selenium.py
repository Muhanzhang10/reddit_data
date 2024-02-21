from seleniumwire import webdriver  # Import from seleniumwire


def fetch_html_content_with_selenium(
    url, proxy_username, proxy_password, proxy_address
):
    # Configure Selenium Wire to use the proxy
    options = {
        "proxy": {
            "http": f"http://{proxy_username}:{proxy_password}@{proxy_address}",
            "https": f"https://{proxy_username}:{proxy_password}@{proxy_address}",
            "no_proxy": "localhost,127.0.0.1",  # Exclude local addresses
        }
    }

    # Initialize the WebDriver with the specified options
    driver = webdriver.Chrome(seleniumwire_options=options)

    try:
        driver.get(url)
        html_content = driver.page_source
        return html_content
    except Exception as e:
        print(f"Error when processing {url}: {e}")
        return ""
    finally:
        driver.quit()


# Example usage
url = "https://www.reddit.com/r/TheGloryHodl/comments/1apvjs5/five_wall_street_banks_hold_223_trillion_in/"
url = ""
proxy_username = "dhqpgqic-rotate"
proxy_password = "9216y6ag38p4"
proxy_address = "p.webshare.io:80"
html_content = fetch_html_content_with_selenium(
    url, proxy_username, proxy_password, proxy_address
)
print(html_content)
