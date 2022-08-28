from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter():
    print(request.method)
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
