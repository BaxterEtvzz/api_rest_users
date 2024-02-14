from fastapi import FastAPI
from routes.user import user_app

app = FastAPI(
    title='BanPay Technical Interview Practice',
    description='Development of a user REST API according to the challenge specifications. This API connects to a MongoDB database for information management, as well as consumes the Studio Ghibli API based on the user´s role.',
    version='0.0.1'
)

app.include_router(user_app)
