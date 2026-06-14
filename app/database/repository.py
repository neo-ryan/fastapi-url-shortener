from json import load, dump
from pathlib import Path

BASE_DIR = Path(__file__).parent

async def get_data():
    with open(BASE_DIR / 'db.json', 'r') as f:
        return load(f)

async def add_slug(url_dict:dict):
    data = await get_data()
    if any(item.get('link') == url_dict['link'] for item in data):
        return 'Already slugged bro, chill'
    else:
        data.append(url_dict)
        with open(BASE_DIR / 'db.json', 'w') as f:
            dump(data, f, indent=2)