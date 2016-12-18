from flask import Flask, render_template, request
from flask import session, url_for, redirect, flash
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
map = None
app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if map == None:
        return redirect(url_for('choose_get'))
    elif score in session:
        thescene = map.SCENES[session[score]]
        return render_template('show_scene.html', scene=thescene)
    else:
        session[score] = map.START.urlname
        thescene = map.SCENES[session[score]]
        return render_template('show_scene.html', scene=thescene)


@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if score in session:
        if userinput is None:
            session.pop(score)
            return render_template('you_died.html')
        else:
            userinput = userinput.lower()
            currentscene = map.SCENES[session[score]]
            nextscene = currentscene.go(userinput)
            if currentscene == map.guessing and session['guess'] < currentscene.guesses : # For games that stay in on scene for more than once
                    session['guess'] +=1
                    return render_template('show_scene.html', scene=currentscene)
            elif nextscene is None:
                #There's no transition for that user input
                #what should your code do in response?
                return render_template('show_scene.html', scene=currentscene, missing="You can't do this. Please try again.")
            elif 'death' in nextscene.urlname:
                session.pop(score)
                return render_template('you_died.html', scene=nextscene)
            else:
                session[score] = nextscene.urlname
                session['guess'] = 0
                return render_template('show_scene.html', scene=nextscene)
    else:
        #There's no session, how could the user get here?
        # What should your code do in response?
        return render_template('you_died.html')

# This urL initializes the session with starting values
@app.route('/choose', methods=['GET'])
def choose_get():
    return render_template('choose.html')
@app.route('/choose', methods=['POST'])
def choose_post():
    choose = request.form.get('map')
    global map
    global score
    if choose == "Gothons Of Planet Percal #25" :
        import map1 as map
        score = 'scene'
    elif choose == "Roadtrip":
        import map2 as map
        score = 'scene2'
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get

@app.route('/')
def index():
    return redirect(url_for('login_get'))
@app.route('/login', methods=['GET'])
def login_get():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('choose_get')) # redirect the browser to the url for game_get

@app.route('/login', methods=['POST'])
def do_admin_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return login_get()

@app.route('/test')
def test():

    POST_USERNAME = "python"
    POST_PASSWORD = "python"

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        return "Object found"
    else:
        return "Object not found " + POST_USERNAME + " " + POST_PASSWORD

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

app.secret_key = '123456789gAmCmJsLd4'

if __name__ == "__main__":
    app.run(debug=True)
