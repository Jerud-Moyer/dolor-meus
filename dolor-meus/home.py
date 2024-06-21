from flask import (Flask, render_template, Blueprint)

bp = Blueprint("home", __name__)

@bp.route('/')
def home():

  subject_options = [
    {
      'label': 'motorcycles',
      'value': 'motorcycles'
    },
    {
      'label': 'guitars',
      'value': 'electric guitars'
    },
    {
      'label': 'metal',
      'value': 'heavy metal music'
    },
    {
      'label': 'cats',
      'value': 'big cats'
    },
    {
      'label': 'wolves',
      'value': 'wolves'
    },
    {
      'label': 'punk rock',
      'value': 'punk rock'
    },
    {
      'label': 'sharks',
      'value': 'sharks'
    },
    {
      'label': 'dinosaurs',
      'value': 'dinosaurs'
    },
    {
      'label': 'swords',
      'value': 'swords'
    },
    {
      'label': 'spaceships';
      'value': 'spaceships from popular fiction'
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
