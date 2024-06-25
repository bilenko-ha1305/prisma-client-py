from fastapi import FastAPI
from fastapi.responses import HTMLResponse

admin_app = FastAPI()


@admin_app.get('/', response_class=HTMLResponse)
def admin():
    return """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """
