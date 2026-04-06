from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/status')
def status():
    return jsonify({
        "status": "up",
        "message": "The server is running smoothly."
    })

@app.route('/api/echo/<message>')
def echo(message):
    return jsonify({
        "received": message,
        "method": "GET"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
