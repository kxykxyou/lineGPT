from flask import Flask, request
import os, openai

openai.api_key: str = os.getenv("OPENAI_ACCESS_KEY")
CHATBOT_API: str = "https://api.openai.com/v1/engines/davinci-codex/completions"

app: Flask = Flask(__name__)


@app.route("/chatbot", methods=["POST"])
def chatbot() -> str:
    response = openai.Completion.create(
        model="text-davinci-003", prompt=request.json["message"], max_tokens=2048
    )
    print("request: ", request)
    print("type: ", type(response))

    return response.choices[0].text


if __name__ == "__main__":
    app.run(debug=True, port=5050)
