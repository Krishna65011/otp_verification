# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid ='AC039b0d94c4b55c7da35c7c449513c2ea'
        auth_token = 'd76b9ab62505aed0ebce135187aceb92'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('IS55191f2dd460348ad72e6caf191442d2') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid ='AC039b0d94c4b55c7da35c7c449513c2ea'
    auth_token = 'd76b9ab62505aed0ebce135187aceb92'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('IS55191f2dd460348ad72e6caf191442d2') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')    # Write code here
    else:
        return redirect("https://www.google.com/search?q=google&rlz=1C1RLNS_enIN994IN994&oq=google&aqs=chrome..69i57j46i131i199i433i465i512j69i60l3j69i65l3.2427j0j7&sourceid=chrome&ie=UTF-8")


if __name__ == "__main__":
    app.run()

