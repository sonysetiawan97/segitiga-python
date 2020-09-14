from os import system, name

def clear(): 

    # for windows 
    if (name == 'nt'): 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

class Segitiga:

    def __init__ (self, tinggi):
        self.tinggi = tinggi
    
    def SegitigaSikuSikuKiri(self):
        i = 1
        string = ""

        while (i <= self.tinggi):
            x = 1
            while(x <= i):
                x += 1
                string += "*"
            i += 1
            string += "\n"
        print(string)

    def SegitigaSikuSikuKanan(self):
        string = ""

        for i in range (self.tinggi):
            start = i+1
            for x in range (start, self.tinggi):
                string += " "
            for y in range (-1, i):
                string += "*"
            string += "\n"
        print(string)

    def SegitigaSikuSikuTerbalikKiri(self):
        string = ""

        for i in range(self.tinggi):
            start = i
            for x in range(start, self.tinggi):
                string += "*"
            string += "\n"
        print(string)

    def SegitigaSikuSikuTerbalikKanan(self):
        string = ""

        for i in range(self.tinggi):
            start = i
            end = i
            for x in range(0, end):
                string += " "
            for y in range(start, self.tinggi):
                string += "*"
            string += "\n"
        print(string)
    
    def SegitigaSamaKakiBentuk1(self):
        i = 1
        string = ""

        while (i <= self.tinggi):
            x = i
            y = 1
            while (x < self.tinggi):
                x += 1
                string += " "
            while (y <= i):
                y += 1
                string += "**"
            i+=1
            string += "\n"
        print(string)

    def SegitigaSamaKakiBentuk2(self):
        i = 1
        string = ""

        while (i <= self.tinggi):
            x = i
            y = 1
            z = 1
            while (x < self.tinggi):
                x += 1
                string += " "
            while (y <= i):
                y += 1
                string += "*"
            while (z < i):
                z += 1
                string += "*"
            i += 1
            string += "\n"
        print(string)

    def SegitigaSamaKakiTerbalikBentuk1(self):
        string = ""

        for i in range(self.tinggi):
            start = i
            end = i
            for x in range(0, end):
                string += " "
            for y in range(start, self.tinggi):
                string += "**"
            string += "\n"
        print(string)

    def SegitigaSamaKakiTerbalikBentuk2(self):
        string = ""

        for i in range(self.tinggi):
            start = i
            end = i
            for x in range(0, end):
                string += " "
            for y in range(start, self.tinggi):
                string += "*"
            for z in range(start+1, self.tinggi):
                string += "*"
            string += "\n"
        print(string)

def main():
    loop = True
    while (loop == True):
        clear()
        print("===== Bentuk-Bentuk Segitiga =====")
        print("1. Segitiga siku kiri")
        print("2. Segitiga siku kanan")
        print("3. Segitiga siku Kiri Terbalik")
        print("4. Segitiga siku kanan Terbalik")
        print("5. Segitiga sama kaki bentuk 1")
        print("6. Segitiga sama kaki bentuk 2")
        print("7. Segitiga sama kaki terbalik bentuk 1")
        print("8. Segitiga sama kaki terbalik bentuk 1")
        print("99. exit")
        pilihan = int(input("pilihan: "))
        if (pilihan == 99):
            loop = False
            print("\nTerima Kasih telah menggunakan aplikasi ini")
        else:
            tinggiSegitiga = int(input("Tinggi segitiga: "))
        print()
        if (pilihan == 1):
            segitiga = Segitiga(tinggiSegitiga)
            segitiga.SegitigaSikuSikuKiri()
        elif (pilihan == 2):
            segitiga = Segitiga(tinggiSegitiga)
            segitiga.SegitigaSikuSikuKanan()
        elif (pilihan == 3):
            segitiga = Segitiga(tinggiSegitiga)
            segitiga.SegitigaSikuSikuTerbalikKiri()
        elif (pilihan == 4):
            segitiga = Segitiga(tinggiSegitiga)
            segitiga.SegitigaSikuSikuTerbalikKanan()
        elif (pilihan == 5):
            segitiga = Segitiga(tinggiSegitiga)
            segitiga.SegitigaSamaKakiBentuk1()
        elif (pilihan == 6):
            segitiga = Segitiga(tinggiSegitiga)
            segitiga.SegitigaSamaKakiBentuk2()
        elif (pilihan == 7):
            segitiga = Segitiga(tinggiSegitiga)
            segitiga.SegitigaSamaKakiTerbalikBentuk1()
        elif (pilihan == 8):
            segitiga = Segitiga(tinggiSegitiga)
            segitiga.SegitigaSamaKakiTerbalikBentuk2()
        input("Press enter to continue")
        clear()

main()