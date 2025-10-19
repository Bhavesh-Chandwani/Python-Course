import argparse
def main():
    parser = argparse.ArgumentParser(description="A simple command line utility")
    parser.add_argument("filename", help="File to Process")
    parser.add_argument("-v", "--verbose", action="store_true", help= "Enable Verbose Output")
    args = parser.parse_args()
    
    if args.verbose:
        print(f"File processing : {args.filename} in verbose mode")
    else:
        print(f"Processing File : {args.filename}")

if __name__ == "__main__":
    main()