#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:55:04 2019

@author: bjafib
"""

import numpy as np
from Q4Mesh import Q4Mesh
from Q4MeshPlot import PlotElemNumb, PlotNodeNumb, PlotDOFNumb

# Order for Gauss quadrature
nGP = 2;

# Dimensions of beam
Length = 10
Height = 4
h = 1

# Number of elements in x and y direction
NElemX = 10
NElemY = 4

# Applied force
P = 1

# Constitutive matrix (for plane stress)
E = 1
nu = 0.3
Em = np.matrix([[1, nu, 0],
                 [nu, 1, 0],
                 [0, 0, (1-nu)/2]]) * E/(1-nu**2)

# Plot mesh
NElem, NNodes, NDOF, CoorX, CoorY, Nodes, DOFs = Q4Mesh(Length,Height,NElemX,NElemY)
PlotElemNumb(CoorX,CoorY,NElem)
PlotNodeNumb(CoorX,CoorY,Nodes,NNodes,NElem)
PlotDOFNumb(CoorX,CoorY,DOFs,NDOF,NElem)