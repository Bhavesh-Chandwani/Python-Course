import argparse
def main():
    parser = argparse.ArgumentParser(description= "Simple Calculator.")
    parser.add_argument("num_1", type=float, help="First Number")
    parser.add_argument("num_2", type=float, help="Second Number")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operations to perform: ")
    args = parser.parse_args()
    print(args)

    if args.operation == "add":
        print(f"The result will be : {args.num_1 + args.num_2}")

    elif args.operation == "sub":
        print(f"The result will be : {args.num_1 - args.num_2}")

    elif args.operation == "mul":
        print(f"The result will be : {args.num_1 * args.num_2}")

    elif args.operation == "div":
        print(f"The result will be : {args.num_1 / args.num_2}")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()