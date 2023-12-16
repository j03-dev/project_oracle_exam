create table article
(
    id               integer primary key autoincrement not null,
    name             varchar(255)  not null,
    description      varchar(1000) not null,
    image_id         integer,
    category_id      integer       not null,
    date_publication date default (date ('now')),
    user_id          integer       not null,
    foreign key (user_id) references user (id),
    foreign key (category_id) references category (id),
    foreign key (image_id) references image (id)
);
