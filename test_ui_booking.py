

def test_submit_message(start_page):
    """
    1. Fill contact form.
    2. Click on Submit button.
    3. Validate according confirmation message on the page.
    4. Validate according POST request with test data was sent from client to server.
    """
    start_page.submit_message()
    start_page.validate_message_submit()
