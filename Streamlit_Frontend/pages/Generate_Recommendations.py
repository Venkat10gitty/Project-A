import requests
import json

# class Generator:
#     def __init__(self,nutrition_input:list,ingredients:list=[],params:dict={'n_neighbors':5,'return_distance':False}):
#         self.nutrition_input=nutrition_input
#         self.ingredients=ingredients
#         self.params=params

#     def set_request(self,nutrition_input:list,ingredients:list,params:dict):
#         self.nutrition_input=nutrition_input
#         self.ingredients=ingredients
#         self.params=params

#     def generate(self,):
#         request={
#             "nutrition_input":self.nutrition_input,
#             "ingredients":self.ingredients,
#             "params":self.params
#         }
#         response=requests.post(url='http://localhost:8000/predict/',data=json.dumps(request))
#         return response
# class Generator:
#     def __init__(self, nutrition_input: list, ingredients: list = [], params: dict = {'n_neighbors': 5, 'return_distance': False}):
#         self.nutrition_input = nutrition_input
#         self.ingredients = ingredients
#         self.params = params

#     def set_request(self, nutrition_input: list, ingredients: list, params: dict):
#         self.nutrition_input = nutrition_input
#         self.ingredients = ingredients
#         self.params = params

#     def generate(self):
#         request = {
#             "nutrition_input": self.nutrition_input,
#             "ingredients": self.ingredients,
#             "params": self.params
#         }
#         response = requests.post(url='http://localhost:8000/predict/', data=json.dumps(request))

        # if response.status_code == 200:
        #     try:
        #         return response.json()
        #     except json.decoder.JSONDecodeError:
        #         return {"error": "The response from the server is not in JSON format."}
        # else:
        #     return {"error": f"The server returned an error: {response.status_code} {response.reason}."}
import requests
import json

class Generator:
    def __init__(self, nutrition_input:list, ingredients:list=[], params:dict={'n_neighbors':5,'return_distance':False}):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def set_request(self, nutrition_input:list, ingredients:list, params:dict):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def generate(self):
        request = {
            "nutrition_input": self.nutrition_input,
            "ingredients": self.ingredients,
            "params": self.params
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url='http://localhost:8080/predict/', json=request, headers=headers)
        #response = requests.post(url='http://127.0.0.1:8000/predict/', json=request, headers=headers)
        #response=requests.post(url='http://backend:8080/predict/',data=json.dumps(request))
        if response.status_code == 200:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                return {"error": "The response from the server is not in JSON format."}
        else:
            return {"error": f"The server returned an error: {response.status_code} {response.reason}."}
