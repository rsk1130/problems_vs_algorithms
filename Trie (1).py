#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[8]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for character in word:
            if character not in current_node.children:
                current_node.insert(character)
            current_node = current_node.children[character]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root
        for letter in prefix:
            current_node = current_node.children[letter]
        
        return current_node


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[91]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
        path_dict = self.children
        
        output_list = []
        
        for key, value in path_dict.items():
            suffix += key
            if value.is_word:
                output_list.append(suffix)
            else:
                output_list += value.suffixes(suffix)
        return output_list

            


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[92]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[93]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        return_list = ['hello', 'goodbye']
    
        current_node = self
        print(current_node)
        print(type(current_node))
        
        for letter in current_node.children:
            
            return_word = letter
            print("return word at 1st iteration is {}".format(return_word))
            
            print(letter)
            print(type(letter))
            
            next_node = current_node.children[letter]
            if next_node.is_word:
                
                print("FOUND A WORD")
                return_list.append(return_word)
            
            print(next_node)
            print(type(next_node))
            
     
            for letter in next_node.children:
                return_word += letter
                print("return word at 2nd iteration is {}".format(return_word))
                next_node = next_node.children[letter]
            return_list.append(return_word)
            
        return return_list
        
       
             
        for letter in self.children:
            print(letter)
            current_node = self.children[letter]
            if current_node.is_word:
                print("FOUND A WORD")
                return_list.append(return_word)
            else:
                print("DIDNT FIND A WORD")
                current_node.suffixes
        
        return return_list      
    
      if current_node.is_word:
            print("Found a word")
            return "HAPPY"
        else:
            print("Keep looking!")
            for letter in current_node.children:
                current_node.suffixes('letter')
 current_node = self
        
        return_list = []
        return_word = ""
        
        for letter in current_node.children:
            return_word += letter
            print("So far, return word is: {}".format(return_word))
            if current_node.children[letter].is_word:
                return_list.append(return_word)
            else:
                current_node = current_node.children[letter]
                current_node.suffixes()
    
        return return_list
      
urrent_node = self
        
        if current_node.is_word:
            return ""
        
        output_list = []
        for key, value in current_node.children.items():
            current_node = value
            smaller_output = current_node.suffixes()
            output_list.append(smaller_output)
        
        
      
    
        return output_list
    
    
        current_node = self
        inner_list = ['this is the list', 'it prints in sequence']
        special_word = "ag"
        for key, value in current_node.children.items():
            print(key)
            special_word += key
            if value.is_word:
                print("FOUND WORD")
                print("Special word is {}".format(special_word))
                inner_list.append(special_word)
                print(inner_list)
            value.suffixes()
        
        return inner_list

