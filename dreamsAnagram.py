#  dreamsAnagram.py
#  
#  Copyright 2017 Francisco Manuel Alexander Bueno
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
# -*- coding: utf-8 -*-
__author__ = 'FranciscoManuelAlexander'
import string
import unicodedata
import numpy as np

def remove_accent(word):
    '''remove accents in the word'''
    good_accents = {'n\u0303'}
    word_output=[]
    for w in word:
        if w !='ñ':
            for c in unicodedata.normalize('NFD', w):
                if unicodedata.category(c) != 'Mn' :
                    word_output.append(c)
        else:
            word_output.append(w)
    return ''.join(word_output)
def position_letters_alphabet(lang):
    '''return dictionary with the position in the alphabet of letters
        lang es,en
        return possition_langs ={'a':1,}
    '''
    possition_langs ={}
    alphabet={'en':list(string.ascii_lowercase),'es':list('abcdefghijklmnñopqrstuvwxyz')}
    for i in range(0,len(alphabet[lang])):
        possition_langs[alphabet[lang][i]]=i+1;
    return possition_langs
def get_coor(word,lang='es'):
    '''return coor of a word on a lang
        lang es,en
        return coor_word={'coor':[position in axis],'r':radius}
    '''
    word=remove_accent(word)
    coor_word={'coor':[]}
    possition_langs=position_letters_alphabet(lang)
    for l in range(0,len(word)):
        letter=word[l]
        coor_word['coor'].append(possition_langs[letter])
    coor_word['r']=np.linalg.norm(np.array(coor_word['coor']))
    return coor_word

#print(get_coor('cigüeña','es') )
