from fastapi import APIRouter, HTTPException
from datetime import datetime

import httpx
from app.services.jsonPlaceHolder import JsonPlaceHolder

service = JsonPlaceHolder()

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    try:
        user_data = await service.get_user(user_id)
        return {**user_data, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Error from external API: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@router.get("/posts")
async def get_user_posts():
    try:
        posts = await service.get_user_posts()
        return {"User Posts": posts, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Error from external API: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )