from objects import Point, RunOrtho
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
	# Testing @@@
	# # point_a = Point(0,0)
	# # point_b = Point(0,100)
	# # link_list = [10,25,50,75]
	# #
	# # ort1 = RunOrtho(point_a,point_b,link_list,None,'m')
	#
	# p_c = Point(0,0)
	# p_d = Point(1816.6,0)
	#
	# link_list_cd = [243,264,275,700,1200,1453,1814]
	# ort_list_cd = [-3,0,-2,0,0,5,16]
	# written_length = 1814
	#
	# runort_cd = RunOrtho(p_c,p_d,link_list_cd,ort_list_cd,written_length,'link')
	# df = runort_cd.fixedPicksDfTable()
	# print(df.round(2).to_string(index=False))
	# df.round(2).to_csv('test.csv',index=False)
	#
	# cord, cord_np = runort_cd.coordinates()
	# # cm = sns.light_palette("seagreen", as_cmap=True)
	# # styled_table = df.style.background_gradient(cmap=cm)
	# # styled_table
	#
	# # fig, ex = plt.subplots(1,1)
	# # ex = plt.scatter(cord_np[:,0],cord_np[:,1])
	# # ex = plt.scatter([p_c.x,p_d.x],[p_c.y,p_d.y])
	# # fig.show()

	ps790 = Point(179650.94, 271726.74)
	ps791 = Point(179760.10, 271821.82)
	ps792 = Point(179648.82, 271818.33)

	l792_791 = RunOrtho(ps792, ps791, [77.8], [-12.8], 111.4, 'm')
	parcel_p_3, parcel_p_3_np = l792_791.coordinates()
	l792_791_df = l792_791.fixedPicksDfTable()
	l792_791_df.round(2).to_csv('l792_791_df.csv', index=False)

	l791_1 = RunOrtho(ps791, ps790, [79], [0], 145, 'm')
	p1, p1_np = l791_1.coordinates()
	l791_1 = l791_1.fixedPicksDfTable()
	l791_1.round(2).to_csv('l791_1.csv', index=False)

	l1_792 = RunOrtho(p1[0], ps792, [19.4], [-1.5], 70.9, 'm')
	parcel_p_1, parcel_p_1_np = l1_792.coordinates()
	l1_792 = l1_792.fixedPicksDfTable()
	l1_792.round(2).to_csv('l1_792.csv', index=False)

	l792_1 = RunOrtho(ps792, p1[0], [70.9 + 25.6], [0], 70.9 + 25.6, 'm')
	parcel_p_2, parcel_p_2_np = l792_1.coordinates()
	l792_1 = l792_1.fixedPicksDfTable()
	l792_1.round(2).to_csv('l792_1.csv', index=False)

	fig, ax = plt.subplots(1, 1)
	plt.axes().set_aspect('auto')
	ax = plt.scatter([ps790.x, ps791.x, ps792.x], [ps790.y, ps791.y, ps792.y])
	ax = plt.scatter(parcel_p_3_np[0, 0], parcel_p_3_np[0, 1], None, 'r')
	ax = plt.scatter(p1_np[0, 0], p1_np[0, 1], None, 'k')
	ax = plt.scatter(parcel_p_1_np[0, 0], parcel_p_1_np[0, 1], None, 'r')
	ax = plt.scatter(parcel_p_2_np[0, 0], parcel_p_2_np[0, 1], None, 'r')
	fig.show()

	hazit1_2 = parcel_p_1[0].distCalc(parcel_p_2[0])
	hazit1_3 = parcel_p_1[0].distCalc(parcel_p_3[0])
	hazit791_2 = ps791.distCalc(parcel_p_2[0])
	hazit791_3 = ps791.distCalc(parcel_p_3[0])

	cordinates = pd.DataFrame([[parcel_p_1_np[0, 0], parcel_p_1_np[0, 1], 'Parcel Point 1'],
	                           [parcel_p_2_np[0, 0], parcel_p_2_np[0, 1], 'Parcel Point 2'],
	                           [parcel_p_3_np[0, 0], parcel_p_3_np[0, 1], 'Parcel Point 3'],
	                           [ps791.x, ps791.y, 'Parcel Point 791']],
	                          columns=['E(m)', 'N(m)', 'Point'])
	print('Coordinates')
	print(cordinates)
	cordinates.round(3).to_csv('cordinates.csv', index=False)

	hazitot = pd.DataFrame([[hazit1_2, '1->2'],
	                        [hazit1_3, '1->3'],
	                        [hazit791_2, '791->2'],
	                        [hazit791_3, '791->3']],
	                       columns=['Length(m)', 'Sides'])
	print('Parcel Sides')
	print(hazitot)
	hazitot.round(3).to_csv('hazitot.csv', index=False)

	cordinates.loc


	def PolyArea(x, y):
		return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


	area = PolyArea(cordinates['E(m)'].to_numpy(),
	                cordinates['N(m)'].to_numpy())
	print(area)

	print('stop')
