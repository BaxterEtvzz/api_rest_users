def userEntity(item) -> dict:
    return {
        'id': item['id'],
        'name': item['name'],
        'role': item['role'],
        'created_at': item['created_at']
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
