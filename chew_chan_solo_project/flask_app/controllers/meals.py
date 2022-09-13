from flask_app import app
from flask import render_template,request,redirect,session,flash, get_flashed_messages
from datetime import datetime
from flask_app.models.user import User
from flask_app.models.meal import Meal


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please log in first", "error")
        return redirect("/logout")
    else:
        return render_template("dashboard.html", 
        user = User.get_by_id({"id" : session["user_id"]}),
        all_meals = Meal.get_all(),
        error = get_flashed_messages(category_filter="error"))


@app.route('/meals/new')
def new_meal():
    if "user_id" not in session:
            flash("Please log in first", "error")
            return redirect("/logout")
    else:    
        return render_template("create.html", 
                meal_msg = get_flashed_messages(category_filter="meal"),
                error = get_flashed_messages(category_filter="error"))

@app.route('/meals/create', methods =['POST'])
def create_meal():
    if "user_id" not in session:
            flash("Please log in first", "error")
            return redirect("/logout")
    if not Meal.validate_meal(request.form):
            return redirect('/meals/new')
    else:
        data ={
                "user_id": session['user_id'],
                "name" : request.form['name'],
                "type" : request.form['type'],
                "description" : request.form['description'],
                "delivery_date" : request.form['delivery_date'],
                "price" : int(request.form['price'])
        }
        meal_id = Meal.create(data)
        return redirect('/dashboard')

@app.route('/meals/view/<int:id>')
def view_meal(id):

    return render_template('view_order.html', 
        user = User.get_by_id({"id" : session["user_id"]}),
        meal=Meal.get_one({"id":id}),
        meal_msg = get_flashed_messages(category_filter="meal"), 
        error = get_flashed_messages(category_filter="error"))

@app.route('/meals/edit/<int:id>')
def edit_meal(id):

    return render_template('edit.html', 
    meal=Meal.get_one({"id":id}),
    meal_msg = get_flashed_messages(category_filter="meal"), 
    error = get_flashed_messages(category_filter="error"))

@app.route('/meals/update/<int:id>', methods =['POST'])
def update_meal(id):
    if "user_id" not in session:
        flash("Must be logged in to do that!", "error")
        return redirect("/logout")
    if not Meal.validate_meal(request.form):
        return redirect('/meals/new')
    else:
        Meal.update(request.form)
        return redirect ('/dashboard')


@app.route('/meals/delete/<int:id>', methods=['POST'])
def delete_meal(id):
    if 'user_id' not in session:
            return redirect ('/logout')
    data={
            "id": id
    }    
    Meal.delete(request.form)
    return redirect('/dashboard')

