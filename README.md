4chanalytics 
==========
This is a simple JSON parser mostly intended for 4chan analytical data.

Current issues
==========
1) If theres more than one quote it doesn't get the reply. 
Solution: loop through list of </a> values to get all the replies
2) Doesn't delete tripcodes (results in encryption string)
3) Cannot handle if you redirect to a different thread.
4) Reformat into objects