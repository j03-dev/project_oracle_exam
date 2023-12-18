create table user
(
    id         integer primary key autoincrement not null,
    username   varchar(255)        not null,
    first_name varchar(255)        not null,
    last_name  varchar(255),
    email      varchar(255) unique not null,
    password   varchar(255)        not null
);
