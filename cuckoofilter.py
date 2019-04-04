
from sklearn.utils import murmurhash3_32 as mmh
import random

import mmh3 

###############
# CuckooFilter
###############

class CuckooFilter:
    def __init__(self, filter_size, fingerprint_size):
        self.filter_size = filter_size
        self.fpsize = fingerprint_size
        self.table = [[],[]]
        self.usage = 0
        self.max_swap = 30
        self.hashseed = 0

    """
    Given a index try to insert a value to hashtable
    """
    # def insert(self,index):

    """
    Add given item to Cuckoo filter
    """
    def add(self,item):
        # TODO : filter computes hash and fingerprint

        hash1 = makehash(item)
        fp = makeFingerprint(item)
        hash2 = makehash2(item)
        
        # Always try to put in the first bucket first
        if self.table[0][hash1] != -1:
            self.table[0][hash1] = fp
            self.usage +=1
            return hash1
        
        # Then try inserting to second index:
        if self.table[1][hash2] != -1:
            self.table[1][hash2] = fp
            self.usage +=1
            return hash2

        # If Both is full swap any of hash1 and hash2 to swap.
        swap_table = 0 if random.random()>=0.5 else 1
        swap_index = hash1 if swap_table==0 else hash2
        
        for i in range(self.max_swap):
            temp_item_fp = self.table[swap_table][swap_index]
            self.table[swap_table][swap_index] = fp
            fp = temp_item_fp
            swap_index = (swap_index ^ self.makehash(fp))%self.filter_size
            swap_table = 0 if swap_table==1 else 1

            if self.table[swap_table][swap_index]==-1:
                self.table[swap_table][swap_index] = fp
                self.usage +=1
                return swap_index
        
        # TODO : need to perform renew hashfunciton.
    
    """
    Remove an item in the Cuckoo filter
    """
    def remove(self,item):
        hash1 = makehash(item)
        fp = makeFingerprint(item)
        hash2 = makehash2(item)
        if self.table[0][hash1] == fp:
            self.table[0][hash1] == -1
            self.usage -= 1
            return True
        if self.table[1][hash2] == fp:
            self.table[1][hash2] == -1
            self.usage -= 1
            return True
        return False        
        

    """
    Get fingerprint of given item
    """
    def makeFingerprint(self,item):
        hash_val = mmh3.hash_bytes(item)
        fp = hash_val[:self.fpsize]
        return fp
    
    """
    Given string item returns hash value
    """
    def makehash(self, item):
        hash_val = mmh(item,self.hashseed)
        hash_val %= self.filter_size
        return hash_val
        
    """
    Get second hash 
    """
    def makehash2(self,hash1,fp):
        # Xor on hash1 and hash of fingerprint
        hash2 = (hash1 ^ makehash(fp))%self.filter_size
        return hash2
