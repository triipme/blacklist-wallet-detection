from resources import *
from flask_cors import CORS

#init
app = Flask(__name__)
api = Api(app)
CORS(app)

#endpoint(s)
api.add_resource(Relatives, "/relatives")

if __name__=='__main__':
    app.run(host="0.0.0.0", port=3306)
    # app.run()