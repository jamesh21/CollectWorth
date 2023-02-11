import requests
import json

pre_url = "https://mpapi.tcgplayer.com/v2/product/"
suffix_url = "/details?mpfev=1479"
product_ids = ["257733", "229277", "278980", "242457", "450086", "185717", "242436", "206027", "256141", "216853", "277324", "236258", "283389", "247654", "221313", "265519"]
products = {}

for product_id in product_ids:
    response = requests.get(
        pre_url + product_id + suffix_url,
        headers={
            'Content-type':'application/json', 
            'Accept':'application/json'
        },
        params={"q": "", "isList": True}
    ).json()
    product = {'name': response['productName'] ,'price': response['marketPrice']}
    if response['productLineName'] not in products:
        products[response['productLineName']] = []
    products[response['productLineName']].append(product)

# Serializing json
json_object = json.dumps(products, indent=4)
 
# Writing to sample.json
with open("product-price.json", "w") as outfile:
    outfile.write(json_object)
# print(products)
