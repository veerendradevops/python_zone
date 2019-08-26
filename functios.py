# function is block of reusable code which can be called whenever required
def test():
    print("hai this is veerendrakumar")
    test()

    #parameterized function
    def printing(x):
        print("printing value of :",x)
        printing("vk")

     #parametrized function with user defined parameter
     def printing(x):
     print("printing value of :",x)
     x=input("taking input from the user::")
     printing(x)
