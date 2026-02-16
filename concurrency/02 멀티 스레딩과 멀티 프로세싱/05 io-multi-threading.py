import time
import os
import threading
import requests
from concurrent.futures import ThreadPoolExecutor

def fetcher(params):
    session, url = params
    print(f"{os.getpid()} process | {threading.get_ident()} url: {url}")
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://www.google.com", "https://apple.com"] * 10
    
    executor = ThreadPoolExecutor(max_workers=10) # multi-threading
    
    with requests.Session() as session:
        params = [(session, url) for url in urls]
        list(executor.map(fetcher, params))
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"소요 시간: {end-start}") # 1.9