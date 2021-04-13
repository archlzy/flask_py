from flask import Flask, render_template
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':   
        return render_template('hello.html',name=None)
    if request.method == 'POST':
        name = request.
        print(name)
        return render_template('hello.html',name=name)

@app.route('/abc/')
def hello_abc():
    return 'hello, abc'

@app.route('/edf/')
def hello_edf():
    return 'hello, edf'

@app.route('/err/')
def err():
    string = "this line will create Error"
    try:
        string=int(string)
    except:
        raise TypeError
    return 'this is err page'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for thart user
    return 'user %s'% escape(username)



@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do the logo'
    if request.method == 'GET':
        return 'this is get of login'




# app.config['DEBUG'] = True


# for i,v in dict(app.config).items():
#     print('-'*80)
#     print(i,v)



# if __name__=='__main__':
#     app.run()

if __name__ == "__main__":
    # To allow aptana to receive errors, set use_debugger=False
    app = create_app(config="config.yaml")

    use_debugger = app.debug and not(app.config.get('DEBUG_WITH_APTANA'))
    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0')