4chanalytics 
==========
##Background 
www.4chan.org provides an incredible wealth of information on internet culture and the increasing difficulties NLP faces with contextual communication. This script can be used to provide statistcal information on many trending topics across the various boards.
This is a simple JSON parser mostly intended for 4chan analytical data.
Currently limited in its usage.

##Usage 
to run:
```python chancrawl.py (board)```

example:
```python chancrawl.py biz```

##Current issues
1. If theres more than one quote it doesn't get the reply. 
Solution: loop through list of </a> values to get all the replies
2. Doesn't delete tripcodes (results in encryption string)
3. Cannot handle if you redirect to a different thread.
4. Reformat into objects

##Future Updates
Updates will be provided to include chart.js classes for data collection. All extensive data will be hosted publically at 4chanalytics.org
