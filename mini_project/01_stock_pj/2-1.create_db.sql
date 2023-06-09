-- create database stock_pj;
use stock_pj;

create table agency_stock (
	agency_name VARCHAR(50) not null,
	date DATE not null,
    stock_price int not null,
    primary key (agency_name, date)
);

create table singer_agency (
	singer VARCHAR(50) primary key not null,
    agency_name VARCHAR(50) not null,
    FOREIGN KEY (`agency_name`) REFERENCES `agency_stock` (`agency_name`)
);

create table yearly_album_chart (
	year int not null,
    ranking int not null,
    singer VARCHAR(50) not null,
    title VARCHAR(100) not null,
    sales int not null,
    release_date varchar(50),
    primary key (year, ranking),
    FOREIGN KEY (`singer`) REFERENCES `singer_agency` (`singer`)
);

-- drop table yearly_album_chart;
-- drop table singer_agency;
-- drop table agency_stock;

-- truncate yearly_album_chart;
-- truncate singer_agency;
-- truncate agency_stock;

select * from singer_agency;
select * from agency_stock;
select * from yearly_album_chart;
