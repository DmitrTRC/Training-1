import requests

url = "https://twinword-word-association-quiz.p.rapidapi.com/type1/"

querystring = {"level": "3", "area": "sat"}

headers = {
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "twinword-word-association-quiz.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
