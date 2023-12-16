create table user
(
    id       integer primary key autoincrement not null,
    email    varchar(255) unique not null,
    password varchar(255) not null,
);
