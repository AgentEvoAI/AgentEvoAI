import requests

def verify_with_ai(input_data):
    # Call AI model inference
    from ai_model.infer import predict_identity
    return predict_identity(input_data) == 1

def verify_with_blockchain(user_id):
    # Mock blockchain call
    # Replace with actual Solana program interaction
    response = requests.post("http://localhost:8899", json={"user_id": user_id})
    return response.status_code == 200
