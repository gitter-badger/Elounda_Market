#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved


def run():
    return """
    SELECT 
    HDate                                                                   AS 'ΗΜΕΡΟΜΗΝΙΑ',
    ESFIItem.Description                                                    AS 'ΠΕΡΙΓΡΑΦΗ',
    ESFIItem.BarCode                                                        AS 'ΚΩΔΙΚΟΣ',
    ESFIItem.fItemSubcategoryCode                                           AS 'ΥΠΟΚΑΤΗΓΟΡΙΑ',
    OldValueS                                                               AS 'ΠΑΛΙΑ ΤΙΜΗ',
    NewValueS                                                               AS 'NEA TIMH',
    iif(OldValueS>NewValueS, 'ΠΤΩΣΗ ΤΙΜΗΣ', 'ΑΥΞΗΣΗ ΤΙΜΗΣ')                 AS 'ΔΕΙΚΤΗΣ',
    ESFIItem.RetailPrice
    from ES00HistoryLog
    left join ESMMSISupplier on ES00HistoryLog.fPK = ESMMSISupplier.GID
    left join ESFIItem on ESMMSISupplier.fItemGID = ESFIItem.GID
    where  convert(varchar(10), HDate, 102) 
    = convert(varchar(10), getdate(), 102)
    and 
    FieldID = 'PurchaseNetPrice'
    and round(OldValueS, 2) != round(NewValueS, 2)
    """

def retail():
    return """
    SELECT 
    HDate                                                                   AS 'ΗΜΕΡΟΜΗΝΙΑ',
    ESFIItem.Description                                                    AS 'ΠΕΡΙΓΡΑΦΗ',
    ESFIItem.BarCode                                                        AS 'ΚΩΔΙΚΟΣ',
    ESFIItem.fItemSubcategoryCode                                           AS 'ΥΠΟΚΑΤΗΓΟΡΙΑ',
    OldValueS                                                               AS 'ΠΑΛΙΑ ΤΙΜΗ',
    NewValueS                                                               AS 'NEA TIMH',
    iif(OldValueS>NewValueS, 'ΠΤΩΣΗ ΤΙΜΗΣ', 'ΑΥΞΗΣΗ ΤΙΜΗΣ')                 AS 'ΔΕΙΚΤΗΣ',
    ESFIItem.RetailPrice
    from ES00HistoryLog
    left join ESFIItem on ES00HistoryLog.fPK= ESFIItem.GID
    where  
    convert(varchar(10), HDate, 102) 
    = convert(varchar(10), getdate()-1, 102)
   and FieldID = 'RetailPrice'
    --and round(OldValueS, 2) != round(NewValueS, 2)
    order by HDate
    """

"select * from ES00HistoryLog where FieldID = 'RetailPrice'"
"select * from esfiitem where GID = '0428F2A6-06C0-4907-A082-E205C6E5331E'"