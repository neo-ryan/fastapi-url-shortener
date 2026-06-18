from string import ascii_letters, digits
from secrets import choice
from app.database import repository
from app.models.url import ValidUrl, ResponseUrl
from fastapi import HTTPException

alphabet = ascii_letters + digits

async def generate_slug(url:ValidUrl):
    slug = ''.join(choice(alphabet) for i in range(8))
    shortened = {'link':str(url.link), 'slug':slug}
    
    result = await add_slug(shortened)
    
    if result == 'Already slugged bro, chill':
        data = await get_database()
        existing = next(item for item in data if item['link'] == shortened['link'])
        return existing
    
    return shortened

async def add_slug(url_data:ResponseUrl):
    return await repository.add_slug(url_data)

async def get_database():
    return await repository.get_data()

async def redirect_user(slug:str):
    res = await repository.compare(slug)
    if res != 'Not Found':
        return res
    else:
        raise HTTPException(status_code=404)