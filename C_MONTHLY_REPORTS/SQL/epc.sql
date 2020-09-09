/*
 * #  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
 */


select ADCode,
       ADRegistrationDate,
       TotalValue
       from
ESFIDocumentAdjustment
LEFT JOIN ESFITradeAccount ON ESFITradeAccount.GID = fAccountGID

WHERE
DATEPART(yyyy, ESFIDocumentAdjustment.ADRegistrationDate) = DATEPART(yyyy, getdate())
and  ADCode LIKE 'ΕΙΧ%'
