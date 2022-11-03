# import os
# import telebot
# from dotenv import load_dotenv
from flask import Flask, request, jsonify
# import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    monthly_basic_pay = data['queryResult']['parameters']['number']


    ot_pay = ot_calculation(monthly_basic_pay)
    response = {
        'fulfillmentText':"Your hourly OT pay should be {}".format(ot_pay)
    }
    return jsonify(response)

def ot_calculation(monthly_basic_pay):
    hourly_basic_pay = (12 * float(monthly_basic_pay)) / (52 * 44)
    hourly_ot_pay = hourly_basic_pay * 1.5
    return('{0:.2f}'.format(hourly_ot_pay))

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