from concurrent.futures import ThreadPoolExecutor
from typing import Protocol
import requests

class CacheInterface(Protocol):
    def set(self, key: str, val: str) -> None:
        ...

    def get(self, key: str) -> tuple[bool, str]:
        ...

class InMemoryCache(Protocol):
    def __init__(self):
        self.mp = {}

    def set(self, key: str, val: str) -> None:
        self.mp[key] = val

    def get(self, key: str) -> tuple[bool, str]:
        if key in self.mp:
            return True, self.mp[key]
        return False, ''

class ProxyServer(Protocol):
    def fetch(self, url: str) -> dict | str:
        ...

class ProxyServerImpl:
    def __init__(self, cache: CacheInterface):
        self.cache = None
        if cache is not None:
            self.cache = cache
    
    def fetch(self, url: str) -> dict | str:
        # Check in cache first:
        if self.cache:
            found, val = self.cache.get(url)
            if found:
                return val
            
        response = requests.get(url=url)
        # Try a json response:
        try:
            resp = response.json()
            return self._cache_and_return(url, resp)
        except requests.JSONDecodeError:
            resp = response.text
            return self._cache_and_return(url, resp)
        except Exception as e:
            print(f'Got an exception while fetching url: {url}, exc:', e)
            return None

    def submit_batch(self, urls: list[str], workers: int = 5) -> list[dict | str | None]:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            return list(pool.map(self.fetch, urls))

    def _cache_and_return(self, url: str, val: str) -> str:
        if self.cache is not None:
            self.cache.set(url, val)
        return val


# Driver function:
def main():
    cache: CacheInterface = InMemoryCache()
    proxy_server: ProxyServer = ProxyServerImpl(cache=cache)
    urls: list[str] = [
        'https://atlassian.com/',
        'https://atlassian.com/',
    ]
    for url in urls:
        response = proxy_server.fetch(url=url)
        print(f'url: {url}\nResponse:{response}')

if __name__ == '__main__':
    main()
