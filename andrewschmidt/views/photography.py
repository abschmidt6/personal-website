"""
Personal Website Projects view.

URLs include:
/
"""
import flask
import arrow
import andrewschmidt


@andrewschmidt.app.route('/photography/', methods=['GET'])
def show_photography():
    """Display / Route."""
    context = dict()
    return flask.render_template("404.html", **context)