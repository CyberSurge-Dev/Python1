
def display_data(table_name, table):
    """ Display imported data(multi-dim array and string name) in a table format """
    # I made a far more complex version of this program in an older C# library I made
    # (EasyIO, now discontinued because it was basically useless.)

    print(f"\n {table_name}:")

    for row in table:
        for column in row:
            print(f" {column}\t", end="")
        print("")
    

    
