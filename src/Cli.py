import argparse
from src.Calendar import Calendar


def main():
    parser = argparse.ArgumentParser(description="Calendar CLI")

    parser.add_argument(
        "--add",
        nargs="+",
    )
    parser.add_argument(
        "--completed",
        nargs="+",
    )
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--clear", action="store_true")

    args = parser.parse_args()

    cal = Calendar()

    if args.add:
        if len(args.add) < 2:
            print("ERROR: --add requires at least DATE and EVENT")
            return

        date = args.add[0]
        event = args.add[1]
        priority = args.add[2] if len(args.add) > 2 else None
        expiry = args.add[3] if len(args.add) > 3 else None

        cal._append_to_calendar([date, event, priority, expiry])

    if args.completed:
        if len(args.completed) < 2:
            print("ERROR: --completed requires at least DATE and EVENT")
            return

        date = args.completed[0]
        event = args.completed[1]
        priority = args.completed[2] if len(args.completed) > 2 else None
        expiry = args.completed[3] if len(args.completed) > 3 else None

        cal._mark_as_completed([date, event, priority, expiry])

    if args.list:
        cal._print_calendar()
        cal._print_completed()

    if args.clear:
        cal._clear_all()


if __name__ == "__main__":
    main()
