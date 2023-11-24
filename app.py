import os
import yaml
import openai
from openai import OpenAI
from flask_cors import CORS
from flask import Flask, request, make_response, jsonify


config = {}
yml_path = os.path.join(os.path.dirname(__file__), 'API_KEY.yml')
with open(yml_path, 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=config['OPENAI_API_KEY'])


def comment_code(language, code):
    prompt = """
    comment this {0} code
    
    {1}
    """.format(language, code)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a skilled code documenter who adds comments to code to make it easier to understand"},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        language = request.form["language"]
        code = request.form["code"]
        commented_code = comment_code(language, code)
        return make_response(jsonify({"commented_code": commented_code}), 201)

    return make_response("OK", 200)


if __name__ == '__main__':
    app.run(debug=True)
