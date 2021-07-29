#!/usr/bin//env python3

import reports
import emails
import requests
import os
import re
import datetime
import datetime
def build_data():

    # need to get our data and build what will be inside the pdf
    desc_path = os.path.join(os.getcwd(), "supplier-data", "descriptions")
    desc_list = os.listdir(desc_path)

    # init the pdf body text
    pdf_body = []
    pdf_text = ""

    # Get the name and weight of each fruit and put inside array
    for file in desc_list:
        with open(os.path.join(desc_path, file), 'r') as f:
            reader_list = f.readlines()
            fruit = {}
            fruit["name"] = reader_list[0].strip()
            fruit["weight"] = reader_list[1].strip()
        pdf_body.append(fruit)
    for fruit in pdf_body:
        for key in fruit:
            pdf_text += f"name: {fruit['name']}<br/>weight: {fruit['weight']}<br/><br/>"
    return pdf_text

if __name__ == "__main__":
    pdf_body = build_data()
    current_date = datetime.datetime.now()
    
    pdf_report = reports.generate_report("/tmp/processed.pdf", "Processed Updated on {}".format(current_date.strftime("%B %d, %Y")), pdf_body)
    message = emails.generate_email("automation@example.com", "{}@example.com".format(os.environ.get('USER')), "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
    emails.send_email(message)
