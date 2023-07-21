import requests

class DadJoke():
    def __init__(self, return_type):
        self.api_url = 'https://icanhazdadjoke.com/'
        self.return_type = return_type
        if self.return_type == "json":
            self.headers = {"Accept": "application/json"}
        elif self.return_type == "text":
            self.headers = {"Accept": "text/plain"}
        else:
            print("invalid return type. Please pass either text or json.")
            self.headers = None

    def randomjoke(self):
        response = requests.get(self.api_url, headers=self.headers)
        if self.return_type == "json":
            return response.json()
        elif self.return_type == "text":
            return response.content.decode()
        else:
            print("Invalid header type")
    
    def search(self, query: str, page=1, limit=20):
        params = {
            "term": query,
            "page": page,
            "limit": limit}
        response = requests.get(f'{self.api_url}/search', headers=self.headers, params=params)
        if self.return_type == "json":
            return response.json()
        elif self.return_type == "text":
            return response.content.decode()
        else:
            print("Invalid header type")