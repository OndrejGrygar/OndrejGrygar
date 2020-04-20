
my_str="""Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Mauris vulputate lacus id eros consequat tempus.
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id
        tiger123@email.cz auctor massa molestie at. Nunc tristique
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas
        massa purus, ultricies a dictum ut, dapibus vitae massa.
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor
        nec molestie quis, auctor a quam. Quisque b2b@money.fr
        pretium dolor et tempor feugiat. Morbi libero lectus,
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est.
        Maecenas gravida turpis nec ultrices aliquet."""
def collect_emails(text):
    words = text.split()
    emails = []
    for word in words:
        if '@' in word:
            emails.append(word)
    return emails
def select_num_emails(emails):
    num_mails = []
    for email in emails:
        if contains_a_number(email):
            num_mails.append(email)
    return num_mails
def contains_a_number(string):
    for num in range(10):
        if str(num) in string:
            return True
    return False
print(collect_emails(my_str))
emails = collect_emails(my_str)
print(select_num_emails(emails))

def domains(emails):
    domains = []
    for email in emails:
        domains.append(email.split('@')[1])
    return domains

print(domains(emails))

def main():
    result = {'emails_with_nums': None,
              'domains': None}
    result['emails_with_nums'] = select_num_emails(emails)
    result['domains'] = domains(emails)
    print(result)

main()











