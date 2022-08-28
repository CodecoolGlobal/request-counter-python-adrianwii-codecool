from flask import Flask, render_template, request
import data_handler

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter():
    dictionary_key = request.method
    statistics_data = data_handler.read_request_counts()
    statistics_data[dictionary_key] += 1

    # SAVE STATISTICS TO TXT FILE
    data_handler.save_request_counts(statistics_data)
    return render_template('main.html')


@app.route('/statistics')
def statistics():
    return render_template('statistics.html', data=data_handler.read_request_counts())


if __name__ == '__main__':
    app.run()
