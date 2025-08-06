from flask import Flask, render_template_string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test-secret-key'

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Social Engineering Awareness - Test</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-body text-center">
                            <h1 class="card-title">🎉 SUCCESS!</h1>
                            <p class="card-text">Your Flask app is working on Render!</p>
                            <div class="alert alert-success">
                                <strong>Deployment Status:</strong> ✅ Working
                            </div>
                            <a href="/test" class="btn btn-primary">Test Another Route</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html

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