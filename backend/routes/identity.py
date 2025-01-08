from fastapi import APIRouter, HTTPException
from services.verifier import verify_with_ai, verify_with_blockchain

identity_router = APIRouter()

@identity_router.post("/verify")
async def verify_identity(data: dict):
    user_id = data.get("user_id")
    input_data = data.get("input_data")

    if not user_id or not input_data:
        raise HTTPException(status_code=400, detail="Missing required fields")

    ai_result = verify_with_ai(input_data)
    blockchain_result = verify_with_blockchain(user_id)

    if ai_result and blockchain_result:
        return {"status": "verified"}
    else:
        raise HTTPException(status_code=400, detail="Verification failed")
