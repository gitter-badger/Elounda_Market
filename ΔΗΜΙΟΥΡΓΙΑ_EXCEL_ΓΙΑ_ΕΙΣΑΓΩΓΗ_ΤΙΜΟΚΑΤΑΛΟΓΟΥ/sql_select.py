#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved


def pda_results(id):
    return  f"""
    SELECT IMP_MobileDocumentLines.ItemCode as 'Είδος' 
    FROM IMP_MobileDocumentLines 
    LEFT JOIN IMP_MobileDocumentHeaders ON 
    IMP_MobileDocumentLines.fDocGID = IMP_MobileDocumentHeaders.GID
    WHERE IMP_MobileDocumentHeaders.Code = {id}
    AND IMP_MobileDocumentHeaders.OrderType like 'ΑΠ_ΜΟΒ'
    """

