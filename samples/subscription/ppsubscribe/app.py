# Flask application for a developer/merchant working with the subscription apis

from flask import Flask, session, render_template, url_for, redirect, request, flash, g
from paypalrestsdk import BillingPlan, BillingAgreement, configure
from datetime import datetime, timedelta
import paypal_config
import logging
import os

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Merchant and User login for the app
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='secret',
    MERCHANT_USERNAME='merchant',
    MERCHANT_PASSWORD='mpass',
    CUSTOMER_USERNAME='customer',
    CUSTOMER_PASSWORD='cpass'
))

# Initialize PayPal sdk
configure({
    "mode": paypal_config.MODE,
    "client_id": paypal_config.CLIENT_ID,
    "client_secret": paypal_config.CLIENT_SECRET
})


@app.route("/")
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if session.get('merchant'):
            return redirect(url_for('admin'))
        elif session.get('customer'):
            return redirect(url_for('subscriptions'))


@app.route("/create", methods=['GET', 'POST'])
def create():
    """Merchant creates new billing plan from input values in the form
    """
    if session.get('logged_in') and session.get('merchant'):
        if request.method == 'POST':
            billing_plan_attributes = {
                "name": request.form['name'],
                "description": request.form['description'],
                "merchant_preferences": {
                    "auto_bill_amount": "yes",
                    "cancel_url": "http://www.cancel.com",
                    "initial_fail_amount_action": "continue",
                    "max_fail_attempts": "1",
                    "return_url": request.form['return_url'],
                    "setup_fee": {
                        "currency": request.form['currency'],
                        "value": request.form['setup_fee']
                    }
                },
                "payment_definitions": [
                    {
                        "amount": {
                            "currency": request.form['currency'],
                            "value": request.form['amount']
                        },
                        "charge_models": [
                            {
                                "amount": {
                                    "currency": request.form['currency'],
                                    "value": request.form['shipping']
                                },
                                "type": "SHIPPING"
                            },
                            {
                                "amount": {
                                    "currency": request.form['currency'],
                                    "value": request.form['tax']
                                },
                                "type": "TAX"
                            }
                        ],
                        "cycles": request.form['cycles'],
                        "frequency": request.form['frequency'],
                        "frequency_interval": request.form['frequency_interval'],
                        "name": request.form['payment_name'],
                        "type": request.form['payment_type']
                    }
                ],
                "type": request.form['type']
            }
            billing_plan = BillingPlan(billing_plan_attributes)
            if billing_plan.create():
                print(
                    "Billing Plan [%s] created successfully" % (billing_plan.id))
            else:
                print(billing_plan.error)
            return redirect(url_for('admin'))
        return render_template('create.html')
    else:
        return redirect(url_for('login'))


@app.route("/activate", methods=['POST'])
def activate():
    """Merchant activates plan after creation
    """
    if session.get('logged_in') and session.get('merchant'):
        billing_plan = BillingPlan.find(request.args.get('id', ''))
        if billing_plan.activate():
            print("Billing Plan [%s] activated successfully" %
                  (billing_plan.id))
        else:
            print(billing_plan.error)
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


@app.route("/subscribe", methods=['POST'])
def subscribe():
    """Customer subscribes to a billing plan to form a billing agreement
    """
    if session.get('logged_in') and session.get('customer'):
        billing_agreement = BillingAgreement({
            "name": "Organization plan name",
            "description": "Agreement for " + request.args.get('name', ''),
            "start_date": (datetime.utcnow() + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "plan": {
                "id": request.args.get('id', '')
            },
            "payer": {
                "payment_method": "paypal"
            },
            "shipping_address": {
                "line1": "StayBr111idge Suites",
                "line2": "Cro12ok Street",
                "city": "San Jose",
                "state": "CA",
                "postal_code": "95112",
                "country_code": "US"
            }
        })
        if billing_agreement.create():
            for link in billing_agreement.links:
                if link.rel == "approval_url":
                    approval_url = link.href
                    return redirect(approval_url)
        else:
            print(billing_agreement.error)
        return redirect(url_for('subscriptions'))
    else:
        return redirect(url_for('login'))


@app.route("/execute")
def execute():
    """Customer redirected to this endpoint by PayPal after payment approval
    """
    if session.get('logged_in') and session.get('customer'):
        payment_token = request.args.get('token', '')
        billing_agreement_response = BillingAgreement.execute(payment_token)
        return redirect(url_for('agreement_details', id=billing_agreement_response.id))
    else:
        return redirect(url_for('login'))


@app.route("/agreement-details")
def agreement_details():
    billing_agreement = BillingAgreement.find(request.args.get('id', ''))
    return render_template('details.html', agreement=billing_agreement)


@app.route("/payment-history")
def transactions():
    """Display transactions that happened over a billing agreement
    """
    start_date, end_date = "2014-07-01", "2014-07-20"
    billing_agreement = BillingAgreement.find(request.args.get('id', ''))
    transactions = billing_agreement.search_transactions(start_date, end_date)
    return render_template('history.html', transactions=transactions.agreement_transaction_list, description=request.args.get('description', ''))


@app.route("/admin")
def admin():
    """If merchant is logged in display billing plans in created and active states
    """
    if session.get('logged_in') and session.get('merchant'):
        plans_created_query_dict = BillingPlan.all({"status": "CREATED",
                                                    "sort_order": "DESC"})
        plans_created = plans_created_query_dict.to_dict().get('plans')
        if not plans_created:
            plans_created = []

        plans_active_query_dict = BillingPlan.all({"status": "ACTIVE",
                                                   "page_size": 5, "page": 0, "total_required": "yes"})
        plans_active = plans_active_query_dict.to_dict().get('plans')
        if not plans_active:
            plans_active = []

        return render_template('admin.html', plans_created=plans_created, plans_active=plans_active)
    else:
        return redirect(url_for('login'))


@app.route("/subscriptions")
def subscriptions():
    """If customer is logged in display active billing plans in
    descending order of creation time
    """
    if session.get('logged_in') and session.get('customer'):

        plans_active_query_dict = BillingPlan.all({"status": "ACTIVE",
                                                   "sort_order": "DESC"})

        if plans_active_query_dict:
            plans_active = plans_active_query_dict.to_dict().get('plans')
        else:
            plans_active = []
        return render_template('subscriptions.html', plans=plans_active)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == app.config['MERCHANT_USERNAME'] and request.form['password'] == app.config['MERCHANT_PASSWORD']:
            session['logged_in'] = True
            session['merchant'] = True
            return redirect(request.args.get('next') or url_for('admin'))
        elif request.form['username'] == app.config['CUSTOMER_USERNAME'] and request.form['password'] == app.config['CUSTOMER_PASSWORD']:
            session['logged_in'] = True
            session['customer'] = True
            return redirect(request.args.get('next') or url_for('subscriptions'))
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """Clear session caches when logout is called
    and return to base url
    """
    for key in ('customer', 'merchant', 'logged_in'):
        session.pop(key, None)
    return redirect(request.args.get('next') or '/')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
