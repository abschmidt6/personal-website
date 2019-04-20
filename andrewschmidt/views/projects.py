"""
Personal Website Photography view.

URLs include:
/
"""
import flask
import arrow
import andrewschmidt


@andrewschmidt.app.route('/projects/', methods=['GET'])
def show_projects():
    """Display / Route."""
    context = dict()
    return flask.render_template("404.html", **context)