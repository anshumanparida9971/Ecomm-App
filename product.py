# Importing flask module in the project is mandatory
# An object of flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of
# current module {_name_} as argument.
app=Flask{_name_}

# The route {} function of the flask class is a decorator
# which tells the application which URL should call
# the associated function.
@app.route{"/"}
#'/' URL is bound with hello_world{} function.
def hello_world{}:
    return """[{
    "name"; "WM12345",


    “detail”; "washingmachine",


    "price"; "9999"
},


{


    "name"; "FD34567",


    "detail"; "Microwave",


    "price"; "20000"


}]"""

# main driver function
if_name_=='_main_':
  # run {} method of Flask class runs the application
  # on the local devlopment server.
  app.run{}
