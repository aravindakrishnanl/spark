from db_retrieval import retrieval

def retrieve_email_name(demand_lst):
    """
    This is a python function that retrieve the respective email from mail.db with unique from the demand_list
    params:
        1. demand_lst = the list with two values, say unique_id of the product and demand of the product
    return:
        The demand lst with unique id, demand of the product,  respective email and the product name of unique id
    """
    for i in range(1, len(demand_lst)+1):
        mail = retrieval(f"select mail from items where id = {str(i)}", "mail")
        product_name = retrieval(f"select name from items where id = {str(i)}", "products")
        demand_lst[i-1].append(mail[0][0])
        demand_lst[i-1].append(product_name[0][0])
    return demand_lst

#sample
# lst = [[8, 52], [10, 51], [13, 53], [15, 54], [18, 57], [22, 55], [25, 51], [28, 58], [36, 51], [38, 53], [45, 52]]
# print(retrieve_email(lst))