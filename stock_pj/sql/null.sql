use stock_pj;

SELECT * FROM yearly_album_chart
WHERE release_date is null;

UPDATE yearly_album_chart SET release_date = null
WHERE release_date = 'nan';