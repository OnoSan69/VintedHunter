echo "# VintedHunter" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/OnoSan69/VintedHunter.git
git push -u origin main

## Fetch Vinted Listings

This repository includes a Python script to fetch the newest listings for a given brand on Vinted.

```
python fetch_vinted_listings.py [BRAND_NAME]
```

Environment variables:
- `VINTED_AUTH_TOKEN` – optional authentication token if required by the API.
- `VINTED_BASE_URL` – base URL (defaults to `https://www.vinted.com`).

Example:

```
VINTED_AUTH_TOKEN=YOUR_TOKEN python fetch_vinted_listings.py Antique
```

