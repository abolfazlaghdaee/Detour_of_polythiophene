import numpy as np


def Detour_Polythiophene(p):

    # base matrix of polythiophene
    base = np.array([[0, 1, 5, 4, 4, 5, 5],
                     [1, 0, 4, 3, 3, 4, 4],
                     [5, 4, 0, 4, 3, 3, 4],
                     [4, 3, 4, 0, 4, 3, 5],
                     [4, 3, 3, 4, 0, 4, 1],
                     [5, 4, 3, 3, 4, 0, 5],
                     [5, 4, 4, 5, 1, 5, 0]])

    # complement matrix of base matrix
    complement = np.array([[0, 4, 3, 3, 4],
                           [4, 0, 4, 3, 5],
                           [3, 4, 0, 4, 1],
                           [3, 3, 4, 0, 5],
                           [4, 5, 1, 5 ,0]])


    n= p*5 +2 #number of nodes


    j = int((n-7) / 5)  # calculate of number of repeats


    new = base
    for i in range(j):
        base = new




        a = base.shape[0]


        new = np.column_stack((new, base[:,a -1] +4)) # extend columns of new matrix (in order)
        new = np.column_stack((new, base[:,a -1] +3))
        new = np.column_stack((new, base[:,a -1] +3))
        new = np.column_stack((new, base[:,a -1] +4))
        new = np.column_stack((new, base[:,a -1] +4))

        




        for k in range(5):
            base = np.column_stack((base, np.zeros(a)))  #extend columns of base matrix



        new = np.vstack((new, new[a-1,:] +4)) #extend row of new matrix (in order)
        new = np.vstack((new, new[a-1,:] +3))
        new = np.vstack((new, new[a-1,:] +3))
        new = np.vstack((new, new[a-1,:] +4))
        new = np.vstack((new, new[a-1,:] +4))

        b = new.shape[0]  - 1
        new[b -4: , b - 4:] =0




        C_col= complement.shape[1]


        # generate new compelement matrix by dimention of new matrix

        for i in range(100):

            if complement.shape[0] == new.shape[0] :
                break
            complement= np.insert(complement, 0, np.zeros(C_col), axis=0)



        C_row = complement.shape[0]

        for i in range(100):

            if complement.shape[1] == new.shape[1] :
                 break
            complement= np.insert(complement, 0, np.zeros(C_row), axis=1)


        new = new + complement



    return new, new.sum()/2




p = int(input("Enter the number of PT: "))
print(Detour_Polythiophene(p))
