def equal_strings(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2


if __name__ == '__main__':
    unittest.main()
