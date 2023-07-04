from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus_page():
    return render_template('aboutus.html')

@app.route('/gettingstarted')
def gettingstarted_page():
    return render_template('gettingstarted.html')

@app.route('/blog')
def blog_page():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run()
