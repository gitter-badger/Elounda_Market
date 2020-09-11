/*
 * #  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
 */

SELECT ReferenceNumber                AS 'ΑΡΙΘΜΟΣ ΕΠΙΤΑΓΗΣ',
       IssueDate                      AS 'ΗΜΕΡΟΜΗΝΙΑ ΚΑΤΑΧΩΡΗΣΗΣ',
       DueDate                        AS 'ΗΜΕΡΟΜΗΝΙΑ ΛΗΞΗΣ',
       Bank                           AS 'ΤΡΑΠΕΖΑ',
       CurrencyValue                  AS 'ΠΟΣΟ',
       ClosedCurrencyValue            AS 'ΕΞΟΦΛΗΜΕΝΟ ΠΟΣΟ',
       HolderName                     AS 'ΕΠΩΝΥΜΙΑ',
       Comments                       AS 'ΣΧΟΛΙΑ',
       IIF(IsOpen = 1 , 'NAI', 'OXI') AS 'ΑΝΟΙΧΤΟ'
       FROM ESFINote
            WHERE
            DATEPART(yyyy, IssueDate) = DATEPART(yyyy, getdate())
       ORDER BY 1