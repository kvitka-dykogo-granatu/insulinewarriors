import os
import requests
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# init app
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_recipient_details(recipient):
    recipient_details = {
        'phone': None,
        'apikey': None,
    }
    return recipient_details


def send_whatsapp_msg_callmebot(msg, recipients):
    """ CallMeBot: https://www.callmebot.com/blog/free-api-whatsapp-messages """

    # prepare msg
    msg = msg.replace(' ', '%20')
    msg = msg.replace('\n', '%0A')

    # prepare url
    url = 'https://api.callmebot.com/whatsapp.php?phone={phone}&apikey={apikey}&text={msg}'


    status = {}
    for recipient in recipients:
        recipient_details = get_recipient_details(recipient)
        if not recipient_details:
            continue
        
        phone = recipient_details.get('phone')
        if not phone:
            status[recipient] = 'phone number not found!'
            continue

        apikey = recipient_details.get('apikey')
        if not apikey:
            status[recipient] = 'apikey not found!'
            continue
        
        # send request to callmeback
        req = requests.get(url=url.format(phone=phone, apikey=apikey, msg=msg))
        status[recipient] = f'{req.status_code}: {str(req.text)}'

    return status



@app.head("/")
async def read_root():
    return {"status": "ok"}


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request, 'gmaps_api_key': 'AIzaSyB8clj46nl80fbyPbdx1b2Fq5gU_vCct_Q'})



@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


@app.get('/status')
async def return_json(request: Request):
    return {"status": "ok"}


@app.get('/locations')
async def return_json(request: Request):
    data = [
      {"latitude": 50.2021368, "longitude": 30.3525061},
      {"latitude": 50.3021368, "longitude": 30.1525061}
    ]
    return data


if __name__ == '__main__':
    pass