/*
 * #  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
 */

-- ΒΡΕΣ ΜΟΥ ΟΛΟΥΣ ΤΟΥΣ ΥΠΑΛΛΗΛΟΥΣ ΠΟΥ ΕΧΟΥΝ ΑΝΟΙΧΤΕΙ ΣΤΟΝ 60
select * from ESFITradeAccount where GLAccountCode = 60

-- ΜΕΤΡΗΣΕ ΜΟΥ ΟΛΟΥΣ ΤΟΥΣ ΥΠΑΛΛΗΛΟΥΣ ΠΟΥ ΕΧΟΥΝ ΑΝΟΙΧΤΕΙ
select count(*) as 'SUM OF EMPLOYEES'
from ESFITradeAccount where GLAccountCode = 60

