class Calendar:
    __first_inizialization = True
    __singelton = None
    __calendar = [("2026-02-14", "Calendar")]
    __completed = [("2026-02-14", "Completed")]

    def __new__(cls):
        if cls.__singelton is None:
            cls.__singelton = super().__new__(cls)
        if cls.__first_inizialization:
            cls.__first_inizialization = False
            cls.__calendar.clear()
            cls.__completed.clear()
        return cls.__singelton

    def _append_to_calendar(self, tuple):
        self.__calendar.append(tuple)

    def _mark_as_completed(self, tuple):
        if self.__calendar.count(tuple):
            self.__calendar.remove(tuple)
            self.__completed.append(tuple)
        else:
            print("ERROR - no matching event for [day, event] = [" + tuple + "]")

    def _print_calendar(self):
        for i in self.__calendar:
            print(i)

    def _print_completed(self):
        for i in self.__completed:
            print(i)


cal1 = Calendar()
cal2 = Calendar()
print("================================================")
cal1._append_to_calendar(("2026-02-14", "Dia de San Valentin"))
cal1._append_to_calendar(("2026-02-14", "Cumple de Renata"))
cal2._append_to_calendar(("2026-02-15", "Hacer Asado"))
print("=============PRINT CALENDARIO : ================")
cal1._print_calendar()
print("=============PRINT COMPLETED :  ================")
cal1._print_completed()
print("================================================")
cal1._mark_as_completed(("2026-02-15", "Hacer Asado"))
print("=============PRINT CALENDARIO : ================")
cal1._print_calendar()
print("=============PRINT COMPLETED :  ================")
cal1._print_completed()
print("================================================")
# print("Start of program")
# parse = Parser ("I public", "I private")
# print("End of program")
# print("extra public: " + parse._public_name)
# print("extra private : " + parse._print_name())

# compilation error; private member cant be accesed!!
# print("extra private : " + parse.__private_name)
