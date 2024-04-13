from azure.identity import DefaultAzureCredential

class AzureClient(object):
    def __init__(self):
        self.credential = DefaultAzureCredential()

    def authenticate(self):
        token = self.credential.get_token('https://management.azure.com/.default')
        return token.token

# Create an AzureClient instance
client = AzureClient()

# Authenticate and get the token
token = client.authenticate()
print(token)
    