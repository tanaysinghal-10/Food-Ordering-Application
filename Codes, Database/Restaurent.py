import sqlite3
from tabulate import tabulate


class Restaurant:
    """Class for fetching restaurant data
    """

    def __init__(self):
        pass

    def show_all(self):
        """Show all available restaurants.
        """

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()
        head = ['INDEX', 'RESTAURANT', 'LATITUDE', 'LONGITUDE']
        idx = list()
        rest = list()
        lati = list()
        longi = list()
        c.execute("SELECT rowid, * FROM Restaurent")
        items = c.fetchall()

        for i, j, k, l in items:
            idx.append(i)
            rest.append(j)
            lati.append(k)
            longi.append(l)

        table_data = list(zip(idx, rest, lati, longi))
        table = tabulate(
            headers=head, tabular_data=table_data, tablefmt="github")
        print(table)

        conn.commit()
        conn.close()

    def read_one(self, x):
        """Get restaurants by rowid.

        Args:
            x (int): rowid

        Returns:
            str: Name, latitude, longitude
        """

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Restaurent WHERE rowid = (?)", (x,))
        items = c.fetchall()
        x = items[0]
        return x[1], x[2], x[3]

    def show_kolkata(self):
        """Display menu for KOLKATA KATHI ROLLS.
        """

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM kolkata")
        items = c.fetchall()
        head = ['INDEX', 'MENU', 'PRICE', 'PREPARATION TIME']
        idx = list()
        menu = list()
        price = list()
        ti = list()

        for i, j, k, l in items:
            idx.append(i)
            menu.append(j)
            price.append(k)
            ti.append(l)

        table_data = list(zip(idx, menu, price, ti))
        table = tabulate(headers=head, tabular_data=table_data, tablefmt="rst")
        print(table)

        conn.commit()
        conn.close()

    def show_Haldiram(self):
        """Display menu for HALDIRAMS.
        """

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Haldiram")
        items = c.fetchall()
        head = ['INDEX', 'MENU', 'PRICE', 'PREPARATION TIME']
        idx = list()
        menu = list()
        price = list()
        ti = list()

        for i, j, k, l in items:
            idx.append(i)
            menu.append(j)
            price.append(k)
            ti.append(l)

        table_data = list(zip(idx, menu, price, ti))
        table = tabulate(headers=head, tabular_data=table_data, tablefmt="rst")
        print(table)
        conn.commit()
        conn.close()

    def show_Bikaner(self):
        """Display menu for BIKANERWALA.
        """

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Bikaner")
        items = c.fetchall()
        head = ['INDEX', 'MENU', 'PRICE', 'PREPARATION TIME']
        idx = list()
        menu = list()
        price = list()
        ti = list()

        for i, j, k, l in items:
            idx.append(i)
            menu.append(j)
            price.append(k)
            ti.append(l)

        table_data = list(zip(idx, menu, price, ti))
        table = tabulate(headers=head, tabular_data=table_data, tablefmt="rst")
        print(table)

        conn.commit()
        conn.close()

    def show_Mongini(self):
        """Display menu for MONGINI-BAKERY.
        """

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Mongini")
        items = c.fetchall()
        head = ['INDEX', 'MENU', 'PRICE', 'PREPARATION TIME']
        idx = list()
        menu = list()
        price = list()
        ti = list()

        for i, j, k, l in items:
            idx.append(i)
            menu.append(j)
            price.append(k)
            ti.append(l)

        table_data = list(zip(idx, menu, price, ti))
        table = tabulate(headers=head, tabular_data=table_data, tablefmt="rst")
        print(table)
        conn.commit()
        conn.close()

    def show_Udupi(self):
        """Display menu for UDUPI.
        """

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Udupi")
        items = c.fetchall()
        head = ['INDEX', 'MENU', 'PRICE', 'PREPARATION TIME']
        idx = list()
        menu = list()
        price = list()
        ti = list()

        for i, j, k, l in items:
            idx.append(i)
            menu.append(j)
            price.append(k)
            ti.append(l)

        table_data = list(zip(idx, menu, price, ti))
        table = tabulate(headers=head, tabular_data=table_data, tablefmt="rst")
        print(table)

        conn.commit()
        conn.close()

    def show_Om(self):
        """Display menu for OM-SWEETS.
        """

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Om")
        items = c.fetchall()
        head = ['INDEX', 'MENU', 'PRICE', 'PREPARATION TIME']
        idx = list()
        menu = list()
        price = list()
        ti = list()

        for i, j, k, l in items:
            idx.append(i)
            menu.append(j)
            price.append(k)
            ti.append(l)

        table_data = list(zip(idx, menu, price, ti))
        table = tabulate(headers=head, tabular_data=table_data, tablefmt="rst")
        print(table)

        conn.commit()
        conn.close()
