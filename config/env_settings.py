# app/supabase_client.py
from supabase import create_client
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str

    class Config:
        env_file = ".env"

@lru_cache(maxsize=None)
def get_settings() -> Settings:
    """
    Retrieve Supabase settings from environment variables.
    """
    return Settings()


def create_supabase_client(settings):
    """
    Create and return a Supabase client using the provided settings.
    """
    return create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)

# Initialize the Supabase client when this module is imported
settings = get_settings()
supabase = create_supabase_client(settings)
