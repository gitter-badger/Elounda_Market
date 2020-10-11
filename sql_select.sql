/*
 * #  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
 */

-- ΒΡΕΣ ΜΟΥ ΟΛΟΥΣ ΤΟΥΣ ΥΠΑΛΛΗΛΟΥΣ ΠΟΥ ΕΧΟΥΝ ΑΝΟΙΧΤΕΙ ΣΤΟΝ 60
select * from ESFITradeAccount where GLAccountCode = 60

-- ΜΕΤΡΗΣΕ ΜΟΥ ΟΛΟΥΣ ΤΟΥΣ ΥΠΑΛΛΗΛΟΥΣ ΠΟΥ ΕΧΟΥΝ ΑΝΟΙΧΤΕΙ
select count(*) as 'SUM OF EMPLOYEES'
from ESFITradeAccount where GLAccountCode = 60

select * from ESFIZItemSubCategory


-- ΕΠΙΤΑΓΕΣ
SELECT ReferenceNumber                AS 'ΑΡΙΘΜΟΣ ΕΠΙΤΑΓΗΣ',
       IssueDate                      AS 'ΗΜΕΡΟΜΗΝΙΑ ΚΑΤΑΧΩΡΗΣΗΣ',
       DueDate                        AS 'ΗΜΕΡΟΜΗΝΙΑ ΛΗΞΗΣ',
       Bank                           AS 'ΤΡΑΠΕΖΑ',
       CurrencyValue                  AS 'ΠΟΣΟ',
       ClosedCurrencyValue            AS 'ΕΞΟΦΛΗΜΕΝΟ ΠΟΣΟ',
       HolderName                     AS 'ΕΠΩΝΥΜΙΑ',
       HolderAddress                  AS 'ΔΙΕΥΘΥΝΣΗ',
       Comments                       AS 'ΣΧΟΛΙΑ',
       IIF(IsOpen = 1 , 'NAI', 'OXI') AS 'ΑΝΟΙΧΤΟ'
       FROM ESFINote
            WHERE
            DATEPART(yyyy, IssueDate) = DATEPART(yyyy, getdate())
       ORDER BY 1


