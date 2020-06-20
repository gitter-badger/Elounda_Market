#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from datetime import datetime
import random

from Private import slack_app,sql_connect
import matplotlib.pyplot as plt
import pandas as pd


# ------ΛΙΣΤΕΣ------------


kataskevastes_lst = ['COCA COLA 3E', 'Pepsico - HBH', 'Κρι Κρι', 'ΟΛΥΜΠΟΣ Γαλακτοβιομηχανία Λαρίσης Α.Ε.',
                     'Δέλτα Τρόφιμα Α.Ε.', 'Hellenic Quality Foods A.E.', 'Ολυμπιακή Ζυθοποιία Α.Ε.',
                     'Αθηναϊκή Ζυθοποιία Α.Ε.', 'Tasty Foods ΑΒΓE', 'ΕΜΜΑΝΟΥΗΛ ΒΑΡΔΑΣ & ΣΙΑ Ο.Ε. ΑΡΤΟΠΟΙΕΙΟ',
                     'BDF - Beiersdorf Hellas A.E.', 'Καραμολέγκος ΑΕ', 'Παπαδοπουλος Ε.Ι. Α.Ε.', 'Βότομος Α.Ε. Ζαρος',
                     'ΖΑΡΓΙΑΝΑΚΗΣ', 'ΒΟΘΥΛΙΑ Α.Ε.', 'Procter & Gamble Ελλάς Ε.Π.Ε', 'Γιώτης Α.Ε.',
                     'Barilla Hellas A.E.', 'Υφαντής Α.Β.Ε.Ε.', 'Ατλάντα Α.Ε.', 'FrieslandCampina Ελλάς Α.Ε.',
                     'Μακριδάκη Α.- Γ.Μακατουνάκης Ο.Ε', 'Ελληνικές Φάρμες Ρεθύμνου', 'Φάγε Α.Ε.', 'Μεταξά ΑΒΕ',
                     'ΣΥΛΛΙΓΑΡΔΟΣ Ο.Ε.', 'ΣΥΝΤΙΧΑΚΗΣ ΝΙΚ ΑΠΒΕΕ', 'DIAGEO Hellas', 'Nestle Ελλάς Α.Ε.',
                     'Λυραράκης - ΓΕΑ ΑΕ', 'AIA Agricola Italiana Alimentare S.P.A.', 'Arla Foods Ελλάς Α.Ε.Β.Ε.',
                     'Bacardi Ελλάς Μονοπρόσωπη ΕΠΕ', 'Bahlsen 30001 Hannover Germany', 'Bic Βιολέξ Α.Ε.',
                     'Bingo Α.Ε. - Tottis Group of Companies', 'Bolton Hellas AEBE', 'Bristol - Myers Squibb AE',
                     'Cadbury Hellas A.E.', 'Candia Nuts® ΑΒΕΕ', 'Chipita A.E.',
                     'Colgate - Palmolive Μονοπρόσωπη Ε.Π.Ε.', 'CPW Ελλάς Δημητριακά Πρωινού Α.Ε.',
                     'Craft Foods Ελλάς Α.Ε.', 'Cretamel', 'Croco® Sc Srl', 'Danone AE', 'Diana Nuova Ε.Π.Ε',
                     'Dimak Plast®', 'Elbisco A.B.E.E. Εταιρία Τροφίμων', 'Mars Hellas A.E.', 'Numil Hellas A.E.',
                     'Olympic Hermes S.A.', 'Optima A.E.', 'Pallas A.E. Ζαχαρώδη', 'Perfeti Van Melle Hellas',
                     'Propharm LTD', 'Reckitt Benckiser Hellas SA', 'S.C. Johnson Hellas Ltd',
                     'Καλαμαράκης Κ.Ε. Α.Β.Ε.Ε. - Καλας Α.Ε.', 'SCA Hygiene Products A.E.',
                     'Κονσερβοοπιια Βορειου Αιγαιου Α.Ε.Β.Ε.', 'Sonel A.E. Loreal Hellas S.A.'
                     ]

coca_cola = (
    'AMITA', 'AVRA', 'Coca-Cola', 'Fanta', 'Frulite', 'Monster', 'Nestea', 'Powerade', 'Schweppes', 'Sprite', 'Λυττός')
pepsico = ('7up', 'Lipton', 'Pepsi', 'RockStar', 'Ήβη')
kri_kri = ('Κρι Κρι', 'Κρι Κρι')
olympos = ('Tyras', 'Όλυμπος')
delta = ('Life', 'Wibe', 'Βλάχας', 'Δέλτα')
hellenic = ('Kanaki', 'Mimikos')
olympiaki = ('Corona', 'Fix', 'Guinness', 'Henninger', 'Kaiser', 'Magners', 'Mythos', 'Somersby', 'Tuborg')
athinaiki = ('Alfa', 'Amstel', 'Buckler', 'Desperados', 'Fisher', 'Heineken', 'Sol', 'Strongbow')
tasty = ('Cheetos', 'Doritos', 'Quaker', 'Tasty')
vardas = ('Βάρδας', 'Βάρδας')
bdf = ('nivea', 'nivea')
karamolegkos = ('Καραμολεγκος', 'Κατσελης')
papadopoulos = ('Papadopoulou', 'Papadopoulou')
zaros = ('Ζάρος', 'Ζάρος')
zargianakis = ('Σητειακό', 'Σητειακό')
bothilia = ('Σεληνάρι', 'Σεληνάρι')
procter = ('Always', 'Ariel', 'Camay', 'Clairol', 'Crest', 'Essex', 'Fairy', 'Gillette', 'Head&Shoulders',
           'Herbal Essences', 'Lenor', 'Oral B', 'Pampers', 'Pantene', 'Rol', 'Swiffer', 'Tampax', 'Tide',
           'Viakal', 'Wash&Go', 'Wella', 'Wellaflex')
giotis = ('Fytro', 'Hemo', 'Άνθος', 'Γιώτης')
barilla = ('Barilla', 'Misko', 'Wasa')
ifantis = ('Υφαντής', 'Υφαντής')
atlanta = ('Kelloggs', 'Twinings', 'Ατλάντα')
frieslandCampina = ('Fina', 'Frisolac', 'Milner', 'Nounou', 'Βλάχας')
makatounis = ('Elli Spices', 'Elli Spices')
ellinikes_farmes = ('Hellenic', 'Hellenic')
fage = ('Φάγε', 'Φάγε')
metaxa = ('Metaxa', 'Metaxa')
siligardos = ('Αγνότης', 'Συλλιγάρδος')
sintixakis = ('Συντιχάκης', 'Συντιχάκης')
diageo = ('Johnnie Walker', 'Haig', 'Dimple', 'Cardhu', 'J&B', 'Classic Malts', 'Smirnoff', 'Cîroc', 'Ketel One',
          'Gordons', 'Gordon Space', 'Tanqueray', 'Captain Morgan', 'Pampero', 'Baileys', 'Grand Marnier',
          'Veuve Clicquot Ponsardin', 'Veuve De Fraince')
nestle = ('Felix', 'Fitness', 'Friskies', 'Gourmet', 'Maggi', 'Nescafe', 'Nesquik', 'Nestle', 'Perrier', 'Purina',
          'Smarties', 'Παπαγάλος')
lyrakis = ('Lyrarakis', 'Lyrarakis')
aia = ('Aia Wudy', 'Gran Podere')
arla = ('Arla', 'Buko', 'Castello', 'Lurpack')
bacardi_hellas = ('Bacardi', 'Bacardi')
bahlsen = ('Bahlsen', 'Bahlsen')
bic = ('Bic', 'Bic')
bingo = ('Amaretti', 'Champion', 'Koukou Roukou', 'Serenata', 'Tottis', 'Τοττης')
bolton = ('Borotalco', 'Fornet', 'Merito', 'Neutro Roberts', 'Omino Bianco', 'Overlay', 'Rio Mare', 'Softex', 'WC Net')
bristol = ('Depon', 'Depon')
cadbury = ('Bassetts', 'Cadbury')
candia = ('Candia Nuts', 'Melibar', 'Μίνως')
chipita = ('7 Days', 'Chipita', 'Extra', 'Fineti', 'Molto', 'Recor')
colgate = ('Azax', 'Colgate', 'Fabuloso', 'Palmolive', 'Soupline')
cpw = ('Cheerios', 'Clusters', 'Fitness', 'Nesquik')
craft = ('Dentyne', 'Energizer', 'Fonzies', 'Halls', 'Jacobs', 'Kraft', 'Maxwell', 'Milka', 'Mondelez', 'Nabisco',
         'Philadelphia', 'Tassimo', 'Toblerone', 'Trident', 'V6', 'Παυλίδης')
cretamel = ('Cretamel', 'Orino')
croco = ('Croco', 'Croco')
danone = ('Actimel', 'Activia', 'Danone')
diana = ('Attiva', 'Diana', 'Diana Ottima', 'Flert', 'Ottima')
dimak = ('Delta Plast', 'Dimak Plast', 'Viomes', 'Viosarp')
elbisco = ('Elite', 'Forma', 'Rollers', 'Αλλατίνη', 'Κρις-Κρις', 'Μανα')
mars = ('Bounty', 'Catisfactions', 'Catsan', 'Dolmio', 'Kitekat', 'Maltesers', 'Mars', 'Milky Way', 'Orbit',
        'Pedigree', 'Perfect Fit', 'Sheba', 'Snickers', 'Twix', 'Uncle Bens', 'Whiskas', 'Wringleys')
numil = ('Aptamil', 'Milupa', 'Nutricia')
olympic = ('Olympic', 'Olympic')
optima = ('Adoro', 'Dirollo', 'Ήπειρος', 'Ταλαγάνι')
pallas = ('Pallas', 'Λάβδας')
perfeti = ('Chupa Chups', 'Fruittella', 'Mentos', 'Vivident')
propharm = ('Olive Touch', 'Propharm', 'Tantra Beauty')
reckit = ('Airwick', 'Brasso', 'Calgon', 'Cilit Bang', 'Clearasil', 'Dettol', 'Dr Scoll', 'Finish',
          'Harpic', 'Quanto', 'Silvo', 'Vanish', 'Veet', 'Vitroglen', 'Woolite')
johnson = ('Autan', 'Baygon', 'Bio Shout', 'Duck', 'Glade', 'Mr Muscle', 'Pronto', 'Raid')
kalamarakis = ('Midland', 'Tulip', 'Ήρα', 'Κάλας', 'Φιλικές')
sca_hygiene = ('Libero', 'Libresse', 'Tena', 'Zewa')
conserva = ('Dakor', 'Flokos', 'Trata')
sonel = ('Ambre Solaire', 'Dermo', 'Elvive', 'Fructis', 'Garnier', 'Loreal', 'minerals', 'Studio', 'Studio FX')

c = [coca_cola, pepsico, kri_kri, olympos, delta, hellenic, olympiaki, athinaiki, tasty, vardas, bdf, karamolegkos,
     papadopoulos, zaros, zargianakis, bothilia, procter, giotis, barilla, ifantis, atlanta, frieslandCampina,
     makatounis, ellinikes_farmes, fage, metaxa, siligardos, sintixakis, diageo, nestle, lyrakis, aia, arla,
     bacardi_hellas, bahlsen, bic, bingo, bolton, bristol, cadbury, candia, chipita, colgate, cpw, craft, cretamel,
     croco, danone, diana, dimak, elbisco, mars, numil, olympic, optima, pallas, perfeti, propharm, reckit, johnson,
     kalamarakis, sca_hygiene, conserva, sonel
     ]

print('Κατασκευαστές Σύνολο: {}'.format(len(c)))

# ------- ΠΡΟΜΗΘΕΥΤΕΣ -----------

compo1 = (
    'Μακριδάκη Α.- Γ.Μακατουνάκης Ο.Ε', 'CANDIA NUTS', 'ΠΕΡΝΙΕΝΤΑΚΗΣ Δ. Α.Ε.Β.Ε. ΑΝΤΙΠΡΟΣΩΠΙΕΣ - ΔΙΑΝΟΜΕΣ - ΕΜΠΟΡΙΟ')
compo2 = ('ΣΙΓΑΝΟΣ Α.Ε. - ΑΝΤΙΠΡΟΣΩΠΕΙΣ - ΕΜΠΟΡΙΟ ΠΟΤΩΝ', 'Bazaar A.E.', 'ΕΜΠΟΡΙΚΗ ΤΡΟΦΟΔΟΤΙΚΗ Α.Ε.')

# ------- OUTPUT FILE -----------
output_file = "/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/EM.xlsx"


#  ----Ονόματα προμηθευτών
query_00 = "SELECT NAME FROM ESFITradeAccount where ESFITradeAccount.Type = 1 and Inactive= 0"
print('Ερώτημα Στην Βάση: Προμηθευτές & Ανάθεση Αποτελέσματος --> Ολοκληρώθηκε:  {}'.format(datetime.now()))
# -----------| SQL QUERY | All Years | All Months | TZIROS | SALES|----------------------------------
query_01 = """
SELECT
    format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy') as 'YEAR'
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 1 then TurnOver end), 0) Jan
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2 then TurnOver end), 0) Feb
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 3 then TurnOver end), 0) Mar
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 4 then TurnOver end), 0) Apr
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 5 then TurnOver end), 0) May
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 6 then TurnOver end), 0) Jun
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 7 then TurnOver end), 0) Jul
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 8 then TurnOver end), 0) Aug
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 9 then TurnOver end), 0) Sep
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 10 then TurnOver end), 0) Oct
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 11 then TurnOver end), 0) Nov
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 12 then TurnOver end), 0) Dec
  ,Sum(ESFIItemPeriodics.TurnOver) AS TurnOver

 FROM ESFIItemPeriodics
     LEFT JOIN ESGOSites AS FK_ESFIItemPeriodics_ESGOSites
       ON ESFIItemPeriodics.fSiteGID = FK_ESFIItemPeriodics_ESGOSites.GID
     LEFT JOIN ESGOFiscalPeriod AS FK_ESFIItemPeriodics_ESGOFiscalPeriod
       ON ESFIItemPeriodics.fFiscalPeriodGID = FK_ESFIItemPeriodics_ESGOFiscalPeriod.GID
     WHERE
        (FK_ESFIItemPeriodics_ESGOSites.Code = '1')
GROUP BY

        format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy')
order by
        format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy')
"""


# sales
def query(inputs):
    q = """

    SELECT
       IsNull(FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode,'') 
        AS SubCategory
        ,Sum(ESFIItemPeriodics.TurnOver) AS TurnOver
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2012 then TurnOver end), 0) as 'f2012'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2013 then TurnOver end), 0) as 'f2013'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2014 then TurnOver end), 0) as 'f2014'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2015 then TurnOver end), 0) as 'f2015'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2016 then TurnOver end), 0) as 'f2016'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2017 then TurnOver end), 0) as 'f2017'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2018 then TurnOver end), 0) as 'f2018'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2019 then TurnOver end), 0) as 'f2019'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2020 then TurnOver end), 0) as 'f2020'


    FROM ESFIItemPeriodics 
     LEFT JOIN ESFIItem AS FK_ESFIItemPeriodics_ESFIItem
       ON ESFIItemPeriodics.fItemGID = FK_ESFIItemPeriodics_ESFIItem.GID
     LEFT JOIN ESGOSites AS FK_ESFIItemPeriodics_ESGOSites
       ON ESFIItemPeriodics.fSiteGID = FK_ESFIItemPeriodics_ESGOSites.GID
     LEFT JOIN ESGOFiscalPeriod AS FK_ESFIItemPeriodics_ESGOFiscalPeriod
       ON ESFIItemPeriodics.fFiscalPeriodGID = FK_ESFIItemPeriodics_ESGOFiscalPeriod.GID
     LEFT JOIN ESFIZItemSubCategory AS FK_ESFIItem_ESFIZItemSubCategory
       ON FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode = FK_ESFIItem_ESFIZItemSubCategory.Code 
       AND FK_ESFIItemPeriodics_ESFIItem.fCompanyCode = FK_ESFIItem_ESFIZItemSubCategory.fCompanyCode
     WHERE
           (FK_ESFIItemPeriodics_ESFIItem.AssemblyType <> 1) --όχι τα σετ
       AND (FK_ESFIItemPeriodics_ESFIItem.ItemType <> 6) -- όχι εγγυοδοσία
       AND (FK_ESFIItemPeriodics_ESFIItem.ItemClass = 1)  -- Κλάση Είδη Αποθήκης (1)
       AND (FK_ESFIItemPeriodics_ESGOSites.Code = 1) -- Υποκατάστημα (1) Κεντρικά Έδρας
       AND (FK_ESFIItemPeriodics_ESFIItem.fItemSubcategoryCode in {}) -- Υποκατηγορία (είσοδος)

    GROUP BY
 -- FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate,
    IsNull(FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode,'')  --  (Brand Name group)

""".format(inputs)
    return q


def count_query(inputs):
    q = """
    SELECT
      count(*)
    FROM  ESFIItem 
        WHERE    
       (ESFIItem.fItemSubcategoryCode in {})
""".format(inputs)
    return q


# ----------- Προμηθευτές -------------------
def querry_suppliers(input):
    q = """
      SELECT
    FK_ESFITradeAccountPeriodics_ESFITradeAccount.Name AS 'Επωνυμία'
    ,Sum(ESFITradeAccountPeriodics.NumberOfInvoices) AS 'Ποσότητα Τιμολογίων'
    ,Sum(ESFITradeAccountPeriodics.NumberOfCreditNotes) AS 'Ποσότητα Πιστωτικών'
    ,Sum(ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover) AS 'Τζίρος'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2012 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2012'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2013 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2013'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2014 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2014'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2015 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2015'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2016 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2016'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2017 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2017'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2018 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2018'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2019 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2019'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2020 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2020'

FROM ESFITradeAccountPeriodics AS ESFITradeAccountPeriodics
     LEFT JOIN ESFITradeAccount AS FK_ESFITradeAccountPeriodics_ESFITradeAccount
       ON ESFITradeAccountPeriodics.fTradeAccountGID = FK_ESFITradeAccountPeriodics_ESFITradeAccount.GID
     LEFT JOIN ESGOSites AS FK_ESFITradeAccountPeriodics_ESGOSites_TradeAccountSite
       ON ESFITradeAccountPeriodics.fTradeAccountSiteGID = FK_ESFITradeAccountPeriodics_ESGOSites_TradeAccountSite.GID
     LEFT JOIN ESGOSites AS FK_ESFITradeAccountPeriodics_ESGOSites_Site
       ON ESFITradeAccountPeriodics.fSiteGID = FK_ESFITradeAccountPeriodics_ESGOSites_Site.GID
     LEFT JOIN ESGOFiscalPeriod AS FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod
       ON ESFITradeAccountPeriodics.fFiscalPeriodGID = FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.GID
     LEFT JOIN ESGOFiscalYear AS FK_ESFITradeAccountPeriodics_ESGOFiscalYear
       ON ESFITradeAccountPeriodics.fFiscalYearGID = FK_ESFITradeAccountPeriodics_ESGOFiscalYear.GID
     LEFT JOIN ESGOPerson AS FK_ESGOPerson_PersonCode1
       ON FK_ESFITradeAccountPeriodics_ESFITradeAccount.fPersonCodeGID = FK_ESGOPerson_PersonCode1.GID
     LEFT JOIN ESFIZTradeAccountFamily AS FK_ESFITradeAccount_ESFIZTradeAccountFamily
       ON FK_ESFITradeAccountPeriodics_ESFITradeAccount.fFamilyCode = FK_ESFITradeAccount_ESFIZTradeAccountFamily.Code
     LEFT JOIN ESGOZRegionGroup AS FK_ESGOSites_ESGOZRegionGroup
       ON FK_ESFITradeAccountPeriodics_ESGOSites_TradeAccountSite.fRegionGroupCode = FK_ESGOSites_ESGOZRegionGroup.Code
     LEFT JOIN ESGOZGroup AS FK_ESGOPerson_ESGOZGroup
       ON FK_ESGOPerson_PersonCode1.fGroupCode = FK_ESGOPerson_ESGOZGroup.Code
     LEFT JOIN ESGOZCategory AS FK_ESGOPerson_ESGOZCategory
       ON FK_ESGOPerson_PersonCode1.fCategoryCode = FK_ESGOPerson_ESGOZCategory.Code
     LEFT JOIN ESGOZActivity AS FK_ESGOPerson_ESGOZActivity
       ON FK_ESGOPerson_PersonCode1.fActivityCode = FK_ESGOPerson_ESGOZActivity.Code
WHERE
        (ESFITradeAccountPeriodics.TradeAccountType in (1,3))
       AND (FK_ESFITradeAccountPeriodics_ESFITradeAccount.Name  in {}) -- tuple με προμθευτές (είσοδος)
       AND (ESFITradeAccountPeriodics.Turnover > 0) --  Τζίρος > 0
       and FK_ESFITradeAccountPeriodics_ESGOSites_Site.Code = 1 -- Υποκατάστημα (1) Κεντρικά Έδρας
       

GROUP BY FK_ESFITradeAccountPeriodics_ESFITradeAccount.Name
order by 4  desc
    """.format(input)
    return q


# -------------ANSWERS----------------------------
answer_00 = pd.read_sql_query(query_00, sql_connect.sql_cnx())
print('Προμηθευτές: SQL Ερώτημα για το σύνολο των Προμηθευτών -> --> Ολοκληρώθηκε:  {}'.format(datetime.now()))
x = ()
for i in range(len(answer_00)):
    x = x + (answer_00['NAME'][i],)



answer_01 = pd.read_sql_query(query_01, sql_connect.sql_cnx())


prod_per_year = answer_01.groupby(['YEAR'])['TurnOver'].sum().reset_index()


X = prod_per_year['YEAR']
y = prod_per_year['TurnOver']
plt.figure(figsize=(15, 9))
plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΤΖΙΡΟΣ' , title= 'ELOUNDA MARKET')
plt.bar(X, y, alpha=0.5)
for a, b in zip(X, y):
    label = "{:.2f} €".format(b)

    # this method is called for each point
    plt.annotate(label,  # this is the text
                 (a, b),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center
plt.grid(True, alpha=0.5)
plt.savefig('views.png')
plt.show()


answer = []
answer_sum = []
answer_count = []
answer_quant = []
year_2012 = []
year_2013 = []
year_2014 = []
year_2015 = []
year_2016 = []
year_2017 = []
year_2018 = []
year_2019 = []
year_2020 = []
for i in range(len(c)):
    answer.append(pd.read_sql_query(query(c[i]), sql_connect.sql_cnx()))
    answer_sum.append(sum(answer[i].TurnOver))
    answer_count.append(len(answer[i]))
    answer_quant.append(pd.read_sql_query(count_query(c[i]), sql_connect.sql_cnx()))
    year_2012.append(sum(answer[i].f2012))
    year_2013.append(sum(answer[i].f2013))
    year_2014.append(sum(answer[i].f2014))
    year_2015.append(sum(answer[i].f2015))
    year_2016.append(sum(answer[i].f2016))
    year_2017.append(sum(answer[i].f2017))
    year_2018.append(sum(answer[i].f2018))
    year_2019.append(sum(answer[i].f2019))
    year_2020.append(sum(answer[i].f2020))


promi8eutes_list = [compo1, compo2, x]


#  ΠΡΟΜΗΘΕΥΤΕΣ
answer_prom = []
answer_prom_count = []
for i in range(len(promi8eutes_list)):
    answer_prom.append(pd.read_sql_query(querry_suppliers(promi8eutes_list[i]), sql_connect.sql_cnx()))
    answer_prom_count.append(len(answer_prom[i]))


# -------------OPEN FILE | WRITE ----------------------------
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:  # doctest: +SKIP
    # PUT ANSWERS INSIDE EXCEL
    answer_01.to_excel(writer, sheet_name='YEAR', startcol=0, startrow=1)
    print('Πωλήσεις εγγραφή στο  Excel --> Ολοκληρώθηκε:  {}'.format(datetime.now()))
    k = 2
    for i in range(len(c)):
        answer[i].to_excel(writer, sheet_name='ΚΑΤΑΣΚΕΥΑΣΤΗΣ', startcol=0, startrow=k)
        k += (4 + answer_count[i])
    excel_positioning = 1
    # Προμηθευτές
    for i in range(len(promi8eutes_list)):
        answer_prom[i].to_excel(writer, sheet_name='ΠΡΟΜΗΘΕΥΤΕΣ', startcol=0, startrow=excel_positioning)
        excel_positioning += (4 + answer_prom_count[i])
    print('Προμηθευτές εγγραφή στο  Excel --> Ολοκληρώθηκε:  {}'.format(datetime.now()))
    # Get access to the workbook and sheet
    workbook = writer.book
    worksheet = writer.sheets['YEAR']
    worksheet_2 = writer.sheets['ΚΑΤΑΣΚΕΥΑΣΤΗΣ']
    worksheet_3 = workbook.add_worksheet('ΓΡΑΦΗΜΑΤΑ')
    worksheet_4 = writer.sheets['ΠΡΟΜΗΘΕΥΤΕΣ']
    worksheet_5 = workbook.add_worksheet('ΣΥΝΟΠΤΙΚΑ')

    # Reduce the zoom a little
    worksheet.set_zoom(90)
    # Center formatting
    center = workbook.add_format({'align': 'center',
                                  # 'border': 1,
                                  'valign': 'vcenter',
                                  'num_format': '#,##0',
                                  'bold': False,
                                  "font_name": "Avenir Next"})

    # Add a number format for cells with money.
    money_fmt = workbook.add_format({'num_format': '€#,##0.00',
                                     'align': 'center',
                                     'bold': False,
                                     "font_name": "Avenir Next"})
    # SET BLUE Foreground on Cells
    set_color = workbook.add_format({'fg_color': '#ffdcd1',
                                     'align': 'center',
                                     # 'border': 1,
                                     'valign': 'vcenter',
                                     'num_format': '#,##0',
                                     'bold': False,
                                     "font_name": "Avenir Next"
                                     })

    # FORMAT CELLS WIDTH
    worksheet.set_column('C:O', 15, money_fmt)
    worksheet.set_column('A:B', 15, center)
    worksheet_2.set_column('A:A', 5, center)
    worksheet_2.set_column('B:W', 15, money_fmt)
    worksheet_4.set_column('A:A', 5, center)
    worksheet_4.set_column('B:B', 40, center)
    worksheet_4.set_column('C:D', 20, center)
    worksheet_4.set_column('E:O', 20, money_fmt)
    print('Format EXCEL --> --> Ολοκληρώθηκε:  {}'.format(datetime.now()))
    # MERGE CELLS
    worksheet.merge_range("M14:R14", 'ΤΕΛΕΥΑΤΑΙΑ ΕΝΗΜΕΡΩΣΗ', set_color)
    worksheet.merge_range("M15:R15", 'ΗΜΕΡΟΜΗΝΙΑ: {}  '.format(datetime.now().strftime("%d/%m/%Y")), set_color)
    worksheet.merge_range("M16:R16", 'ΩΡΑ: {}  '.format(datetime.now().strftime("%H:%M:%S")), set_color)
    print('MERGING CELLS -- > --> Ολοκληρώθηκε:  {}'.format(datetime.now()))
    # Conditional Formating
    worksheet.conditional_format('O1:O15', {'type': '3_color_scale'})
    print('Conditional Formating -- > --> Ολοκληρώθηκε:  {}'.format(datetime.now()))
    # CHARTS
    chart01 = workbook.add_chart({'type': 'column'})
    chart01.add_series({'categories': '=YEAR!$B$3:$B$11',
                        'values': '=YEAR!$O$3:$O$11',
                        'data_labels': {'value': True,
                                        'position': 'outside_end'
                                        },
                        'name': 'ΤΖΙΡΟΣ'
                        }, )
    chart01.set_x_axis({'name': 'YEAR'})
    chart01.set_y_axis({'name': 'ΤΖΙΡΟΣ'})
    chart01.set_size({'width': 1100, 'height': 300})
    worksheet.insert_chart('A12', chart01)
    print('CHARTS INSIDE EXCEL --> --> Ολοκληρώθηκε:  {}'.format(datetime.now()))
    # Counters για τα Γραφήματα
    a = []
    b = []
    for i in range(0, 900, 13):
        for j in range(0, 22, 7):
            a.append(i)
            b.append(j)
    print('Counters για τα Γραφήματα --> Ολοκληρώθηκε:  {}'.format(datetime.now()))


    # Function CHART
    def chart(i, j, k):
        chart02 = workbook.add_chart({'type': 'column'})
        chart02.add_series({'categories': '=ΚΑΤΑΣΚΕΥΑΣΤΗΣ!$D$3:$L$3',
                            'values': '=ΚΑΤΑΣΚΕΥΑΣΤΗΣ!$D${}:$L${}'.format(j, j),
                            'name': '{}'.format(kataskevastes_lst[i])
                            }, )
        chart02.set_x_axis({'name': 'YEAR'})
        chart02.set_y_axis({'name': 'ΤΖΙΡΟΣ'})
        chart02.set_legend({'position': 'none'})
        chart02.set_size({'width': 400, 'height': 250})
        # worksheet_2.insert_chart('M{}'.format(k), chart02)
        worksheet_3.insert_chart(a[i], b[i], chart02)


    # Function MERGE CELLS
    def w(number, lista, count, sumi):
        worksheet_2.merge_range("A{}:D{}".format(number, number), '{}'.format(kataskevastes_lst[lista]), set_color)
        worksheet_2.merge_range("E{}:F{}".format(number, number), 'Πλήθος Κωδικών:', set_color)
        worksheet_2.merge_range("G{}:H{}".format(number, number), '{}'.format(count), set_color)
        worksheet_2.merge_range("I{}:J{}".format(number, number), 'Τζίρος:', set_color)
        worksheet_2.merge_range("K{}:L{}".format(number, number), '{}€'.format(round(sumi, 2)), set_color)
        worksheet_2.merge_range("A{}:L{}".format(number + 1, number + 1), '{}'.format(c[i]), set_color)


    j = 1
    k = 1
    row_num = 0
    col_num = 0
    for i in range(len(c)):
        worksheet_2.conditional_format('C{}:C{}'.format(j + 3, j + 3 + answer_count[i]), {'type': 'data_bar'})
        w(j, i, answer_quant[i].values, answer_sum[i])
        j += (answer_count[i] + 2)
        worksheet_2.write(j, 3, year_2012[i])
        worksheet_2.write(j, 4, year_2013[i])
        worksheet_2.write(j, 5, year_2014[i])
        worksheet_2.write(j, 6, year_2015[i])
        worksheet_2.write(j, 7, year_2016[i])
        worksheet_2.write(j, 8, year_2017[i])
        worksheet_2.write(j, 9, year_2018[i])
        worksheet_2.write(j, 10, year_2019[i])
        worksheet_2.write(j, 11, year_2020[i])
        j += 1
        chart(i, j, k)
        j += 1
        k += 10


    # Προμηθευτές
    def fun_suppliers(input):
        worksheet_4.merge_range('$A${}:$M${}'.format(input, input),
                                'Επιλεγμένη Λίστα Προμηθευτών', set_color)


    prom_counter = 1
    for i in range(len(promi8eutes_list)):
        worksheet_4.conditional_format('C{}:C{}'.format(prom_counter + 2, prom_counter + 2 + answer_prom_count[i]),
                                       {'type': 'data_bar', 'bar_color': 'blue'})
        worksheet_4.conditional_format('D{}:D{}'.format(prom_counter + 2, prom_counter + 2 + answer_prom_count[i]),
                                       {'type': 'data_bar', 'bar_color': 'green'})
        worksheet_4.conditional_format('E{}:E{}'.format(prom_counter + 2, prom_counter + 2 + answer_prom_count[i]),
                                       {'type': 'data_bar', 'bar_color': 'red'})
        fun_suppliers(prom_counter)
        prom_counter += (answer_prom_count[i] + 4)

    # Συνοπτικά
    worksheet_5.write(0, 0, 'Κατασκευαστής')
    j = 2012
    for i in range(1, 9):
        worksheet_5.write(0, i, '{}'.format(j))
        j += 1
    j = 1
    for i in range(len(c)):
        worksheet_5.write(j, 0, kataskevastes_lst[i])
        worksheet_5.write(j, 1, year_2012[i])
        worksheet_5.write(j, 2, year_2013[i])
        worksheet_5.write(j, 3, year_2014[i])
        worksheet_5.write(j, 4, year_2015[i])
        worksheet_5.write(j, 5, year_2016[i])
        worksheet_5.write(j, 6, year_2017[i])
        worksheet_5.write(j, 7, year_2018[i])
        worksheet_5.write(j, 8, year_2019[i])
        worksheet_5.write(j, 9, year_2020[i])
        j += 1

    # INSERT IMAGES
    # worksheet.insert_image('A27', 'sap.png', {'x_scale': 0.2, 'y_scale': 0.2})
    # worksheet.insert_image('I27', 'crystal.png', {'x_scale': 0.27, 'y_scale': 0.29})

plt.figure(figsize=(50, 50))
j=1
for i in range(len(c)):
    y = []
    y.append(year_2012[i])
    y.append(year_2013[i])
    y.append(year_2014[i])
    y.append(year_2015[i])
    y.append(year_2016[i])
    y.append(year_2017[i])
    y.append(year_2018[i])
    y.append(year_2019[i])
    y.append(year_2020[i])
    X = ['12', '13', '14', '15', '16', '17', '18', '19', '20']
    Y = y
    plt.subplot(8, 8, j, ylabel='ΤΖΙΡΟΣ', title=kataskevastes_lst[i])
    plt.bar(X, y, color=f"#{random.randrange(0x1000000):06x}")
    j+=1

plt.grid(True, alpha=0.5)
plt.savefig('kataskevastis_views.png')
plt.show()

slack_app.send_text("""
>ΣΤΑΤΙΣΤΙΚΑ ELOUNDA MARKET
`Ενημερώθηκε Το Αρχείο: EM.xlsx`
""", slack_app.channels[1])

slack_app.send_files('EM.xlsx', output_file, 'xlsx', slack_app.channels[1])
slack_app.send_files('views.png', 'views.png', 'png', slack_app.channels[1])
slack_app.send_files('kataskevastis_views.png', 'kataskevastis_views.png', 'png', slack_app.channels[1])