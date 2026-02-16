from src.Calendar import Calendar
import unittest


class TestCalenda(unittest.TestCase):
    def test_singleton(self):
        cal1 = Calendar()
        cal2 = Calendar()
        self.assertIs(cal1, cal2)

    def test_append_to_calendar(self):
        event = ("2026-02-16", "Terminar la Tarea")
        cal1 = Calendar()
        cal1._append_to_calendar(event)
        cal2 = Calendar()
        self.assertEqual([event], cal1._get_calendar())
        self.assertEqual([event], cal2._get_calendar())
        cal1._clear_all()

    def test_mark_completed(self):
        event = ("2026-02-16", "Hacer Asado")
        cal1 = Calendar()
        cal1._append_to_calendar(event)
        cal2 = Calendar()
        self.assertEqual([event], cal1._get_calendar())
        self.assertEqual([event], cal2._get_calendar())
        cal1._mark_as_completed(event)
        self.assertEqual([], cal1._get_calendar())
        self.assertEqual([], cal2._get_calendar())
        self.assertEqual([event], cal1._get_completed())
        self.assertEqual([event], cal2._get_completed())


if __name__ == "__main__":
    unittest.main()

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
cal1._clear_all()
# print("Start of program")
# parse = Parser ("I public", "I private")
# print("End of program")
# print("extra public: " + parse._public_name)
# print("extra private : " + parse._print_name())

# compilation error; private member cant be accesed!!
# print("extra private : " + parse.__private_name)
