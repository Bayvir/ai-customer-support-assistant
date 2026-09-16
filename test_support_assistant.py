from support_assistant import analyze_customer_message


def test_password_issue():
    result = analyze_customer_message("I cannot login because I forgot my password.")
    assert "Account / Login" in result
    assert "Medium" in result


def test_refund_issue():
    result = analyze_customer_message("I want my money back.")
    assert "Refund" in result
    assert "High" in result


def test_delivery_issue():
    result = analyze_customer_message("My order has not arrived.")
    assert "Order / Delivery" in result
    assert "Medium" in result


def test_general_issue():
    result = analyze_customer_message("I have a question about your service.")
    assert "General Support" in result
    assert "Low" in result
