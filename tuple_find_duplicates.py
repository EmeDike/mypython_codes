def display_duplicates_of_tuple(input_tuple):
        seen = set()
        duplicates = set()

        for item in input_tuple:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)

        return tuple(duplicates)

