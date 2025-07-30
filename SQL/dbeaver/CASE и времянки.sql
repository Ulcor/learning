/*4) Посчитать количество покупателей, чеков, сумму покупок, средний чек, сгруппировать по стране и городу. Подсветить город с наибольшим средним чеком и с наибольшей
суммой заказов, выделить их в отдельных полях MaxCheck и MaxRevenue, принимает значение 'Yes' и 'No'*/

/* В оконном выражении WITH можно посчитать промежуточные данные, которые затем использовать с помощью JOIN*/
WITH cte AS (
SELECT 
	i.BillingCountry, --- 1 порядок для group by
	i.BillingCity,  --- 2 порядок для group by
	COUNT(DISTINCT i.CustomerId) as [количество покупателей], 
	COUNT(i.InvoiceId) as [кол-во чеков],
	SUM(i.Total) as [сумма покупк],
	ROUND(SUM(i.Total) / COUNT(i.InvoiceId), 2) as [средн. чек]
--	MAX(ROUND(SUM(i.Total) / COUNT(i.InvoiceId), 2)) as MaxCheck,
--	MAX(SUM(i.Total)) as MaxRevenue
FROM Invoice as i
GROUP BY 1, 2
ORDER BY 6  DESC
),

/* Можно таким образом сохранятб несколько запросов, разделяя их , */
max_check AS ( 
SELECT 
	i.BillingCountry, --- 1 порядок для group by
	i.BillingCity,  --- 2 порядок для group by
	MAX([средн. чек]) as MaxCheck
FROM cte AS i
GROUP BY 1, 2
ORDER BY MaxCheck DESC
LIMIT 1
),

max_revenue AS (
SELECT 
	i.BillingCountry, --- 1 порядок для group by
	i.BillingCity,  --- 2 порядок для group by
	MAX([сумма покупк]) as MaxRevenue
FROM cte AS i
GROUP BY 1, 2
ORDER BY MaxRevenue DESC
LIMIT 1
)


/* Все запросы cte "живут" только в момент запуска скрипта */
SELECT 
	  cte.*
	, CASE WHEN cte.[средн. чек] = mc.MaxCheck
		 THEN 'Yes'
		 ELSE 'No'
		 END AS MaxCheck
	, CASE WHEN cte.[сумма покупк] = mr.MaxRevenue
		 THEN 'Yes'
		 ELSE 'No'
		 END AS MaxRevenue
FROM cte
LEFT JOIN max_check AS mc ON mc.BillingCountry = cte.BillingCountry AND mc.BillingCity = cte.BillingCity
LEFT JOIN max_revenue AS mr ON mr.BillingCountry = cte.BillingCountry AND mr.BillingCity = cte.BillingCity
