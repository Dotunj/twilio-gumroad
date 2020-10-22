import os
from flask import Flask, request, Response
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

app = Flask(__name__)

twilio_client = Client()

@app.route('/incoming/sales', methods=['POST'])
def send_sms():
    product_name= request.form['product_name']
    message= f"Hello, you just made a Sale! Your product {product_name} was just purchased on Gumroad!"
    twilio_from = os.getenv("TWILIO_NUMBER")
    to_phone_number = os.getenv("TO_PHONE_NUMBER")
    twilio_client.messages.create(body=message, from_=f"{twilio_from}", to=f"{to_phone_number}")
    return Response()

if __name__ == '__main__':
    app.run()

