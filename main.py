from flask import Flask,abort,jsonify
from flask_restful import Api,Resource
from errors_xy import InvalidUsage


app = Flask(__name__)
api = Api(app)

names = {'karthik':{'age':20,'gender':'male'},
        'bill':{'age':25,'gender':'male'}}



class HelloWorld(Resource):
    def get(self,name):
        if name in names:
            return names[name]
        else:
            return abort(404)

    def post(self,name,age,gender):
        names[name]=name
        return names

class CustomErrorApi(Resource):
    def get(self):
        raise InvalidUsage("This vieew is gone",status_code=410)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
api.add_resource(HelloWorld,'/helloworld/<string:name>')
api.add_resource(CustomErrorApi,'/error')




if __name__ == '__main__':
    app.run(debug=True)