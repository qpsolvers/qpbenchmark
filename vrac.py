from qpsolvers_benchmark import Problem

problem = Problem.from_mat_file("maros_meszaros/CONT-300.mat")
print(problem.ub)
