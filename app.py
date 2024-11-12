from flask import Flask, render_template_string

app = Flask(__name__)

# Define a simple HTML template as a string
html_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Flask App</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            color: #333;
        }
        .container {
            text-align: center;
            border: 2px solid #4CAF50;
            border-radius: 8px;
            padding: 20px;
            background-color: white;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4CAF50;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Devops lifecycle automation</h1>
        <p>Welcome to my awesome Flask application running in Docker.</p>
        <p>Feel free to explore!</p>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

