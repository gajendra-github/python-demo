def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

email = input("Enter email address: ")
old_domain = input("Enter old domain: ")
new_domain = input("Enter new domain: ")

result = replace_domain(email, old_domain, new_domain)
print(result)




