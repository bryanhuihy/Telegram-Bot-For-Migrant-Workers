from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'I love Prof Andrew'

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    if data['queryResult']['parameters']['number']:
        monthly_basic_pay = data['queryResult']['parameters']['number']
        ot_pay = ot_calculation(monthly_basic_pay)
        response = {
            'fulfillmentText':"Your hourly OT pay should be ${}\n What else would you like to know?".format(ot_pay)
        }
    
    if data['queryResult']['parameters']['currency-from']:
        source_currency = data['queryResult']['parameters']['currency-from']
        amount = data['queryResult']['parameters']['amount']
        target_currency = data['queryResult']['parameters']['currency-to']
        cf = fetch_conversion_factor(source_currency,target_currency)
        final_amount = amount * cf
        final_amount = round(final_amount,2)
        response = {
            'fulfillmentText':"${} {} is ${} {}\n What else would you like to know?".format(amount,source_currency,final_amount,target_currency)
        }
    
    return jsonify(response)

def ot_calculation(monthly_basic_pay):
    hourly_basic_pay = (12 * float(monthly_basic_pay)) / (52 * 44)
    hourly_ot_pay = hourly_basic_pay * 1.5
    return('{0:.2f}'.format(hourly_ot_pay))

def fetch_conversion_factor(source,target):

    url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=9aa0c54f5ad4c460c36d".format(source,target)

    response = requests.get(url)
    response = response.json()

    return response['{}_{}'.format(source,target)]

if __name__ == "__main__":
    app.run(debug=True)