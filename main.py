# %%
# This is how you transform from feet to meters:
feet = 6
inches = 2.8
meters = 0.3048 * feet
meters += 0.0254 * inches  # convert from inches to meters
#%%
'''
This is a multi-line comment
surrounded by single or
double quotes 
'''
a = 4

# %%
# Line continuations
sum = 1 + \
      2 + \
      3 + \
      4 + \
      5
# %%
long_poem = 'Animula, vagula, blandula \
    Hospes comesque corporis \
    Quae nunc abibis in loca \
    Pallidula, rigida, nudula, \
    Nec, ut soles, dabis iocos'
# %%
sum = (1 +
       2 +
       3 +
       4 +
       5)
# %%
bull_market = True
if bull_market:
    print('hold')
else:
    print('sell')
# %%
clouds = False
cold = False

if clouds:
    if cold:
        print('winter')
    else:
        print('summer')
else:
    if cold:
        print('spring')
    else:
        print('summer')
# %%
day = 'Monday'
if day == 'Monday':
    print('first')
elif day == 'Tuesday':
    print('second')
elif day == 'Wednesday':
    print('third')
elif day == 'Thursday':
    print('fourth')
elif day == 'Friday':
    print('fifth')
elif day == 'Saturday':
    print('sixth')
elif day == 'Sunday':
    print('seventh')
   
# %%
x = 3
5 > x
x == 4
x < 10
(x < 10) and (x <  20)
(x < 10) and not (x == 4)
(x < 10) or (x > 10)
1 < x < 10
1 < x < 10 < 20
# %%
