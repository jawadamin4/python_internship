import requests

with open("valid_proxies", "r") as f:
    proxies = f.read().split("\n")

sites_to_check =['https://books.toscrape.com/',
                 'https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
                 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html']

counter = 0
for site in sites_to_check:
    try:
        print(f"using the proxy : {proxies[counter]}")
        res = requests.get(site, proxies={
            "http": proxies[counter],
            "https": proxies[counter]})
        print(res.text)
        print(res.status_code)
    except:
        print("failed")
    finally:
        counter += 1