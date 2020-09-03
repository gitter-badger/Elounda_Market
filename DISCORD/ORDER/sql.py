#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def sql_query(input_param, type_of_forma):
    return f"""
SELECT  BarCode, ItemDescription as 'Περιγραφή', quant as 'Ποσότητα'
        FROM IMP_MobileDocumentLines
        left join IMP_MobileDocumentHeaders
        on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        left join ESFITradeAccount
        on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and IMP_MobileDocumentHeaders.Code = {input_param}
        and OrderType = '{type_of_forma}'
        --and OrderType = 'ΔΕΑ'
"""

def data_query(input_param, type_of_forma):
    return f"""
SELECT  distinct OrderType as 'Type', IMP_MobileDocumentHeaders.Code as 'Code', ESFITradeAccount.Name as 'Name',
        IMP_MobileDocumentHeaders.PdaId as 'ID'
        FROM IMP_MobileDocumentLines
        left join IMP_MobileDocumentHeaders
        on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        left join ESFITradeAccount
        on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and IMP_MobileDocumentHeaders.Code = {input_param}
        and OrderType = '{type_of_forma}'
        --and OrderType = 'ΔΕΑ'
"""

def extract_mail(input_param, type_of_forma):
    return f"""
SELECT  
        distinct FK_ESGOPerson_PersonCode1.EMailAddress AS EMailAddress,
        FK_ESGOPerson_ESGOSites.Telephone1 AS Telephone1
        FROM IMP_MobileDocumentLines

        left join IMP_MobileDocumentHeaders
        on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        left join ESFITradeAccount
        on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
        LEFT JOIN ESGOPerson AS FK_ESGOPerson_PersonCode1
       ON ESFITradeAccount.fPersonCodeGID = FK_ESGOPerson_PersonCode1.GID 
       INNER JOIN ESGOSites AS FK_ESGOPerson_ESGOSites
       ON FK_ESGOPerson_PersonCode1.fMainAddressGID = FK_ESGOPerson_ESGOSites.GID
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and IMP_MobileDocumentHeaders.Code = {input_param}
        and OrderType = '{type_of_forma}'
        --and OrderType = 'ΔΕΑ'
"""


