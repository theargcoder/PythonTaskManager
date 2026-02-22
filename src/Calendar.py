import json
import os


class Calendar:
    __first_inizialization = True
    __singelton = None
    __calendar = [["DATE", "EVENT", "PRIORITY", "EXPIRY-DATE"]]
    __completed = [["DATE", "EVENT", "PRIORITY", "EXPIRY-DATE"]]
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

            self.__calendar = [list(x) for x in data.get("calendar", [])]
            self.__completed = [list(x) for x in data.get("completed", [])]

    def __clear_file(self):
        data = {"calendar": [], "completed": []}
        with open(self._get_full_path_and_file_name(), "w") as f:
            json.dump(data, f, indent=4)

    def _append_to_calendar(self, list):
        if not self.__calendar.__contains__(list):
            self.__calendar.append(list)
            self.__save_to_file()
            print("Event added!")
        else:
            print("this entry already exist")

    def _mark_as_completed(self, item):
        for entry in self.__calendar:
            if entry[0] == item[0] and entry[1] == item[1]:
                self.__calendar.remove(entry)
                self.__completed.append(entry)
                self.__save_to_file()
                print("Event completed!")
                return

        print("ERROR - no matching event found")

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
