# Airplane class
# author: Petar Cosic  
# email: cpetar112@gmail.com
# created: 8.2.2022.

class Airplane:
    """A class that defines the basic atributes of an aircraft"""
    def __init__(self,id,name,num_of_pass,length,wing_span,height,M_empty,M_fuel,MTOW,P,Vmax,W,L,H_max):
        self.name = name
        self.id = id
        self.num_of_pass = num_of_pass
        self.length = length
        self.wing_span = wing_span
        self.height = height
        self.M_empty = M_empty
        self.M_fuel = M_fuel
        self.MTOW = MTOW
        self.P = P
        self.Vmax = Vmax
        self.W = W
        self.L = L
        self.H_max = H_max

        


