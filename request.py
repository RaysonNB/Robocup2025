from flask import Flask
import requests

app = Flask(__name__)
@app.route("/Fambot")
def testpost_api():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    my_todo = {"Question1":"123","Question2":"nigga","Question3":"555"}
    response = requests.post(api_url, json=my_todo)
    result = response.json()
    return result

if __name__ == "__main__":
    app.run()
    
'''
import requests
r = requests.get("http://127.0.0.1:5000/Fambot",timeout=2.5)
response_data = r.text
print(response_data)
'''
