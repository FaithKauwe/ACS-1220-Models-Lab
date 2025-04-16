"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from books_app.models import Book, Author, Genre, User

# Import app and db from events_app package so that we can run app
from books_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    # query for all instances of 'User' and send to the template
    all_users = User.query.all()
    return render_template('home.html')

@main.route('/profile/<username>')
def profile(username):
    # attempt to find record or show 404 Not Found page
    user = User.query.filter_by(username=username).first_or_404()
    # query for the user with the given username, and send to the template
    return render_template('profile.html', username=username)
