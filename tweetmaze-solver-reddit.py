maze_string = '7347737258493420'

'''Copy and paste maze strings into the above to change which maze is being run.
Other maze strings to play with:
422230
313210
313110
7347737258493420
'''

maze = [int(i) for i in maze_string]

solution = [0]  #this is the solution stack. append to put on new steps, 
    #pop() to backtrack.
    #algorithm doesn't work if I don't initialize the solution list with the 0 position. Hits max recursion depth.

solution_steps = []

def valid(position, direction):
    #pass in the current position, desired direction of move
    global maze
    if direction == 'right':
        return True if position + maze[position] < len(maze) else False
    elif direction == 'left':
        return True if position - maze[position] >= 0 else False
    
def solve(position):
    global solution
    global maze
    
    #if maze is solved, return True
    if maze[position] == 0:
        return True
    
    #try branches  
    if valid(position, 'right') and (position + maze[position] not in solution):
        new = position + maze[position]
        solution.append(new)
        if solve(new):
            solution_steps.append(f'Current position: {position}. Stepping right by {maze[position]} to index {new}.')
            return True
        solution.pop()
        
    if valid(position, 'left') and (position - maze[position] not in solution):
        new = position - maze[position]
        solution.append(new)
        if solve(new):
            solution_steps.append(f'Current position: {position}. Stepping left by {maze[position]} to index {new}.')
            return True
        solution.pop()
    
    solution.append('no solution')
    return False

def display_solution():
    global maze
    global solution
    print(maze)
    for i in solution:
        point = ' ' + 3*i*' ' + '#'
        print(point)
        
if __name__ == "__main__":
    
    solve(0)
    
    if solution != 'no solution':
        for step in reversed(solution_steps):
            print(step)
        print(f'\nSolution stack shows these positions: {solution}\n')   
        display_solution()
    else:
        print(solution)
