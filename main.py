from app import app
from views import home
# @app.route('/')
# def index():
#     return '1234567890'
    
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port = 5000)