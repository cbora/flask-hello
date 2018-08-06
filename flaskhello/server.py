from flaskhello import app


@app.route('/')
def index2():
    return 'index 2'
