#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from datetime import datetime
from Private import sql_connect
import pandas as pd
from DISCORD.ELOUNDA import slack, excel, sql, plot

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

# print('Κατασκευαστές Σύνολο: {}'.format(len(c)))

# ------- ΠΡΟΜΗΘΕΥΤΕΣ -----------

compo1 = (
    'Μακριδάκη Α.- Γ.Μακατουνάκης Ο.Ε', 'CANDIA NUTS', 'ΠΕΡΝΙΕΝΤΑΚΗΣ Δ. Α.Ε.Β.Ε. ΑΝΤΙΠΡΟΣΩΠΙΕΣ - ΔΙΑΝΟΜΕΣ - ΕΜΠΟΡΙΟ')
compo2 = ('ΣΙΓΑΝΟΣ Α.Ε. - ΑΝΤΙΠΡΟΣΩΠΕΙΣ - ΕΜΠΟΡΙΟ ΠΟΤΩΝ', 'Bazaar A.E.', 'ΕΜΠΟΡΙΚΗ ΤΡΟΦΟΔΟΤΙΚΗ Α.Ε.')




def run():
    # ------- OUTPUT FILE -----------
    output_file = "/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/EM.xlsx"
    # -------------ANSWERS----------------------------
    answer_00 = pd.read_sql_query(sql.query_00(), sql_connect.sql_cnx())
    print(' 00: Προμηθευτές: SQL Ερώτημα για το σύνολο των Προμηθευτών -> --> Ολοκληρώθηκε:  {}'.format(
        datetime.now().strftime("%H:%M:%S")))
    x = ()
    for i in range(len(answer_00)):
        percent = int((100 * (i + 1)) / len(answer_00))
        filler = "█" * percent
        remaining = '-' * (100 - percent)
        x = x + (answer_00['NAME'][i],)
        print(f'\r 00: Adding {answer_00["NAME"][i]} Done:[{filler}{percent}%{remaining}]', end='', flush=True)

    answer_01 = pd.read_sql_query(sql.query_01(), sql_connect.sql_cnx())
    print(f'\n 02: SQL QUERY DONE: {datetime.now().strftime("%H:%M:%S")}', end='')

    prod_per_year = answer_01.groupby(['YEAR'])['TurnOver'].sum().reset_index()
    print(f'\n 03: GROUPING DONE: {datetime.now().strftime("%H:%M:%S")}', end='')

    # ------------- PLOT ----------------------------
    plot.run_01(prod_per_year)

    print(f'\n 04: Plot DONE: {datetime.now().strftime("%H:%M:%S")}')

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
        percent = int((100 * (i + 1)) / len(c))
        filler = "█" * percent
        remaining = '-' * (100 - percent)

        answer.append(pd.read_sql_query(sql.query(c[i]), sql_connect.sql_cnx()))
        answer_sum.append(sum(answer[i].TurnOver))
        answer_count.append(len(answer[i]))
        answer_quant.append(pd.read_sql_query(sql.count_query(c[i]), sql_connect.sql_cnx()))
        year_2012.append(sum(answer[i].f2012))
        year_2013.append(sum(answer[i].f2013))
        year_2014.append(sum(answer[i].f2014))
        year_2015.append(sum(answer[i].f2015))
        year_2016.append(sum(answer[i].f2016))
        year_2017.append(sum(answer[i].f2017))
        year_2018.append(sum(answer[i].f2018))
        year_2019.append(sum(answer[i].f2019))
        year_2020.append(sum(answer[i].f2020))
        print(f'\r 05: Doing SUMS with counter Done:[{filler}{percent}%{remaining}]', end='', flush=True)

    promi8eutes_list = [compo1, compo2, x]
    print()

    #  ------------- ΠΡΟΜΗΘΕΥΤΕΣ -------------
    answer_prom = []
    answer_prom_count = []
    for i in range(len(promi8eutes_list)):
        percent = int((100 * (i + 1)) / len(promi8eutes_list))
        filler = "█" * percent
        remaining = '-' * (100 - percent)

        answer_prom.append(pd.read_sql_query(sql.querry_suppliers(promi8eutes_list[i]), sql_connect.sql_cnx()))
        answer_prom_count.append(len(answer_prom[i]))
        print(f'\r 06: looping with counter {i} Done:[{filler}{percent}%{remaining}]', end='', flush=True)

    # ------------- EXCEL ----------------------------
    excel.run(output_file, answer, answer_01, answer_count, c, promi8eutes_list, answer_prom, answer_prom_count,
              kataskevastes_lst, answer_quant, answer_sum, year_2012, year_2013, year_2014, year_2015, year_2016,
              year_2017, year_2018, year_2019, year_2020)
    # ------------- PLOT ----------------------------
    plot.run_02(year_2012, year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020,
                kataskevastes_lst, c)
    # ------------- SLACK ----------------------------
    slack.run(output_file)
