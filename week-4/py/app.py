# from email import message_from_binary_file
from flask import Flask
import functions

app = Flask(
    import_name=__name__,
    static_folder='public',
    static_url_path='/'
)
app.config['SECRET_KEY'] = 'test'
functions.configureRoutes(app)

if __name__ == '__main__':
	# app.run(port=3000, debug=True)
    app.run(host='0.0.0.0', port=3000)