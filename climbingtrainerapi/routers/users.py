from fastapi import APIRouter

from climbingtrainerapi.schemas.users import UserSchema


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', status_code=201)
async def add(user: UserSchema) -> dict[str, str]:
    return {'message': f'Add new user {user.name}'}


@router.get("/{user_id}")
async def get(user_id: int) -> dict[str, str]:
    return {'message': f'Details of user with id {user_id}'}


@router.delete("/{user_id}")
async def delete(user_id: int) -> dict[str, str]:
    return {'message': f'Deleting user with id {user_id}'}


@router.put("/{user_id}")
async def update(user_id: int) -> dict[str, str]:
    return {'message': f'Updating user with id {user_id}'}
