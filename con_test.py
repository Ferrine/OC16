import pickle

from rassadka_modules import rassadka_exceptions
from rassadka_modules.controller import Controller


if __name__ == "__main__":
    prefix = "test_out\\"

    settings = "exceltestdata/settings.xlsx"
    people = "exceltestdata/people.xlsx"
    print("getting settings")
    con = Controller(settings)
    print("got settings")
    print("getting people")
    con.load_people(people)
    con.split_people()
    print("got people")
    print("rassadka...")
    try:
        con.place_them()
        print("...end")
    except rassadka_exceptions.NoFreeAuditory:
        print("...bad end")
    print("making xlsx file...")
    con.dump_seated()
    print("done")
    print("printing self...")
    print(con.whole_summary(), file=open(prefix + "whole_sum.txt", "w"))
    print("dumping self...")
    with open(prefix + "dump.pkl", "wb") as d:
        pickle.dump(con, d)
    print("loading self...")
    n = pickle.load(open(prefix + "dump.pkl", "rb"))
    print(n.auds)
    n.write_maps_with_data(prefix + "with_klass.xlsx", "klass")
    n.write_maps_with_status(prefix + "with_status.xlsx")
    n.xlsx_summary()


