CREATE TABLE projects(
    pid         INTEGER NOT NULL PRIMARY KEY,
    title       VARCHAR(256),
    description VARCHAR(1024),
    class       VARCHAR(128),
    daterange   VARCHAR(128)
);

CREATE TABLE project_action_points(
    apid        INTEGER NOT NULL PRIMARY KEY,
    proj_id     INTEGER NOT NULL,
    bp          VARCHAR(1024)

);

CREATE TABLE project_links(
    plid        INTEGER NOT NULL PRIMARY KEY,
    proj_id     INTEGER NOT NULL,
    link        VARCHAR(128) NOT NULL,
    link_type   VARCHAR(64) NOT NULL
);

CREATE TABLE photography_places(
    pid         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    filename    VARCHAR(64) NOT NULL,
    location    VARCHAR(128),
    description VARCHAR(1024),
    date_taken  DATE,
    places_group VARCHAR(64)
);

CREATE TABLE photography_themes(
    pid         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    filename    VARCHAR(64) NOT NULL,
    location    VARCHAR(128),
    description VARCHAR(1024),
    date_taken  DATE,
    themes_group VARCHAR(64)
);