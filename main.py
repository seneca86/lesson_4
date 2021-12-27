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
