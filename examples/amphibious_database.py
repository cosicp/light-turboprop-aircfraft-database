# Amphibious aircraft database example
# author: Petar Cosic 
# github: https://github.com/cosicp
# email: cpetar112@gmail.com
# created: 8.2.2022.


import matplotlib.pyplot as plt
import numpy as np
import airplane_class as apc

# --------------------------------------------------------------------
#                           OPTIONS

# Save figures YES/NO
SAVE_FIG = 1  #  1 - YES , 0 - NO

# Chose image type
IMG_FORMAT = 1  #  1 - jpg  2 - eps  3 - svg 4 - custom
CUSTOM_FORMAT = 'pdf'  # define other custom format

# Show popup image 
IMG_SHOW = 1  #  1 - YES  0 - NO

# Trendline ON/OFF 
TREND_LINE = 1 # 1 - YES  0 - NO

# Show grid on plots
PLT_GRID = 0 # 1 - YES  0 - NO

# Calculate optimal values for the initial maximal takeoff weight 
CALCULATE_OPTIMAL_VALUES = 1  # 1 - YES , 0 - NO
INITIAL_MAX_TAKEOFF_MASS  = 2545 # [kg] turboprop


#    initializing
a = {}
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                                   DATABASE 2 - Amphibious aircraft
a[1] = apc.Airplane(id = 1,name = 'Grumman G-73 Mallard' ,num_of_pass = 17, length = 14.7,wing_span = 20.3, height = 5.72,M_empty = 3969 ,M_fuel = 'NaN', MTOW = 6350, P = 450 ,Vmax = 346, W =6.9 ,L = 2074, H_max = 7500)
a[2] = apc.Airplane(id = 2,name = 'Short Sealand I' ,num_of_pass = 7, length = 12.86,wing_span = 17.99, height = 4.57,M_empty = 3190 ,M_fuel = 330, MTOW = 4130, P = 254 ,Vmax = 300, W =4.5 ,L = 1063, H_max = 6280)
a[3] = apc.Airplane(id = 3,name = 'Noorduyn Norseman' ,num_of_pass = 10, length = 9.86,wing_span = 15.7, height = 3.07,M_empty = 1923 ,M_fuel = 278, MTOW = 3357, P = 450 ,Vmax = 275, W =3 ,L = 1500, H_max = 5200)
a[4] = apc.Airplane(id = 4,name = 'de Havilland Canada DHC-2 Beaver' ,num_of_pass = 6, length = 9.22,wing_span = 14.63, height = 2.74,M_empty = 1361 ,M_fuel = 190, MTOW = 2313, P = 336 ,Vmax = 255, W =5.2 ,L = 732, H_max = 5486)
a[5] = apc.Airplane(id = 5,name = 'de Havilland Canada DHC-3 Otter' ,num_of_pass = 10, length = 12.8,wing_span = 17.69, height = 3.83,M_empty = 2010 ,M_fuel = 290, MTOW = 3629, P = 448 ,Vmax = 257, W =4.3 ,L = 1520, H_max = 5730)
a[6] = apc.Airplane(id = 6,name = 'de Havilland Canada DHC-6 Twin Otter' ,num_of_pass = 19, length = 15.77,wing_span = 19.8, height = 4.9,M_empty = 2653 ,M_fuel = 472, MTOW = 5246, P = 410 ,Vmax = 297, W =8.1 ,L = 1427, H_max = 7620)
a[7] = apc.Airplane(id = 7,name = 'Fairchild 82' ,num_of_pass = 9, length = 11.25,wing_span = 15.54, height = 2.86,M_empty = 1388 ,M_fuel = 'NaN', MTOW = 2869, P = 391 ,Vmax = 249, W =4.6 ,L = 1054, H_max = 4770)
a[8] = apc.Airplane(id = 8,name = 'Fairchild F-11 Husky ',num_of_pass = 10, length = 11.58,wing_span = 16.69, height = 4.97,M_empty = 2061 ,M_fuel = 'NaN', MTOW = 3314, P = 410 ,Vmax = 205.9, W ='NaN' ,L = 'NaN', H_max = 4724)
a[9] = apc.Airplane(id = 9,name = 'Fairchild 45-80' ,num_of_pass = 12, length = 11.94,wing_span = 17.27, height = 3.63,M_empty = 3223 ,M_fuel = 371, MTOW = 4313, P = 300 ,Vmax = 308.9, W =6 ,L = 'NaN', H_max = 4572)
a[10] = apc.Airplane(id = 10,name =' Fairchild Super 71' ,num_of_pass = 8, length = 10.82,wing_span = 17.67, height = 3.2,M_empty = 1733 ,M_fuel = 254, MTOW = 3178, P = 388 ,Vmax = 223.6, W =4.08 ,L = 1314, H_max = 'NaN')
a[11] = apc.Airplane(id = 11,name =' Found FBA-2' ,num_of_pass = 5, length = 8.05,wing_span = 10.97, height = 2.54,M_empty = 703 ,M_fuel = 'NaN', MTOW = 1338, P = 187 ,Vmax = 237, W =5.6 ,L = 980, H_max = 4875)
a[12] = apc.Airplane(id = 12,name = 'GAF Nomad' ,num_of_pass = 12, length = 12.56,wing_span = 16.52, height = 4.52,M_empty = 2150 ,M_fuel = 'NaN', MTOW = 3855, P = 313 ,Vmax = 350, W =7.4 ,L = 1074, H_max = 6400)
a[13] = apc.Airplane(id = 13,name = 'Dornier Seastar' ,num_of_pass = 12, length = 12.7,wing_span = 17.74, height = 4.83,M_empty = 2900 ,M_fuel = 428, MTOW = 4600, P = 478 ,Vmax = 365, W =6.6 ,L = 1385, H_max = 4500)
a[14] = apc.Airplane(id = 14,name = 'Beriev Be-103' ,num_of_pass = 5, length = 10.7,wing_span = 12.5, height = 3.7,M_empty = 1730 ,M_fuel = 186, MTOW = 2270, P = 157 ,Vmax = 240, W =6.1 ,L = 845, H_max = 5000)
a[15] = apc.Airplane(id = 15,name = 'Beechcraft Model 18' ,num_of_pass = 6, length = 10.41,wing_span = 14.53, height = 2.95,M_empty = 2800 ,M_fuel = 325, MTOW = 3959, P = 336 ,Vmax = 360, W =5.4 ,L = 1800, H_max = 7930)
a[16] = apc.Airplane(id = 16,name = 'Bellanca CH-300 Pacemaker' ,num_of_pass = 5, length = 8.5,wing_span = 14.1, height = 2.5,M_empty = 1032 ,M_fuel = 'NaN', MTOW = 1847, P = 246 ,Vmax = 266, W ='NaN' ,L = 1086, H_max = 'NaN')
a[17] = apc.Airplane(id = 17,name = 'Cessna 180' ,num_of_pass = 5, length = 7.85,wing_span = 10.92, height = 2.36,M_empty = 771 ,M_fuel = 114, MTOW = 1270, P = 170 ,Vmax = 274, W =5.6 ,L = 1648, H_max = 5400)
a[18] = apc.Airplane(id = 18,name = 'Cessna 206' ,num_of_pass = 5, length = 8.61,wing_span = 10.97, height = 2.83,M_empty = 987 ,M_fuel = 148, MTOW = 1632, P = 224 ,Vmax = 280, W =5 ,L = 1352, H_max = 4785)
a[19] = apc.Airplane(id = 19,name = 'Cessna 185 Skywagon',num_of_pass = 5, length = 7.85,wing_span = 10.92, height = 2.36,M_empty = 793 ,M_fuel = 137, MTOW = 1520, P = 220 ,Vmax = 287, W =5.1 ,L = 1333, H_max = 5230)
a[20] = apc.Airplane(id = 20,name = 'Cessna 208 Caravan' ,num_of_pass = 9, length = 11.46,wing_span = 15.88, height = 4.55,M_empty = 2145 ,M_fuel = 326, MTOW = 3629, P = 503 ,Vmax = 344, W =6.27 ,L = 1982, H_max = 7600)
a[21] = apc.Airplane(id = 21,name = 'Grumman G-44 Widgeon ',num_of_pass = 5, length = 9.47,wing_span = 12.19, height = 3.48,M_empty = 1470 ,M_fuel = 'NaN', MTOW = 2053, P = 150 ,Vmax = 246, W =3.6 ,L = 1481, H_max = 4500)
a[22] = apc.Airplane(id = 22,name = 'Piper PA-23' ,num_of_pass = 5, length = 9.52,wing_span = 11.34, height = 3.15,M_empty = 1442 ,M_fuel = 210, MTOW = 2360, P = 187 ,Vmax = 346, W =7.1 ,L = 1445, H_max = 5775)
a[23] = apc.Airplane(id = 23,name = 'Quest Kodiak' ,num_of_pass = 9, length = 10.42,wing_span = 13.7, height = 4.65,M_empty = 1710 ,M_fuel = 293, MTOW = 3290, P = 559 ,Vmax = 339, W =4.1 ,L = 1096, H_max = 7620)
a[24] = apc.Airplane(id = 24,name = 'Wilson Global Explorer ',num_of_pass = 6, length = 12.14,wing_span = 20.42, height = 4.71,M_empty = 2266 ,M_fuel = 'NaN', MTOW = 3629, P = 220 ,Vmax = 193, W ='NaN' ,L = 'NaN', H_max = 'NaN')
a[25] = apc.Airplane(id = 25,name =' An - 2 ',num_of_pass = 12, length = 12.4,wing_span = 14.2, height = 4.1,M_empty = 3300 ,M_fuel = 511, MTOW = 5500, P = 550 ,Vmax = 258, W =3.5 ,L = 845, H_max = 4500)
a[26] = apc.Airplane(id = 26,name = 'Vultee V-1A ',num_of_pass = 8, length = 11.28,wing_span = 15.24, height = 3.1,M_empty = 2424 ,M_fuel = 'NaN', MTOW = 4200, P = 458 ,Vmax = 378, W =5.1 ,L = 1210, H_max = 6100)
a[27] = apc.Airplane(id = 27,name = 'Fleet 50' ,num_of_pass = 10, length = 10.97,wing_span = 13.72, height = 3.99,M_empty = 2087 ,M_fuel = 'NaN', MTOW = 3777, P = 246 ,Vmax = 241, W =5.1 ,L = 1046, H_max = 4570)
a[28] = apc.Airplane(id = 28,name = 'Murphy Moose' ,num_of_pass = 5, length = 7.01,wing_span = 10.97, height = 2,M_empty = 1800 ,M_fuel = 308, MTOW = 3500, P = 265 ,Vmax = 282, W =7.1 ,L = 969, H_max = 4575)
a[29] = apc.Airplane(id = 29,name = 'Besson H-5' ,num_of_pass = 5, length = 14.7,wing_span = 19, height = 4,M_empty = 2050 ,M_fuel = 'NaN', MTOW = 3475, P = 220 ,Vmax = 170, W =6.2 ,L = 1000, H_max = 5400)
a[30] = apc.Airplane(id = 30,name = 'CAMS 55' ,num_of_pass = 5, length = 15.03,wing_span = 20.4, height = 5.01,M_empty = 2590 ,M_fuel = 598, MTOW = 6500, P = 373 ,Vmax = 195, W =4.2 ,L = 1875, H_max = 3400)
a[31] = apc.Airplane(id = 31,name = 'CANT Z.501' ,num_of_pass = 5, length = 14.3,wing_span = 20, height = 'NaN',M_empty = 1850 ,M_fuel = 'NaN', MTOW = 7050, P = 456 ,Vmax = 275, W ='NaN' ,L = 1400, H_max = 7000)
a[32] = apc.Airplane(id = 32,name =' Fokker F.11' ,num_of_pass = 6, length = 13.72,wing_span = 17.98, height = 3.96,M_empty = 2041 ,M_fuel = 'NaN', MTOW = 6577, P = 392 ,Vmax = 180, W =6.2 ,L = 640, H_max = 3200)
a[33] = apc.Airplane(id = 33,name = 'de Havilland Dragon Rapide' ,num_of_pass = 8, length = 10.5,wing_span = 14.6, height = 3.1,M_empty = 3470 ,M_fuel = 519, MTOW = 5833, P = 150 ,Vmax = 253, W =4.3 ,L = 920, H_max = 5090)
a[34] = apc.Airplane(id = 34,name = 'Kingston I' ,num_of_pass = 6, length = 15,wing_span = 20.07, height = 4.1,M_empty = 4150 ,M_fuel = 'NaN', MTOW = 5595, P = 336 ,Vmax = 169, W =5.3 ,L = 'NaN', H_max = 5000)
a[35] = apc.Airplane(id = 35,name = 'Supermarine Swan ',num_of_pass = 10, length = 14.7,wing_span = 20.09, height = 5.5,M_empty = 4588 ,M_fuel = 523, MTOW = 5819, P = 336 ,Vmax = 175, W =2.6 ,L = 583, H_max = 3110)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#  Displaying the database in the terminal
print('')
names = []
for i in range(1,len(a)+1):
    names.append(a[i].name)
spaces = len(max(names, key=len))+3
print((int(spaces/2)-4)*' ','Name',(int(spaces/2)-4)*' ',f'Passengers    Length [m]     Wing span [m]     Height [m]     M(empty) [kg]     M_fuel [kg]     MTOW [kg]     P [kW]       Vmax [km/h]      W [m/s]        L [km]        H_max [m]')
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
for i in range(1,len(a)+1):
    print(a[i].name,(spaces-len(a[i].name))*' ',a[i].num_of_pass,(10-len(str(a[i].num_of_pass)))*' ',a[i].length,(14-len(str(a[i].length)))*' ',a[i].wing_span \
        ,' '*(15-len(str(a[i].wing_span))),a[i].height,' '*(15-len(str(a[i].height))),a[i].M_empty,' '*(15-len(str(a[i].M_empty))),a[i].M_fuel,\
            ' '*(12-len(str(a[i].M_fuel))),a[i].MTOW,' '*(12-len(str(a[i].MTOW))),a[i].P,' '*(13-len(str(a[i].P))),a[i].Vmax,' '*(13-len(str(a[i].Vmax))),a[i].W\
                ,' '*(13-len(str(a[i].W))),a[i].L ,' '*(13-len(str(a[i].L))),a[i].H_max)
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

# sorting out image formats
if IMG_FORMAT == 1:
    IMG_FORMAT = 'jpg'
elif IMG_FORMAT == 2:
    IMG_FORMAT = 'eps'
elif IMG_FORMAT == 3:
    IMG_FORMAT = 'svg'
elif IMG_FORMAT == 4:
    IMG_FORMAT = CUSTOM_FORMAT
else:
    raise ValueError("non valid image format")

k = 1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_len = np.array([])
length = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].length =='NaN':
        continue
    MTOW_len = np.append(MTOW_len,a[j].MTOW)
    length = np.append(length,a[j].length)
polynomial = np.polyfit(MTOW_len,length,1) 
plt.plot(MTOW_len,length,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('length of the airplane [m]')
plt.title('length of the airplane = f(MTOW)')
print(f'approximated length is for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[m]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_len),max(MTOW_len),3),np.polyval(polynomial,np.linspace(min(MTOW_len),max(MTOW_len),3)),color = 'red')
    plt.legend(["data", f"trendline: length of the airplane = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES ==1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(length),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(length)\
        ,head_width=(1.015*np.average(MTOW_len)-np.average(MTOW_len)),head_length=(1.015*np.average(length)-np.average(length)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_len)\
        ,0,head_width=(1.015*np.average(length)-np.average(length)),head_length=(1.015*np.average(MTOW_len)-np.average(MTOW_len)),fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_len.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()


k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_num_of_pass = np.array([])
num_of_pass = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].num_of_pass =='NaN':
        continue
    MTOW_num_of_pass = np.append(MTOW_num_of_pass,a[j].MTOW)
    num_of_pass = np.append(num_of_pass,a[j].num_of_pass)
polynomial = np.polyfit(MTOW_num_of_pass,num_of_pass,1)
plt.plot(MTOW_num_of_pass,num_of_pass,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('number of passengers')
plt.title('number of passengers = f(MTOW)')
print(f'approximated number of passangers for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_num_of_pass),max(MTOW_num_of_pass),3),np.polyval(polynomial,np.linspace(min(MTOW_num_of_pass),max(MTOW_num_of_pass),3)),color = 'red')
    plt.legend(["data", f"trendline: number of passengers = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES ==1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(num_of_pass),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(num_of_pass),head_width=(1.015*\
        np.average(MTOW_num_of_pass)-np.average(MTOW_num_of_pass)),head_length=(1.015*np.average(num_of_pass)-np.average(num_of_pass)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_num_of_pass),0,head_width=(1.015*np.average\
        (num_of_pass)-np.average(num_of_pass)),head_length=(1.015*np.average(MTOW_num_of_pass)-np.average(MTOW_num_of_pass)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_num_of_pass.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()

k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_wing_span = np.array([])
wing_span = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].wing_span =='NaN':
        continue
    MTOW_wing_span = np.append(MTOW_wing_span,a[j].MTOW)
    wing_span = np.append(wing_span,a[j].wing_span)
polynomial = np.polyfit(MTOW_wing_span,wing_span,1)
plt.plot(MTOW_wing_span,wing_span,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('Wing span [m]')
plt.title('Wing span = f(MTOW)')
print(f'approximated wing span for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[m]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_wing_span),max(MTOW_wing_span),3),np.polyval(polynomial,np.linspace(min(MTOW_wing_span),max(MTOW_wing_span),3)),color = 'red')
    plt.legend(["data", f"trendline: Wing span = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES ==1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(wing_span),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(wing_span)\
        ,head_width=(1.015*np.average(MTOW_wing_span)-np.average(MTOW_wing_span)),head_length=(1.015*np.average(wing_span)-np.average(wing_span)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_wing_span)\
        ,0,head_width=(1.015*np.average(wing_span)-np.average(wing_span)),head_length=(1.015*np.average(MTOW_wing_span)-np.average(MTOW_wing_span)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_wing_span.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()

k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_height = np.array([])
height = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].height =='NaN':
        continue
    MTOW_height = np.append(MTOW_height,a[j].MTOW)
    height = np.append(height,a[j].height) 
polynomial = np.polyfit(MTOW_height,height,1)
plt.plot(MTOW_height,height,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('height [m]')
plt.title('height of the airplane = f(MTOW)')
print(f'approximated height for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[m]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_height),max(MTOW_height),3),np.polyval(polynomial,np.linspace(min(MTOW_height),max(MTOW_height),3)),color = 'red')
    plt.legend(["data", f"trendline: height = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES == 1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(height),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(height),head_width=\
        (1.015*np.average(MTOW_height)-np.average(MTOW_height)),head_length=(1.015*np.average(height)-np.average(height)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_height),0,head_width=\
        (1.015*np.average(height)-np.average(height)),head_length=(1.015*np.average(MTOW_height)-np.average(MTOW_height)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_height.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()

k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_M_empty = np.array([])
M_empty = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].M_empty =='NaN':
        continue
    MTOW_M_empty = np.append(MTOW_M_empty,a[j].MTOW)
    M_empty = np.append(M_empty,a[j].M_empty)
polynomial = np.polyfit(MTOW_M_empty,M_empty,1)
plt.plot(MTOW_M_empty,M_empty,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('Empty weight [kg]')
plt.title('Empty weight = f(MTOW)')
print(f'approximated empty weight for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[kg]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_M_empty),max(MTOW_M_empty),3),np.polyval(polynomial,np.linspace(min(MTOW_M_empty),max(MTOW_M_empty),3)),color = 'red')
    plt.legend(["data", f"trendline: Empty weight = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES == 1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(M_empty),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(M_empty),head_width=\
        (1.015*np.average(MTOW_M_empty)-np.average(MTOW_M_empty)),head_length=(1.015*np.average(M_empty)-np.average(M_empty)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_M_empty),0,head_width=\
        (1.015*np.average(M_empty)-np.average(M_empty)),head_length=(1.015*np.average(MTOW_M_empty)-np.average(MTOW_M_empty)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_M_empty.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()

k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_P = np.array([])
P = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].P =='NaN':
        continue
    MTOW_P = np.append(MTOW_P,a[j].MTOW)
    P = np.append(P,a[j].P)
polynomial = np.polyfit(MTOW_P,P,1)
plt.plot(MTOW_P,P,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('P [kW]')
plt.title('P = f(MTOW)')
print(f'approximated P for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[kW]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_P),max(MTOW_P),3),np.polyval(polynomial,np.linspace(min(MTOW_P),max(MTOW_P),3)),color = 'red')
    plt.legend(["data", f"trendline: P = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES == 1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(P),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(P),head_width=\
        (1.015*np.average(MTOW_P)-np.average(MTOW_P)),head_length=(1.015*np.average(P)-np.average(P)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_P),0,head_width=\
        (1.015*np.average(P)-np.average(P)),head_length=(1.015*np.average(MTOW_P)-np.average(MTOW_P)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_P.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()

k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_Vmax = np.array([])
Vmax = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].Vmax =='NaN':
        continue
    MTOW_Vmax = np.append(MTOW_Vmax,a[j].MTOW)
    Vmax = np.append(Vmax,a[j].Vmax)
polynomial = np.polyfit(MTOW_Vmax,Vmax,1)
plt.plot(MTOW_Vmax,Vmax,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('Vmax [km/h]')
plt.title('Vmax = f(MTOW)')
print(f'approximated maximum Velocity for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[km/h]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_Vmax),max(MTOW_Vmax),3),np.polyval(polynomial,np.linspace(min(MTOW_Vmax),max(MTOW_Vmax),3)),color = 'red')
    plt.legend(["data", f"trendline: Vmax = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES == 1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(Vmax),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(Vmax),head_width=\
        (1.015*np.average(MTOW_Vmax)-np.average(MTOW_Vmax)),head_length=(1.015*np.average(Vmax)-np.average(Vmax)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_Vmax),0,head_width=\
        (1.015*np.average(Vmax)-np.average(Vmax)),head_length=(1.015*np.average(MTOW_Vmax)-np.average(MTOW_Vmax)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_Vmax.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()


k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_W = np.array([])
W = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].W =='NaN':
        continue
    MTOW_W = np.append(MTOW_W,a[j].MTOW)
    W = np.append(W,a[j].W)
polynomial = np.polyfit(MTOW_W,W,1)
plt.plot(MTOW_W,W,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('W [m/s]')
plt.title('W = f(MTOW)')
print(f'approximated climb speed for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[m/s]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_W),max(MTOW_W),3),np.polyval(polynomial,np.linspace(min(MTOW_W),max(MTOW_W),3)),color = 'red')
    plt.legend(["data", f"trendline: W = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES == 1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(W),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(W),head_width=\
        (1.015*np.average(MTOW_W)-np.average(MTOW_W)),head_length=(1.015*np.average(W)-np.average(W)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_W),0,head_width=\
        (1.015*np.average(W)-np.average(W)),head_length=(1.015*np.average(MTOW_W)-np.average(MTOW_W)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_W.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()

k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_L = np.array([])
L = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].L =='NaN':
        continue
    MTOW_L = np.append(MTOW_L,a[j].MTOW)
    L = np.append(L,a[j].L)
polynomial = np.polyfit(MTOW_L,L,1)
plt.plot(MTOW_L,L,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('L [km]')
plt.title('L = f(MTOW)')
print(f'approximated range for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[km]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_L),max(MTOW_L),3),np.polyval(polynomial,np.linspace(min(MTOW_L),max(MTOW_L),3)),color = 'red')
    plt.legend(["data", f"trendline: L = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES == 1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(L),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(L),head_width=\
        (1.015*np.average(MTOW_L)-np.average(MTOW_L)),head_length=(1.015*np.average(L)-np.average(L)),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_L),0,head_width=\
        (1.015*np.average(L)-np.average(L)),head_length=(1.015*np.average(MTOW_L)-np.average(MTOW_L)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_L.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()

k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_H_max = np.array([])
H_max = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].H_max =='NaN':
        continue
    MTOW_H_max = np.append(MTOW_H_max,a[j].MTOW)
    H_max = np.append(H_max,a[j].H_max)
polynomial = np.polyfit(MTOW_H_max,H_max,1)
plt.plot(MTOW_H_max,H_max,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('Hmax [m]')
plt.title('Hmax = f(MTOW)')
print(f'approximated celing for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[m]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_H_max),max(MTOW_H_max),3),np.polyval(polynomial,np.linspace(min(MTOW_H_max),max(MTOW_H_max),3)),color = 'red')
    plt.legend(["data", f"trendline: Hmax = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES == 1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(H_max),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(H_max),head_width=\
        (1.015*np.average(MTOW_H_max)-np.average(MTOW_H_max)),head_length=1.015*np.average(H_max)-np.average(H_max),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_H_max),0,head_width=\
        (1.015*np.average(H_max)-np.average(H_max)),head_length=(1.015*np.average(MTOW_H_max)-np.average(MTOW_H_max)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_H_max.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()

k +=1
plt.figure(k,figsize = [8,6.5],dpi = 100)
MTOW_M_fuel = np.array([])
M_fuel = np.array([])
for j in range(1,len(a)+1):
    if a[j].MTOW == 'NaN' or a[j].M_fuel =='NaN':
        continue
    MTOW_M_fuel = np.append(MTOW_M_fuel,a[j].MTOW)
    M_fuel = np.append(M_fuel,a[j].M_fuel)
polynomial = np.polyfit(MTOW_M_fuel,M_fuel,1)
plt.plot(MTOW_M_fuel,M_fuel,'o')
plt.xlabel('MTOW [kg]')
plt.ylabel('Mfuel [kg]')
plt.title('Mfuel = f(MTOW)')
print(f'approximated fuel weight for a maximal takeoff weight of {INITIAL_MAX_TAKEOFF_MASS}[kg] is {np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS):.4f}[kg]')
if TREND_LINE==1:
    plt.plot(np.linspace(min(MTOW_M_fuel),max(MTOW_M_fuel),3),np.polyval(polynomial,np.linspace(min(MTOW_M_fuel),max(MTOW_M_fuel),3)),color = 'red')
    plt.legend(["data", f"trendline: Mfuel = {polynomial[1]:.5f}+{polynomial[0]:.5f}*MTOW"], loc ="best")
if CALCULATE_OPTIMAL_VALUES == 1:
    plt.plot(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,INITIAL_MAX_TAKEOFF_MASS,),'o',color = 'green')
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,0.9*min(M_fuel),0,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS))-0.9*min(M_fuel),head_width=\
        (1.015*np.average(MTOW_M_fuel)-np.average(MTOW_M_fuel)),head_length=1.015*np.average(M_fuel)-np.average(M_fuel),length_includes_head = True,fc="k", ec="k")
    plt.arrow(INITIAL_MAX_TAKEOFF_MASS,np.polyval(polynomial,(INITIAL_MAX_TAKEOFF_MASS)),-INITIAL_MAX_TAKEOFF_MASS+0.9*min(MTOW_M_fuel),0,head_width=\
        (1.015*np.average(M_fuel)-np.average(M_fuel)),head_length=(1.015*np.average(MTOW_M_fuel)-np.average(MTOW_M_fuel)),length_includes_head = True,fc="k", ec="k")
if PLT_GRID == 1:
    plt.grid()
if SAVE_FIG == 1:
    plt.savefig(f'images/MTOW_M_fuel.{IMG_FORMAT}')
if IMG_SHOW == 1:
    plt.show()










