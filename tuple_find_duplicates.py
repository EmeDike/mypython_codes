def find_duplicates(input_tuple):
    seen = ()
    duplicates = ()

    for item in input_tuple:
        if item in seen:
            duplicates += (item,)
        else:
            seen += (item,)

    return duplicates
