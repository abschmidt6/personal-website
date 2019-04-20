"""
Personal Website About Me view.

URLs include:
/
"""
import flask
import arrow
import andrewschmidt


@andrewschmidt.app.route('/aboutme/', methods=['GET'])
def show_aboutme():
    """Display / Route."""
    context = dict()
    return flask.render_template("aboutme.html", **context)