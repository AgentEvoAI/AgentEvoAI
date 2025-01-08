import React, { useState } from "react";

const Verify = () => {
    const [status, setStatus] = useState("");
    const [userId, setUserId] = useState("");
    const [inputData, setInputData] = useState("");

    const handleVerification = async () => {
        try {
            const response = await fetch("/api/verify", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user_id: userId, input_data: inputData }),
            });
            const result = await response.json();
            setStatus(result.status);
        } catch (error) {
            setStatus("Verification failed.");
        }
    };

    return (
        <div>
            <h1>Verify Identity</h1>
            <input
                type="text"
                placeholder="User ID"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
            />
            <textarea
                placeholder="Input Data"
                value={inputData}
                onChange={(e) => setInputData(e.target.value)}
            />
            <button onClick={handleVerification}>Verify</button>
            <p>{status}</p>
        </div>
    );
};

export default Verify;
