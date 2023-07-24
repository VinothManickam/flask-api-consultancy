import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

NOTION_KEY = 'secret_PEaWTQb12wSvcDdVKnSuNeufcHFIS6Ltod1bUs1JpRf'
NOTION_RESUME_DATABASE_ID = 'f922d1a720d0472ebfa56c2e25154e01'
NOTION_BASE_URL = 'https://api.notion.com/v1/databases/{}/query'.format(NOTION_RESUME_DATABASE_ID)
HEADERS = {
    'Authorization': 'Bearer {}'.format(NOTION_KEY),
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16',
}
@app.route('/')
def home():
    return "Welcome to the home page!"


@app.route('/company', methods=['GET'])
def get_companies_by_title():
    title = request.args.get('title')
    if not title:
        return jsonify({'error': 'Company title is required.'}), 400

    # Make a request to the Notion API to fetch data from the database
    response = requests.post(NOTION_BASE_URL, headers=HEADERS, json={
        "filter": {
            "property": "Title",
            "text": {
                "contains": title
            }
        }
    })

    # Process the response data and return filtered companies
    if response.status_code == 200:
        data = response.json()
        filtered_companies = [company['properties'] for company in data['results']]
        return jsonify(filtered_companies)
    else:
        return jsonify({'error': 'Failed to fetch data from Notion database.'}), 500

# ... Other routes and functions ...

if __name__ == '__main__':
    app.run(debug=True)
