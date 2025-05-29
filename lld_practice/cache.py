from typing import Any, Dict, Optional, Protocol, Tuple


class CacheInterface(Protocol):
    def get(self, key: str) -> Tuple[Optional[Any], bool]:
        ...
    
    def set(self, key: str, value: Any) -> None:
        ...
        

# Impl:
class InMemoryCache:
    def __init__(self, capacity: int):
        self.cache: Dict[str, Any] = {}
        self.cap = capacity
        
    def get(self, key: str) -> Tuple[Optional[Any], bool]:
        if key in self.cache:
            return self.cache[key], True
        return None, False
    
    def set(self, key: str, value: Any) -> None:
        self.cache[key] = value
    