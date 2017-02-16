from avatar_generator import Avatar
from flask import Flask, make_response
app = Flask(__name__)

@app.route('/<text>.png')
def example(text):
    text = string[0:2].upper()
    avatar = Avatar.generate(500, 255, text, 'PNG')
    headers = { 'Content-Type': 'image/png' }
    return make_response(avatar, 200, headers)

if __name__ == "__main__":
    app.run()
