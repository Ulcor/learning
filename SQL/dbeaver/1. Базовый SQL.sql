'''урок по базовым SELECT выражениям'''

--Комментарии

'''Так обычно выделяют название / описание кода в начале. В таких ковычках любой ввод превращается в коммент. Работает с MySQL'''
--так можно закоментить строку. Так пишут комменты к конкретной строке кода, а также коментят временно ненужные строки, которые 
/* могут пригодятся потом, чтобы их не удалять */

--Последовательность запроса
SELECT -- пишем поля, которые хотим забрать. Вид - таблица.столбец , т.столбец. т - это сокращение, алиас, alias, он нужен для читаемости кода 
FROM -- из какой таблицы забирать данные? Вид from article as a либо from article a
JOIN -- объединение с другими таблицами. Читать тут https://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins
WHERE -- ограничения, что будет / не будет показываться
GROUP BY -- нужно, когда мы в SELECT применяем агрегацию, группирует данные по полученным значениям, как сводная таблица Excel
HAVING -- то же, что и WHERE, но можно применит после GROUP BY. По этому ест больше ресурсов на выполнение
ORDER BY -- фильтр от 'А' до 'Я', от 1 до 99999. Можно сделать на несколько колонок, как в Excel, будет применяться сначала на 1, потом на 2 и так далее. Изначально фильтрует по asc, можно дописать desc
LIMIT -- для БД MySQL и ей подобных. Для 

--Простой код, показывающий объединение данных из 1 таблицы данными из 2 таблицы
--Алиасы тут очень нужны - без них запрос будет очень громоздким, особенно когда в объедиении много таблиц
--Так можно сделать алиасы: album as a, album [a], album a. Результат будет одним и тем же
SELECT -- выбириаем нужные поля, из обоих таблиц
	a.Name,
	COUNT(al.AlbumId) as albums -- после агрегации столбец с кол-вом альбомов будет (без названия). По этому так же используем алиасы
FROM -- объединяем альбом и артиста по общему ключу - это поле есть в обеих таблицах. Так же работают и другие join'ы
	Album as al
	left join Artist as a ON al.ArtistId = a.ArtistId
WHERE -- like или not like убирают строки по совпадению. 'значение' внутри '' это текст. %т% будет искать все символы до и после значения в %%. Изумительный пример тут https://www.w3schools.com/sql/sql_wildcards.asp 
	al.Title not like '%Balls%' 
GROUP BY -- группируем, потому что мы посчитали количество альбомов. По всем НЕагригационным колонкам
	a.Name
ORDER BY -- изначально фильтрует по asc - восходящий. Desc - низходящий. Можно применять к нескольким столбцам
	albums desc
LIMIT 100 -- ограничивает выборку, только для MySQL. Для SQL sever используется top 5 конструкция, в начале SELECT
;