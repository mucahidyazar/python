from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Mucahid Yazar/OneDrive/Desktop/notes/python/worksheets/14-flask-orm-sqlachademy/todo.db'
db = SQLAlchemy(app)

#Index HTML ile FLUSK 'i baglamak
@app.route('/')
def index():
    todos = Todo.query.all() #Bu bize bir liste donecek ve ana sayfada yakalayabilecegiz
    return render_template('index.html', todos = todos)

@app.route('/add', methods=['POST'])
def addTodo():
    title = request.form.get('title') #formdan gelen title namesini almak
    newTodo = Todo(title = title, complete = False) #Todo objesini olusturmak
    db.session.add(newTodo) #Todo objesini databaseye eklemek
    db.session.commit() #commiti gerceklestirmek
    return redirect(url_for('index')) #ekledikten sonra indexe tekrar yonlendirmek

@app.route('/complete/<string:id>') #<string:id> linkten gelen id yi dinamik oalrak alabiliriz
def completeTodo(id): #id yukaridaki generatorden geliyor
    todo = Todo.query.filter_by(id = id).first() #first aslinda id den gelen ilk degeri alacak liste olarak dusunursek ama aslinda buna gerek yok
    # if todo.complete == True:
    #     todo.complete = False
    # else:
    #     todo.complete = True
    todo.complete = not todo.complete #yukaridakinin kisa hali
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))
#veri tabanina eklenecek tablo
#db.Model ilede veritabanindaki tabloyu kullanabilecegiz
class Todo(db.Model):
    #id columnu olustur demisiz
    #ozelligi integer olsun demisiz
    #primary key olsun ve eklendikce otomatik unique bir key olsun demisiz
    id = db.Column(db.Integer, primary_key=True)
    #max80 karakter
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    db.create_all() #Tum classlari tablo olarak ekler (olusmus tablolari tekrar olusturmaz)
    app.run(debug=True)































































































# from flask import Flask,render_template,redirect,url_for,request

# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/user/Desktop/TodoApp/todo.db'
# db = SQLAlchemy(app)
# @app.route("/")
# def index():
#     todos = Todo.query.all()
#     return render_template("index.html",todos = todos)
# @app.route("/complete/<string:id>")
# def completeTodo(id):
#     todo = Todo.query.filter_by(id = id).first()
#     """if todo.complete == True:
#         todo.complete = False
#     else:
#         todo.complete = True"""
#     todo.complete = not todo.complete

#     db.session.commit()
#     return redirect(url_for("index"))
# @app.route("/add",methods = ["POST"])
# def addTodo():
#     title = request.form.get("title")
#     newTodo = Todo(title = title,complete = False)
#     db.session.add(newTodo)
#     db.session.commit()

#     return redirect(url_for("index"))


# @app.route("/delete/<string:id>")
# def deleteTodo(id):
#     todo = Todo.query.filter_by(id = id).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect(url_for("index"))

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80))
#     complete = db.Column(db.Boolean)

# if __name__ == "__main__":
#     db.create_all()
#     app.run(debug=True)