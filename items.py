import requests
from bs4 import BeautifulSoup

# URL of the product page
url = "https://www.hollisterco.com/shop/us/p/sherpa-lined-vegan-leather-jacket-58474320?categoryId=12552&faceout=model&seq=05"

# Request the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract description and material

results = soup.find(id = 'product-mfe-web-service-ProductPageFrontend')
material = results.find('h4', class_= 'h4 fabric-care-mfe__label')

#print(description)
#description = soup.find('div', {'class': 'h4 fabric-care-mfe__label'}).text 
#material = soup.find('div', {'class': 'material'}).text

if material:
    material_text = material.get_text(strip=True)
    print("Material:", material_text)
else:
    print("Material description not found.")

#print("Description:", description)

#print("Material:", material)
