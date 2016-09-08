import sys

# Main method
def main(argv):
    exitStatus = 0

    if len(argv) == 1:
        print "Not enough arguments"
        exitStatus = 1
    else:
        branchName = argv[1]
        if branchName in "master":
            print("Branch Name: " + branchName)

    sys.exit(exitStatus)

if __name__ == "__main__":
    main(sys.argv)
