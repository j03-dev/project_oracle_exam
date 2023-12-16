create table category
(
    id      integer primary key autoincrement not null,
    name    varchar(255) not null,
    user_id integer      not null,
    foreign key (user_id) references admin (id)
);
