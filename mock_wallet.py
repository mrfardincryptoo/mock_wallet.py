import secrets

def generate_mock_address():
    # Generate a random 40-character hex string prefixed with 0x
    return "0x" + secrets.token_hex(20)

print(f"Test Wallet Address: {generate_mock_address()}")
