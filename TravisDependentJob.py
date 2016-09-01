import requests
import json
import time
import sys

# Define paths for different requests, slugID is obtained through travis API but normally its just the repo name
url = 'https://api.travis-ci.com/repo/{slugID}}/'
# Path to trigger a build
triggerPath = 'requests'
# Path to check a current or past build
statusPath = 'builds'
# To retrieve build info about a different branch then change this branch here
data = '{"request": {"branch":"master"}}'

# Authorization Token could be moved to Travis environemnt variable if wanted
authorization = '{authorizationToken}'
headers = {'Content-Type': 'application/json', 'Travis-API-Version': '3', 'Authorization': authorization }

# Triggers build of the automated testing repo on travis
def triggerBuild():
    # Send request to trigger the build
    response = requests.post(url + triggerPath, data=data, headers=headers)
    if (response.ok):
        print "Build trigger sucessful"
    else:
        print "Build was not triggered please review"
        sys.exit(1) # If we can't build the job then we have encountered an error

# Retrieves the current build status from the travis API
def retrieveBuildStatus():
    status = ""
    response = requests.get(url + statusPath, headers=headers)

    if (response.ok):
        json_data = json.loads(response.text)
        # Grabs the state of the most recent build which would be the one we just kicked off
        status = json_data.get('builds')[0].get('state')
    else:
        print "There was a problem getting the build status of the build"
        sys.exit(1) # Exit there was an error

    return status

def main():
    buildStatus = "started"
    triggerBuild()
    print "Waiting 60 seconds for the build to start"
    time.sleep(60)

    # Loop this every 15 Seconds, stupid infinte loop style syntax because python doesn't like or statments
    while (True):
        buildStatus = retrieveBuildStatus()
        if("passed" in buildStatus):
            print "Build passed!"
            break
        elif ("errored" in buildStatus):
            print "Build has an error please review tests"
            sys.exit(1) # Error out if we get an errored build status
        time.sleep(15) # Poll every 15 seconds to see if the build is complete

    sys.exit(0)

if __name__ == "__main__":
    main()
