def analyze_customer_message(message):
    message_lower = message.lower()

    if "password" in message_lower or "login" in message_lower:
        category = "Account / Login"
        priority = "Medium"
        action = "Check the customer's account and assist with password recovery."

    elif "refund" in message_lower or "money back" in message_lower:
        category = "Refund"
        priority = "High"
        action = "Check the customer's payment and refund status."

    elif "charged" in message_lower or "payment" in message_lower:
        category = "Payment / Billing"
        priority = "High"
        action = "Review the customer's payment transaction."

    elif "delivery" in message_lower or "order" in message_lower:
        category = "Order / Delivery"
        priority = "Medium"
        action = "Check the customer's order and delivery status."

    else:
        category = "General Support"
        priority = "Low"
        action = "Review the request and determine the appropriate support department."

    response = f"""
Customer Support Analysis
--------------------------

Category: {category}
Priority: {priority}

Suggested Response:
Thank you for contacting us. We understand your concern regarding your request.
Our support team will review the issue and assist you as soon as possible.

Recommended Action:
{action}
"""

    return response


if __name__ == "__main__":
    customer_message = input("Enter the customer's message: ")
    result = analyze_customer_message(customer_message)
    print(result)
