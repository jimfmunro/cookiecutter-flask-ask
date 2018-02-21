# coding=utf-8

# {{ cookiecutter.skill_name }}
# By {{ cookiecutter.author_name }} <{{ cookiecutter.author_email_address }}>
#
# {{ cookiecutter.skill_short_description }}

import logging
from datetime import datetime
from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement

__author__ = '{{ cookiecutter.author_name }}'
__email__ = '{{ cookiecutter.author_email_address }}'


app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

# Session starter
#
# This intent is fired automatically at the point of launch (= when the session starts).
# Use it to register a state machine for things you want to keep track of, such as what the last intent was, so as to be
# able to give contextual help.

@ask.on_session_started
def start_session():
    """
    Fired at the start of the session, this is a great place to initialise state variables and the like.
    """
    logging.debug("Session started at {}".format(datetime.now().isoformat()))

# Launch intent
#
# This intent is fired automatically at the point of launch.
# Use it as a way to introduce your Skill and say hello to the user. If you envisage your Skill to work using the
# one-shot paradigm (i.e. the invocation statement contains all the parameters that are required for returning the
# result

@ask.launch
def handle_launch():
    """
    (QUESTION) Responds to the launch of the Skill with a welcome statement and a card.

    Templates:
    * Initial statement: 'welcome'
    * Reprompt statement: 'welcome_re'
    * Card title: '{{ cookiecutter.skill_name }}
    * Card body: 'welcome_card'
    """

    welcome_text = render_template('welcome')
    welcome_re_text = render_template('welcome_re')
    welcome_card_text = render_template('welcome_card')

    return question(welcome_text).reprompt(welcome_re_text).standard_card(title="{{ cookiecutter.skill_name }}",
                                                                          text=welcome_card_text)


# Built-in intents
#
# These intents are built-in intents. Conveniently, built-in intents do not need you to define utterances, so you can
# use them straight out of the box. Depending on whether you wish to implement these in your application, you may keep
# or delete them/comment them out.
#
# More about built-in intents: http://d.pr/KKyx

# (STATEMENT) Handles the 'stop' built-in intention.
@ask.intent('AMAZON.StopIntent')
def handle_stop():
    farewell_text = render_template('stop_bye')
    return statement(farewell_text)


# (STATEMENT) Handles the 'cancel' built-in intention.
@ask.intent('AMAZON.CancelIntent')
def handle_cancel():
    farewell_text = render_template('cancel_bye')
    return statement(farewell_text)


# (Question) Handles the 'help' built-in intention.
@ask.intent('AMAZON.HelpIntent')
def handle_help():
    help_text = render_template('help_text')
    return question(help_text)


# Handles the 'no' built-in intention.
@ask.intent('AMAZON.NoIntent')
def handle_no():
    pass


# Handles the 'yes'  built-in intention.
@ask.intent('AMAZON.YesIntent')
def handle_yes():
    pass


# Handles the 'go back!'  built-in intention.
@ask.intent('AMAZON.PreviousIntent')
def handle_back():
    pass


# (Question) Handles the 'start over!'  built-in intention.
@ask.intent('AMAZON.StartOverIntent')
def start_over():
    pass

# ==================================#
# Specify your custom intents here. #
# ==================================#


@ask.intent('YourCustomIntent')
def my_custom_intent():
    pass


# Ending session
@ask.session_ended
def session_ended():
    return "{}", 200


# If using a local webhost
if __name__ == '__main__':
    app.run(debug=True)


# If using a Lambda directly. Install requirements/lambda_requirements.txt
def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)