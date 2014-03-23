READ ME:

This is a simple JSON parser mostly intended for 4chan analytical data.

Current bugs:
1) If theres more than one quote it doesn't get the reply. 
^ loop through list of </a> values to get all the reply 
2) Doesn't delete tripcodes
3) if you direct to a different thread, it messes up and places that as part of the reply.
4) treat <br> as breaks---Check
5) FORMAT INTO FUNCTIONS