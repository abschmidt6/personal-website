"""
Personal Website index (main) view.

URLs include:
/
"""
import flask
import arrow
import andrewschmidt


@andrewschmidt.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / Route."""
    context = dict()
    return flask.render_template("index.html", **context)