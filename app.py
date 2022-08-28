from flask import Flask, render_template, request

app = Flask(__name__)

statistics_data = {
    'GET': 0,
    'POST': 0
}

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter():
    dictionary_key = request.method
    statistics_data[dictionary_key] += 1
    return render_template('main.html')


@app.route('/statistics')
def statistics():
    return render_template('statistics.html', data=statistics_data)


if __name__ == '__main__':
    app.run()
