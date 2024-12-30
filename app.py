from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.json.get('from')
    to_currency = request.json.get('to')
    amount = float(request.json.get('amount'))  # Convert to float
    api_key = 'YOUR_API_KEY'

    url = f'https://api.currencyapi.com/v3/latest?apikey={api_key}¤cies={to_currency}&base_currency={from_currency}'
    response = requests.get(url)
    data = response.json()
    
    if 'data' in data and to_currency in data['data']:
        rate = data['data'][to_currency]['value']
        converted_amount = amount * float(rate)  # Ensure rate is a float
        return jsonify({'converted_amount': converted_amount, 'rate': rate})
    else:
        return jsonify({'error': 'Conversion not available'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)