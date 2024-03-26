from flask import Flask

#creating the app instance
app = Flask(__name__) 


@app.route('/home')
def home():
    return '<h2> Barcode Scanner </h2>'


if __name__ == '__main__':
    app.run(debug=True)
