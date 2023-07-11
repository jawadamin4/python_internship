import requests
import pandas as pd
import grequests

from bs4 import BeautifulSoup
import gevent.monkey

gevent.monkey.patch_ssl()


# Make the initial request to the API and get the JSON response
url = "https://www.laufen.co.at/automatic-category-detail?p_p_id=ProductList_INSTANCE_80H5hgzHtYEp&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&roca_env=3vjR5WgLKZIHLB3Uu8eoUA%3D%3D"
response = requests.get(url)
data = response.json()

# Extract the product URLs from the JSON response
product_list = data['products']
product_urls = [product['url'] for product in product_list]

# Use grequests to send asynchronous requests to scrape data from the product detail pages
rs = (grequests.get(url) for url in product_urls)
responses = grequests.map(rs)

# Process the responses and extract the required data
scraped_data = []
for response in responses:
    if response is not None:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the required data from the page using BeautifulSoup selectors
        category1 = soup.select_one('.coleccion-name').text.strip()
        category2 = soup.select_one('.coleccion-title').text.strip()
        series = soup.select_one('.coleccion-title').text.strip()
        name = soup.select_one('.coleccion-article').text.strip()
        article_number = soup.select_one('.coleccion-article')['id']
        length = soup.select_one('#dim-txt').text.strip().split(' x ')[0]
        width = soup.select_one('#dim-txt').text.strip().split(' x ')[1]
        height = soup.select_one('#dim-txt').text.strip().split(' x ')[2]
        color = soup.select_one('.color-display').text.strip()
        product_type = ''
        short_description = ''
        material = ''
        datasheet = ''
        data_3d = ''
        long_description = ''
        main_image = soup.select_one('.slider-single img')['src']
        gallery_images = [img['src'] for img in soup.select('.slider-nav img')]

        # Append the extracted data to the scraped_data list
        scraped_data.append({
            'Category 1': category1,
            'Category 2': category2,
            'Series': series,
            'Name': name,
            'Article Number': article_number,
            'L': length,
            'W': width,
            'H': height,
            'Color': color,
            'Type': product_type,
            'Short Description': short_description,
            'Material': material,
            'Datasheet': datasheet,
            '3D Data': data_3d,
            'Long Description': long_description,
            'Main image': main_image,
            'Gallery image': ', '.join(gallery_images),
            'Product Url': response.url
        })

# Create a DataFrame from the scraped_data list
df = pd.DataFrame(scraped_data)

# Do further processing or save the DataFrame as desired
