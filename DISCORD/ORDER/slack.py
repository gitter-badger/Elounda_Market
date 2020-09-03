#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import slack_app


def run(output_file, supplier, store, answer_02, person, phone_number, file_path):
    slack_app.send_text(f"""
    >ΚΑΤΑΧΩΡΗΘΗΚΕ Η ΠΑΡΑΓΓΕΛΙΑ
    `ΑΡΧΕΙΟ: {output_file}`
    `ΠΡΟΜΗΘΕΥΤΗΣ: {supplier}`
    `ΥΠΟΚΑΤΑΣΤΗΜΑ: {store}`
    `PDA ID: {answer_02.ID[0]}`
    `E-MAIL: {person.EMailAddress[0]}`
    `Τηλ.: {phone_number}`
    >
    >Data Science Tools Used:
    >:slack: :github: :docker: :kubernetes: :python: :javascript: :nodejs: :react: :vue: :fbwow:
    """, slack_app.channels[3])

    slack_app.send_files(output_file, file_path, 'xlsx', slack_app.channels[3])
