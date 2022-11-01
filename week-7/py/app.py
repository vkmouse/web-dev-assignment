from flask import Flask
from member_system import MySQLUnitOfWork
from member_system import configureRoutes
from member_system import configureAPIRoutes

app = Flask(
    import_name=__name__,
    static_folder='public',
    static_url_path='/public'
)
app.config['SECRET_KEY'] = 'test'

unitOfWork = MySQLUnitOfWork('config.json')

configureRoutes(app, unitOfWork)
configureAPIRoutes(app, unitOfWork)

if __name__ == '__main__':
	app.run(port=3000, debug=True)