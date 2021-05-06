I decided to use a backtracking depth-first search with constraint satisfaction. This approach seemed the most logical, I did look at other algorithms, basic and heuristic searches did not seem to be well suited to this problem.
These kinds of searches would really require information about the whole search space, which would mean generating it, and for this problem, the search space is very large. A brute force approach would take more time than we have ever had whilst
the universe has existed to compute (Norvig, 2011), hence this did not seem like a suitable method to solve the problem. A local search seemed like a bad idea because the number of constraints on a Sudoku puzzle meant that not
using them seemed suboptimal. I felt that using a complete algorithm would be better to guarantee that either I got the solution or the problem was unsolvable, though this approach probably would've been my second choice. I also looked
at a dancing links technique which would've been a very good solution to solve the Sudoku puzzles quickly however this seemed very difficult to implement and unnecessary for the assignment. Overall I concluded that a backtracking depth-first
search with constraint propagation would work efficiently enough and not too difficult to implement. 

Once I had made my decision on the approach to use I began to look at how I might go about implementing it. I did some research and thought Norvig presented some good concepts that inspired my solution. A starting point for me
was thinking about the constraints at the beginning and how it would be possible to define what possibilities there are for a square to take. To get the information to the squares about possible numbers they could take I
used dictionaries and a list of the squares. This concept was taken from Norvig's approach. To make this work each square would start off being able to take any number 1-9 and that would be updated as constraints came in. The starting
constraints come straight from the input, squares get set to the number they take in the input, but this also affects other possibilities. As these numbers are set, it is important to make sure that no other numbers on the same row,
column, or block as that square have that squares value in their possible values. To take this possibility out of those other squares I used another dictionary, one that maps squares to the squares it affects. I could then look up in the
dictionary what squares the square I am setting effects and remove the value it is being set to from their possible values. Then one last constraint needed to be looked at, and that was the possibility of a value having only 1 possible
square to go to. In that case, we would need to assign that value to that square, and to do this another dictionary was used. One that matched squares to each "unit" was a part of, its row, column, and block. This way I could check how many
places there were for a specific value to in a specific block that hadn't been assigned yet and if it was only one then I could assign it.

Now that I had dealt with how I was going to handle the constraints it was time to think about the backtracking depth-first search part of the algorithm. The return case would be either if the board was unsolvable or the board was
solved. The board would be solved if every single square on the board only had 1 number left in the dictionary of possible values for a square, and these possible values would be the final values. However in the case the board had not
been solved yet but was still possibly solvable I needed to decide which square to try and decide the value of next, and that would be the square with the least possible values remaining. This is because it would improve efficiency and
certainty, choosing a square with a low number of possibilities left kept the branching factor as low as possible and in turn would create other squares with lower numbers of possible values. Once I got the square with the least number of
possible values left it was time to recurse. We will apply the new value to the square we decided on, make sure all the affected squares get their possibilities updated, and see what happens. Since this is a depth-first approach we will
go as far as we can on a particular route until one of two things happen: it either finds a solution or it fails and we backtrack. If we find a value that makes it impossible to solve the puzzle then we go back to that value and change
it up until we either find a value that keeps it solvable or we go back to the number that was set before that one and we start trying different possibilities of that number and keep backtracking until we eventually can't go back
any further and it is unsolvable or we find a path to solve the puzzle. 

Norvig, P., 2011. Solving Every Sudoku Puzzle. [online] Norvig.com. Available at: <http://norvig.com/sudoku.html>.



