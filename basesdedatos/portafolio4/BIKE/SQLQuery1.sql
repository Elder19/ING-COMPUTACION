

use BikeStores;
go 

create function OrdeneesDate (@Fecha1 date, @fecha2 date)
returns table 
as 
return (
 Select * from sales.orders so 
 where so.order_date BETWEEN @Fecha1 AND @fecha2 

);

SELECT * 
FROM dbo.OrdeneesDate('2017-01-01', '2017-12-31');
