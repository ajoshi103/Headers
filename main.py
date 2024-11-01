from flask import Flask, render_template_string
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    # The API endpoint and data to post
    url = "https://chimpu.online/api/post.php"
    # Get the phone number from environment variables
    phone_number = os.getenv('PHONE_NUMBER', '1234567890')  # Default for testing
    payload = {'phonenumber': phone_number}  # Use the phone number from environment variable

    # Send POST request and get headers
    response = requests.post(url, data=payload)
    headers = response.headers

    # Render headers in an HTML template
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Headers Display</title>
    </head>
    <body>
        <h2>Headers received from the API:</h2>
        <ul>
            {% for key, value in headers.items() %}
                <li><strong>{{ key }}:</strong> {{ value }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    ''', headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
