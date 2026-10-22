"""
Question:
The candidate must build an in-memory rate limiter that enforces request limits on a per-customer basis using the method interface boolean allowRequest(String customerId) to implement an initial policy of $X$ requests per $Y$ seconds. 
As follow-up requirements are introduced, the candidate must transition the underlying strategy from a basic Fixed Window Counter to a Sliding Window Log or Token Bucket to eliminate traffic spikes at window boundaries.
The requirements then expand to include a credit rollover system where unused capacity within a window is credited toward handling future traffic bursts. Finally, the candidate must adapt the implementation to run safely in a multi-threaded environment using synchronization locks or thread-safe atomic references.
"""

"""
RateLimiter

request -> rate_limiter -> rate limiter strategy


rate_limiter -> policy





"""

import datetime
import time
from collections import defaultdict
from dataclasses import dataclass
from typing import Protocol


# DTOs:
@dataclass(frozen=True)
class CustomerRequest:
    customer_id: str


@dataclass(frozen=True)
class CustomerResponse:
    allowed: bool


# Protocol - Interfaces:
class RateLimiter(Protocol):
    def allow_request(self, request: CustomerRequest) -> CustomerResponse:
        ...


class RateLimiterStrategy(Protocol):
    def allow_request(self, request: CustomerRequest) -> CustomerResponse:
        ...


# Implementations:
@dataclass(frozen=True)
class WindowRateLimitConfig:
    no_of_requests: int
    time_frame: int


class FixedWindowRateLimiterStrategy:
    def __init__(self, config: WindowRateLimitConfig):
        self._config = config
        self.mp = defaultdict(lambda: defaultdict(int)) # seconds -> user_id -> count

    def allow_request(self, request: CustomerRequest) -> CustomerResponse:
       # Get current date and time
        now = datetime.datetime.now()

        # Format to show only Hours:Minutes:Seconds
        current_time = now.strftime("%H:%M:%S")
        self.mp[current_time][request.customer_id] += 1

        if self.mp[current_time][request.customer_id] > self._config.no_of_requests:
            return CustomerResponse(allowed=False)

        return CustomerResponse(allowed=True)
       


# Main Rate limiter service:
class APIRateLimiterService:
    def __init__(self, rate_limiter_strategy: RateLimiterStrategy):
        self._strategy = rate_limiter_strategy

    def allow_request(self, request: CustomerRequest) -> CustomerResponse:
        try:
            response = self._strategy.allow_request(request)
            return response
        except Exception as e:
            print(e)
            raise



if __name__ == "__main__":
    config = WindowRateLimitConfig(3, 1)
    strategy = FixedWindowRateLimiterStrategy(config=config)
    rate_limiter = APIRateLimiterService(rate_limiter_strategy=strategy)

    # Test:
    request = CustomerRequest(customer_id='12345')
    print(rate_limiter.allow_request(request=request)) # true
    print(rate_limiter.allow_request(request=request)) # true
    print(rate_limiter.allow_request(request=request)) # true
    print(rate_limiter.allow_request(request=request)) # false

    print('sleeping')
    time.sleep(1)
    print(rate_limiter.allow_request(request=request)) # true    