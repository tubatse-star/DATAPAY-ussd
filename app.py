from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "DATAPAY is live! Dial *120*DATAPAY# to use USSD"

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", "")
    text = request.values.get("text", "")
    
    if text == "":
        response = "CON Welcome to DATAPAY\n1. Send Money\n2. Buy Airtime\n3. Check Balance\n4. Pay Bill"
    elif text == "1":
        response = "CON Enter phone number:"
    elif text == "2":
        response = "CON Enter amount for Airtime:"
    elif text == "3":
        response = "END Your DATAPAY balance is R 1,250.00"
    elif text == "4":
        response = "CON Enter account number:"
    elif text.startswith("1*"):
        response = "END Money sent! You will receive SMS confirmation."
    else:
        response = "END Thank you for using DATAPAY"
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
