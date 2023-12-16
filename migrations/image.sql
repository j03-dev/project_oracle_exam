create table image (
    id integer primary key autoincrement not null,
    path varchar(255) unique not null
);