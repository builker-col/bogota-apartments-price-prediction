from main import app
import gunicorn

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)