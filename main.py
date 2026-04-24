from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Shopee API server is running!"

@app.route("/callback")
def callback():
    code = request.args.get("code")
    shop_id = request.args.get("shop_id")

    return f"""
    Authorization Code: {code}
    Shop ID: {shop_id}
    """

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

