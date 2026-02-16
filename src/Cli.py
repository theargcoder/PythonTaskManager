import argparse
from src.Calendar import Calendar


def main():
    parser = argparse.ArgumentParser(description="Calendar CLI")

    parser.add_argument("--add", nargs=2, metavar=("DATE", "EVENT"))
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--completed", nargs=2, metavar=("DATE", "EVENT"))

    args = parser.parse_args()

    cal = Calendar()

    if args.add:
        date, event = args.add
        cal._append_to_calendar((date, event))
        print("Event added!")

    if args.completed:
        date, event = args.completed
        cal._mark_as_completed((date, event))
        print("Event competed!")

    if args.list:
        cal._print_calendar()
        cal._print_completed()


if __name__ == "__main__":
    main()
