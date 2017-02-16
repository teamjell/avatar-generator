from avatar_generator import Avatar
from flask import Flask, make_response
app = Flask(__name__)

@app.route('/<name>.png')
def example(name):
    avatar = Avatar.generate(500, 255, name, 'PNG')
    headers = { 'Content-Type': 'image/png' }
    return make_response(avatar, 200, headers)

if __name__ == "__main__":
    app.run()
