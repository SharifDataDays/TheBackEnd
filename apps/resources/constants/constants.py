from dataclasses import dataclass

api_token = 'if@1030!asjdfcc0e$paipofjip00qu2'


@dataclass
class ApiToken:
    api_token: str


api_tokens = ApiToken(api_token)