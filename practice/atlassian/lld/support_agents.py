from typing import Protocol
from dataclasses import dataclass
from typing_extensions import Literal


@dataclass
class Agent:
    id: str

@dataclass(frozen=True)
class CustomerSupportAgentSubmitRatingRequest:
    agent_id: str
    score: int

    def __post_init__(self):
        if not 1 <= self.score <= 5:
            raise ValueError(f'Score value can only be from 1 to 5, got: {self.score}')


@dataclass(frozen=True)
class CustomerSupportAgentSubmitRatingResponse:
    status: Literal['success', 'failure']

@dataclass(frozen=True)
class CustomerSupportAgentRankedResponse:
    ranked: list[Agent]

class CustomerSupportAgentService(Protocol):
    def submit_rating(
            self, 
            request: CustomerSupportAgentSubmitRatingRequest
        ) -> CustomerSupportAgentSubmitRatingResponse:
        ...

    def get_agents_ranked() -> CustomerSupportAgentRankedResponse:
        ...


class CustomerSupportAgentServiceImpl:
    def __init__(self):
    def submit_rating(
            self, 
            request: CustomerSupportAgentSubmitRatingRequest
        ) -> CustomerSupportAgentSubmitRatingResponse:    

        