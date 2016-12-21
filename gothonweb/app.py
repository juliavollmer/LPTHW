from flask import Flask, render_template, request
from flask import session, url_for, redirect
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
map = None
score = 'scene'
app = Flask(__name__)
name = 'Player'

@app.route('/game', methods=['GET'])
def game_get():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if map == None:
            return redirect(url_for('choose_get'))
        elif score in session:
            thescene = map.SCENES[session[score]]
            return render_template('show_scene.html', scene=thescene)
        else:
            session[score] = map.START.urlname
            thescene = map.SCENES[session[score]]
            session['money'] = 0
            return render_template('show_scene.html', scene=thescene)


@app.route('/game', methods=['POST'])
def game_post():
    userinput = (request.form.get('userinput'))
    if score in session:
        if userinput is None:
            session.pop(score)
            return render_template('end.html')
        else:
            userinput = userinput.lower()
            currentscene = map.SCENES[session[score]]
            nextscene = currentscene.go(userinput)
            if nextscene == map.code_death and session['guess'] < currentscene.guesses : # For games that stay in on scene for more than once
                    session['guess'] +=1
                    return render_template('show_scene.html', scene=currentscene)
            elif nextscene is None:
                #There's no transition for that user input
                #what should your code do in response? Allow user to type in again.
                return render_template('show_scene.html', scene=currentscene, missing="You can't do this. Please try again.")
            elif nextscene.amount >= 1:
                session['money'] = session['money'] + nextscene.amount
                session[score] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene, missing="You now have $%d" % session['money'])
            elif session['money'] >= 20:
                 session.pop(score)
                 nextscene = map.the_end_winner
                 session['points'] += 1
                 highscore1 = session['points']
                 return render_template('end.html', scene=nextscene, highscore=highscore1)
            elif 'death' in nextscene.urlname:
                session.pop(score)
                session['money']=0
                return render_template('end.html', scene=nextscene)
            elif 'winner' in nextscene.urlname:
                session.pop(score)
                session['points'] += 1
                highscore1 = session['points']
                return render_template('end.html', scene=nextscene, highscore=highscore1)

            else:
                session[score] = nextscene.urlname
                session['guess'] = 0
                return render_template('show_scene.html', scene=nextscene)

    else:
        #There's no session, how could the user get here?
        # What should your code do in response?
        return redirect(url_for('choose_get'))

# Select the game you want to play
@app.route('/choose', methods=['GET'])
def choose_get():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('choose.html', name= name)
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

#redirecting to login
@app.route('/')
def index():
    return redirect(url_for('login_get'))

@app.route('/login', methods=['GET'])
def login_get():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('choose_get'))

#Login
@app.route('/login', methods=['POST'])
def do_admin_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    global name
    session['points'] = 0
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    name = POST_USERNAME
    if result:
        session['logged_in'] = True
    else:
        pass
    return login_get()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

#Signing up
@app.route("/signup",  methods=['GET'])
def signup_get():
    return render_template('signup.html')

@app.route("/signup",  methods=['POST'])
def signup_post():
    Session = sessionmaker(bind=engine)
    session = Session()

    username = str(request.form['username'])
    password = str(request.form['password'])

    user = User(username, password)
    session.add(user)

    session.commit()
    return redirect(url_for('login_get'))

@app.route('/reset')
def reset():
    session.pop(score)
    session['money'] = 0
    return redirect(url_for('game_get'))


app.secret_key = '123456789gAmCmJsLd4'

if __name__ == "__main__":
    app.run()
