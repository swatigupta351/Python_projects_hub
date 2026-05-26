from flask import Flask

app = Flask(__name__)

@app.route('/tickets', methods=['GET'])
def get_tickets():
    return {
        "ticket_id": 123,
        "status": "closed",
        "title": "Server Down Issue"
    }

if __name__ == '__main__':
    app.run(debug=True , port=5001)