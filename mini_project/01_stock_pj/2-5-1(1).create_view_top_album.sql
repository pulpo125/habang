-- 연도별 3사 앨범 판매량 1위 View 생성

use stock_pj;

-- 2018년도 3사 앨범 판매량 1위
CREATE VIEW top_rank_2018 as 
(
	select MIN(ranking) as top_rank
	from yearly_album_chart as yac
		join singer_agency as sa 
		on yac.singer = sa.singer
	where (yac.year = 2018 and agency_name = 'JYP') or (yac.year = 2018 and agency_name = 'YG') or (yac.year = 2018 and agency_name = 'SM')
	group by agency_name
);

select * from top_rank_2018;

-- 2019
CREATE VIEW top_rank_2019 as 
(
	select MIN(ranking) as top_rank
	from yearly_album_chart as yac
		join singer_agency as sa 
		on yac.singer = sa.singer
	where (yac.year = 2019 and agency_name = 'JYP') or (yac.year = 2019 and agency_name = 'YG') or (yac.year = 2019 and agency_name = 'SM')
	group by agency_name
);

select * from top_rank_2019;

-- 2020
CREATE VIEW top_rank_2020 as 
(
	select MIN(ranking) as top_rank
	from yearly_album_chart as yac
		join singer_agency as sa 
		on yac.singer = sa.singer
	where (yac.year = 2020 and agency_name = 'JYP') or (yac.year = 2020 and agency_name = 'YG') or (yac.year = 2020 and agency_name = 'SM')
	group by agency_name
);

select * from top_rank_2020;

-- 2021
CREATE VIEW top_rank_2021 as 
(
	select MIN(ranking) as top_rank
	from yearly_album_chart as yac
		join singer_agency as sa 
		on yac.singer = sa.singer
	where (yac.year = 2021 and agency_name = 'JYP') or (yac.year = 2021 and agency_name = 'YG') or (yac.year = 2021 and agency_name = 'SM')
	group by agency_name
);

select * from top_rank_2021;

-- 2022
CREATE VIEW top_rank_2022 as 
(
	select MIN(ranking) as top_rank
	from yearly_album_chart as yac
		join singer_agency as sa 
		on yac.singer = sa.singer
	where (yac.year = 2022 and agency_name = 'JYP') or (yac.year = 2022 and agency_name = 'YG') or (yac.year = 2022 and agency_name = 'SM')
	group by agency_name
);

select * from top_rank_2022;