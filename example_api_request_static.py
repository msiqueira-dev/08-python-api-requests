import requests

class Model_Api_Static():
    """ 
        PT-BR:
            Isso é um comentário padrão de classe e será ignorado pelo Python
            A classe Model_Api_Static é uma classe que tem como propósito ter métodos que fazem requisições não genéricas a APIs.
        EN: 
            This is a function comment and will be ignored by Python.
            The class Model_Api_Static is a class that has the porpuse of having functions that can make non dynamic API calls.
    """
    def get(self, url):
        """ 
        PT-BR:
            Isso é um comentário padrão de classe e será ignorado pelo Python
            Faz uma requisição a uma API em método get, de forma básica, sem muitos tratamentos a um endereço fornecido.
        EN: 
            This is a function comment and will be ignored by Python.
            Make an API request with the method get, with basic treatement on a provided address.
        """
        if url is None:
            print('Empty url')
            return None
        response = requests.get(url)
        if response:
            if response.status_code:
                if response.status_code == 200:
                    return response.json()
            print('Error in the API response')
        return None


url = 'https://api.discogs.com/artists/14651/releases?page=1&per_page=1'
model_api_obj = Model_Api_Static()
content = model_api_obj.get(url)

print(content)
print(content["releases"])
print('------------')
print('------------')
print('------------')
print(content['releases'][0]['artist'])
print(content['releases'][0]['title'])
print(content['releases'][0]['year'])