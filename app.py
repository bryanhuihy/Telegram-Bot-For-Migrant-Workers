# import os
# import telebot
# from dotenv import load_dotenv
from flask import Flask,request
# import requests

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    
    print(data)
#     source_currency = data['queryResult']['parameters']['unit-currency']['currency']
#     amount = data['queryResult']['parameters']['unit-currency']['amount']
#     target_currency = data['queryResult']['parameters']['currency-name']


#     cf = fetch_conversion_factor(source_currency,target_currency)
#     final_amount = amount * cf
#     final_amount = round(final_amount,2)
#     response = {
#         'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
#     }
#     return jsonify(response)

# def ot_calculation(message):
#     monthly_basic_pay = message.text
#     hourly_basic_pay = (12 * float(monthly_basic_pay)) / (52 * 44)
#     hourly_ot_pay = hourly_basic_pay * 1.5
#     return(hourly_ot_pay)

# def fetch_conversion_factor(source,target):

#     url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=9aa0c54f5ad4c460c36d".format(source,target)

#     response = requests.get(url)
#     response = response.json()

#     return response['{}_{}'.format(source,target)]


if __name__ == "__main__":
    app.run(debug=True)

# load_dotenv()
# API_KEY = os.getenv('API_KEY')
# bot = telebot.TeleBot(API_KEY)

# def OT_calculation(message):
#     monthly_basic_pay = message.text
#     hourly_basic_pay = (12 * float(monthly_basic_pay)) / (52 * 44)
#     hourly_ot_pay = hourly_basic_pay * 1.5
#     return(hourly_ot_pay)


# @bot.message_handler(command=['otcalculator'])
# def otcalculator(message):
#     bot.send_message(message, 'Hello, please type in your monthly basic pay:\n')
#     print(message)


# bot.infinity_polling()