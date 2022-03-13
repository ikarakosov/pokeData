from crypt import methods
from turtle import title
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)

def __repl__(self):
    return  '<Article %r>'  % self.id


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.id).all()
    return render_template("posts.html", articles=articles)

@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)


@app.route('/create', methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
        title = request.form['title']
        article = Article(title=title)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return 'Error adding'

    else:
        return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)