"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqdcg2qv2dcb94pvf0-a.oregon-postgres.render.com",
        database="demo_j3di",
        user="demo_j3di_user",
        password="yElIqyfzkBWqmLbNywSyUM5YKKV1IDgk")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
