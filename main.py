'''
Function Name: towerOfHanoi
Parameters: n, initPeg, endPeg, tmpPeg
Return: None
Description: This function prints out the steps 
    of the Tower of Hanoi game using recursion.
'''
def towerOfHanoi(n, initPeg, endPeg, tmpPeg):
    if n == 1:
        print(f'{initPeg} -> {endPeg}')
    else:
        towerOfHanoi(n-1, initPeg, tmpPeg, endPeg)
        print(f'{initPeg} -> {endPeg}')
        towerOfHanoi(n-1, tmpPeg, endPeg, initPeg)



'''
Function Name: main
Arguments: None
Return: None
Description: This function will call the recursive function with the
    arguments n, start, and end. 
    'n' being the number of disks. 
    'start' being the starting peg
    'end' being the ending peg.
'''
def main() -> None:
    peg_count = int(input("Enter the amount of pegs:"))
    start_peg = int(input("Enter the starting peg: "))
    end_peg = int(input("Enter the end peg: "))
    tmp_peg = int(input("Enter the temporary peg: "))



    towerOfHanoi(peg_count, start_peg, end_peg, tmp_peg)

    # When the program ends it will say that the world ended.
    print("OH NO! THE PRIESTS BEAT THE TOWER OF HANOI!! THE WORLD HAS ENDED!!!!!!")
    

if __name__ == "__main__":
    main()
