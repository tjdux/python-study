import time
import os
import threading
import requests

def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url: {url}")
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://www.google.com", "https://apple.com"] * 10
    
    with requests.Session() as session:
        results = [fetcher(session, url) for url in urls]
        

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"소요 시간: {end-start}") # 5