***IT Resume is a great base with different test tasks from interviews for data analysts. For this reason i decided to train my skills.***

**1. [Test Alpha Bank] Purchases after October 10**
>
>The following table structure is given:
>
>![image](https://github.com/tverdoetelo/Portfolio/assets/150687862/fca3d31f-8ba1-468c-b323-c1f17f69358e)
>
>Task:
>>It is necessary to deduce the number of people who bought goods with id = 5 after October 10, 2021 (inclusive).
>
>Solution:
>>      select count(created_at)
>>
>>      from Purchases p
>>
>>      join skus s on s.id = p.sku_id
>>
>>      where (s.id = 5 and created_at > '10.10.2021'::date)

**2. [Test Tinkoff] Undeclared customers**
>
>The following table structure is given:
>
>![image](https://github.com/tverdoetelo/Portfolio/assets/150687862/ac2839aa-3b18-4003-88dc-0bdaecefa6ab)
>
>Task:
>>Get information on customers (Customers table) who called and did not get through 29.05.2019.
>>
>>Columns as a result
>>>date (date of call)
>>>
>>>last_nm
>>>
>>>first_nm
>>>
>>>middle_nm
>>
>>Note: for correct operation of your request, be sure to specify the table scheme - tinkoff. For example, FROM tinkoff.employees.
>
>Solution:
>>      select start_dttm as date, last_nm, first_nm, middle_nm
>>
>>      from tinkoff.customers c
>>
>>      join tinkoff.calls cl on c.customer_id = cl.customer_id
>>
>>      where (start_dttm = '05.29.2019'::date and duration = 0)
>>
**3. Find counties where there were no purchases**
>
>The following table structure is given:
>
>![image](https://github.com/user-attachments/assets/5526b9fc-6bc0-4252-aa85-08317164631e)
>
>Task:
>>It is necessary to find the names of all districts, which residents have never made a purchase in this store.
>>
>>Columns as a result
>>>name 
>
>Solution:
>>      select c.name
>>
>>      from county c
>>
>>      left join customer cr on c.county_code = cr.county_code
>>
>>      left join c_orders o on cr.id_customer = o.id_customer
>>
>>      where o.id_orders is null

**4. [Tinkoff] Successful transactions**
>
>The following table is given:
>
>Table TRANSACTION_TIN:

Column            Data type   Description
transaction_id    int         Transaction ID
customer_id       int         Client ID
amount_rur        float       Transaction amount in Russian rubles
transaction_dttm  datetime    Date and time of transaction
success_flg       bool        Successful transaction flag (TRUE)
The tables are in interview.ACCOUNT_TIN.
>
>Task:
>>It is necessary to make a report on clients whose successful transactions exceed the amount of 100 thousand rubles. The report should contain customer identifiers (customer_id) and the sum of their successful transactions in Russian rubles (amount_rur). A successful transaction is considered to be one where the success_flg flag value is TRUE. Sort the result by the client identifier (customer_id).
>>
>>Columns as a result
>>>customer_id
>>>amount_rur 
>
>Solution:
>>      select customer_id, amount_rur
>>
>>      from interview.TRANSACTION_TIN
>>
>>      where success_flg is TRUE and customer_id in (
>>
>>                                                    select customer_id
>>
>>                                                    from interview.TRANSACTION_TIN
>>
>>                                                    group by customer_id
>>
>>                                                    having sum(amount_rur) > 100000)
>>
>>      order by customer_id
