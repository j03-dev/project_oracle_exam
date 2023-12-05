create table produit
(
    id               integer primary key autoincrement not null,
    name             varchar(255) not null,
    description      varchar(1000)         not null,
    image            varchar(255),
    id_category      integer      not null,
    date_publication date default (date('now')),
    id_admin         integer       not null,
    foreign key (id_admin) references admin (id),
    foreign key (id_category) references category (id)
);
