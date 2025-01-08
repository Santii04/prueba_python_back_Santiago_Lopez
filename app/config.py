from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """    
    Application settings model using Pydantic BaseSettings.

    Attributes:
        API_BASE_URL (str): The base URL for API requests, loaded from environment variables.
    """
    API_BASE_URL: str
    
    class Config:
        env_file = ".env"
        
settings = Settings()