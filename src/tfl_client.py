import httpx

class TflClient:
    def __init__(self, client: httpx.Client):
        self.client = client

    def get_tube_statuses(self) -> list[dict]:
        response = self.client.get(
            "https://api.tfl.gov.uk/Line/Mode/tube/Status"
        )
        response.raise_for_status()
        return response.json()
