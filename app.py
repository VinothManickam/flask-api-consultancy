from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()


NOTION_KEY = os.environ.get("NOTION_KEY")
NOTION_RESUME_DATABASE_ID = os.environ["NOTION_RESUME_DATABASE_ID"]


# ... (Your existing code remains unchanged)

def fetch_companies_by_consultancy_name(consultancy_name):
    url = f"https://api.notion.com/v1/databases/{NOTION_RESUME_DATABASE_ID}/query"
    headers = {
        'Authorization': f'Bearer {NOTION_KEY}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    payload = {
        "filter": {
            "property": "ConsultancyName",
            "rich_text": {
                "contains": consultancy_name
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def fetch_companies_by_jobs_offered(jobs_offered):
    url = f"https://api.notion.com/v1/databases/{NOTION_RESUME_DATABASE_ID}/query"
    headers = {
        'Authorization': f'Bearer {NOTION_KEY}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    payload = {
        "filter": {
            "property": "JobsOffered",
            "rich_text": {
                "contains": jobs_offered
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

@app.route('/company', methods=['GET'])
def get_company():
    consultancy_name = request.args.get('ConsultancyName')
    jobs_offered = request.args.get('JobsOffered')

    if consultancy_name:
        data = fetch_companies_by_consultancy_name(consultancy_name)
    elif jobs_offered:
        data = fetch_companies_by_jobs_offered(jobs_offered)
    else:
        return jsonify({"message": "Invalid query parameters"}), 400

    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "No data found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
