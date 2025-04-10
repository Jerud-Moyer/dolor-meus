from flask import (Blueprint, render_template, stream_template, Response, request)
# from openai import OpenAI
import os

bp = Blueprint('request', __name__)
print('WUT')
# client = OpenAI()
# SYSTEM_MESSAGE = os.getenv('SYSTEM_MESSAGE')

# def stream_response(response):
#   for chunk in response:
#     if chunk.choices[0].delta.content is not None:
#       print(chunk.choices[0].delta.content, end="")
#       yield chunk.choices[0].delta.content

# @bp.route('/ai', methods=['POST'])
# def ai():

#   subject = request.json['subject']

#   response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#       {"role": "system", "content": SYSTEM_MESSAGE},
#       {"role": "user", "content": subject},
#     ],
#     stream=True
#   )

#   return Response(stream_response(response), mimetype='text/event-stream')
