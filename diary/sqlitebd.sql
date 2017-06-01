CREATE TABLE IF NOT EXISTS welldiary (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    long_well_name TEXT NOT NULL DEFAULT '',
    field_name TEXT NOT NULL DEFAULT '',

 
    drilled DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);