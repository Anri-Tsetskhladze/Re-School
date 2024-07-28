#https://www.codewars.com/kata/5b707fbc8adeaee7ac00000c/train/python
import math

def solution(force1, force2, theta):
    theta_rad = math.radians(theta)
    
    R = math.sqrt(force1**2 + force2**2 + 2 * force1 * force2 * math.cos(theta_rad))
    
    phi_rad = math.atan2(force2 * math.sin(theta_rad), force1 + force2 * math.cos(theta_rad))
    phi = math.degrees(phi_rad)
    
    return [R, phi]

force1 = 10
force2 = 20 
theta = 30 

solution(force1, force2, theta)
