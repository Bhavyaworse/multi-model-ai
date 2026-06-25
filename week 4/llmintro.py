import json

def build_model_completion(user_input, system_personality="Role: QA Diagnostic Operator."):
    payload_dictionary = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": system_personality},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.2
    }
    
    mocked_api_return = {
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Status Update: Analysis verified. Structural elements confirmed operational."
            }
        }]
    }
    
    extracted_string = mocked_api_return["choices"]["message"]["content"]
    return extracted_string

test_string = "Inspect vibration logs for Assembly Line C."
output_summary = build_model_completion(test_string)
print(output_summary)
