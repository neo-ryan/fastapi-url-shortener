from pydantic import BaseModel, AnyUrl

class ValidUrl(BaseModel):
    link:AnyUrl
    
class ResponseUrl(ValidUrl):
    slug:str