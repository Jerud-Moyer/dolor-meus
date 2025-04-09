from flask import (Flask, render_template, Blueprint)

bp = Blueprint("home", __name__)

@bp.route('/')
def home():

  subject_options = [
    {
      'label': 'Motorcycles',
      'value': 'motorcycles'
    },
    {
      'label': 'Guitars',
      'value': 'electric guitars'
    },
    {
      'label': 'Metal',
      'value': 'heavy metal music'
    },
    {
      'label': 'Cats',
      'value': 'big cats'
    },
    {
      'label': 'Wolves',
      'value': 'wolves'
    },
    {
      'label': 'Punk rock',
      'value': 'punk rock'
    },
    {
      'label': 'Sharks',
      'value': 'sharks'
    },
    {
      'label': 'Dinosaurs',
      'value': 'dinosaurs'
    },
    {
      'label': 'Swords',
      'value': 'swords'
    },
    {
      'label': 'Spaceships',
      'value': 'spaceships from popular fiction'
    },
    {
      'label': 'Pizza',
      'value': 'pizza'
    },
    {
      'label': 'Norse Mythology',
      'value': 'norse mythology'
    },
    {
      'label': 'Ancient Rome',
      'value': 'ancient Rome'
    }
  ]

  nums = [
    {
      'label': 1,
      'value': 'one'
    },
    {
      'label': 2,
      'value': 'two'
    },
    {
      'label': 3,
      'value': 'three'
    },
    {
      'label': 4,
      'value': 'four'
    },
    {
      'label': 5,
      'value': 'five'
    },
    {
      'label': 6,
      'value': 'six'
    },
    {
      'label': 7,
      'value': 'seven'
    },
    {
      'label': 8,
      'value': 'eight'
    },
    {
      'label': 9,
      'value': 'nine'
    },
    {
      'label': 10,
      'value': 'ten'
    },
  ]

  context = {
    "special_message": 'this crazy!',
    "subject_options": subject_options,
    "nums_options": nums
  }

  return render_template('home.html', context=context)
