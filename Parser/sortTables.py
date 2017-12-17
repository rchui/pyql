""" Sort tables based on 2 length comparisons and size """

def order_tables(froms, indexes, comparisons, attributes, table_counts):
    """
    froms: froms list
    indexes: indexes dict
    comparisons: comparison dict

    returns: Ordered tables
    """

    # print(froms)

    # order froms by small to large
    new_count_list = []
    for from_ in froms:
        if from_[0] not in table_counts.keys():
            new_count_list.append(table_counts[indexes[from_[0]][2].split('.')[0]])
        else:
            new_count_list.append(table_counts[from_[0]])

    _, froms = zip(*sorted(zip(new_count_list, froms)))


    # get the alias name and the attributeindex number of table when it has a 2 length rule
    # print(froms)

    store_current_list_ind = None
    for key in comparisons.keys():
        for rule_list in comparisons[key]:
            if len(rule_list) == 2:
                # store the table alias name and the attribute_idx of the 2 len rule
                index_of_att = rule_list[0]

                 # convert the attribute number index into the attr name
                att_name = attributes[key][index_of_att]

                # num to keep track, from_ is a list in a list of lists
                for num, from_ in enumerate(froms):
                    # print(num, "woooooo")
                    if key == from_[1]:
                        actual = from_[0]
                        # need to check if the froms is optimally ordered
                        if indexes[actual][0] == att_name:
                            # print(indexes[actual][0], att_name)
                            # print(num)
                            if num != 0:
                                # print('yes')
                                store_current_from = from_
                                store_current_list_ind = num
                                # print(store_current_from, store_current_list_ind)
                                break
                        else:
                            pass
                            # print("didn't work", indexes[actual][0], att_name)

    if store_current_list_ind is not None:
        del froms[store_current_list_ind]
        froms.insert(0, store_current_from)

    return froms
