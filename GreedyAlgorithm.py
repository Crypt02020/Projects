#!/usr/bin/env python
# coding: utf-8

# In[7]:

import os
print(os.getcwd())
import numpy as np
from PIL import Image

image = 'clinton.tif'
im = Image.open(image)
imarray = np.array(im)
imarray[:5, :5]

# In[8]:


n, m = imarray.shape
n, m


# In[9]:

##
def get_neighbors(i, j):
    neighbors = {}
    if i - 1 >= 0:
        pt = i - 1, j + 1
        val = imarray[i - 1, j + 1]
        neighbors[pt] = val
    if i + 1 < m:
        pt = i + 1, j + 1
        val = imarray[i + 1, j + 1]
        neighbors[pt] = val

    pt = i, j + 1
    val = imarray[i, j + 1]
    neighbors[pt] = val

    return neighbors


# In[10]:


def greedy_move(i, j, path):
    current_val = imarray[i, j]
    neighbors = get_neighbors(i, j)
    neighbors = {pt: abs(val - current_val) for pt, val in neighbors.items()}

    min_val = min(neighbors.values())
    opt_pt = [pt for pt in neighbors.keys() if neighbors[pt] == min_val]

    for k in opt_pt:
        if k not in path:
            result = k
            return result
            break;


# In[11]:

## Starts from point i, j, moves greedy moves to the rightmost point
def get_path(i, j):
    path = [(i, j)]
    while j != (m - 1):
        i, j = greedy_move(i, j, set(path))
        path.append((i, j))
    return path


# In[23]:

## Runs previous function, starting point
path = get_path(1650, 0)

# In[24]:

## Everything in that path is white
for pt in path:
    i, j = pt
    imarray[i, j] = 255

# In[25]:


new_im = Image.fromarray(imarray)
new_im.save("numpy_altered_sample2.png")
