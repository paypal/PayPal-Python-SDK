from paypalrestsdk import BillingAgreement
import logging

BILLING_AGREEMENT_ID = "I-HT38K76XPMGJ"

try:
    billing_agreement = BillingAgreement.find(BILLING_AGREEMENT_ID)
    print("Billing Agreement [%s] has outstanding balance %s" % (
        billing_agreement.id, billing_agreement.outstanding_balance.value))

    outstanding_amount = {
        "value": "4500",
        "currency": "USD"
    }

    if billing_agreement.set_balance(outstanding_amount):
        billing_agreement = BillingAgreement.find(BILLING_AGREEMENT_ID)
        print("Billing Agreement [%s] has outstanding balance %s" % (
            billing_agreement.id, billing_agreement.outstanding_balance.value))

        outstanding_amount_note = {
            "note": "Billing Balance Amount",
            "amount": outstanding_amount
        }

        if billing_agreement.bill_balance(outstanding_amount_note):
            billing_agreement = BillingAgreement.find(BILLING_AGREEMENT_ID)
            print("Billing Agreement [%s] has outstanding balance %s" % (
                billing_agreement.id, billing_agreement.outstanding_balance.value))

        else:
            print(billing_agreement.error)

    else:
        print(billing_agreement.error)

except ResourceNotFound as error:
    print("Billing Agreement Not Found")
