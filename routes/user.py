from fastapi import APIRouter, Response
from config.db import collection
from schemas.user import userEntity, usersEntity
from models.user import User
from fastapi import FastAPI, HTTPException
import uuid
import requests
import json
from starlette.status import HTTP_204_NO_CONTENT

user_app = APIRouter()


@user_app.get('/users', response_model=list[User], tags=['Users'])
def get_users():
    return usersEntity(collection.find())


def validate_user_role(role: str):
    if role.lower() not in ['films', 'people', 'locations', 'species', 'vehicles']:
        raise HTTPException(status_code=404, detail='Invalid user role')


@user_app.post('/create', response_model=User, tags=['Users'])
def create_user(user: User):
    try:
        validate_user_role(user.role)
        user.id = str(uuid.uuid4())
        new_user = user.model_dump()
        id = collection.insert_one(new_user).inserted_id
        user = collection.find_one({'_id': id})
        return userEntity(user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=404, detail='Invalid user:' + str(e))


@user_app.get('/user/{id_user}', response_model=User, tags=['Users'])
def get_user(id_user: str):
    try:
        r = collection.find_one({'id': id_user}, {'_id': 0})
        return r
    except StopIteration:
        raise HTTPException(status_code=404, detail='User not found')


@user_app.get('/user/ghibli/{id_user}', tags=['Studio Ghibli API'])
def get_data_ghibli(id_user: str):
    try:
        user = collection.find_one({'id': id_user}, {'_id': 0})
        data = []
        url_base = 'https://ghibliapi.vercel.app/'
        if user['role'] in ['films', 'people', 'locations', 'species', 'vehicles']:
            r = requests.get(url_base + user['role'])
            response = json.loads(r.text)
            for r in response:
                if 'title' in r:
                    data.append(r['title'])
                elif 'name' in r:
                    data.append(r['name'])
        else:
            raise HTTPException(status_code=404, detail='Invalid user role')
        return data
    except StopIteration:
        raise HTTPException(status_code=404, detail='User not found')


@user_app.delete('/user/{user_id}', status_code=HTTP_204_NO_CONTENT, tags=['Users'])
def delete_user(user_id: str):
    try:
        userEntity(collection.find_one_and_delete({'id': user_id}, {'_id': 0}))
        return Response(status_code=HTTP_204_NO_CONTENT)
    except StopIteration:
        raise HTTPException(status_code=404, detail='User not found')


@user_app.put('/user/{user_id}', response_model=User, tags=['Users'])
def update_user(user_id: str, updated_user: User):
    try:
        if updated_user.role.lower() in ['films', 'people', 'locations', 'species', 'vehicles']:
            collection.find_one_and_update({'id': user_id}, {
                                           '$set': {'name': updated_user.name, 'role': updated_user.role}})
            return 'User has been successfully updated'
        else:
            raise HTTPException(status_code=404, detail='Invalid user role')
    except StopIteration:
        raise HTTPException(status_code=404, detail='User not found')
