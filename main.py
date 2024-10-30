from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # The API endpoint and data to post
    url = "https://chimpu.online/api/post.php"
    payload = {'phonenumber': '1234567890'}  # Replace with actual phone number

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
