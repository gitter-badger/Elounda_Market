#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from datetime import datetime


# Create Class Here
class Timokatalogos:
    def __init__(self, id, start, end, comments):
        self.id = id
        self.start = start
        self.end = end
        self.comments = comments
        self.quantity = 0
        self.turn_over = 0


january_2020_02 = Timokatalogos(1,
                                datetime(2020, 1, 14),
                                datetime(2020, 2, 8),
                                'Αφορά: Β Δεκαπενθήμερο Προσφορών Ιανουαρίου')

nestle_2020 = Timokatalogos(2,
                            datetime(2020, 2, 1),
                            datetime(2020, 2, 20),
                            'Αφορά: Σοκολάτες που Λήγουν')

feb_2020 = Timokatalogos(3,
                         datetime(2020, 2, 11),
                         datetime(2020, 2, 29),
                         'Αφορά: Β Δεκαπενθήμερο Προσφορών Φεβρουαρίου')

kinder_2020 = Timokatalogos(4,
                            datetime(2020, 2, 25),
                            datetime(2020, 4, 30),
                            'Αφορά: Πασχαλινό Αυγό')

xtapodi_2020 = Timokatalogos(5,
                             datetime(2020, 2, 29),
                             datetime(2020, 3, 2),
                             'Αφορά: Καθαρή Δευτέρα "Θαλασσινά"')

nescafe_2020 = Timokatalogos(6,
                             datetime(2020, 3, 3),
                             datetime(2020, 3, 31),
                             'Αφορά: Προϊόντα που Λήγουν')

march_2020 = Timokatalogos(7,
                           datetime(2020, 3, 4),
                           datetime(2020, 3, 15),
                           'Αφορά: Α Δεκαπενθήμερο Προσφορών Μαρτίου')

april_2020 = Timokatalogos(8,
                           datetime(2020, 3, 24),
                           datetime(2020, 4, 12),
                           'Αφορά: Α Δεκαπενθήμερο Προσφορών Απριλίου')

alevri_2020 = Timokatalogos(9,
                            datetime(2020, 4, 2),
                            datetime(2020, 4, 19),
                            'Αφορά: Φυτίνη και Αλεύρι')

may_2020 = Timokatalogos(10,
                         datetime(2020, 4, 21),
                         datetime(2020, 5, 10),
                         'Αφορά: Α Δεκαπενθήμερο Προσφορών Μαϊου')

may_2020_b = Timokatalogos(11,
                           datetime(2020, 5, 21),
                           datetime(2020, 5, 31),
                           'Αφορά: Nuvoleta Υγρά Πλυντηρίου')

nuvoleta_2020 = Timokatalogos(12,
                              datetime(2020, 5, 12),
                              datetime(2020, 5, 31),
                              'Αφορά: B Δεκαπενθήμερο Προσφορών Μαϊου')

june_2020 = Timokatalogos(13,
                          datetime(2020, 6, 1),
                          datetime(2020, 6, 15),
                          'Αφορά: Α Δεκαπενθήμερο Προσφορών Ιουνίου & Eπέκταση (Nivea - PizBuin)')

june_extra_2020 = Timokatalogos(14,
                                datetime(2020, 6, 16),
                                datetime(2020, 6, 30),
                                'Αφορά: B Δεκαπενθήμερο Προσφορών Ιουνίου & Επέκταση (Nivea - PizBuin - Royal Dutch - '
                                'Παπαγάλος)')

jule_2020 = Timokatalogos(15,
                          datetime(2020, 7, 1),
                          datetime(2020, 7, 15),
                          'Αφορά: Α Δεκαπενθήμερο Προσφορών Ιουλίου & Eπέκταση (Nivea - PizBuin - Nutella - Lays - '
                          'Παπαγάλος)')

jule_2020_b = Timokatalogos(16,
                            datetime(2020, 7, 16),
                            datetime(2020, 7, 31),
                            'Αφορά: Eπέκταση (Nivea (1+1) - Παπαγάλος - Nutella - Μαναβική)')

lista_2020 = [january_2020_02, nestle_2020, feb_2020, kinder_2020, xtapodi_2020, nescafe_2020, march_2020, april_2020,
              alevri_2020, may_2020, may_2020_b, nuvoleta_2020, june_2020, june_extra_2020, jule_2020, jule_2020_b]

for i in lista_2020:
    print(i.id, i.comments)
