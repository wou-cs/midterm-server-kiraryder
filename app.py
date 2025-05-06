from flask import Flask, request

app = Flask(__name__)


@app.route('/api/calcs/<number>', methods=["GET"])
def calculate(number):
    try:
        number = int(number)

        if number <= 0:
            return (
                '{"error": "Non-positive integer"}',
                400,
                {'Content-Type': 'application/json'}
            )

        dec = number - 1
        hex_value = hex(number)

        response_data = '{"dec": ' + str(dec) + ', "hex": "' + hex_value + '"}'

        return (
            response_data,
            200,
            {'Content-Type': 'application/json'}
        )

    except ValueError:
        return (
            '{"error": "Invalid integer input"}',
            400,
            {'Content-Type': 'application/json'}
        )


