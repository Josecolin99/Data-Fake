import random
from list import *

class DataFake():

    def RandomOneName():
        sex = random.choice(['male', 'female'])
        if sex == 'male':
            name = random.choice(name_m) + " " +random.choice(last_names) + " " + random.choice(last_names)
            return name.title()
        elif sex == 'female':
            name = random.choice(name_f) + " " +random.choice(last_names) + " " + random.choice(last_names)
            return name.title()
        
    def RandomTwoName():
        sex = random.choice(['male', 'female'])
        if sex == 'male':
            name = random.choice(name_m) + " " + random.choice(name_m) + " " +random.choice(last_names) + " " + random.choice(last_names)
            return name.title()
        elif sex == 'female':
            name = random.choice(name_f) + " " + random.choice(name_f) + " " +random.choice(last_names) + " " + random.choice(last_names)
            return name.title()
        
    def RandomName():
        name_length = random.choice([1, 2])
        if name_length == 1:
            name = DataFake.RandomOneName()
            print(name.center(50, '*'))
            return name
        elif name_length == 2:
            name = DataFake.RandomTwoName()
            print(name.center(50, '*'))
            return name
    
    def checkSex(name):
        name_list = name.split(' ')
        if name_list[0].upper() in name_m:
            return 'male'
        elif name_list[0].upper() in name_f:
            return 'female'
        else:
            return 'El nombre no esta en la lista, si quieres un sexo random utiliza: '
        
    def RandomEmail(nombre):
        """Devuelve un email al pasarle un nombre
        Parameters
        ----------
        nombre : str
            Cadena que contendra el nombre del cual se generara un email
        Returns
        -------
        email : str
            Cadena que contiene el emial generado
        """
        servers = [
            'gmail',
            'outlook',
            'yahoo',

        ]
        dot = [
            '.com',
            '.net',
            '.es',
            '.mx',
        ]
        list_name = nombre.split(' ')
        num_name = len(list_name)
        if num_name >= 5:
            first_name = list_name[0]
            first_letter_name = first_name[0]
            last_name_ma = list_name[3]
            last_name_fa = list_name[4]
            first_letter_last_fa = last_name_fa[0]
            user = (first_letter_name + last_name_ma +
                    first_letter_last_fa).lower()
            email = user + '@' + random.choice(servers) + random.choice(dot)
            return email
        if num_name == 4:
            first_name = list_name[0]
            first_letter_name = first_name[0]
            last_name_ma = list_name[2]
            last_name_fa = list_name[3]
            first_letter_last_fa = last_name_fa[0]
            user = (first_letter_name + last_name_ma +
                    first_letter_last_fa).lower()
            email = user + '@' + random.choice(servers) + random.choice(dot)
            return email
        elif num_name == 3:
            first_name = list_name[0]
            first_letter_name = first_name[0]
            last_name_ma = list_name[1]
            last_name_fa = list_name[2]
            first_letter_last_fa = last_name_fa[0]
            user = (first_letter_name + last_name_ma +
                    first_letter_last_fa).lower()
            email = user + '@' + random.choice(servers) + random.choice(dot)
            return email
        elif num_name == 2:
            first_name = list_name[0]
            first_letter_name = first_name[0]
            last_name_ma = list_name[1]
            user = (first_letter_name + last_name_ma).lower()
            email = user + '@' + random.choice(servers) + random.choice(dot)
            return email
        elif num_name == 1:
            first_name = list_name[0]
            user = (first_name).lower()
            email = user + '@' + random.choice(servers) + random.choice(dot)
            return email

    def PersonalizedEmail(nombre, servidor_web):
        """Devuelve un email al pasarle un nombre
        Parameters
        ----------
        nombre : str
            Cadena que contendra el nombre del cual se generara un email.
            Ejemplo: Jose Angel Colin Najera
        servidor_web : str
            Cadena que contendra el servidor con el que cuente el email.
            Ejemplo: gmail.com
        Returns
        -------
        email : str
            Cadena que contiene el emial generado
        """
        list_name = nombre.split(' ')
        num_name = len(list_name)
        if num_name >= 5:
            first_name = list_name[0]
            first_letter_name = first_name[0]
            last_name_ma = list_name[3]
            last_name_fa = list_name[4]
            first_letter_last_fa = last_name_fa[0]
            user = (first_letter_name + last_name_ma +
                    first_letter_last_fa).lower()
            email = user + '@' + servidor_web
            return email
        if num_name == 4:
            first_name = list_name[0]
            first_letter_name = first_name[0]
            last_name_ma = list_name[2]
            last_name_fa = list_name[3]
            first_letter_last_fa = last_name_fa[0]
            user = (first_letter_name + last_name_ma +
                    first_letter_last_fa).lower()
            email = user + '@' + servidor_web
            return email
        elif num_name == 3:
            first_name = list_name[0]
            first_letter_name = first_name[0]
            last_name_ma = list_name[1]
            last_name_fa = list_name[2]
            first_letter_last_fa = last_name_fa[0]
            user = (first_letter_name + last_name_ma +
                    first_letter_last_fa).lower()
            email = user + '@' + servidor_web
            return email
        elif num_name == 2:
            first_name = list_name[0]
            first_letter_name = first_name[0]
            last_name_ma = list_name[1]
            user = (first_letter_name + last_name_ma).lower()
            email = user + '@' + servidor_web
            return email
        elif num_name == 1:
            first_name = list_name[0]
            user = (first_name).lower()
            email = user + '@' + servidor_web
            return email


if __name__ == '__main__':
    data = DataFake
    x = 0
    while x != 100:
        nombreRandom = data.RandomName()
        email = data.RandomEmail(nombreRandom)
        emailPersonalizado = data.PersonalizedEmail(nombreRandom, 'outlook.com')
        sex = data.checkSex(nombreRandom)
        print("".center(50, '-'))
        print(email)
        print(emailPersonalizado)
        print(nombreRandom)
        print(sex)
        print("".center(50, '-'))
        x += 1
