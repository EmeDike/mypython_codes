

#Suppose you have a list of URLs.
# How can you check if each URL starts with "https://" using a string method?
def starts_with_method(string):
    url_list = []
    for element in my_url_list:
        if element.startswith("http://"):
            url_list.append(element)
    return url_list





my_url_list = ["https://example.com", "http://example.org"]
result = starts_with_method(my_url_list)
print(result)