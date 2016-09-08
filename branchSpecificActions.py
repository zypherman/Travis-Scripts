import sys

# Main method
def main(argv):
    int exitStatus = 0
    if len(argv) == 1:
        print "Not enough arguments"
        exitStatus = 1
    else:
        print("Branch Name: " + argv[1])

    sys.exit(exitStatus)

if __name__ == "__main__":
    main(sys.argv)
