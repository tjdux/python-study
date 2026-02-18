from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()


class MongoDB:
    def __init__(self):
        self.client: Optional[AsyncIOMotorClient] = None
        self.engine: Optional[AIOEngine] = None

    def connect(self):
        self.client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
        self.engine = AIOEngine(
            client=self.client, database=os.getenv("MONGO_DB_NAME", "default_db")
        )

    def close(self):
        if self.client is not None:
            self.client.close()

    def get_engine(self):
        return self.engine


mongodb = MongoDB()
