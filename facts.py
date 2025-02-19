import requests

###
# Class to handle fetching cat facts from an API
###
class CatFacts:

    # Initialize the CatFacts class with a specific API URL
    def __init__(self):
        self.url = 'https://catfact.ninja/fact'

    # Method to fetch a cat fact from the API
    def get_fact(self) -> None:
        response = requests.get(self.url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract JSON data from the response
            data = response.json()
            print(data["fact"])
        else:
            # Error message if the request was unsuccessful
            print(f"status code: {response.status_code}")

###
# Main
###
if __name__ == "__main__":
    facts = CatFacts()
    facts.get_fact()
