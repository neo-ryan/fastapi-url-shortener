from fastapi import APIRouter
from app.services import slugger
from app.models.url import ValidUrl, ResponseUrl

router = APIRouter()

@router.get('/')
async def get_database():
    return await slugger.get_database()

@router.post('/shorten')
async def shorten(url:ValidUrl) -> ResponseUrl:
    return await slugger.generate_slug(url)

@router.get('/{slug}')
async def redirect(slug):
    return await slugger.redirect_user(slug)
