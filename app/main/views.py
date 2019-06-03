from flask import render_template, request, redirect,url_for,abort
from . import main
from ..models import Pitch,User, Comment
from .forms import PitchForm, UpdateProfile, CommentsForm
from flask_login import login_required, current_user
from .. import db,photos
import markdown2 

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Make the right first impression"

    return render_template('index.html',title = title)


@main.route('/categories/')
def categories():

    '''
    View categories page function that returns the categories details page and its data
    '''

    pitches = Pitch.get_pitches('categories')

    return render_template('categories.html', pitches = pitches)
