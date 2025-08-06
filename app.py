from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "🎉 SUCCESS! Your Flask app is working on Render! ✅"

@app.route('/test')
def test():
    return "Test route working! ✅"

@app.route('/health')
def health():
    return {"status": "healthy", "message": "App is running"}

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port) 