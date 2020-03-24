#dictRandom.py



####week7#########


#loose ends-while
#hw qs
#dict/tuple/set
#hand back midterm

#######dict(ionary)######-----note pay attention to whether method returns or modifies
#sort and sorted are polar opposities
'''
dict
-key


suppose that we want to write a phone book application. Given a name, we want to
retrieve corrsponding phone number.

how do we store the data?

names=['frank', 'sue', 'sally']
numbers=[333,222,666]

or

phonenums = [('frank',333)...]

but there is somthing better!
phonenums={'frank':333, 'sue': 222,...}

#retreive items by key
>>>phonenums['sue']
222

format:
{key: value}
keys must be immutable
-can't change key
values can be any data type
-can change value



use a tuple instead to add more stuff to a dictionary
tuples are like listss ut immutable

phonenums[('Curie', 'Marie')]=888

reasons for speed with dictionaries is because comparing integers is faster
then comparing objects
'''

######hw qs##########3
'''
>>>primeFac(90)
[2,3,3,5]
>>>primeFac(13)
[13]


n=90
accumulate list of factors
facs=[]

potfac=2

observe that 2 divides 90, so perform division
n=45
facs=[2]
potfac=2

observe 2 does not divide 90, so increment
n=45
facs=[2]
potfac=3

3 divides 45, so do it
n=15
facs=[2,3]
potfac=3

3 divides 15, so do it
n=5
facs=[2,3,3]
potfac=3

3 does not divide 5
n=5
facs=[2,3,3]

4 does not divide 5, incrememte potfac
n=5
facs=[2,3,3]
potfac=5

5 does divide so do it
n=1
facs=[2,3,3,5]
potfac=5

STOP BECAUSE n==1
===============


start with n=n, potfac=2,facs=[]
while number not factored
(i...e, while...)
    if potfac is a factor
        perform division
        divide n by potfac
        n changes
        facs change
        add potfac to facs
    otherwise(not factor)
        increment potfac
'''

'''
>>>sublist([1,2,3][5,1,4,2,5,3,9])
True
>>>sublist([1,2,1][5,1,4,2,5,3,9])
False
>>>>>>sublist([1,2,1][5,1,1,2,7]])
False

maintain counters i and j into frst and second list (resp.)
i=0 #counter for first list
j=0 #counter for second list

whilei i and j are still in range:
    if first list at position i matches second at postiiion j
        incrememnbt both counters
    otherwise (not a match)
        increment j
when loop ends,one or both of i and j are out of range

if i is out of range, you found all the matches and return true

otherwise return j is out of range (and i is not) and return false
'''

