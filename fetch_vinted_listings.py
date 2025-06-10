import os
import requests
import sys

VINTED_BASE_URL = os.getenv('VINTED_BASE_URL', 'https://www.vinted.com')

TOKEN = os.getenv('VINTED_AUTH_TOKEN')

HEADERS = {
    'User-Agent': 'Mozilla/5.0',
}

if TOKEN:
    HEADERS['Authorization'] = TOKEN


def fetch_brand_id(brand_name: str) -> int:
    params = {'q': brand_name}
    url = f"{VINTED_BASE_URL}/api/v2/brands"
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    data = r.json()
    for brand in data.get('brands', []):
        if brand.get('title', '').lower() == brand_name.lower():
            return brand['id']
    raise ValueError(f"Brand '{brand_name}' not found")


def fetch_newest_items(brand_id: int, per_page: int = 10):
    url = f"{VINTED_BASE_URL}/api/v2/catalog/items"
    params = {
        'brand_id': brand_id,
        'order': 'newest_first',
        'per_page': per_page,
    }
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    return r.json().get('items', [])


def main():
    brand_name = ' '.join(sys.argv[1:]) or 'Antique'
    print(f"Searching for brand: {brand_name}")
    brand_id = fetch_brand_id(brand_name)
    print(f"Brand ID: {brand_id}")
    items = fetch_newest_items(brand_id)
    for item in items:
        print(f"#{item['id']}: {item['title']} - {item['price']} {item['currency']}")


if __name__ == '__main__':
    main()
