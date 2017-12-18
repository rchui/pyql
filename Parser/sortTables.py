""" Sort tables based on 2 length comparisons and size """
import operator
def order_tables(froms, indexes, comparisons, attributes, table_counts):
    """
    froms: froms list
    indexes: indexes dict
    comparisons: comparison dict

    returns: Ordered tables
    """
    # If no = on index value
    # Then find the table with the most 3 length rules

    # order froms by small to large
    new_count_list = []
    for from_ in froms:
        if from_[0] not in table_counts.keys():
            new_count_list.append(table_counts[indexes[from_[0]][2].split('.')[0]])
        else:
            new_count_list.append(table_counts[from_[0]])

    _, froms = zip(*sorted(zip(new_count_list, froms)))

    froms=list(froms)
    # get the alias name and the attributeindex number of table when it has a 2 length rule

    store_current_list_ind = None
    no_eq_on_idx=True

    num_3_len_rules={}

    for key in comparisons.keys():
        for rule_list in comparisons[key]:
            if len(rule_list) == 3:
                if key in num_3_len_rules.keys():
                    num_3_len_rules[key]+=1
                else:
                    num_3_len_rules[key]=1
                # store the table alias name and the attribute_idx of the 2 len rule
                index_of_att = rule_list[0]

                 # convert the attribute number index into the attr name
                att_name = attributes[key][index_of_att]

                # num to keep track, from_ is a list in a list of lists
                for num, from_ in enumerate(froms):
                    if key == from_[1]:
                        actual = from_[0]
                        # need to check if the froms is optimally ordered
                        if indexes[actual][0] == att_name:
                            no_eq_on_idx=False
                            if num != 0:
                                store_current_from = from_
                                store_current_list_ind = num
                                break
                        else:
                            pass
    if store_current_list_ind is not None:
        del froms[store_current_list_ind]
        froms.insert(0, store_current_from)

    if no_eq_on_idx:
        sorted_x = sorted(num_3_len_rules.items(), key=operator.itemgetter(1))
        key=sorted_x[0][0]
        for idx, f in enumerate(froms):
            if f[1] == key:
                key_idx = idx
                new_from = f
                break
        del froms[key_idx]
        froms.insert(0, new_from)
    return froms
