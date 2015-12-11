import sys
import launchpadlib
from launchpadlib.launchpad import Launchpad
def no_credential():
 print("Can't proceed without Launchpad credentials.")
 sys.exit()
lp = Launchpad.login_with('Mass package bug subscription adder', 'production', credential_save_failed=no_credential)
teamtowrite = (raw_input('What person/team would you like to use for this(ID not full name)? '))
filepath = (raw_input('Please specify the path of the input file: '))
with open(filepath, "r") as ins:
 filearray = []
 for line in ins:
  filearray.append(line.strip())
for i in range(len(filearray)):
 print("Assigning:")
 print(filearray[i])
 lp.distributions['ubuntu'].getSourcePackage(name=filearray[i]).addBugSubscription(subscriber=lp.people[teamtowrite])
 print("Complete")
