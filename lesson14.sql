drop database lesson14;
CREATE DATABASE lesson14;
CREATE TABLE lesson14.users (
id bigint unsigned primary key auto_increment,
username varchar(30) unique not null,
password varchar(15) not null,
email varchar(35) null
);
CREATE TABLE lesson14.seller (
id bigint unsigned primary key auto_increment,
company varchar(30) unique not null,
phone varchar(15) not null
);
CREATE TABLE lesson14.products (
id bigint unsigned primary key auto_increment,
name varchar(30) unique not null,
cost integer,
count integer,
seller_id bigint unsigned not null,
foreign key (seller_id) references seller(id)
);
CREATE TABLE lesson14.orders (
id int unsigned primary key auto_increment,
user_id bigint unsigned not null,
product_id bigint unsigned not null,
count integer,
foreign key (user_id) references users(id),
foreign key (product_id) references products(id)
);
