from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>DataBite Platform is running successfully!</h1><p>Deployed via GitHub Actions on AWS EC2.</p>"

if __name__ == '__main__':
    # אנחנו מגדירים לשרת להישאר דלוק, להקשיב לכל הכתובות (0.0.0.0) ובפורט 80
    app.run(host='0.0.0.0', port=80)