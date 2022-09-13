from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,request,redirect,session,flash, get_flashed_messages
import re
from flask_app.models import meal

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "meal_prep"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.zipcode = data['zipcode']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO users 
        (first_name, last_name, email, password,address,city,state,zipcode )
        VALUES 
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(address)s, %(city)s, %(state)s, %(zipcode)s);
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id =%(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # check to see if there were any results, if not, the email deosn't exist in the db
        if len(result) < 1:
            return False
        this_user = cls(result[0])
        return this_user

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email =%(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # check to see if there were any results, if not, the email deosn't exist in the db
        if len(result) < 1:
            return False
        this_user = cls(result[0])
        return this_user

    @staticmethod
    def validate_reg(user_data):
        is_valid = True
        user_in_db = User.get_by_email(user_data)
        if user_in_db:
            is_valid = False
            flash("Email already taken.","register")
        if not EMAIL_REGEX.match(user_data['email']):
            is_valid = False
            flash("Please enter a valid Email","register") 
        if len(user_data['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.","register")
        if len(user_data['last_name']) < 2:
            flash("Last name must be at least 2 characters.","register")
            is_valid = False
        if not user_data ['password'] == user_data ['confirm_pass']:
            is_valid = False
            flash("Password do not match!", "register")
        if len(user_data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters", "register")
        return is_valid

    @staticmethod
    def validate_log(user_data):
        user = User.get_by_email({'email': user_data["email"]})
        if user and bcrypt.check_password_hash(user.password,request.form['password']):
            user_id = user.id
        else:
            flash("Invalid email/password combination!", "login")
            user_id = 0
        return user_id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def full_address(self):
        return f"{self.address} {self.city} {self.state} {self.zipcode}"

    # @classmethod
    # def get_one_order(cls,data):
    #     query = """
    #     SELECT * FROM users 
    #     JOIN meals ON 
    #     users.id = meals.user_id
    #     WHERE
    #     id = %(id)s;"""
    #     result = connectToMySQL(cls.db).query_db(query,data)
    #     print(result)
    #     if len(result) < 1:
    #         return False
    #     row = result[0]
    #     #create the review object
    #     order = cls(row)
    #     #create the user object
    #     meal_data ={
    #                 'id':row['meals.id'],
    #                 'name': row['name'],
    #                 'type': row['type'],
    #                 'description': row['description'],
    #                 'delivery_date': row['delivery_date'],
    #                 'price': row['price'],
    #                 'created_at': row['meals.created_at'],
    #                 'updated_at': row['meals.updated_at']
    #         }
    #     meal_ob = meal.Meal(meal_data)
    #     #associate the two objects together
    #     order.meals = meal_ob
    #     return order