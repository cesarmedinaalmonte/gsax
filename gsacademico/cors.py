class CorsMiddleware(object):
    def process_response(self, req, resp):
        response["Access-Control-Allow-Origin"] = "*"
        return response

    MIDDLEWARE_CLASSES = (
        # ...
        'app.CorsMiddleware'
    )