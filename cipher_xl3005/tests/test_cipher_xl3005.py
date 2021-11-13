#!/usr/bin/env python
# coding: utf-8

# In[2]:


from cipher_xl3005 import cipher_xl3005 as cp
import pytest


# In[ ]:


def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text


# In[ ]:


def test_cipher_with_word():
    example = 'ABCDEFG'
    expected = 'BCDEFGH'
    actual = cipher(example, 1)
    assert expected == actual, 'Should be True'


# In[ ]:


def test_cipher_negative_shift():
    example = 'BCDEFGH'
    expected = 'ABCDEFG'
    actual = cipher(example, -1)
    assert expected == actual, 'Should be True'


# In[ ]:


def test_cipher_non_alpha():
    example = 'QMSS GR5072'
    expected = 'RNTT HS5072'
    actual = cipher(example, 1)
    assert expected == actual, 'Should be True'


# In[ ]:


def test_cipher_assertion():
    with pytest.raises(AssertionError):
        cipher('Columbia', 'two')

