# PROGRAMMING ASSIGNMENT 

# Question1

----------commands for executing and compiling the program are given at the end QUESTION------------

1. I have solved my first problem using recursion approach 
in which my recursive function is ```def ProbSolve(person, k, index):```

2. Now this recursive function takes 3 parameters as input
  1 ```person``` = vector of persons who are alive
  
  2```k``` = kth person to the right of the current person

  3```index``` = index of the current function

  
3. Now this recursive function finds the person who is going to get killed, after finding it deletes the person from the vector and prints it,
   if length of the vector is 1 then number of persons who are alive is 1 hence it prints the value of that person.
 
4.  Note that my program  stops only when number of person remaining alive is 1, and hence valid input should be given. If any invalid input is given it will print ```please enter valid input``` 

5. I have given numering to persons as ```1,2,3..``` not    ``` a,b,c..``` because if n>26 then it might create a trouble 

If n <= 26 then you can interpret 1=A, 2=B, 3=C ..... 26=Z

6. For executing this program type
   ```python main.py```

   or else type ```python3 main.py```

   after this my program will start taking input for N and K