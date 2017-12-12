## Sort tables based on 2 length comparisons and size
import sys

def order_tables(froms, indexes, comparisons, attributes):
    """
    froms: froms list
    indexes: indexes dict
    comparisons: comparison dict

    returns: Ordered tables
    """

    #for key in indexes.keys():
    #    print(key, indexes[key][0])

    #get the alias name and the attributeindex number of table when it has a 2 length rule
    
    print(froms)
    store_current_list_idx = None
    for key in comparisons.keys():
        for rule_list in comparisons[key]:
            if len(rule_list)==2:
                index_of_att=rule_list[0] #store the table alias name and the attribute_idx of the 2 len rule

                 #convert the attribute number index into the attr name
                att_name=attributes[key][index_of_att]
    
                for num, from_ in enumerate(froms): #num to keep track, from_ is a list in a list of lists
                    print(num, "woooooo")
                    if key==from_[1]:
                        actual=from_[0]
                        if indexes[actual][0]==att_name: #need to check if the froms is optimally ordered
                            print(indexes[actual][0], att_name)
                            if num != 0:
                                store_current_from=from_
                                store_current_list_ind=num
                            else: #num==0, the tables are orderd optimally in froms, were good to go
                                break
                        else:
                            print("didn't work", indexes[actual][0], att_name)

    if store_current_list_idx != None:
        del froms[store_current_list_ind]
        froms.insert(0, store_current_from)
                


    
    print(froms)
    
    sys.exit()


