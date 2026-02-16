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

    def _clear_all(self):
        self.__calendar.clear()
        self.__completed.clear()

    def _print_calendar(self):
        for i in self.__calendar:
            print(i)

    def _print_completed(self):
        for i in self.__completed:
            print(i)

    def _get_calendar(self):
        return list(self.__calendar)

    def _get_completed(self):
        return list(self.__completed)
