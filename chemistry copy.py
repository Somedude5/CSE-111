def make_periodic_table():
        table = [

        ["Ac", "Actinium", 227],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
        ]

        print(*table,sep='\n')
        return table



def main ():
    make_periodic_table()

if __name__ == "__main__":
    main()
