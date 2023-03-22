DROP TABLE IF EXISTS tblUsers;
CREATE TABLE tblUsers (
    id INTEGER NOT NULL,
    first_name TEXT NULL,
    last_name TEXT NULL,
    sex TEXT NULL,
    birth_date TEXT NULL,
    rating FLOAT NULL,
    primary_skills TEXT NULL,
    secondary_skill TEXT NULL,
    company TEXT NULL,
    active BOOLEAN NULL,
    country TEXT NULL,
    language TEXT NULL,
    search_count INT NULL
);
