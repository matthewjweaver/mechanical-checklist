- uses
  - homebrew et al
  - cryptography.io
  - work servers 
  - notification followup (dear X, did you sweep up yet)


User Story:

  - openssl released, notification happens[1]
  - tool finds out[2]
  - tool sends notifications
  - tool creates new copy of checklist
    - i.e. "this is the heartbleed copy of your openssl checklist"
  - user checks stuff off!

events:
  types: 
    * openssl
    * semi-arbitrary package: django, apache
  sources:
    * https://nvd.nist.gov/download/nvd-rss.xml
    * buttons

checklists:
PLAIN TEXT OR GTFO

outputs (notifications):
https://github.com/WhisperSystems/TextSecure-Server/wiki/API-Protocol
pagerduty event
email

config inputs:
a. package list? (event list)
b. checklists
c. outputs (notifications)
tuples of a-c
