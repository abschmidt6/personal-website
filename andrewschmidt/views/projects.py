"""
Personal Website Projects view.

URLs include:
/
"""
import flask
import arrow
import andrewschmidt


@andrewschmidt.app.route('/projects/', methods=['GET'])
def show_projects():
    """Display / Route."""
    cursor = andrewschmidt.model.get_db().cursor()

    query = """SELECT * FROM projects ORDER BY pid ASC;"""
    context = dict()
    context['projects'] = dict()
    context['sorted_daterange'] = list()
    cursor.execute(query)

    for row in cursor.fetchall():
        dr = row['daterange']
        if dr not in context['projects']:
            context['projects'][dr] = list()
            context['sorted_daterange'].append(dr)

        # Get bullet points
        points = list()
        bullet_query = """SELECT * FROM project_action_points WHERE
        proj_id = {} ORDER BY apid ASC;""".format(row['pid'])
        cursor.execute(bullet_query)
        for row2 in cursor.fetchall():
            points.append(row2['bp'])

        links = dict()
        file_query = """SELECT * FROM project_links WHERE proj_id = {}; """.format(row['pid'])
        cursor.execute(file_query)
        for row3 in cursor.fetchall():
            links[row3['link']] = row3['link_type']


        proj = {
            'pid':      row['pid'],
            'title':    row['title'],
            'class':    row['class'],
            'daterange': row['daterange'],
            'bullet_points': points,
            'links': links
        }
        context['projects'][dr].append(proj)
    return flask.render_template("projects.html", **context)