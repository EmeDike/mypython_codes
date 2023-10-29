

def split_string(string):

    domains = []
    for email in email_addresses:
        element = email.split("@")
        domains.append(element[1])
    return domains



email_addresses = ["user1@example.com", "user2@gmail.com"]
result = split_string(email_addresses)
print(result)
