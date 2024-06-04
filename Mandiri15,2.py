import re
import random
import string

emails = [
    "anton@mail.com dimiliki oleh antonius",
    "budi@gmail.co.id dimiliki oleh budi anwari",
    "slamet@getnada.com dimiliki oleh slamet slumut",
    "matahari@tokopedia.com dimiliki oleh toko matahari",
    "gagalmoveon@yahoo.com dimiliki oleh kenzie"
]
for email_info in emails:
    email = email_info.split()[0]
    username = re.findall(r'([^@]+)[@]', email)[0]
    characters = string.ascii_letters + string.digits
    password =  ''.join(random.choice(characters) for _ in range(8))
    print(f"{email} username: {username}, password: {password}")