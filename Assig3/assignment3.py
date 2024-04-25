import urllib.request
import base64
import binascii
from pymd5 import md5, padding

from problem1 import ctxts_hex, ctxts_bin
from problem2 import KEY, get_user_url, query_url

################################################################################
# 
# Starter file for UChicago CMSC 23200 Assignment 3, Winter 2024
#
################################################################################

##Crib drag logic
# XOR two cipher texts tg => newciphx2
# XOR newciphx2 with crib of choice (crib = small word/phrase)
# print output of bytes, should be english text
# look for sections that look like words/parts of words, think of words that include those letters
# redo crib drag with new crib word
# xor the discovered english phrase with corresponding bytes in cipher1 to reveal parts of the key
# xor part of key with  cipher2, 3, 4 etc to reveal messages



################################################################################
# PROBLEM 1 SOLUTION
################################################################################

def trial(index):
    return(len(ctxts_bin[index])) #a helper function to ensure recovered plaintexts are the same length as the ciphertext

    
def cribdrag(ciphertext, crib): 
    cribmultiplier = len(ciphertext) // len(crib) + 1 #finds out how many individual crib strings need to be in the paddedcrib
    paddedcrib = (crib * cribmultiplier)[:len(ciphertext)] #makes a bytes object with crib repeated until it is the same length as the ciphertext
                                                           #Slicing and indexing in Python inspiration: https://www.freecodecamp.org/news/slicing-and-indexing-in-python/
    juice = bytes([a ^ b for a, b in zip(ciphertext, paddedcrib)]) #XOR's the provided ciphertext with the paddedcrib and stores in juice 
                                                                #XOR and zip inspiration: https://nitratine.net/blog/post/xor-python-byte-strings/ 
    return juice                                                #returns

def decoder(word):
    crib = bytes(word) #converts entered crib string into bytes 

    m1 = ctxts_bin[3] #extracts one ciphertext out of ctxts_bin
    m2 = ctxts_bin[0] #extracts another ciphertext out of ctxts_bin
 
    max_size = max(len(m1), len(m2)) #compares the two sizes of the ciphertexts and sets the variable as the longer length
    m1 = m1.ljust(max_size, b'A') #pads ciphertext with A's in case it is not equal to max_size 
                                  #ljust idea: https://www.w3schools.com/python/ref_string_ljust.asp
    m2 = m2.ljust(max_size, b'A') #pads ciphertext with A's in case it is not equal to max_size 
                                  #max documentation: https://docs.python.org/3/library/functions.html#max 

    temp = bytearray(m1) #store the newly padded and length-verified ciphertext
    for i, byte in enumerate(m2): # XOR two cipher texts tg => temp
                                  #enumerate for loop inspiration: https://www.geeksforgeeks.org/enumerate-in-python/ 
        temp[i] ^= m2[i]
    
    nicetry = cribdrag(temp, crib) #drag crib through XOR'd ciphertexts with cribdrag helper function

    english = nicetry.decode('ascii', errors='replace') #change into plaintext english for guess/checking using ascii scheme, also ignore any errors that might occur in XOR'ing with 'replace'
    
    return english #returns 

# Submission function for grading
def problem1():
    # Fill in this array with the four decoded plaintexts *in order*
    # no further implementation required in this function
    ptxts = [b'Libraries pulled through, of course, but then the rise of the internet renewed fears of obsolescence. So far, the internet has not killed libraries either. But the percentage of higher-education budgets dedicated to libraries has been dwindling since the 1980s, and at many institutions there\xe2\x80\x99s been a corresponding drop in reported spending on print materials. The game is most gratifying when players devise the canniest, most unexpected, and most unnecessary ways to trick the poor villagers whose unfortunate assignment it is to share a world with this wicked waterfowl. Sneaking and cheating are game-play elements that get rewarded; being a bad goose is what it must feel like to be a card sharp. PhD student Shawn Shan and alumni Emily Wenger and Jenna Cryan were named to the Forbes 30 Under 30 list for 2024. Forbes editors reached out to the team for their work on Glaze, a tool for artists to protect their creative property against AI models. This is the first time the Department of Computer Science has had students make the list. On the surface, his art may appear to be a kind of elaborate prank. He injected a piece of lasagna with heroin for a work titled lasagna on heroin, and he drove his aunts car from her house outside Miami and parked it in front of the Bass Museum of Art for a piece called my aunts car. There is a bit of Well, what happens if to his work.']
    #0 Libraries pulled through, of course, but then the rise of the internet renewed fears of obsolescence. So far, the internet has not killed libraries either. But the percentage of higher-education budgets dedicated to libraries has been dwindling since the 1980s, and at many institutions there\xe2\x80\x99s been a corresponding drop in reported spending on print materials.
    #1 The game is most gratifying when players devise the canniest, most unexpected, and most unnecessary ways to trick the poor villagers whose unfortunate assignment it is to share a world with this wicked waterfowl. Sneaking and cheating are game-play elements that get rewarded; being a bad goose is what it must feel like to be a card sharp.
    #2 PhD student Shawn Shan and alumni Emily Wenger and Jenna Cryan were named to the Forbes 30 Under 30 list for 2024. Forbes editors reached out to the team for their work on Glaze, a tool for artists to protect their creative property against AI models. This is the first time the Department of Computer Science has had students make the list.
    #3 On the surface, his art may appear to be a kind of elaborate prank. He injected a piece of lasagna with heroin for a work titled lasagna on heroin, and he drove his aunts car from her house outside Miami and parked it in front of the Bass Museum of Art for a piece called my aunts car. There is a bit of Well, what happens if to his work.
    return ptxts 

################################################################################
# PROBLEM 2 SOLUTION
################################################################################

def problem2(cnet):
    url = get_user_url(cnet)
    msg1 = url.split(b'api_tag=')[1].split(b'&')[0] 
    h = md5(state=bytes.fromhex(msg1.decode('utf-8')), count=512)
  
    h.update(b'&role=admin')
    newtag = h.hexdigest()
    start_url = "http://www.flickur.com/?api_tag=" + newtag + "&uname=" + cnet.decode('utf-8') + "&role=user"

    #hexkey = '92384792387498279239898792873234098230498a'
    #KEY = binascii.unhexlify(hexkey)
    for keylength in range(128, 264, 8): 
        pad_add = (keylength + ((len('uname=') + len(cnet) + len('&role=user')) * 8))
        padding_padadd = padding(pad_add)
        new_url = bytes(start_url.encode('utf-8')) + padding_padadd + b'&role=admin'
        result = query_url(new_url)
        if result == b"Admin Login Success":
            return new_url

    return new_url



################################################################################

# Code below here will be run if you execute 'python4 assignment3.py'.
# This code here won't be graded, and your code above shouldn't depend on it.
if __name__ == "__main__":

    # optional driver code here, e.g., to help test your solution to Problem 1 ###########################

    #tried = trial(1)
    #print(tried)
    #dec = decoder(b'On the surface, his art may appear to be a kind of elaborate prank. He injected a piece of lasagna with heroin for a work titled lasagna on heroin, and he drove his aunts car from her house outside Miami and parked it in front of the Bass Museum of Art for a piece called my aunts car. There is a bit of Well, what happens if to his work.')
    print(dec)
   
    #sanity check for length 
    #c0 = bytes(b'Libraries pulled through, of course, but then the rise of the internet renewed fears of obsolescence. So far, the internet has not killed libraries either. But the percentage of higher-education budgets dedicated to libraries has been dwindling since the 1980\'s, and at many institutions there\'s been a corresponding drop in reported spending on print materials. ')
    #print(len(c0))
    
    # optional driver code here, e.g., to help test your solution to Problem 2
    cnet_id = b'harshita'
    url = get_user_url(cnet_id)
    print(url)
    msg1 = url.split(b'api_tag=')[1].split(b'&')[0] 
    print(msg1)
    forged_url = problem2(cnet_id)
    result = query_url(forged_url)
    print(result)
    
    exit()
