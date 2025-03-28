from flask import Flask
from datetime import datetime

app = Flask(__name__)
start = datetime.now()

@app.route('/health')
def health():
    return {'nama': 'Muhammad Nabil Afrizal Rahmadani',
            'nrp': '5025231014',
            'status': 'UP',
            'timestamp': datetime.now(),
            'uptime': str(datetime.now() - start)
            }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)