class InteractionAPI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key  # API key for accessing the drug interaction API
        self.base_url = base_url  # The base URL of the API

    def fetch_interaction(self, drug1, drug2):
        # Logic to send an API request to check for drug interactions
        url = f"{self.base_url}?drug1={drug1.name}&drug2={drug2.name}&api_key={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # Parse the API response and create an Interaction instance
            interaction_type = data.get("interaction_type", "Unknown")
            description = data.get("description", "No details available")
            return Interaction(drug1, drug2, interaction_type, description)
        else:
            return None