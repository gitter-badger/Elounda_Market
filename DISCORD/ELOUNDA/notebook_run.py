#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
import matplotlib.pyplot as plt

def cset(data, name, brands):
    df = data[data.SubCategory.isin(brands)]
    df_pivot = df.pivot(index='SubCategory', columns='YEAR', values='TurnOver')
    df_pivot['ΣΥΝΟΛΑ'] = df_pivot.sum(axis=1)
    df_pivot.loc['TOTAL'] = df_pivot.sum(axis=0)
    df_pivot = df_pivot.fillna(0)
    ccplot = df.groupby('YEAR').sum().reset_index()
    X = ccplot.YEAR
    y = ccplot.TurnOver
    plt.figure(figsize=(25, 9))
    plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΤΖΙΡΟΣ', title=name)
    colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
    plt.bar(X, y, alpha=0.9, color=colors)
    for a, b in zip(X, y):
        label = "{:.2f} €".format(b)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (a, b),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.5)
    plt.show()
    plt.close()
    return df_pivot


def names():
    kataskevastes_lst = ['COCA COLA 3E', 'Pepsico - HBH', 'Κρι Κρι', 'ΟΛΥΜΠΟΣ Γαλακτοβιομηχανία Λαρίσης Α.Ε.',
                         'Δέλτα Τρόφιμα Α.Ε.', 'Hellenic Quality Foods A.E.', 'Ολυμπιακή Ζυθοποιία Α.Ε.',
                         'Αθηναϊκή Ζυθοποιία Α.Ε.', 'Tasty Foods ΑΒΓE', 'ΕΜΜΑΝΟΥΗΛ ΒΑΡΔΑΣ & ΣΙΑ Ο.Ε. ΑΡΤΟΠΟΙΕΙΟ',
                         'BDF - Beiersdorf Hellas A.E.', 'Καραμολέγκος ΑΕ', 'Παπαδοπουλος Ε.Ι. Α.Ε.',
                         'Βότομος Α.Ε. Ζαρος',
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
    return kataskevastes_lst

def brands():
    coca_cola = [
        'Amita', 'Avra', 'Coca-Cola', 'Fanta', 'Frulite', 'Monster', 'Nestea', 'Powerade', 'Schweppes', 'Sprite',
        'Λυττός']
    pepsico = ['7up', 'Lipton', 'Pepsi', 'RockStar', 'Ήβη']
    kri_kri = ['Κρι Κρι']
    olympos = ['Tyras', 'Όλυμπος']
    delta = ['Life', 'Wibe', 'Βλάχας', 'Δέλτα']
    hellenic = ['Kanaki', 'Mimikos']
    olympiaki = ['Corona', 'Fix', 'Guinness', 'Henninger', 'Kaiser', 'Magners', 'Mythos', 'Somersby', 'Tuborg']
    athinaiki = ['Alfa', 'Amstel', 'Buckler', 'Desperados', 'Fisher', 'Heineken', 'Sol', 'Strongbow']
    tasty = ['Cheetos', 'Doritos', 'Quaker', 'Tasty']
    vardas = ['Βάρδας']
    bdf = ['Nivea']
    karamolegkos = ['Καραμολεγκος', 'Κατσελης']
    papadopoulos = ['Papadopoulou']
    zaros = ['Ζάρος']
    zargianakis = ['Σητειακό']
    bothilia = ['Σεληνάρι']
    procter = ['Always', 'Ariel', 'Camay', 'Clairol', 'Crest', 'Essex', 'Fairy', 'Gillette', 'Head&Shoulders',
               'Herbal Essences', 'Lenor', 'Oral B', 'Pampers', 'Pantene', 'Rol', 'Swiffer', 'Tampax', 'Tide',
               'Viakal', 'Wash&Go', 'Wella', 'Wellaflex']
    giotis = ['Fytro', 'Hemo', 'Άνθος', 'Γιώτης']
    barilla = ['Barilla', 'Misko', 'Wasa']
    ifantis = ['Υφαντής']
    atlanta = ['Kelloggs', 'Twinings', 'Ατλάντα']
    frieslandCampina = ['Fina', 'Frisolac', 'Milner', 'Nounou', 'Βλάχας']
    makatounis = ['Elli Spices']
    ellinikes_farmes = ['Hellenic']
    fage = ['Φάγε']
    metaxa = ['Metaxa']
    siligardos = ['Αγνότης', 'Συλλιγάρδος']
    sintixakis = ['Συντιχάκης']
    diageo = ['Johnnie Walker', 'Haig', 'Dimple', 'Cardhu', 'J&B', 'Classic Malts', 'Smirnoff', 'Cîroc', 'Ketel One',
              'Gordons', 'Gordon Space', 'Tanqueray', 'Captain Morgan', 'Pampero', 'Baileys', 'Grand Marnier',
              'Veuve Clicquot Ponsardin', 'Veuve De Fraince', 'Veuve Clicquot Ponsa']
    nestle = ['Felix', 'Fitness', 'Friskies', 'Gourmet', 'Maggi', 'Nescafe', 'Nesquik', 'Nestle', 'Perrier', 'Purina',
              'Smarties', 'Παπαγάλος']
    lyrakis = ['Lyrarakis']
    aia = ['Aia Wudy', 'Gran Podere']
    arla = ['Arla', 'Buko', 'Castello', 'Lurpack']
    bacardi_hellas = ['Bacardi']
    bahlsen = ['Bahlsen']
    bic = ['Bic']
    bingo = ['Amaretti', 'Champion', 'Koukou Roukou', 'Serenata', 'Tottis', 'Τοττης']
    bolton = [
    'Borotalco', 'Fornet', 'Merito', 'Neutro Roberts', 'Omino Bianco', 'Overlay', 'Rio Mare', 'Softex', 'WC Net']
    bristol = ['Depon']
    cadbury = ["Bassett's", 'Cadbury']
    candia = ['Candia Nuts', 'Melibar', 'Μίνως']
    chipita = ['7 Days', 'Chipita', 'Extra', 'Fineti', 'Molto', 'Recor']
    colgate = ['Azax', 'Colgate', 'Fabuloso', 'Palmolive', 'Soupline']
    cpw = ['Cheerios', 'Clusters', 'Fitness', 'Nesquik']
    craft = ['Dentyne', 'Energizer', 'Fonzies', 'Halls', 'Jacobs', 'Kraft', 'Maxwell', 'Milka', 'Mondelez', 'Nabisco',
             'Philadelphia', 'Tassimo', 'Toblerone', 'Trident', 'V6', 'Παυλίδης']
    cretamel = ['Cretamel', 'Orino']
    croco = ['Croco']
    danone = ['Actimel', 'Activia', 'Danone']
    diana = ['Attiva', 'Diana', 'Diana Ottima', 'Flert', 'Ottima']
    dimak = ['Delta Plast', 'Dimak Plast', 'Viomes', 'Viosarp']
    elbisco = ['Elite', 'Forma', 'Rollers', 'Αλλατίνη', 'Κρις-Κρις', 'Μανα']
    mars = ['Bounty', 'Catisfactions', 'Catsan', 'Dolmio', 'Kitekat', 'Maltesers', 'Mars', 'Milky Way', 'Orbit',
            'Pedigree', 'Perfect Fit', 'Sheba', 'Snickers', 'Twix', 'Uncle Bens', 'Whiskas', 'Wringleys']
    numil = ['Aptamil', 'Milupa', 'Nutricia']
    olympic = ['Olympic']
    optima = ['Adoro', 'Dirollo', 'Ήπειρος', 'Ταλαγάνι']
    pallas = ['Pallas', 'Λάβδας']
    perfeti = ['Chupa Chups', 'Fruittella', 'Mentos', 'Vivident']
    propharm = ['Olive Touch', 'Propharm', 'Tantra Beauty']
    reckit = ['Airwick', 'Brasso', 'Calgon', 'Cilit Bang', 'Clearasil', 'Dettol', 'Dr Scoll', 'Finish',
              'Harpic', 'Quanto', 'Silvo', 'Vanish', 'Veet', 'Vitroglen', 'Woolite']
    johnson = ['Autan', 'Baygon', 'Bio Shout', 'Duck', 'Glade', 'Mr Muscle', 'Pronto', 'Raid']
    kalamarakis = ['Midland', 'Tulip', 'Ήρα', 'Κάλας', 'Φιλικές']
    sca_hygiene = ['Libero', 'Libresse', 'Tena', 'Zewa']
    conserva = ['Dakor', 'Flokos', 'Trata']
    sonel = ['Ambre Solaire', 'Dermo', 'Elvive', 'Fructis', 'Garnier', 'Loreal', 'minerals', 'Studio', 'Studio FX']

    c = [coca_cola, pepsico, kri_kri, olympos, delta, hellenic, olympiaki, athinaiki, tasty, vardas, bdf, karamolegkos,
         papadopoulos, zaros, zargianakis, bothilia, procter, giotis, barilla, ifantis, atlanta, frieslandCampina,
         makatounis, ellinikes_farmes, fage, metaxa, siligardos, sintixakis, diageo, nestle, lyrakis, aia, arla,
         bacardi_hellas, bahlsen, bic, bingo, bolton, bristol, cadbury, candia, chipita, colgate, cpw, craft, cretamel,
         croco, danone, diana, dimak, elbisco, mars, numil, olympic, optima, pallas, perfeti, propharm, reckit, johnson,
         kalamarakis, sca_hygiene, conserva, sonel
         ]
    return c