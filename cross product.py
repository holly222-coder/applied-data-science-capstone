# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:22:56 2020

@author: 26902
"""

import numpy as np

a = np.array([1,2,3])

b = np.array([4,5,6])

c = np.cross(a,b)

d = np.array([[1,2,3],
      [3,4,5]])
e = d.T

import numpy as np
a = np.eye(2)
b = 5
c = np.outer(b,a)

e = c[:,:,np.newaxis,np.newaxis]
d = np.kron(e,a)

yI = np.arange(-1.0,1.0,0.002)