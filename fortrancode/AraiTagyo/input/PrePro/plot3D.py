# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# import matplotlib.pyplot as plt
# import numpy as np

# # Read the file. 
# # f1 = open('lattice.asc', 'r')
# # f2 = open('emb20DEMplot.asc', 'r')
# # f3 = open('emb20layer_2.asc', 'r')
# f4 = open('emb20layer_1.asc', 'r')
# # read the whole file into a single variable, which is a list of every row of the file.

# f3 = open('test0_newDEMRI_out.asc', 'r')
# f2 = open('emb20DEMplot.asc', 'r')

# lines = f2.readlines()
# f2.close()

# lines1 = f3.readlines()
# f3.close()

# lines2 = f4.readlines()
# f4.close()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')


# xF = []
# yF = []
# zF = []
# # FF = []


# # for i in range(len(lines0)):
# # 	F = lines0[i].split()
# # 	xF.append(F[0])
# # 	yF.append(F[1])
# # 	zF.append(F[2])
# # 	if float(F[3]) > 10.0:
# # 		FF.append(0.0)
# # 	if float(F[3]) < 10.0:
# # 		FF.append(F[3])

# axF = np.array(xF, dtype=float)
# ayF = np.array(yF, dtype=float)
# azF = np.array(zF, dtype=float)
# # aFF = np.array(FF, dtype=float)

# cmap = plt.matplotlib.cm.jet

# ax.scatter(axF, ayF, azF, cmap=cmap)
# # ax.set_title('Arai and Tagyo', fontsize='30')

# plt.xlabel('Wdith (m)', fontsize='26')
# plt.ylabel('Distance (m)', fontsize='26')
# ax.set_zlabel('Height (m)', fontsize='26')

# plt.tick_params(labelsize=24)

# # matplotlib.rc('xtick', labelsize='30')




# # grid size
# gdsx = 133
# gdsy = 133

# #cell size
# csix = 0.5
# csiy = 0.5 

# # initialize some variable to be lists:
# x = np.linspace(0, gdsx*csix, gdsx)
# y = np.linspace(0, gdsy*csiy, gdsy)

# xm = []
# ym = []
# pm = []
# qm = []
# rm = []

# for i in range(len(x)):
# 	# counter checking
# 	# print i
# 	for j in range(len(y)):
# 		p = lines[i].split()
# 		q = lines1[i].split()
# 		r = lines2[i].split()
# 		xm.append(x[i])
# 		ym.append(y[j])
# 		pm.append(p[j])
# 		# print x[i],",", y[j],",", p[j]
# 		qm.append(q[j])
# 		if float(r[j]) > 0.0:
# 			rm.append(r[j])
# 		if float(r[j]) < 0.0:
# 			rm.append(p[j])# 	rm.append(0.0)

# # for i in range(len(x)):
# # 	for j in range(len(y)):
# # 		p = lines[i].split()
# # 		q = lines1[i].split()
# # 		r = lines2[i].split()
# # 		# if float(p[j]) == -9999.0:
# # 		# 	print x[i],",", y[j],",", 900.0
# # 		# else: 
# # 		# print x[i],",", y[j],",", q[j]
# # 		xm.append(x[i])
# # 		ym.append(y[j])
# # 		if abs(float(p[j]) - float(q[j])) > 0.0:
# # 			pm.append(q[j])
# # 			print x[i],",", y[j],",", q[j]
# # 		elif float(p[j]) - float(q[j]) < 0.0:
# # 			pm.append(0)
# # 		else:
# # 			pm.append(0)


# axm=np.array(xm, dtype=float)
# aym=np.array(ym, dtype=float)
# apm=np.array(pm, dtype=float)
# aqm=np.array(qm, dtype=float)
# arm=np.array(rm, dtype=float)

# ax.scatter(axm, aym, apm, color= 'yellow')
# ax.scatter(axm, aym, aqm, color= 'brown', s=8)
# # ax.scatter(axm, aym, arm, color= colour2)

# # ax.view_init(elev=0.0, azim=360)
# # ax.bar(axm, aym, apm)
# # ax.text(50.0, 30.0, 40.0, "HAY", color="red")

# plt.show()

# # # for i in range(len(x)):
# # # 	# counter checking
# # # 	print i
# # # 	for j in range(len(y)):
# # # 		p = lines[i].split()
# # # 		q = lines1[i].split()
# # # 		ax.plot([float(x[i])],[float(y[j])],[float(p[j])], markerfacecolor= colour, marker='o')
# # # 		ax.plot([float(x[i])],[float(y[j])],[float(q[j])], markerfacecolor= colour1, marker='o')

# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# import matplotlib.pyplot as plt
# import numpy as np

# # Read the file. 
# # f1 = open('lattice.asc', 'r')
# # f2 = open('emb20DEMplot.asc', 'r')
# f3 = open('emb20layer_2.asc', 'r')
# f4 = open('emb20layer_1.asc', 'r')
# # read the whole file into a single variable, which is a list of every row of the file.
# f2 = open('emb20DEMplot.asc', 'r')

# lines = f2.readlines()
# f2.close()

# lines1 = f3.readlines()
# f3.close()

# lines2 = f4.readlines()
# f4.close()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')


# xF = []
# yF = []
# zF = []
# # FF = []


# # for i in range(len(lines0)):
# # 	F = lines0[i].split()
# # 	xF.append(F[0])
# # 	yF.append(F[1])
# # 	zF.append(F[2])
# # 	if float(F[3]) > 10.0:
# # 		FF.append(0.0)
# # 	if float(F[3]) < 10.0:
# # 		FF.append(F[3])

# axF = np.array(xF, dtype=float)
# ayF = np.array(yF, dtype=float)
# azF = np.array(zF, dtype=float)
# # aFF = np.array(FF, dtype=float)

# cmap = plt.matplotlib.cm.jet

# ax.scatter(axF, ayF, azF, cmap=cmap)
# # ax.set_title('Arai and Tagyo', fontsize='30')

# plt.xlabel('Wdith (m)', fontsize='26')
# plt.ylabel('Distance (m)', fontsize='26')
# ax.set_zlabel('Height (m)', fontsize='26')

# plt.tick_params(labelsize=24)

# # matplotlib.rc('xtick', labelsize='30')

# # # grid size
# # gdsx = 86
# # gdsy = 152

# # grid size
# gdsx = 133
# gdsy = 133

# #cell size
# csix = 0.5
# csiy = 0.5

# # initialize some variable to be lists:
# x = np.linspace(0, gdsx*csix, gdsx)
# y = np.linspace(0, gdsy*csiy, gdsy)

# xm = []
# ym = []
# pm = []
# qm = []
# rm = []

# # for i in range(len(x)):
# # 	# counter checking
# # 	# print i
# # 	for j in range(len(y)):
# # 		p = lines[i].split()
# # 		q = lines1[i].split()
# # 		r = lines2[i].split()
# # 		# if abs(float(p[j])-2000.0) > 0.0:
# # 		# 	xm.append(x[i])
# # 		# 	ym.append(y[j])
# # 		# 	pm.append(p[j])
# # 		# print x[i],",", y[j],",", p[j]
# # 		# qm.append(q[j])
# # 		# if float(r[j]) > 0.0:
# # 		# 	rm.append(r[j])
# # 		# if float(r[j]) < 0.0:
# # 		# 	rm.append(p[j])# 	rm.append(0.0)

# for i in range(len(x)):
# 	for j in range(len(y)):
# 		p = lines[i].split()
# 		q = lines1[i].split()
# 		r = lines2[i].split()
# 		# if float(p[j]) == -9999.0:
# 		# 	print x[i],",", y[j],",", 900.0
# 		# else: 
# 		# print x[i],",", y[j],",", q[j]
# 		xm.append(x[i])
# 		ym.append(y[j])
# 		if abs(float(p[j]) - float(q[j])) > 0.0:
# 			pm.append(q[j])
# 			print x[i],",", y[j],",", q[j]
# 		elif float(p[j]) - float(q[j]) < 0.0:
# 			pm.append(0)
# 		else:
# 			pm.append(0)


# axm=np.array(xm, dtype=float)
# aym=np.array(ym, dtype=float)
# apm=np.array(pm, dtype=float)
# aqm=np.array(qm, dtype=float)
# arm=np.array(rm, dtype=float)

# ax.scatter(axm, aym, apm, color= 'yellow', s=100)
# ax.scatter(axm, aym, apm, color= 'brown', s=8)

# # ax.scatter(axm, aym, aqm, color= 'brown', s=8)
# # ax.scatter(axm, aym, arm, color= colour2)

# # ax.view_init(elev=0.0, azim=360)
# # ax.bar(axm, aym, apm)
# # ax.text(50.0, 30.0, 40.0, "HAY", color="red")
# ax.set_zlim3d(1500,3000)
# plt.show()

# # for i in range(len(x)):
# # 	# counter checking
# # 	print i
# # 	for j in range(len(y)):
# # 		p = lines[i].split()
# # 		q = lines1[i].split()
# # 		ax.plot([float(x[i])],[float(y[j])],[float(p[j])], markerfacecolor= colour, marker='o')
# # 		ax.plot([float(x[i])],[float(y[j])],[float(q[j])], markerfacecolor= colour1, marker='o')

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

# Read the file. 
# f1 = open('lattice.asc', 'r')
# f2 = open('emb20DEMplot.asc', 'r')
f2 = open('test16_newDEM_out.asc', 'r')
f3 = open('emb20layer_2.asc', 'r')
f4 = open('emb20layer_1.asc', 'r')
# read the whole file into a single variable, which is a list of every row of the file.

lines = f2.readlines()
f2.close()

lines1 = f3.readlines()
f3.close()

lines2 = f4.readlines()
f4.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


xF = []
yF = []
zF = []
# FF = []


# for i in range(len(lines0)):
# 	F = lines0[i].split()
# 	xF.append(F[0])
# 	yF.append(F[1])
# 	zF.append(F[2])
# 	if float(F[3]) > 10.0:
# 		FF.append(0.0)
# 	if float(F[3]) < 10.0:
# 		FF.append(F[3])

axF = np.array(xF, dtype=float)
ayF = np.array(yF, dtype=float)
azF = np.array(zF, dtype=float)
# aFF = np.array(FF, dtype=float)

cmap = plt.matplotlib.cm.jet

ax.scatter(axF, ayF, azF, cmap=cmap)
# ax.set_title('Donald and Giam', fontsize='30')

# plt.xlabel('Wdith (m)', fontsize='26')
plt.ylabel('Distance (m)', fontsize='26')
ax.set_zlabel('Height (m)', fontsize='26')

colour = 'green'
colour1= 'red'
colour2= 'grey'

# grid size
gdsx = 133
gdsy = 133

#cell size
csix = 0.5
csiy = 0.5

# initialize some variable to be lists:
x = np.linspace(0, gdsx*csix, gdsx)
y = np.linspace(0, gdsy*csiy, gdsy)

xm = []
ym = []
pm = []
qm = []
rm = []

for i in range(len(x)):
	# counter checking
	# print i
	for j in range(len(y)):
		p = lines[i].split()
		q = lines1[i].split()
		r = lines2[i].split()
		xm.append(x[i])
		ym.append(y[j])
		pm.append(p[j])
		print x[i], ",", y[j],",", r[j]
		# qm.append(q[j])
		if float(q[j]) > 0.0:
			qm.append(q[j])
		if float(q[j]) < 0.0:
			qm.append(p[j])# 	rm.append(0.0)
		if float(r[j]) > 0.0:
			rm.append(r[j])
		if float(r[j]) < 0.0:
			rm.append(p[j])# 	rm.append(0.0)

axm=np.array(xm, dtype=float)
aym=np.array(ym, dtype=float)
apm=np.array(pm, dtype=float)
aqm=np.array(qm, dtype=float)
arm=np.array(rm, dtype=float)

ax.scatter(axm, aym, aqm, color= "brown")
ax.scatter(axm, aym, arm, color= "blue")
ax.scatter(axm, aym, apm, color= "green")
# ax.text(50.0, 30.0, 40.0, "HAY", color="red")
plt.tick_params(labelsize=24)
ax.view_init(elev=0.0, azim=360)
plt.show()

# for i in range(len(x)):
# 	# counter checking
# 	print i
# 	for j in range(len(y)):
# 		p = lines[i].split()
# 		q = lines1[i].split()
# 		ax.plot([float(x[i])],[float(y[j])],[float(p[j])], markerfacecolor= colour, marker='o')
# 		ax.plot([float(x[i])],[float(y[j])],[float(q[j])], markerfacecolor= colour1, marker='o')