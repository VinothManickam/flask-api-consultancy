from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Fetch sensitive information from environment variables
NOTION_KEY = 'secret_Mzoz4xIINL6LBasTElU4cVikpdm18NtHaZzxHWB5CXQ'
NOTION_RESUME_DATABASE_ID = 'a197366da7b1482d981f52d0e433a750'


def fetch_consultancy_database():
    url = f"https://api.notion.com/v1/databases/{NOTION_RESUME_DATABASE_ID}"
    headers = {
        'Authorization': f'Bearer {NOTION_KEY}',
        'Notion-Version': '2022-06-28',
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


@app.route('/consultancy_database', methods=['GET'])
def get_consultancy_database():
    data = fetch_consultancy_database()
    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "Error occurred while fetching data"}), 500


def fetch_jobs_offered():
    url = f"https://api.notion.com/v1/databases/Vwqw/query"
    headers = {
        'Authorization': f'Bearer {NOTION_KEY}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    response = requests.post(url, headers=headers, json={})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


@app.route('/jobs_offered', methods=['GET'])
def get_jobs_offered():
    data = fetch_jobs_offered()
    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "Error occurred while fetching data"}), 500


if __name__ == '__main__':
    app.run(debug=True)