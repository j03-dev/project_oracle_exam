create table category
(
    id       integer primary key autoincrement not null,
    name     varchar(255) not null,
    id_admin integer not null,
    foreign key (id_admin) references admin (id)
);
