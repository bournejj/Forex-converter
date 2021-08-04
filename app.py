
import decimal
from flask import Flask, request, jsonify, render_template, redirect, flash
from flask.helpers import get_flashed_messages, url_for
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes, CurrencyRates, RatesNotAvailableError
from decimal import *

# forex_converter = Converter()

app = Flask(__name__)
app.config['SECRET_KEY'] = "MyApp"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

cc = CurrencyCodes()

cr = CurrencyRates()

@app.route('/')
def home_page():

    to_currency = request.args.get('to_currency', "")
    from_currency = request.args.get('from_currency',"" )
    amount = request.args.get('amount', "")
    return render_template("home.html", to_currency=to_currency, from_currency=from_currency, amount=amount)


@app.route('/get_data')
def get_currency():

        to_currency = request.args['to-currency']
        from_currency = request.args['from-currency']
        amount = request.args['amount']
        result = ""
        symbol = ""

        errors = list()

        try:
        
            Decimal(amount)

        except :
            errors.append(f"Not a vailid amount: {amount} ")
            flash(f"Not a vailid amount: {amount} ")

         

        try:
            cr.get_rates(to_currency)
           
        except:
           errors.append(f"Not a vailid currency: {to_currency} ")
           flash(f"Not a vailid currency: {to_currency} ")

        try:
            cr.get_rates(from_currency)
           
        except:
            errors.append(f"Not a vailid currency: {from_currency} ")
            flash(f"Not a vailid currency: {from_currency} ")

        try:

            newAmount = float(int(amount))
            result = round((cr.convert(from_currency,to_currency, newAmount)), 2)
            symbol = cc.get_symbol(to_currency)

        except:
            errors.append(f"We could not convert" )
            flash(f"We could not convert" )

    
        
           
        if get_flashed_messages():
            flash(errors)
            
            return redirect(url_for("home_page", to_currency=to_currency, from_currency=from_currency, amount=amount))
            
            
        return render_template("get_currency.html", result=result, symbol = symbol)

        # except (ValueError, TypeError):
        #     # flash("Not a valid amount", 'error')
        #     # return redirect('/')


 