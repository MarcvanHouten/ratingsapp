import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Rating API trigger function processed a request.')

    
    if req.method == 'GET':
        return func.HttpResponse('',status_code=200)

    if req.method == 'POST':
        try:
            body = req.get_json()
        except ValueError:
            pass
        else:
            userId = body.get('')
