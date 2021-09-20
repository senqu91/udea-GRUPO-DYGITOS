# método GAUSS - SEIDEL
# AUTHOR SAMUEL ELIECER NIÑO

import cmath 
import math 
import numpy as np

# ---------------- Tensión Nodos de entrada ---------------- 

V_Bus1 = 1.05
V_Bus2 = 1
V_Bus3 = 1.02
V_Bus4 = 1.01
V_Bus5 = 1.05
V_Bus6 = 1

# ---------------- Potencia Nodos de entrada ---------------- 

P_Bus1 = 0
P_Bus2 = 0.5634
P_Bus3 = 1.6998
P_Bus4 = 0.9167
P_Bus5 = 2.4713
P_Bus6 = 0.9845

Q_Bus1 = 0j
Q_Bus2 = 0.039j
Q_Bus3 = 0.0904j
Q_Bus4 = 0.15j
Q_Bus5 = 0.5249j
Q_Bus6 = 0.1025j

# ---------------- Admitancias de línea de entrada ---------------- 

Z_Bus1_Bus_2 = 0.0250 + 0.1682j
Z_Bus2_Bus_3 = 0.0238 + 0.2108j
Z_Bus3_Bus_4 = 0.0328 + 0.1325j
Z_Bus4_Bus_5 = 0.1021 + 0.8957j
Z_Bus5_Bus_6 = 0.2130 + 0.8957j
Z_Bus6_Bus_2 = 0.1494 + 0.3692j
Z_Bus6_Bus_3 = 0.1191 + 0.2704j

# ---------------- Admitancias de línea de entrada ---------------- 
B_Bus1_Bus_2 = 0.0259j
B_Bus2_Bus_3 = 0.3017j
B_Bus3_Bus_4 = 0.0325j
B_Bus4_Bus_5 = 0.2406j
B_Bus5_Bus_6 = 0.2406j
B_Bus6_Bus_2 = 0.0412j
B_Bus6_Bus_3 = 0.0328j

# ---------------- Limites de línea MW (BAse 100 MVA) ---------------- 

L_Bus1_Bus_2 = 160
L_Bus2_Bus_3 = 75
L_Bus3_Bus_4 = 60
L_Bus4_Bus_5 = 100
L_Bus5_Bus_6 = 80
L_Bus6_Bus_2 = 75
L_Bus6_Bus_3 = 75

# ----------------Número de generadores
Pg_1_min = 150
Pg_1_max = 200
Qg_1_min = -120
Qg_1_max = 120

Pg_3_min = 30
Pg_3_max = 63
Qg_3_min = 0
Qg_3_max = 98
Pg3 = 0

Pg_4_min = 50
Pg_4_max = 70
Qg_4_min = -50
Qg_4_max = 81
Pg4 = 60

Pg_5_min = 380
Pg_5_max = 400
Qg_5_min = -110
Qg_5_max = 110
Pg5 = 380

# ----------------Tensiones



# ----------------Potencias



# ----------------Cargas



# ----------------Admitancias rectangulares 
y_11 = 1/Z_Bus1_Bus_2
print(y_11)
y_12 = 1/Z_Bus1_Bus_2 + (B_Bus1_Bus_2/2)
y_13 = 0
y_14 = 0
y_15 = 0
y_16 = 0

y_21 = 1/Z_Bus1_Bus_2
y_22 = 1/Z_Bus1_Bus_2 + 1/Z_Bus2_Bus_3 + 1/Z_Bus6_Bus_2 + (B_Bus1_Bus_2/2) + (B_Bus2_Bus_3/2) + (B_Bus6_Bus_2/2)
y_23 = 1/Z_Bus2_Bus_3
y_24 = 0
y_25 = 0
y_26 = 1/Z_Bus6_Bus_2

y_31 = 0
y_32 = 1/Z_Bus2_Bus_3
y_33 = (1/Z_Bus2_Bus_3) + (1/Z_Bus3_Bus_4) + (1/Z_Bus6_Bus_3) + (B_Bus2_Bus_3/2) + (B_Bus6_Bus_3/2) + (B_Bus3_Bus_4/2)
y_34 = 1/Z_Bus3_Bus_4
y_35 = 0
y_36 = 1/Z_Bus6_Bus_3

y_41 = 0
y_42 = 0
y_43 = 1/Z_Bus3_Bus_4
y_44 = (1/Z_Bus3_Bus_4) + (1/Z_Bus4_Bus_5) +  (B_Bus3_Bus_4/2) + (B_Bus4_Bus_5/2)
y_45 = 1/Z_Bus4_Bus_5
y_46 = 0

y_51 = 0
y_52 = 0
y_53 = 0
y_54 = 1/Z_Bus4_Bus_5
y_55 = (1/Z_Bus5_Bus_6) + (1/Z_Bus4_Bus_5) + (B_Bus5_Bus_6/2) + (B_Bus4_Bus_5/2)
y_56 = 1/Z_Bus5_Bus_6

y_61 = 0
y_62 = 1/Z_Bus6_Bus_2
y_63 = 1/Z_Bus6_Bus_3
y_64 = 0
y_65 = 1/Z_Bus5_Bus_6
y_66 = (1/Z_Bus6_Bus_2) + (1/Z_Bus6_Bus_3) + (1/Z_Bus5_Bus_6) + (B_Bus6_Bus_2/2) + (B_Bus6_Bus_3/2) + (B_Bus5_Bus_6/2)



# ----------------Admitancias----------------  

Y_11 = cmath.polar(y_11)
Y_12 = cmath.polar(y_12)
Y_13 = cmath.polar(y_13)
Y_14 = cmath.polar(y_14)
Y_15 = cmath.polar(y_15)
Y_16 = cmath.polar(y_16)

Y_21 = cmath.polar(y_21)
Y_22 = cmath.polar(y_22)
Y_23 = cmath.polar(y_23)
Y_24 = cmath.polar(y_24)
Y_25 = cmath.polar(y_25)
Y_26 = cmath.polar(y_26)

Y_31 = cmath.polar(y_31)
Y_32 = cmath.polar(y_32)
Y_33 = cmath.polar(y_33)
Y_34 = cmath.polar(y_34)
Y_35 = cmath.polar(y_35)
Y_36 = cmath.polar(y_36)

Y_41 = cmath.polar(y_41)
Y_42 = cmath.polar(y_42)
Y_43 = cmath.polar(y_43)
Y_44 = cmath.polar(y_44)
Y_45 = cmath.polar(y_45)
Y_46 = cmath.polar(y_46)

Y_51 = cmath.polar(y_51)
Y_52 = cmath.polar(y_52)
Y_53 = cmath.polar(y_53)
Y_54 = cmath.polar(y_54)
Y_55 = cmath.polar(y_55)
Y_56 = cmath.polar(y_56)

Y_61 = cmath.polar(y_61)
Y_62 = cmath.polar(y_62)
Y_63 = cmath.polar(y_63)
Y_64 = cmath.polar(y_64)
Y_65 = cmath.polar(y_65)
Y_66 = cmath.polar(y_66)

print("-------------------MATRIZ DE ADMITANCIAS-----------------------------")
Matriz_admitancia = [[Y_11,Y_12,Y_13,Y_14,Y_15,Y_16],[Y_21,Y_22,Y_23,Y_24,Y_25,Y_26],[Y_31,Y_32,Y_33,Y_34,Y_35,Y_36],
[Y_41,Y_42,Y_43,Y_44,Y_45,Y_46],[Y_51,Y_52,Y_53,Y_54,Y_55,Y_56],[Y_61,Y_62,Y_63,Y_64,Y_65,Y_66]]
m_Y = np.array(Matriz_admitancia)
print(m_Y)

print("-------------------MATRIZ DE ADMITANCIAS-- polares---------------------------")
m_Y_polar = np.zeros((6,6))
m_Y_polar_rad = np.zeros((6,6))
for i in range (m_Y.shape[0]):
    for j in range (m_Y.shape[1]):
        n_polar = cmath.polar(m_Y[i][j])
        m_Y_polar[i][j] = n_polar[0]
        m_Y_polar_rad[i][j] = n_polar[1]
print(m_Y_polar)
print(m_Y_polar_rad)


# ----------------ITERACIONES---------------- 