from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from itm.documents import User
from itm.auth.hash import HashService
from itm.auth.token import TokenService
from itm.shared.http import NotFound, UnprocessableEntity


router = APIRouter()


class EditItem(BaseModel):
    displayName: str = ''
    email: str = ''
    password: str = ''
    photoUrl: str = ''


@router.put('/{user_id}/')
def edit_user(user_id: str, item: EditItem):
    user = User.get(user_id, ignore=NotFound.code)

    if not user:
        raise NotFound

    if item.displayName:
        user.name = item.displayName

    if item.password:
        user.password = HashService.hash(item.password)

    if item.photoUrl:
        user.avatarUrl = item.photoUrl

    user.save(refresh=True)


@router.get('/')
def list_users():
    def format_user(user):
        return {
            'uid': user.id,
            'displayName': user.name,
            'photoUrl': user.avatarUrl,
        }

    users = User.search() \
        .source(['name', 'email', 'avatarUrl']) \
        .scan()

    return list(map(format_user, users))


@router.post('/')
def invite_user(item: EditItem):
    if not item.email or not item.displayName or not item.photoUrl:
        raise UnprocessableEntity('Missing fields')

    if User.find_by_email(item.email):
        raise UnprocessableEntity('Already exists')

    invitation = {
        'invitedAt': datetime.utcnow(),
        'token': TokenService.encode({'email': item.email}, {'days': 1}),
    }

    User(name=item.displayName,
         email=item.email,
         avatarUrl=item.photoUrl,
         invitation=invitation).save(refresh=True)
