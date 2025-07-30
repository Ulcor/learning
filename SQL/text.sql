SELECT
date1,
clientID,
source
FROM (
      SELECT CAST(dateTime AS DateTime)        AS date1,
             concat(clientID, '_', counterID)  AS clientID,
             concat(UTMSource, '_', UTMMedium) AS source,
             UTMCampaign
      FROM big_data.logsapivisitsdaily
      WHERE date1 BETWEEN yesterday() - 90 AND yesterday()
        AND bounce <> '1'
        AND clientID <> ''
      GROUP BY date1,
               clientID,
               source,
               UTMCampaign
               
      UNION ALL
      
      SELECT CAST(dateTime AS DateTime)        AS date1,
             concat(clientID, '_', counterID)  AS clientID,
             concat(UTMSource, '_', UTMMedium) AS source,
             UTMCampaign
      FROM big_data.logsapivisits
      WHERE date1 BETWEEN yesterday() - 90 AND yesterday()
        AND bounce <> '1'
        AND clientID <> ''
      GROUP BY date1,
               clientID,
               source,
               UTMCampaign
         )
GROUP BY
date1,
clientID,
source