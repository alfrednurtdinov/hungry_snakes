import json

from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

node_path = 'hungry-snakes.herokuapp.com'


def encode(obj: str) -> dict:
    result = {}
    for i in obj.split('&'):
        x, y = i.split('=')
        result[x] = y
    return result


@app.post("/")
@app.get("/")
async def get(request: Request):
    response = await request.body()
    data = response.decode('utf-8')
    print("DAta=" + data)
    try:
        dct = encode(data)
        if len(dct) == 1 and len(dct['username']) < 25:
            print('BUUUR!'+dct['username'])
            return templates.TemplateResponse(
                'game.html',
                context={'request': request, 'address': node_path,'username': dct['username']}
            )
        else:
            return templates.TemplateResponse('home.html', context={'request': request})
    except Exception:
        return templates.TemplateResponse('home.html', context={'request': request})
