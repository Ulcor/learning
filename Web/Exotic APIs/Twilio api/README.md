## Twilio message API exporter

### Brief
The module designed to load message logs from your Twilio account <br >
Final data will be limited by date range and loaded by 200m/batch to avoid API lock <br >
Logs wil contain personal information, such as phone numbers <br >
Use it only after necessary precautions

### How to use

1) Go to API keys & tokens at [Twilio console](twilio.com/console)
2) Insert Account SID and Primary token, put them into environmental variables
3) Run a test cell. If You're getting messages, then everything is working fine so far
4) In main etl change start_date and end_date parameters
5) Load raw results. I use BigQuery, but it is just an example, data can be loaded to any database or CSV/JSON

### Extras
You can also add/remove columns using records.needed_column and add it into resulting dataframe <br >

### SQL examples
```
/* Get long and short URL from a link to order in a message */

         order link WITH Hosts AS (SELECT date_sent_format,
                      REGEXP_EXTRACT(body, r'https?://([^/]+)') AS host_url,
                      REGEXP_EXTRACT(body, r'https?://[^\s]+')  AS full_link,
                      phone_to
               FROM your_project.your_dataset.twilio
               WHERE date_sent_format >= "2024-02-01"
                 AND phone_to != 1234567 -- user writing back to a bot. Insert your bot number
               ORDER BY date_sent_format DESC) 

SELECT
    host_url,
    full_link,
    COUNT(DISTINCT phone_to) AS users
FROM Hosts
GROUP BY 1, 2
ORDER BY 1, 2;

```
Imagine a message from a bot:
"Hi there! It seem like your order is already packed and ready to go. 
Click on - https://www.awesome_shop.com/orders/d7278d89-3b1c-4926-b8fb-45163207f2e9?utm_source=whatsapp_notification&event=order_ready <br >
What can we get from that message?
```
/* Get particular text data from messages */

SELECT date_sent,
       date_sent_format,
       phone_to,
       body,
       REGEXP_EXTRACT(body, r'/orders/([^/?]+)')                                             AS order_uuid,
       REGEXP_EXTRACT(body, r'event=([^&]+)')                                                AS event,
       COUNT(phone_to) OVER (PARTITION BY phone_to)                                          AS messages_per_user,
       COUNT(phone_to) OVER (PARTITION BY phone_to, date_sent_format)                        AS messages_per_session,
       COUNT(phone_to)
             OVER (PARTITION BY REGEXP_EXTRACT(body, r'/orders/([^/?]+)'), date_sent_format) AS messages_per_order
FROM your_project.your_dataset.twilio
WHERE date_sent_format = '2024-02-14'
  AND phone_to != 1234567 -- user writing back to a bot. Insert your bot number
GROUP BY 1, 2, 3, 4
ORDER BY 1, 2, 3;
```