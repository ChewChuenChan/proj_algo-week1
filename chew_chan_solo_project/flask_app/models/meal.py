from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,request,redirect,session,flash, get_flashed_messages
import re
from flask_app.models import user

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class Meal:
    db = "meal_prep"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.description = data['description']
        self.delivery_date = data['delivery_date']
        self.price = data['price']
        self.user_id = data ['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = None
        # self.users_ids_who_favorited =[]
        # self.users_who_favorited=[]
        

    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO meals
        (name, type, description, delivery_date, price, user_id)
        Values 
        (%(name)s,%(type)s,%(description)s,%(delivery_date)s,%(price)s,%(user_id)s);
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result

    @classmethod
    def get_all_meals(cls):
        query = "SELECT * FROM meals;"
        result = connectToMySQL(cls.db).query_db(query)
        meals_list = []
        for row in result:
            meals_list.append(cls(row))
        return meals_list    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM meals JOIN users ON meals.user_id = users.id ;"
        result = connectToMySQL(cls.db).query_db(query)
        meals_list = []
        for row in result:
            #create the meal object
            meal_ob = cls(row)
            #create associated user object
            user_data ={
                'id':row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'address': row['address'],
                'city': row['city'],
                'state': row['state'],
                'zipcode': row['zipcode'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
        }
            user_ob = user.User(user_data)
            #associate the two objects together
            meal_ob.user = user_ob
            #addon meal object to list of meal
            meals_list.append(meal_ob)
        return meals_list

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM meals JOIN users ON meals.user_id = users.id WHERE meals.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result)<1:
            return False
        row=result[0]
        meal_ob=cls(row)
        user_data ={
            'id':row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password': row['password'],
            'address': row['address'],
            'city': row['city'],
            'state': row['state'],
            'zipcode': row['zipcode'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
    }
        meal_ob.users= user.User(user_data)
        return meal_ob

    @classmethod
    def one_order(cls,data):
        query ="SELECT * FROM meals WHERE delivery_date=%(delivery_date)s"
        result = connectToMySQL(cls.db).query_db(query,data)
        this_order = cls(result[0])
        print(this_order)
        return this_order

    @classmethod
    def update(cls,data):
        query = """
        UPDATE meals SET 
        name = %(name)s, type=%(type)s ,description = %(description)s, 
        delivery_date=%(delivery_date)s, price=%(price)s
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM meals WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @staticmethod
    def validate_meal( meal_data ):
        is_valid = True
        if len(meal_data['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters ","meal")
        if meal_data['type'] == "":
            is_valid = False
            flash("Please select type","meal")
        if meal_data['delivery_date'] == "":
            is_valid = False
            flash("Please select delivery date.","meal")
        if meal_data['description'] == "" :
            is_valid = False
            flash("Please enter description.","meal")
        if meal_data['price'] == "":
            is_valid = False
            flash("Please enter price.", "meal")
        elif int(meal_data['price']) < 0:
            is_valid = False
            flash("price must be more than 0","meal")
        return is_valid


    # @staticmethod
    # def meal_type (meal_data):
    #     is_valid = True
    #     if meal_data['type'] == "Classic":
    #         is_valid = False
    #         <div class="orange">
    #     elif meal_data ['type'] == "Lean":
    #         is_valid = False
    #         <div class="Blue">
    #     elif meal_data ['type'] == "Vegetarian":
    #         is_valid = False
    #         <div class ="Green">
    #     return is_valid

    @classmethod
    def sum(cls,data):
        query = "SELECT SUM(price)as total, name, price FROM meals WHERE delivery_date =%(delivery_date)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result) < 1:
            return False
        total = cls(result[0])
        return total

