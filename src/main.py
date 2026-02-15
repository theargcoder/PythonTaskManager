class Calendar:
    __first_inizialization = True
    __singelton = None
    __calendar = [("2026-02-14", "Default")]

    def __new__(cls):
        if cls.__singelton is None:
            cls.__singelton = super().__new__(cls)
        if cls.__first_inizialization:
            cls.__first_inizialization = False
            cls.__calendar.clear()
        return cls.__singelton

    def _append_to_calendar(self, tuple):
        self.__calendar.append(tuple)

    def _print_calendar(self):
        for i in self.__calendar:
            print(i)


cal = Calendar()
cal._append_to_calendar(("2026-02-14", "Dia de San Valentin"))
cal._append_to_calendar(("2026-02-14", "Cumple de Renata"))
cal._append_to_calendar(("2026-02-15", "Hacer Asado"))
cal._print_calendar()
# print("Start of program")
# parse = Parser ("I public", "I private")
# print("End of program")
# print("extra public: " + parse._public_name)
# print("extra private : " + parse._print_name())

# compilation error; private member cant be accesed!!
# print("extra private : " + parse.__private_name)
