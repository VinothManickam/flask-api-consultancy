from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get-companies-by-job', methods=['GET'])
def get_companies_by_job():
    job_title = request.args.get('jobTitle')

    if job_title:
                integration_token = 'secret_PEaWTQb12wSvcDdVKnSuNeufcHFIS6Ltod1bUs1JpRf'

        # Replace this with the URL to your Notion database
        database_url = 'https://www.notion.so/Consultancy-Database-f922d1a720d0472ebfa56c2e25154e01'

        headers = {
            'Authorization': f'Bearer {integration_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'jobTitle': job_title,
        }

        response = requests.get(database_url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            # Process the data from the response
            companies = data['companies']
            return jsonify({"companies": companies}), 200
        else:
            return jsonify({"message": "Error fetching data from Notion."}), response.status_code

    else:
        return jsonify({"message": "Please provide a job title in the query parameters."}), 400

if __name__ == '__main__':
    app.run(debug=True)
