'''
Investigating the behaviour of mutable and immutable sequences and how python
shares the data
'''
mutable = [1, 1, 2, 3, 5, 8]    #can be changed and shared
immutable = (5, 8, 13, 21)      #can be shared but not changed

# 1. Assign above objects to new varaible - this creates 2 references

mutable_ref = mutable
immutable_ref = immutable
print([mutable_ref is mutable, immutable_ref is immutable]) #[true, true]

# 2. Change one of the references

mutable += [mutable[-2] + mutable[-1]]        #extends the list, returns None
immutable += (immutable[-2] + immutable[-1],)  #builds new tuple object

# 3. Po tych zmianach, zobaczmy co wypisza poszczegolne 'zmienne'

print([mutable])        # [1 1 2 3 5 8 13]
print([mutable_ref])    # same as above
print([immutable])      # [5 8 13 21 34] - new tuple
print([immutable_ref])  # [5 8 13 21] - Nothing changed, points to old tuple

'''
When the number of references to an object reaches 0, that means that this
object is no longer needed and it can be removed from the memory'''
