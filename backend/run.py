from resources import *

#init
app = Flask(__name__)
api = Api(app)

#endpoint(s)
api.add_resource(Relatives, "/relatives")

if __name__=='__main__':
    app.run(host="0.0.0.0", port=3306)
    # app.run()