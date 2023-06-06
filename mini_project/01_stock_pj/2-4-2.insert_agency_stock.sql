use stock_pj;

-- stock -> python
select * from agency_stock;

-- singer_agency
insert into singer_agency values 
					('2PM', 'JYP'),
                    ('슈퍼주니어 (Super Junior)', 'JYP'),
                    ('DAY6', 'JYP'),
                    ('TWICE', 'JYP'),
                    ('Stray Kids (스트레이 키즈)', 'JYP'),
                    ('ITZY (있지)', 'JYP'),
                    ('NMIXX', 'JYP'),
                    ('EXO', 'SM'),
                    ('소녀시대', 'SM'),
                    ('샤이니 (SHINee)', 'SM'),
                    ('레드벨벳(Red Velvet)', 'SM'),
                    ('NCT', 'SM'),
                    ('NCT DREAM', 'SM'),
                    ('NCT 127', 'SM'),
                    ('aespa', 'SM'),
                    ('BIGBANG', 'YG'),
                    ('iKON', 'YG'),
                    ('위너(WINNER)', 'YG'),
                    ('BLACKPINK', 'YG');
                    
select * from singer_agency;

-- yearly_album_chart -> python
select * from yearly_album_chart;

-- album -> python
select * from album;