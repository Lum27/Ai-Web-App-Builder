from flask import Blueprint, request
import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

stripe_webhook = Blueprint('stripe_webhook', __name__)

@stripe_webhook.route("/webhook", methods=["POST"])
def webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = os.getenv("STRIPE_SIGNING_SECRET")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError:
        return "Invalid signature", 400

    event_type = event["type"]

    if event_type == "invoice.payment_failed":
        customer_id = event["data"]["object"]["customer"]
        # TODO: mark user as frozen in DB or file
        print(f"Freeze account: {customer_id}")

    elif event_type == "invoice.payment_succeeded":
        customer_id = event["data"]["object"]["customer"]
        # TODO: unfreeze user
        print(f"Unfreeze account: {customer_id}")

    return "OK", 200
