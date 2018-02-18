from flask import Flask
app=Flask(__name__)
@app.route('/')
def headlines():
   return "News for all"
if __name__=='main':
   app.run(debug=True)
