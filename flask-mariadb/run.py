from app import app

if __name__ == "__main__":
    port = os.getenv("PORT", 5000)
    app.run(host="localhost", port=port, debug=True)