from flask import Flask

app = Flask(__name__)

@app.route('/<format>')
def fast(format="html"):
    if format=="html":
        return "<h1>HELLO</H1>"
    else:
        return "Not html"

from subapi import SubAPI as another_api
app.register_blueprint(another_api.api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)