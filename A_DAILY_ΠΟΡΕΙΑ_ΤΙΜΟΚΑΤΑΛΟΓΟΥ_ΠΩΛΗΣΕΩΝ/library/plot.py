#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt
from datetime import datetime as dt
import squarify
import numpy as np
import seaborn as sns


def run(choose_pricelist, from_date, to_date, brand_sales, final_result, dates_ranges,
        tziros_per_day, quantity_per_day, tim_id):
    # -------------------- PLOT --------------------
    plt.figure(figsize=(15, 9))
    plt.subplot(
        title=f'ΕΝΕΡΓΕΙΑ: {tim_id}η || {choose_pricelist.comments} || [ΕΝΑΡΞΗ: {from_date.strftime("%d-%m")} - ΛΗΞΗ: {to_date.strftime("%d-%m")}]')
    plt.bar(brand_sales.BRAND, brand_sales.Turnover, alpha=0.5, color='red', label='ΤΖΙΡΟΣ')
    plt.plot(brand_sales.BRAND, brand_sales.SalesQuantity, alpha=0.5, color='blue', label='ΠΟΣΟΤΗΤΑ', marker='o',
             linestyle="None")
    for x, y in zip(brand_sales.BRAND, brand_sales.SalesQuantity):
        if y - int(y) == 0:
            quant_type = 'TEM'
        else:
            quant_type = 'ΚΙΛ'
        label = "{:.2f}\n{}".format(y, quant_type)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (x, y),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 4),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.xticks(rotation=20)
    plt.grid(True, alpha=0.8)
    plt.box(False)
    plt.legend()
    plt.savefig('images/bar.png')
    plt.close()

    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel=f'ΗΜΕΡΟΜΗΝΙΕΣ (EΝΗΜΕΡΩΘΗΚΕ:{dt.now().strftime("%d/%m %H:%M:%S")})',
                title=f"""
    ΠΩΛΗΣΕΙΣ ΑΝΑ ΗΜΕΡΑ || ΣΥΝΟΛΑ: {round(final_result.SalesQuantity.sum(), 2)}TEM / {round(final_result.Turnover.sum(), 2)}€  
    """)
    colors = [plt.cm.Spectral(i / float(len(dates_ranges))) for i in range(len(dates_ranges))]
    plt.bar(dates_ranges.strftime('%a \n%d/%m'), tziros_per_day, alpha=0.9, color=colors, label='ΤΖΙΡΟΣ')
    plt.plot(dates_ranges.strftime('%a \n%d/%m'), quantity_per_day, alpha=0.9, color='darkgreen', label='ΠΟΣΟΤΗΤΑ',
             marker='o',
             linestyle="None")
    for x, y in zip(dates_ranges.strftime('%a \n%d/%m'), quantity_per_day):
        label = "{:.2f}\nTEM".format(y)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (x, y),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 12),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.axhline(y=round(np.mean(tziros_per_day), 2), xmin=0, xmax=1, linestyle='-.',
                label=f'Μ.Ο. ΤΖΙΡΟΥ: ({round(np.mean(tziros_per_day), 2)} EUR)',
                color='black', alpha=.2)
    plt.axhline(y=round(np.mean(quantity_per_day)), xmin=0, xmax=1, linestyle='--',
                label=f'Μ.Ο. ΠΟΣΟΤΗΤΑΣ: ({round(np.mean(quantity_per_day))} TEM)',
                color='red', alpha=.4)
    plt.grid(True, alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.box(False)
    plt.savefig('images/daily.png')
    # plt.show()
    plt.close()

    # -------------------- TREE MAP --------------------
    # Prepare Data
    try:
        df = brand_sales

        labels = df.apply(
            lambda x: f'{x[0]}\n({x[1]} {"TEM" if x[1] - int(x[1]) == 0 else "ΚΙΛ"})\n({round(x[2], 2)} EUR)',
            axis=1)
        sizes = df['SalesQuantity'].values.tolist()
        colors = [plt.cm.Spectral(i / float(len(labels))) for i in range(len(labels))]

        # Draw Plot
        plt.figure(figsize=(15, 9))
        squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)

        # Decorate
        plt.title(
            f"ΠΩΛΗΣΕΙΣ ΠΟΣΟΤΗΤΑ || ΣΥΝΟΛΑ: {round(final_result.SalesQuantity.sum(), 2)}TEM / {round(final_result.Turnover.sum(), 2)}€  ")
        plt.axis('off')
        plt.savefig('images/tree_map_quantity.png')
        # plt.show()
        plt.close()
    except ZeroDivisionError:
        print('ΣΦΑΛΜΑ ZeroDivisionError ΣΤΟ TREE MAP')
    except:
        print('ΑΛΛΟ ΣΦΑΛΜΑ ΣΤΟ TREE MAP')
    finally:
        plt.close()

    # -------------------- PIE --------------------
    x = brand_sales.Turnover
    y = brand_sales.BRAND
    plt.figure(figsize=(15, 9))
    explode = (
        0, .1, 0, 0, .1, 0, .1, 0, .1, 0, 0, .1, 0, .1, 0, .1, 0, 0, .1, 0, 0, .1, 0, 0, .1, 0, .1, 0, .1, 0, 0, .1, 0,
        .1,
        0, .1, 0, 0, .1, 0, 0, .1)
    colors = [plt.cm.Spectral(i / float(len(x))) for i in range(len(x))]
    e = tuple(explode[:len(x)])
    plt.subplot(
        title=f'ΑΠΕΙΚΟΝΙΣΗ: ΤΖΙΡΟΣ / BRAND || ΕΝΕΡΓΕΙΑ: {tim_id}η || {choose_pricelist.comments} || [ΕΝΑΡΞΗ: {from_date.strftime("%d-%m")} - ΛΗΞΗ: {to_date.strftime("%d-%m")}]')
    plt.pie(x, labels=y, autopct='%.1f%%', explode=e, colors=colors)
    plt.axis('equal')
    plt.savefig('images/pricelist_pie.png')
    # plt.show()
    plt.close()

    # -------------------- HEAT MAP --------------------


def heatmap(df, name):
    f, ax = plt.subplots(figsize=(15, 9))
    cmap = sns.diverging_palette(133, 10, as_cmap=True)
    sns.heatmap(df, annot=True, fmt='.2f', linewidths=.5, ax=ax, cmap='YlGnBu').set(title=f'{name}')
    plt.savefig('images/heatmap.png')
    plt.box(False)
    # plt.show()
    plt.close()


def heatmap_02(df, name):
    f, ax = plt.subplots(figsize=(15, 9))
    cmap = sns.diverging_palette(133, 10, as_cmap=True)
    sns.heatmap(df, annot=True, fmt='.2f', linewidths=.5, ax=ax, cmap='coolwarm').set(title=f'{name}')
    plt.savefig('images/heatmap_turnover.png')
    plt.box(False)
    # plt.show()
    plt.close()


# -------------------- BOX PLOT --------------------

def sea_boxplot(data, name):
    f, ax = plt.subplots(figsize=(15, 9))
    sns.boxplot(data=data, x='BRAND', y='QUANTITY', palette="Blues_d").set(title=f'{name}')
    plt.savefig('images/boxplot.png')
    plt.box(False)
    # plt.show()
    plt.close()


# -------------------- Violin PLOT --------------------

def sea_violinplot(data, name):
    f, ax = plt.subplots(figsize=(15, 9))
    sns.violinplot(data=data, x='BRAND', y='TURNOVER', palette="Blues_d").set(title=f'{name}')
    plt.savefig('images/violin.png')
    plt.box(False)
    # plt.show()
    plt.close()
