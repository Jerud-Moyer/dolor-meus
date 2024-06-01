from flask import (Flask, render_template, Blueprint)

bp = Blueprint("home", __name__)

@bp.route('/why')
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
      'label': 'cats',
      'value': 'big cats'
    },
    {
      'label': 'wolves',
      'value': 'wolves'
    },
  ]

  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  context = {
    "special_message": 'this crazy!',
    "subject_options": subject_options,
    "nums": nums
  }

  return render_template('home.html', context=context)
