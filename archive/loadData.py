"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
LOAD ALL DATA
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# execute the properties file so we have all necessary imports and variables
exec(open("props.py"))

# column names we don't want to keep can be added here
toDrop = ['bikeid']

# column names to rename to so it's easier to deal with the data
# MAKE SURE YOUR DATA ALWAYS COMES IN WITH THESE COLUMNS IN THIS ORDER!
# checked that Jan,Jun,Dec are okay for this ordering
colNames = ['tripduration',
             'starttime',
             'stoptime',
             'startstationid',
             'startstationname',
             'startstationlatitude',
             'startstationlongitude',
             'endstationid',
             'endstationname',
             'endstationlatitude',
             'endstationlongitude',
             'bikeid',
             'usertype',
             'birth year',
             'gender']

# Read in data
Jan17 = pd.read_csv(os.path.join(dataFolder,'201701_tripdata.csv'))
Jan17.columns = colNames
Jan17.drop(toDrop, axis=1, inplace=True)

Jun17 = pd.read_csv(os.path.join(dataFolder,'201706_tripdata.csv'))
Jun17.columns = colNames
Jun17.drop(toDrop, axis=1, inplace=True)

Dec17 = pd.read_csv(os.path.join(dataFolder,'201712_tripdata.csv'))
Dec17.columns = colNames
Dec17.drop(toDrop, axis=1, inplace=True)

months = [Jan17, Jun17, Dec17]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MAKE ANY NECESSARY MODIFICATIONS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
for mIdx,m in enumerate(months):
    """
    User Type is a string - map to numbers
    """
    reassignNans(m,'usertype',0)   
    reassignVals(m,'usertype','Subscriber',1)
    reassignVals(m,'usertype','Customer',2)
    m['usertype'] = m['usertype'].astype('int64') # must cast this data column
                                                  # from obj to int


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
THE FINAL PRODUCT
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Jan17 = months[0]
Jun17 = months[1]
Dec17 = months[2]
# months is already made