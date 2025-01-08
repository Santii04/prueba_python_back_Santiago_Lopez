import httpx
from app.config import settings
from app.logger import logger

class JsonPlaceHolder:
    """
    Class to manage the petitions to the API of JsonPlaceHolder
    
    Attributes:
        last_user_id: Tracks the las id fetched using the get_user method
        
    Methods:
        get_user(user_id: int): Fetch an user using the ID specified
        get_user_posts(user_id: int = None): Fetch he user posts for a given user id or the last fetched user using the get_user method
    """
    
    def __init__(self):
        self.last_user_id = None

    async def get_user(self, user_id: int):
        """Fetch an user using the ID specified

        Args:
            user_id (int): User id to be fetch

        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{settings.API_BASE_URL}/users/{user_id}")
                self.last_user_id = user_id
                response.raise_for_status()
                logger.info(f"Success fetching user with id: {user_id}")
                return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Service error!: {__name__}. Error fetching user with id: {user_id}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in {__name__}: {str(e)}")
            raise
        
    async def get_user_posts(self, user_id: int = None):
        """Fetch the user posts for the user id specified or the last fetched user

        Args:
            user_id (int, optional): User id to fetch respectively posts . Defaults to None.

        """
        
        target_user_id = user_id if user_id is not None else self.last_user_id
        
        if not target_user_id:
            logger.error(f"Service error!: {__name__}. First fetch a user using /users/user_id")
            raise ValueError("No user has been fetched or is not provided")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{settings.API_BASE_URL}/posts", params={"userId": target_user_id})
                response.raise_for_status()
                posts = response.json()
                
                if not posts:
                    logger.error(f"Service error!: {__name__}. No posts found for user {target_user_id}")
                    raise ValueError(f"No posts found for user {target_user_id}")
                
                logger.info(f"Success fetching posts for user: {self.last_user_id}")
                return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Service error!: {__name__}. Error fetching posts for user {self.last_user_id}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in {__name__}: {str(e)}")
            raise