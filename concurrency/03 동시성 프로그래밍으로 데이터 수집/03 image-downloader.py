import aiohttp
import asyncio
from dotenv import load_dotenv
import os
import aiofiles

load_dotenv()

CLIENT_ID = os.getenv("X-Naver-Client-Id")
CLIENT_SECRET = os.getenv("X-Naver-Client-Secret")

async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]
    
    try:
        os.makedirs("./images")
    except FileExistsError:
        pass
    
    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                await file.write(await response.read())


async def fetch(session, url):
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        await asyncio.gather(*[img_downloader(session, img) for img in images])
        

async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image.json"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1 + i*20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])

if __name__ == "__main__":
    asyncio.run(main())