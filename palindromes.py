#Global variable
month_days_dict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

class Palindromes:
    """
    Creates a list of all palindromes in an input century

    Attributes
    ----------
    century : int
        century to find palindromes in
    pal_list : list
        list of palindromes
    only_month: int
        only possible month that could have a palidrome for a given century
    years: list
        only possible years for there to be a palidrome in
    """

    def __init__(self, century):
        """
        instantiate the class with century
        """
        self.century = int(century)

    def get_palindromes(self):
        """
        create list of palidromes, sequences necessary functions
        """

        self.get_possible_years()
        self.pal_list =  self.check_for_palidromes()

    def write_palindromes_list(self):
        """
        write all palidromes in data format in a new line to a text file
        """

        infile = open('palindromes_' + str(self.century) + '.txt', 'w')
        for pal in self.pal_list:
            infile.write(pal+'\n')
        infile.close()


    def get_possible_years(self):
        """
        determine all possible years that a palidrome could be in
        """
        self.only_month = int(str(self.century)[:2][::-1])

        years = []
        if self.only_month < 13:
            for day in range(1, month_days_dict[self.only_month]+1): # iterate through all the days in the only month to determine possible years
                years.append(day + self.century)
        
        self.years = years

    def check_for_palidromes(self):
        """
        using the base of the years list, reverse those years and check if any of those values are palidromes
        """

        pal_list = []

        for year in self.years:
            pal = str(year)[::-1] + str(year) #reverse the year string to create possible palidrome
            day = pal[0:2] #subset the string by each part of the date
            month = pal[2:4] 
            year = pal[4:]

            if int(day) <= month_days_dict[int(self.only_month)]: #check dictionary to see if palidromes days are valid for the month of the date
                pal_str = day + '/' + month + '/' + year #recreate the date string
                pal_list.append(pal_str)

        return pal_list



palObj = Palindromes(4000)
palObj.get_palindromes()
palObj.write_palindromes_list()



