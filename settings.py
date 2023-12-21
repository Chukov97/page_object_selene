from typing import Literal, Optional
from pydantic_settings import BaseSettings
from demoqa_tests.models.constatn import BASE_URL
from utils import path


class Config(BaseSettings):
    context: Literal['stage', 'local'] = 'local'

    base_url: str = BASE_URL
    driver_name: str = 'chrome'
    load_strategy: str = 'eager'
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 4.0

    remote_url: Optional[str] = None


config = Config(_env_file=path.relative_from_root(f'.env.{Config().context}'))
