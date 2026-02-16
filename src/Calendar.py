import json
import os


class Calendar:
    __first_inizialization = True
    __singelton = None
    __calendar = [("2026-02-14", "Calendar")]
    __completed = [("2026-02-14", "Completed")]
    __file_name = "calendar_persistency.json"
    __path = ""

    def __new__(cls, filename="calendar_persistency.json", path=""):
        if cls.__singelton is None:
            cls.__singelton = super().__new__(cls)
        if cls.__first_inizialization:
            cls.__first_inizialization = False
            cls.__calendar.clear()
            cls.__completed.clear()

        cls.__file_name = filename
        cls.__path = path
        cls.__load_from_file(cls.__singelton)
        return cls.__singelton

    def _get_full_path_and_file_name(self):
        return self.__path + self.__file_name

    def __save_to_file(self):
        data = {"calendar": self.__calendar, "completed": self.__completed}
        with open(self.__path + self.__file_name, "w") as f:
            json.dump(data, f, indent=4)

    def __load_from_file(self):
        if not os.path.exists(self._get_full_path_and_file_name()):
            return

        with open(self._get_full_path_and_file_name(), "r") as f:
            data = json.load(f)

            self.__calendar = [tuple(x) for x in data.get("calendar", [])]
            self.__completed = [tuple(x) for x in data.get("completed", [])]

    def __clear_file(self):
        data = {"calendar": [], "completed": []}
        with open(self._get_full_path_and_file_name(), "w") as f:
            json.dump(data, f, indent=4)

    def _append_to_calendar(self, tuple):
        self.__calendar.append(tuple)
        self.__save_to_file()

    def _mark_as_completed(self, tuple):
        if self.__calendar.count(tuple):
            self.__calendar.remove(tuple)
            self.__completed.append(tuple)
            self.__save_to_file()
        else:
            print(
                "ERROR - no matching event for [day, event] = ["
                + tuple[0]
                + ","
                + tuple[1]
                + "]"
            )

    def _clear_all(self):
        self.__calendar.clear()
        self.__completed.clear()
        self.__clear_file()

    def _print_calendar(self):
        print("============== CALENDAR =================")
        for i in self.__calendar:
            print(i)

    def _print_completed(self):
        print("============== COMPLETED ================")
        for i in self.__completed:
            print(i)

    def _get_calendar(self):
        return list(self.__calendar)

    def _get_completed(self):
        return list(self.__completed)
