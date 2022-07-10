import os

import motor.motor_asyncio
from beanie import init_beanie

from app.server.models.product_review import ProductReview

mongo_user = os.getenv("MONGO_USERNAME", "mongo")
mongo_password = os.getenv("MONGO_PASSWORD", "m0ng0")
mongo_host = os.getenv("MONGO_HOST", "mongo")


async def init_db():
    print(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:27017")
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:27017"
    )

    await init_beanie(database=client.db_name, document_models=[ProductReview])
