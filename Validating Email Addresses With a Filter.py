import re

def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split('@')
        website,extension = url.split('.')
    except ValueError:
        return False
    
    if username.replace('-','').replace('_','').isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True
    #email_re = r'[a-zA-Z0-9\.-]+@[\w\.-]+'
    #return lambda x: re.match(email_re,x)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
