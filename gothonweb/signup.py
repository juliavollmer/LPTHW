USERNAME = str(request.form['username'])
PASSWORD = str(request.form['password'])

user = User(USERNAME, PASSWORD)
session.add(user)
