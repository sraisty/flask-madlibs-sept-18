"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")


    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    playgame = request.args.get("playgame")
    # print("playgame value is {}".format(playgame))
    # print("playgame type is {}".format(type(playgame)))
    if playgame=="yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib', methods=['POST', 'GET'])
def show_madlib():
    if request.method == "POST":
        color = request.form.get("color")
        noun = request.form.get("noun")
        adjective = request.form.get("adjective")
        person = request.form.get("person")
        pets = request.form.getlist("pets")
        # print("Pets are: {}".format(pets))
    elif request.method == "GET":
        color = request.args.get("color")
        noun = request.args.get("noun")
        adjective = request.args.get("adjective")
        person = request.args.get("person")
        pets = request.args.getlist("pets")

    return render_template("madlib.html", 
                           color=color, 
                           noun=noun, 
                           adjective=adjective, 
                           person=person, 
                           pets=pets)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
