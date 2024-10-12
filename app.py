from flask import Flask, render_template

app = Flask(__name__)

# Routes for each HTML page
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/rooms.html')
def rooms():
    return render_template('rooms.html')

@app.route('/single-blog.html')
def single_blog():
    return render_template('single-blog.html')

if __name__ == '__main__':
    app.run(debug=True)
