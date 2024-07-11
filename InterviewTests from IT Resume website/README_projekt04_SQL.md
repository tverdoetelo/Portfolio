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
>>select count(created_at)
>>
>>from Purchases p
>>
>>join skus s on s.id = p.sku_id
>>
>>where (s.id = 5 and created_at > '10.10.2021'::date)

**2. Test Tinkoff] Undeclared customers**
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
>>select start_dttm as date, last_nm, first_nm, middle_nm
>>
>>from tinkoff.customers c
>>
>>join tinkoff.calls cl on c.customer_id = cl.customer_id
>>
>>where (start_dttm = '05.29.2019'::date and duration = 0)
