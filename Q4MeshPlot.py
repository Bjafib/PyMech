#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:56:36 2019

@author: bjafib
"""

import matplotlib.pyplot as plt
import numpy as np

def PlotElemNumb(CoorX,CoorY,NElem):
    
    fig, ax = plt.subplots(1, 1)
    x, y = np.meshgrid(CoorX, CoorY)
    c = np.ones_like(x)
    ax.pcolor(x, y, c, facecolor='none', edgecolor='k')
    
    for elem in range(NElem):
        coorX = CoorX[0:4,elem:elem+1]
        coorY = CoorY[0:4,elem:elem+1]
        X = np.mean(coorX[0:2])
        Y = np.mean(coorY[1:3])
        ax.text(X, Y, str(elem+1), fontsize=12)
        
def PlotNodeNumb(CoorX,CoorY,Nodes,NNodes,NElem):
    
    NodesCoorX = np.zeros((NNodes,1))
    NodesCoorY = np.zeros((NNodes,1))
    
    for elem in range(NElem):
        elemnodes = Nodes[0:4,elem]-1
        coorX = CoorX[0:4,elem:elem+1]
        coorY = CoorY[0:4,elem:elem+1]
        NodesCoorX[elemnodes.astype(int)] = coorX
        NodesCoorY[elemnodes.astype(int)] = coorY
    
    fig, ax = plt.subplots(1, 1)
    x, y = np.meshgrid(CoorX, CoorY)
    c = np.ones_like(x)
    ax.pcolor(x, y, c, facecolor='none', edgecolor='k')

    for node in range(NNodes):
        ax.text(NodesCoorX[node],NodesCoorY[node], str(node+1), fontsize=12)
        
def PlotDOFNumb(CoorX,CoorY,DOFs,NDOF,NElem):
    
    DOFsCoorX = np.zeros((NDOF,1))
    DOFsCoorY = np.zeros((NDOF,1))
    
    for elem in range(NElem):
        dofs = DOFs[0:8,elem]-1
        coorX = CoorX[0:4,elem:elem+1]
        coorY = CoorY[0:4,elem:elem+1]
        DOFsCoorX[dofs[0:8:2].astype(int)] = coorX
        DOFsCoorX[dofs[1:8:2].astype(int)] = coorX
        DOFsCoorY[dofs[0:8:2].astype(int)] = coorY
        DOFsCoorY[dofs[1:8:2].astype(int)] = coorY

    fig, ax = plt.subplots(1, 1)
    x, y = np.meshgrid(CoorX, CoorY)
    c = np.ones_like(x)
    ax.pcolor(x, y, c, facecolor='none', edgecolor='k')  

    for dof in range(0,NDOF,2):
        ax.text(DOFsCoorX[dof],DOFsCoorY[dof], str(dof+1)+str(',')+str(dof+2), fontsize=12)
        
#    for dof in range(1,NDOF,2):
#        ax.text(DOFsCoorX[dof],DOFsCoorY[dof], str('   ,')+str(dof+1), fontsize=12)
    