"""
Personal Website Projects view.

URLs include:
/
"""
import flask
import arrow
import andrewschmidt


@andrewschmidt.app.route('/photography/', methods=['GET'])
def show_photography_grid():
    """Display / Route."""
    context = dict()
    context['grid_items'] = [{
            'href': '/photography/places/',
            'text': 'Places',
            'img':  'bixby-bridge-big-sur-california.jpg'
        }, {
            'href': '/photography/timelapses/',
            'text': 'Timelapses',
            'img':  'slicer-linear-output.jpg'
        }, {
            'href': '/photography/astro/',
            'text': 'Astrophotography',
            'img':  'milky_way_browns_tract_pond_2015_1.jpg'
        }, {
            'href': '/photography/sports/',
            'text': 'Sports',
            'img':  'US_OPEN_TENNIS_Maria_Sharapova_RUS-3.jpg'
        }
    ]
    return flask.render_template("photography_grid.html", **context)

@andrewschmidt.app.route('/photography/<category>/', methods=['GET'])
def show_photography_categories(category):
    """Display / Route."""
    cursor = andrewschmidt.model.get_db().cursor()
    context = dict()
    context['category'] = category
    query = ""

    if category == "places":
        context['grid_items'] = [{
                'href': '/photography/places/venice-and-balkans/',
                'text': 'Venice and The Balkans',
                'img':  'venice-street-scene.jpg'
            }, {
                'href': '/photography/places/athens/',
                'text': 'Athens',
                'img':  'acropolis_athens_greece-4.jpg'
            }, {
                'href': '/photography/places/santorini/',
                'text': 'Santorini',
                'img':  'oia_santorini_sunrise_morning-1.jpg'
            }, {
                'href': '/photography/places/istanbul/',
                'text': 'Istanbul',
                'img':  'istanbul_blue_mosque_daytime.jpg'
            }, {
                'href': '/photography/places/st-martin-anguilla/',
                'text': 'St. Martin and Anguilla',
                'img':  'Saint-Martin-Anse-Marcel-Sunset.jpg'
            }, {
                'href': '/photography/places/cali/',
                'text': 'California',
                'img':  'bixby-bridge-big-sur-california.jpg'
            }, {
                'href': '/photography/places/adk/',
                'text': 'The Adirondacks',
                'img':  'dock_mist_morning_adirondacks_ny.jpg'
            }, {
                'href': '/photography/places/nyc/',
                'text': 'New York City',
                'img':  'nighttime-in-nyc-bokeh-lights.jpg'
            }, {
                'href': '/photography/places/london-vienna-prague/',
                'text': 'London, Vienna, and Prague',
                'img':  'harraford-square-london-england.jpg'
            }, {
                'href': '/photography/places/jamaica/',
                'text': 'Jamaica',
                'img':  'jamaican-sunset-with-boat.jpg'
            }, {
                'href': '/photography/places/nj/',
                'text': 'New Jersey',
                'img':  'fall-park-bench.JPG'
            }
        ]

        return flask.render_template("photography_grid.html", **context)

    elif category == "timelapses":
        query = "SELECT * FROM photography_other WHERE category = 'Timelapse';"
        cursor.execute(query)
        videos = list()
        for row in cursor.fetchall():
            videos.append({
                    'filename': row['filename'],
                    'location': row['location'],
                    'desc':     row['description'],
                    'date':     row['date_taken'],
                    'group':    row['category']
                })

        context['videos'] = videos
        return flask.render_template("video_gallery.html", **context)

    elif category == "astro":
        query = "SELECT * FROM photography_other WHERE category = 'Astro';"
        context['category'] = 'Astrophotography'

    elif category == "sports":
        query = "SELECT * FROM photography_other WHERE category = 'Sports';"
        context['category'] = 'Sports'

    else:
        return flask.render_template("404.html", **context)

    cursor.execute(query)
    images = list()
    for row in cursor.fetchall():
        images.append({
                'filename': row['filename'],
                'location': row['location'],
                'desc':     row['description'],
                'date':     row['date_taken'],
                'group':    row['category']
            })
    cols = [list(), list(), list(), list()]
    for i in range(len(images)):
        cols[i % len(cols)].append(images[i])

    context['images'] = cols

    return flask.render_template("photography_gallery.html", **context)

@andrewschmidt.app.route('/photography/places/<place>/', methods=['GET'])
def show_photography_places(place):
    group = ""
    if place == "venice-and-balkans":
        group = "Venice and the Balkans"
    elif place == "athens":
        group = "Athens"
    elif place == "santorini":
        group = "Santorini"
    elif place == "istanbul":
        group = "Istanbul"
    elif place == "st-martin-anguilla":
        group = "Saint Martin and Anguilla"
    elif place == "cali":
        group = "California"
    elif place == "adk":
        group = "The Adirondacks"
    elif place == "nyc":
        group = "New York City"
    elif place == "london-vienna-prague":
        group = "London, Vienna, and Prague"
    elif place == "jamaica":
        group = "Jamaica"
    elif place == "nj":
        group = "New Jersey"
    else:
        group = ""


    cursor = andrewschmidt.model.get_db().cursor()
    context = dict()
    context['category'] = group
    query = "SELECT * FROM photography_places WHERE category = '{}';".format((group))

    cursor.execute(query)
    images = list()
    for row in cursor.fetchall():
        images.append({
                'filename': row['filename'],
                'location': row['location'],
                'desc':     row['description'],
                'date':     row['date_taken'],
                'group':    row['category']
            })
    cols = [list(), list(), list(), list()]
    for i in range(len(images)):
        cols[i % len(cols)].append(images[i])

    context['images'] = cols

    return flask.render_template("photography_gallery.html", **context)
