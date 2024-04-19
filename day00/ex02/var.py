def my_var():
    var_1 = 42
    var_2 = "42"
    var_3 = "quarante-doux"
    var_4 = 42.0
    var_5 = True
    var_6 = [42]
    var_7 = {42: 42}
    var_8 = (42,)
    var_9 = set()
    
    for var in (var_1, var_2, var_3,var_4, var_5,var_6, var_7, var_8, var_9):
        print(f"{var} has a type {type(var)}")

if __name__ == '__main__':
    my_var()
