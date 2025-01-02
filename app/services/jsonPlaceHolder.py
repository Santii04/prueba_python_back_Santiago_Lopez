import httpx
from app.config import settings
from app.logger import logger

class JsonPlaceHolder:
    
    def __init__(self):
        self.last_user_id = None

    async def get_user(self, user_id: int):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{settings.API_BASE_URL}/users/{user_id}")
                self.last_user_id = user_id
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Service error!: {__name__}. Error fetching user with id: {user_id}: {str(e)}")
            raise
        
    async def get_user_posts(self):
        if not self.last_user_id:
            raise ValueError("No user has been fetched")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{settings.API_BASE_URL}/posts", params={"userId": self.last_user_id})
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Service error!: {__name__}. Error fetching posts for user {self.last_user_id}: {str(e)}")
            raise