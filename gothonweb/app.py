from flask import Flask, render_template, request
from flask import session, url_for, redirect
import map1
map = map1
app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        session['scene'] = map.START.urlname
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            session.pop('scene')
            return render_template('you_died.html')
        else:
            userinput = userinput.lower()
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if currentscene == map.guessing and session['guess'] < currentscene.guesses : # For games that stay in on scene for more than once
                    session['guess'] +=1
                    return render_template('show_scene.html', scene=currentscene)
            elif nextscene is None:
                #There's no transition for that user input
                #what should your code do in response?
                return render_template('show_scene.html', scene=currentscene, missing="You can't do this. Please try again.")
            else:
                session['scene'] = nextscene.urlname
                session['guess'] = 0
                return render_template('show_scene.html', scene=nextscene)
    else:
        #There's no session, how could the user get here?
        # What should your code do in response?
        return render_template('you_died.html')

# This urL initializes the session with starting values
@app.route('/', methods=['GET'])
def index_get():
#     return render_template('choose.html')
# @app.route('/', methods=['POST'])
# def index_post():
#     if request.form['map'] == "Game 1" :
#         map = map1
#         return map
#     elif request.form['map'] == "Game 2":
#         pass

    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get

app.secret_key = '123456789gAmCmJsLd4'

if __name__ == "__main__":
    app.run()
