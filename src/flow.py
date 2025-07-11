# check_for_reorder.py -> reorder_list
# retrieve_email.py -> list of email, demand products, id, name
# automate_email.py -> df to send the mail with send_mail function


import os
import sys
from retrieve_email import retrieve_email_name
from check_for_reorder import check_for_reorder
from automate_email import automate_email
import pandas as pd

sample_shop = 2
sample_product = 1

reorder_list = check_for_reorder(sample_shop)
retrieved_email = retrieve_email_name(reorder_list)

grouped_df = pd.DataFrame(retrieved_email, columns = ["id", "quantity", "email_id", "product_name"])

automate_email(df= grouped_df)