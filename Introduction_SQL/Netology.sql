-- deduct taxes from staff salaries
select staff_id , salary - (salary*0.2) - (salary*0.13) - (salary*0.08)
from staff

-- select customers names begin with B
select last_name , first_name 
from customer
where first_name like 'B%'

-- select item that starts with D and ends with 1
select product 
from product
where product ilike 'd%1'

-- change the first letter of the name to X for users with names to B
select first_name, last_name, overlay(first_name placing 'X' from 1 for 1) 
from customer
where first_name like 'B%'

-- get a year from 15.02.2021
select date_part('year', '2021.02.15'::date)

-- get a day from 15.02.2021
select date_part('day', '2021.02.15'::date)

-- get a month and a year from 15.02.2021
select date_trunc('month', '2021.02.15'::date)

-- get a day from 15.02.2021
select date_trunc('day', '2021.02.15'::date)

-- creation of a delivery table
create table delivery(
	delivery_id serial primary key,
	address_id int references address(address_id) not null,
	delivery_date date not null,
	time_range text[] not null,
	staff_id int references staff(staff_id) not null,
	status del_status not null default 'в обработке',
	last_update timestamp,
	create_date timestamp default now(),
	deleted boolean not null default false
)

select * from delivery

--adding data with delivery_id
insert into delivery (address_id, delivery_date, time_range, staff_id)
values(102, '2022.02.25', array['10:00:00', '18:00:00'], 2),
(34, '2022.02.25', array['10:00:00', '18:00:00'], 2),
(12, '2022.02.25', array['10:00:00', '18:00:00'], 2),
(78, '2022.02.25', array['10:00:00', '18:00:00'], 2),
(55, '2022.02.25', array['10:00:00', '18:00:00'], 2)

update orders
set delivery_id = 1
where order_id = 1

update orders
set delivery_id = 2
where order_id = 2

update orders
set delivery_id = 3
where order_id = 3

update orders
set delivery_id = 4
where order_id = 4

update orders
set delivery_id = 5
where order_id = 5

select *
from orders

--selecting cities where was delivery
select o.order_id, c.city 
from orders o
join delivery d on o.delivery_id = d.delivery_id 
join address a on a.address_id = d.address_id 
join city c on c.city_id = a.city_id 

--selecting combination of usernames where usernames are different
select c.first_name, c2.first_name 
from customer c 
cross join customer c2 
where c.first_name != c2.first_name 

--selecting a list of orders where was no information about delivery
select o.order_id , d.delivery_id 
from orders o 
left join delivery d on d.delivery_id = o.delivery_id 
where d.delivery_id is null

--aggregation functions
select customer_id, count(order_id), sum(amount), avg(amount), max(amount), min(amount)
from orders o 
group by customer_id 

--aggregation finction vol.2
select customer_id, date_trunc('MONTH',last_update), count(order_id), sum(amount), avg(amount), max(amount), min(amount)
from orders o 
group by customer_id, date_trunc('MONTH',last_update)

--selecting sum, min, max, and avg of payments according to the customer name
select c.last_name, c.first_name, sum(amount), min(amount), max(amount), avg(amount)
from customer c 
join orders o on o.customer_id = c.customer_id 
group by c.customer_id 

--selecting sum, min, max, and avg of payments according to the customer name
--if sum > 20000, amount > 100
select c.last_name, c.first_name, sum(amount), min(amount), max(amount), avg(amount)
from customer c 
join orders o on o.customer_id = c.customer_id 
where amount > 100
group by c.customer_id 
having sum(amount) > 20000

--Homework1
select count(amount)
from orders o 

select count(*)
from product p
join category c on c.category_id = p.category_id
where c.category = 'Игрушки'

select c.category, count(*)
from product p 
join category c on c.category_id = p.category_id 
group by c.category_id 
order by 2 desc

select c.category, count(*)
from product p 
join category c on c.category_id = p.category_id 
group by c.category_id 
having count(*) =
	(select max(count)
	from (
		select category_id, count(*)
		from product 
		group by category_id) t)

select sum(opl.amount)
from orders o 
join customer c on o.customer_id = c.customer_id 
join order_product_list opl on o.order_id = opl.order_id 
join product p on opl.product_id = p.product_id 
where c.first_name = 'Linda' and c.last_name = 'Williams' and p.product = 'Черепаха'

--subqueries
select customer_id, sum(amount)/
	(select sum(amount) from orders)
from orders o 
group by customer_id 

select o.customer_id, concat, sum(amount) 
from orders o 
join (select customer_id, concat(last_name,' ', first_name)
	from customer c 
	where left(last_name,1)='A') t
on t.customer_id = o.customer_id 
group by o.customer_id, concat

select customer_id, sum(amount) 
from orders o 
where customer_id in (
	select customer_id 
	from customer c 
	where left(last_name,1)='A') 
group by customer_id

select t.product_id, sum/price
from (select opl.product_id, sum(o.amount)
	from orders o 
	join order_product_list opl on o.order_id = opl.order_id 
	group by opl.product_id) t
join (select product_id, price
	from product p) t2 on t2.product_id = t.product_id
	
select t.product_id, sum / (select price
							from product p
							where p.product_id = t.product_id)
from (select opl.product_id, sum(o.amount)
	from orders o 
	join order_product_list opl on o.order_id = opl.order_id 
	group by opl.product_id) t

--
select distinct opl.product_id, sum(o.amount) over (partition by p.product_id) / price
from orders o
join order_product_list opl on o.order_id = opl.order_id 
join product p on p.product_id = opl.product_id 

-- data about every 1000 order
select *
from(
	select order_id , customer_id , amount ,
	row_number () over (order by order_id)
from orders o) t
where t.row_number % 1000 = 0

--
select order_id, customer_id, amount,
	sum(amount) over (partition by customer_id order by order_id)
from orders

select order_id, customer_id, amount,
	avg(amount) over (partition by customer_id order by order_id)
from orders

--view
create view customers_sum_avg as
	select c.last_name, c.first_name, c2.category, sum(o.amount), count(o.order_id)
	from orders o
	join order_product_list opl on o.order_id = opl.order_id 
	join product p on p.product_id = opl.product_id 
	join category c2 on c2.category_id = p.category_id
	join customer c on c.customer_id = o.customer_id
	group by c.last_name, c.first_name, o.customer_id, p.category_id, c2.category
	order by o.customer_id
	
select * from customers_sum_avg

create materialized view customers_sum_avg_mat as
	select c.last_name, c.first_name, c2.category, sum(o.amount), count(o.order_id)
	from orders o
	join order_product_list opl on o.order_id = opl.order_id 
	join product p on p.product_id = opl.product_id 
	join category c2 on c2.category_id = p.category_id
	join customer c on c.customer_id = o.customer_id
	group by c.last_name, c.first_name, o.customer_id, p.category_id, c2.category
	order by o.customer_id
	
select * from customers_sum_avg_mat
	
create view task_1 as
select *
from(
select order_id, customer_id, amount,
	row_number() over (partition by customer_id order by order_id desc)
from orders) t
where row_number = 1

select * from task_1

create materialized view task_2 as
select *
from(
select order_id, customer_id, amount,
	row_number() over (partition by customer_id order by order_id desc)
from orders) t
where row_number = 1
with no data

select * from task_2

refresh materialized view task_2

drop materialized view task_2

--Homework2
select round(count(*)::numeric/sum(count(*)) over () * 100, 3)
from product p 
group by category_id 
order by 1 desc
