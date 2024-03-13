## Twilio message API exporter

### Brief
The module designed to load message logs from your Twilio account <br >
Final data will be limited by date range and loaded by 200m/batch to avoid API lock <br >
Logs wil contain personal information, that is protected by international law <br >
Use it only after necessary precautions

### How to use

1) Go to API keys & tokens at [Twilio console](twilio.com/console)
2) Insert Account SID and Primary token, put them into environmental variables
3) Run a test cell. If You're getting messages, then everything is working fine so far
4) In main etl change start_date and end_date parameters
5) Load raw results. I use BigQuery, but it is just an example, data can be loaded to any database or CSV/JSON

### Extras
You can also add/remove columns using records.needed_column and add it into resulting dataframe <br >