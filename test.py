#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

# η πραγματική μου διαφορά είναι 610
x =610
# η χρέωση μου είναι 0.063 / 0.11
a = .063
b = .11

# o πρώτος λογαριασμός ήταν 61,43 synollika 81.17
# ο δεύτερος λογαριασμός ήταν 35,95 synolika 47,5
# ο τρίτος είναι 35,95 synolika 47,5

logariasmoi = [61.43, 35.95, 35.95]
katanalosi_low = 0
katanalosi_high = 0
for i in logariasmoi:
    katanalosi_low += i / a
    katanalosi_high += i / b


print(round(katanalosi_low), round(katanalosi_high))

print(487 *0.11028)
print(487 *0.063)

"""
alphabet                                    αλφάβητο
what's your name                            Πως σε λένε
surname                                     επίθετο
How do you spell it                         Πως γράφεται
number                                      αριθμός
What's your telephone number                Ποιό είναι το τηλέφωνό σου
theory                                      θεωρία
consonant                                   σύμφωνο
vowel                                       φωνήεν
alarm clock                                 ξυπνητήρι
digital camera                              ψηφιακή φωτογραφική μηχανή
agenda                                      αντζέντα
scarf                                       φουλάρι
pencil case                                 μολυβοθήκη
glue                                        κόλλα   

"""