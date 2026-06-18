# Url shortener

This is a small url shortener made in FastAPI, it takes a url sent by the user in the /shorten endpoint and creates a 'slug' for it, saving it in a json, the slug is a code that, when given 
in the get /{slug} request, will return the original url, it does not redirect the user by itself. I plan on adding a RedirectResponse so that i can implement it on a frontend to redirect users
completely.

## How to use
It is highly recommended and more intuitive to use FastAPI's docs resource, after installing fastapi, start the server by running (when on the same directory as the main.py):
```
fastapi dev main.py
```
then going to http://127.0.0.1:8000/docs, the default docs url, the url of the server appears in your terminal once you start it, in there, you can test each endpoint easily.
