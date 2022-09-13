from flask import render_template, redirect, session, request, flash
from flask_app import app
import requests

@app.route("/recipe")
def recipe():
    headers ={
        'Cookie': 'route=4ebff1d2ae8df64bdc65f1e53a63331e'
    }

    r = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q=vegetables&app_id=486ca9a4&app_key=2023213d6390b521126a3e1ec5c7f95c&diet=low-carb&mealType=Dinner&imageSize=REGULAR',headers=headers)
    code=r.json()
    return render_template("recipe.html",items=code)