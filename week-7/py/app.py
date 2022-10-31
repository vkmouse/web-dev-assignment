import json
from flask import Flask
from member_system import MemoryUnitOfWork, MySQLUnitOfWork, configureRoutes

app = Flask(
    import_name=__name__,
    static_folder='public',
    static_url_path='/public'
)
app.config['SECRET_KEY'] = 'test'

# unitOfWork = MemoryUnitOfWork()
unitOfWork = MySQLUnitOfWork('config.json')

configureRoutes(app, unitOfWork)

if __name__ == '__main__':
	app.run(port=3000, debug=True)