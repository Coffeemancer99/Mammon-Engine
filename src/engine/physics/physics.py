"""
    About this file:
    this is a scratch file that WILL BE REFACTORED LATER into multiple files for physics
"""
# The box needs a Vector of doubles x and y and another class that implements Vector and has a mass and friction
# Treat force and acceleration as a 2d vector and treat them as x and y. Gravity = y vector direction = x vector

import pygame
import math
import sympy


""" (Force formula)
    
    Uses mass and multiplies it by acceleration
    This function needs to be looped so it can be updated
    
    :param mass: - the mass that needs to be computed
    :param acceleration: - that acceleration that needs to be computed
    
    :return: - float type: the force 

"""


def force(mass, acceleration):
    return float(mass * acceleration)


""" (Normal Force formula)

    Uses the earth's gravity and multiples it by the mass provided 
    This function needs to be looped so it can update 
    
    :param mass: - the mass that needs to be computed for force
    
    :return: - float type: normal force with mass 
    
"""


def computeMovementForce(mass):
    return float(mass * -9.81)


""" (Friction formula)

    f = mu*N
    mu = coefficient of friction
    N = Normal force
    
    Note: Must call the force function before you can use friction, and must pass in a known friction coefficient
    
    Uses the mass provided to calculate normal force then multiples it by the coefficientOfFriction provided
    
    :param mass: - the mass that needs to be provided :param coefficientOfFriction: - coefficientOfFriction that can 
    be calculated or remained as a constant that will determined later 

    :return: - float type: friction
    
"""


def friction(mass, coefficientOfFriction):
    return float(coefficientOfFriction * computeMovementForce(mass))
