from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("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")

FINE_TUNED_MODEL = "ftjob-WXHgOJlfgDFSHF9JDcgwZyWS"  # Replace with your fine-tuned model ID
DEFAULT_MODEL = "gpt-4.1-2025-04-14"

def chat_with_assistant(prompt_text):
    try:
        resp = openai.ChatCompletion.create(
            model=FINE_TUNED_MODEL,
            messages=[{'role': 'user', 'content': prompt_text}]
        )
    except openai.error.InvalidRequestError:
        resp = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=[{'role': 'user', 'content': prompt_text}]
        )
    return resp.choices[0].message.content.strip()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    reply = chat_with_assistant(user_input)
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
