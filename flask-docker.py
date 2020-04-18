from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Changed it up a bit!again'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int("80"))
<<<<<<< HEAD
print("hello")
=======
print("hello1")
>>>>>>> e28ca849144a7b6884bfd79f3d64425ea5a50d20
