from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/consultancy_database', methods=['GET'])
def get_consultancy_database():
    url = "https://api.notion.com/v1/databases/a197366da7b1482d981f52d0e433a750"
    headers = {
        'Authorization': 'Bearer secret_Mzoz4xIINL6LBasTElU4cVikpdm18NtHaZzxHWB5CXQ',
        'Notion-Version': '2022-06-28',
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"message": "Error occurred while fetching data"}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)