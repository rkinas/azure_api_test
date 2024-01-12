from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/get_weekday', methods=['GET'])
def get_weekday():
    date_str = request.args.get('date', default = '', type = str)
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        return jsonify({'weekday': date_obj.strftime('%A')})
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use DD.MM.YYYY'}), 400

if __name__ == '__main__':
    app.run()
