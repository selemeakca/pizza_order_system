import csv
import datetime


# pizza üst sinifini olusturuyoruz:

class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost

#pizza sınıfının alt sınıflarını olusturuyoruz
class KlasikPizza(Pizza):
    cost = 100

    def __init__(self):
        self.description = "\nKlasik pizza: zeytin,Sosis,Sucuk ve Kasar  olusmaktadir..."
        print(self.description)


class MargaritaPizza(Pizza):
    cost = 90

    def __init__(self):
        self.description = "\nMargarita pizza: Mozarella,Domates,Feslegenden olusmaktadir..."
        print(self.description)


class TurkPizza(Pizza):
    cost = 120

    def __init__(self):
        self.description = "\nTurk pizza: Pastırma,Sogan,Sarimsakdan olusmaktadir..."
        print(self.description)


class SadePizza(Pizza):
    cost = 40

    def __init__(self):
        self.description = "\nSade pizza: Sadece kaşardan olusmaktadir..."
        print(self.description)


# pizza sınıfının decorator üst sınıfımız olusturduk

class Decorator(Pizza):
    def __init__(self, ing):
        super().__init__()
        self.component = ing

    def get_cost(self):
        return self.component.get_cost() + \
               Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
               ' ;' + Pizza.get_description(self)


# decoratorun super sınıfları
class Zeytin(Decorator):
    cost = 5.0

    def __init__(self, ing):
        super().__init__(ing)


class Mantar(Decorator):
    cost = 5.0

    def __init__(self, ing):
        super().__init__(ing)


class KeciPeynir(Decorator):
    cost = 7.0

    def __init__(self, ing):
        super().__init__(ing)


class Et(Decorator):
    cost = 10.0

    def __init__(self, ing):
        super().__init__(ing)


class Sogan(Decorator):
    cost = 5.0

    def __init__(self, ing):
        super().__init__(ing)


class Misir(Decorator):
    cost = 5.0

    def __init__(self, ing):
        super().__init__(ing)


# Menuyu ekrana yazdirma fonksiyonu:
def main():
    with open("menu.txt", "r") as cust_menu:
        for i in cust_menu:
            print(i, end="")

    class_dict = {1: KlasikPizza,
                  2: MargaritaPizza,
                  3: TurkPizza,
                  4: SadePizza,
                  11: Zeytin,
                  12: Mantar,
                  13: KeciPeynir,
                  14: Et,
                  15: Sogan,
                  16: Misir}

    button = input("Lütfen Pizzanızı Seçiniz: ")
    while button not in ["1", "2", "3", "4"]:
        button = input("Lutfen 1-4 arasında bir sayı seciniz: ")

    order = class_dict[int(button)]()

    while button != "+":
        button = input(
            "Fazladan malzeme almak istiyorsaniz numarasını(11-16) giriniz (Siparişinizi Onaylamak İçin '+' ya  basiniz): ")
        if button in ["11", "12", "13", "14", "15", "16"]:
            order = class_dict[int(button)](order)
#ekrana pizza ve secilen soslar ile fiyatı yazdırma
    print("\n" + order.get_description().strip() + "| $" + str(order.get_cost()))
    print("\n")

    # Siparisi veritabanına kaydetme

    print("----------Siparis Bilgileri----------\n")
    name = input("İsminiz: ")
    TC = input("TC Kimlik Numaranız: ")
    kart_no = input("Kredi Kartı Numaranızı Giriniz: ")
    kart_sifre = input("Kredi Kartı Şifrenizi Giriniz: ")
    time = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter='|') #| ile ayırma işlemleri yap
        #isim,tc,kart no kart sifresi malzemeler fiyatı ve zaman ile yazdır.
        orders.writerow([name, TC, kart_no, kart_sifre, order.get_description(),str(order.get_cost()), time])
    print("Siparisiniz Onaylandı.")


main()