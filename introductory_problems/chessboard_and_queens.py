#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

def print_board(board):
	for x in board:
		print(x)


def diagonal_attack(x, y, board):

	if board[x][y] == '*':
		return None
	else:
		board[x] = board[x][:y] + "*" + board[x][y+1:]
		x_temp = x - 1
		y_temp = y + 1
		while x_temp >= 0 and y_temp < 8:
			board[x_temp] = board[x_temp][:y_temp] + "*" + board[x_temp][y_temp+1:]
			x_temp -= 1
			y_temp += 1

		x_temp = x + 1
		y_temp = y + 1
		while x_temp < 8 and y_temp < 8:
			board[x_temp] = board[x_temp][:y_temp] + "*" + board[x_temp][y_temp+1:]
			x_temp += 1
			y_temp += 1

		x_temp = x + 1
		y_temp = y - 1
		while x_temp < 8 and y_temp >= 0:
			board[x_temp] = board[x_temp][:y_temp] + "*" + board[x_temp][y_temp+1:]
			x_temp += 1
			y_temp -= 1

		x_temp = x - 1
		y_temp = y - 1
		while x_temp >= 0 and y_temp >= 0:
			board[x_temp] = board[x_temp][:y_temp] + "*" + board[x_temp][y_temp+1:]
			x_temp -= 1
			y_temp -= 1

		return board


board_input = []

for i in range(8):
	row = input()
	board_input.append(row)

rem_list_0 = list(range(8))
count = 0

for i in rem_list_0:
	# print("try", i)
	board_0 = board_input.copy()
	board_0 = diagonal_attack(i, 0, board_0)
	if board_0 == None:
		continue
	rem_list_1 = rem_list_0.copy()
	rem_list_1.remove(i)
	#print("success",i)
	#print_board(board_0)
	for j in rem_list_1:
		#print("try", i,j)
		board_1 = board_0.copy()
		board_1 = diagonal_attack(j, 1, board_1)
		if board_1 == None:
			continue
		rem_list_2 = rem_list_1.copy()
		rem_list_2.remove(j)
		#print("success",i,j)
		#print_board(board_1)
		for k in rem_list_2:
			#print("try", i,j,k)
			board_2 = board_1.copy()
			board_2 = diagonal_attack(k, 2, board_2)
			if board_2 == None:
				continue
			rem_list_3 = rem_list_2.copy()
			rem_list_3.remove(k)
			#print("success",i,j,k)
			#print_board(board_2)
			for l in rem_list_3:
				#print("try", i,j,k,l)
				board_3 = board_3 = board_2.copy()
				board_3 = diagonal_attack(l, 3, board_3)
				if board_3 == None:
					continue
				rem_list_4 = rem_list_3.copy()
				rem_list_4.remove(l)
				#print("success",i,j,k,l)
				#print_board(board_1)
				for m in rem_list_4:
					#print("try", i,j,k,l,m)
					board_4 = board_3.copy()
					board_4 = diagonal_attack(m, 4, board_4)
					if board_4 == None:
						continue
					rem_list_5 = rem_list_4.copy()
					rem_list_5.remove(m)
					#print("success",i,j,k,l,m)
					#print_board(board_4)
					for n in rem_list_5:
						#print("try", i,j,k,l,m,n)
						board_5 = board_4.copy()
						board_5 = diagonal_attack(n, 5, board_5)
						if board_5 == None:
							continue
						rem_list_6 = rem_list_5.copy()
						rem_list_6.remove(n)
						#print("success",i,j,k,l,m,n)
						#print_board(board_5)
						for o in rem_list_6:
							#print("try", i,j,k,l,m,n,o)
							board_6 = board_5.copy()	
							board_6 = diagonal_attack(o, 6, board_6)
							if board_6 == None:
								continue
							rem_list_7 = rem_list_6.copy()
							rem_list_7.remove(o)
							#print("success",i,j,k,l,m,n,o)
							#print_board(board_6)
							for p in rem_list_7:
								#print("try", i,j,k,l,m,n,o,p)
								board_7 = board_6.copy()
								board_7 = diagonal_attack(p, 7, board_7)
								if board_7 == None:
									continue
								count += 1
								#print(i,j,k,l,m,n,o,p)

print(count)
