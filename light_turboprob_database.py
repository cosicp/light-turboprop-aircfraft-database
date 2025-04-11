# Light Turboprop Aircraft Database
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
INITIAL_MAX_TAKEOFF_MASS  = 3350 # [kg] turboprop


#    initializing
a = {}
#                                                                                                            DATABASE 1 - Light turboprop aircraft
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a[1] =  apc.Airplane( id=1  ,name = 'PA-46 M600'         , num_of_pass = 6  ,length = 9.05  ,wing_span = 13.15 ,height = 3.44  ,M_empty = 1656  ,M_fuel = 984   ,MTOW = 2721  ,P = 450    ,Vmax = 507    ,W = 7.9   ,L = 2668   ,H_max =9144 )
a[2] =  apc.Airplane( id=2  ,name = 'PA-46 M500'         , num_of_pass = 6  ,length = 9.02  ,wing_span = 13.11 ,height = 3.44  ,M_empty = 1559  ,M_fuel = 644   ,MTOW = 2310  ,P = 370    ,Vmax = 482    ,W = 7.9   ,L = 1852   ,H_max =9144 )
a[3] =  apc.Airplane( id=3  ,name = 'PC-12NG'            , num_of_pass = 11 ,length = 14.4  ,wing_span = 16.28 ,height = 4.26  ,M_empty = 2810  ,M_fuel = 1226  ,MTOW = 4740  ,P = 890    ,Vmax = 528    ,W = 9.75  ,L = 3417   ,H_max =9144 )
a[4] =  apc.Airplane( id=4  ,name = 'King Air C90'       , num_of_pass = 9  ,length = 12.17 ,wing_span = 14    ,height = 4.7   ,M_empty = 3150  ,M_fuel = 1167  ,MTOW = 4580  ,P = 410    ,Vmax = 500    ,W = 10.2  ,L = 2446   ,H_max =9144 )
a[5] =  apc.Airplane( id=5  ,name = 'Epic LT'            , num_of_pass = 6  ,length = 10.92 ,wing_span = 13    ,height = 3.81  ,M_empty = 1814  ,M_fuel = 1090  ,MTOW = 3311  ,P = 890    ,Vmax = 630    ,W = 14.11 ,L = 3471   ,H_max =9400 )
a[6] =  apc.Airplane( id=6  ,name = 'SOCATA TBM 900'     , num_of_pass = 8  ,length = 10.72 ,wing_span = 12.83 ,height = 4.36  ,M_empty = 2097  ,M_fuel = 1100  ,MTOW = 3354  ,P = 630    ,Vmax = 611    ,W = 8.4   ,L = 3304   ,H_max =9449 )
a[7] =  apc.Airplane( id=7  ,name = 'Myasishchev M-101T' , num_of_pass = 7  ,length = 9.98  ,wing_span = 13    ,height = 3.72  ,M_empty = 2016  ,M_fuel = 450   ,MTOW = 3000  ,P = 567    ,Vmax = 525    ,W = 5.06  ,L = 1410   ,H_max =7600 )
a[8] =  apc.Airplane( id=8  ,name = 'Kestrel K-350'      , num_of_pass = 8  ,length = 11.7  ,wing_span = 13.7  ,height = 3.9   ,M_empty = 2359  ,M_fuel = 960   ,MTOW = 3879  ,P = 740    ,Vmax = 593    ,W = 11.4  ,L = 2084   ,H_max =9400 )
a[9] =  apc.Airplane( id=9  ,name = 'Aero Ae 270 Spirit' , num_of_pass = 8  ,length = 12.23 ,wing_span = 13.82 ,height = 4.78  ,M_empty = 2300  ,M_fuel = 956   ,MTOW = 3700  ,P = 630    ,Vmax = 500    ,W = 8.7   ,L = 2980   ,H_max =9140 )
a[10] = apc.Airplane( id=10 ,name = 'GROB G14TP'         , num_of_pass = 6  ,length = 8.91  ,wing_span = 10.6  ,height = 2.8   ,M_empty = 'NaN' ,M_fuel = 956   ,MTOW = 3300  ,P = 340    ,Vmax = 500    ,W = 11.9  ,L = 'NaN'  ,H_max =7620 )
a[11] = apc.Airplane( id=11 ,name = 'KAI KT1'            , num_of_pass = 2  ,length = 10.26 ,wing_span = 10.59 ,height = 3.86  ,M_empty = 1910  ,M_fuel = 408   ,MTOW = 3311  ,P = 708    ,Vmax = 648    ,W = 17.7  ,L = 'NaN'  ,H_max =11580)
a[12] = apc.Airplane( id=12 ,name = 'PAC 750XL'          , num_of_pass = 10 ,length = 11.07 ,wing_span = 12.81 ,height = 3.84  ,M_empty = 1406  ,M_fuel = 1996  ,MTOW = 3402  ,P = 560    ,Vmax = 314    ,W = 8.13  ,L = 1077   ,H_max =6096 )
a[13] = apc.Airplane( id=13 ,name = 'Intracom GM-19'     , num_of_pass = 8  ,length = 10.46 ,wing_span = 13.92 ,height = 4.84  ,M_empty = 1400  ,M_fuel = 976   ,MTOW = 3500  ,P = 560    ,Vmax = 360    ,W = 9.5   ,L = 2660   ,H_max =7165 )
a[14] = apc.Airplane( id=14 ,name = 'Pilatus PC-9M'      , num_of_pass = 2  ,length = 10.13 ,wing_span = 10.13 ,height = 3.26  ,M_empty = 1725  ,M_fuel = 1100  ,MTOW = 3200  ,P = 708    ,Vmax = 593    ,W = 'NaN' ,L = 1573   ,H_max =11580)
a[15] = apc.Airplane( id=15 ,name = 'Cessna 208 Caravan' , num_of_pass = 10 ,length = 11.46 ,wing_span = 15.87 ,height = 4.53  ,M_empty = 2145  ,M_fuel = 1000  ,MTOW = 3538  ,P = 503    ,Vmax = 344    ,W = 6.27  ,L = 1982   ,H_max =7600 )
a[16] = apc.Airplane( id=16 ,name = 'Daher TBM 910'      , num_of_pass = 6  ,length = 10.74 ,wing_span = 12.87 ,height = 4.37  ,M_empty = 2100  ,M_fuel = 884.5 ,MTOW = 3354  ,P = 633.84 ,Vmax = 611.16 ,W = 12.19 ,L = 3204   ,H_max =9449 )
a[17] = apc.Airplane( id=17 ,name = 'Epic 1000'          , num_of_pass = 6  ,length = 10.92 ,wing_span = 13.11 ,height = 3.81  ,M_empty = 2087  ,M_fuel = 875.4 ,MTOW = 3629  ,P = 894.84 ,Vmax = 616.6  ,W = 20.32 ,L = 3055.8 ,H_max =10362)
a[18] = apc.Airplane( id=18 ,name = 'Beechcraft Denali'  , num_of_pass = 11 ,length = 14.86 ,wing_span = 16.54 ,height = 4.62  ,M_empty = 'NaN' ,M_fuel = 499   ,MTOW = 'NaN' ,P = 920    ,Vmax = 528    ,W = 'NaN' ,L = 2963   ,H_max =9449 )
a[19] = apc.Airplane( id=19 ,name = 'Bonanza G36'        , num_of_pass = 6  ,length = 8.32  ,wing_span = 10.21 ,height = 2.62  ,M_empty = 1175  ,M_fuel = 'NaN' ,MTOW = 1656  ,P = 224    ,Vmax = 326    ,W = 6.25  ,L = 1074   ,H_max =5639 )
a[20] = apc.Airplane( id=20 ,name = 'PAC Cresco 08-600'  , num_of_pass = 9  ,length = 11.07 ,wing_span = 12.18 ,height = 3.63  ,M_empty = 1270  ,M_fuel = 545.5 ,MTOW = 3175  ,P = 450    ,Vmax = 274    ,W = 6.32  ,L = 852    ,H_max =5500 )
a[21] = apc.Airplane( id=21 ,name = 'Pilatus PC-7'       , num_of_pass = 2  ,length = 9.78  ,wing_span = 10.4  ,height = 3.21  ,M_empty = 1330  ,M_fuel = 474   ,MTOW = 2700  ,P = 480    ,Vmax = 412    ,W = 10.9  ,L = 2630   ,H_max =10000)
a[22] = apc.Airplane( id=22 ,name = 'Pilatus PC-21'      , num_of_pass = 2  ,length = 11.23 ,wing_span = 9.11  ,height = 3.74  ,M_empty = 2270  ,M_fuel = 'NaN' ,MTOW = 4250  ,P = 'NaN'  ,Vmax = 685    ,W = 20.32 ,L = 1333   ,H_max =11580)
a[23] = apc.Airplane( id=23 ,name = 'A67 Dragon'         , num_of_pass = 2  ,length = 10.39 ,wing_span = 12    ,height = 'NaN' ,M_empty = 2177  ,M_fuel = 'NaN' ,MTOW = 4627  ,P = 930    ,Vmax = 687    ,W = 'NaN' ,L = 3026   ,H_max =11000)
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










