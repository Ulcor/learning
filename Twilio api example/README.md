## Twilio message API exporter

### Brief
The module designed to load message logs from your Twilio account(s) using <br >
Final data will be limited by date range and loaded by 200m/batch to avoid API lock

### How to use

1) Go to API keys & tokens
2) Insert Account SID and Primary token (or whatever you should use in your situation), put them into environmental variables
3) Run a test cell. If You're getting a messages, then everything is working fine so far
4) In main cell change start_date and end_date parameters
5) Load raw results or clean them by adding extra cells into notebook

### Extras
You can also add/remove columns in resulting dataframe. You should see what columns are available by typing record. In most instruments You should see all the available columns. Then modify the script to add them into the final dataframe 