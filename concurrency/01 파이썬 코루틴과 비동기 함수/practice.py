# import requests

# def fetcher(session, url):
#     with session.get(url) as response:
#         return response.text

# def main():
#     urls = ["https://www.naver.com", "https://www.google.com", "https://www.instagram.com"] * 10
    
#     with requests.Session() as session:
#         results = [fetcher(session, url) for url in urls]
#         print(results)

# if __name__ == "__main__":
#     main()

import aiohttp
import asyncio

async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://www.naver.com", "https://www.google.com", "https://www.instagram.com"] * 10
    
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)

if __name__ == "__main__":
    asyncio.run(main())