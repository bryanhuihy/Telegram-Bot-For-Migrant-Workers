from flask import Flask, request, jsonify
import requests

#To put in .env file
API_KEY = 'N68ZMEuCXO8402w65EdHn9LZfVGaWmyR'

app = Flask(__name__)

@app.route('/')
def home():
    return 'I love Prof Andrew'

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    if 'number' in data['queryResult']['parameters']:
        monthly_basic_pay = data['queryResult']['parameters']['number']
        ot_pay = ot_calculation(monthly_basic_pay)
        response = {
            'fulfillmentText':"Your hourly OT pay should be ${}\nWhat else would you like to know?".format(ot_pay)
        }
    
    if 'currency-from' in data['queryResult']['parameters']:
        source_currency = data['queryResult']['parameters']['currency-from']
        source_currency = round(float(source_currency),2)
        amount = data['queryResult']['parameters']['amount']
        target_currency = data['queryResult']['parameters']['currency-to']
        cf = fetch_conversion_factor(source_currency,target_currency, amount)
        final_amount = round(cf,2)
        response = {
            'fulfillmentText':"${} {} is ${} {}\nWhat else would you like to know?".format(amount,source_currency,final_amount,target_currency)
        }
    
    return jsonify(response)

def ot_calculation(monthly_basic_pay):
    hourly_basic_pay = (12 * float(monthly_basic_pay)) / (52 * 44)
    hourly_ot_pay = hourly_basic_pay * 1.5
    return('{0:.2f}'.format(hourly_ot_pay))

def fetch_conversion_factor(source, target, amount):

    url = "https://api.apilayer.com/fixer/convert?to={}&from={}&amount={}".format(target, source, amount)

    payload = {}
    headers= {
        "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()

    return result['result']

if __name__ == "__main__":
    app.run(debug=True)