import logging

import azure.functions as func


def main(req: func.HttpRequest, ratings: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not ratings:
        logging.warning("No rating found")
    else:
        # Return the ratings in JSON format
        return func.HttpResponse(f"", status_code=200)
