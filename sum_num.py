class ListOfNumbers(object):

    def __init__(self, numbers=[]):
        self.num_list = numbers
        self.sum = None
        self.max_diff = None

    def sum_numbers(self):
        """ returns the sum of numbers in an inputted list

        :param numlist: list of values – each entry will be added up
        :returns: sum of each entries from input num_list
        :raises: TypeError
        :raises: ValueError
        :raises: ImportError
        """

        try:
            import logging
        except ImportError:
            logging.error("There is an ImportError")
            print("Requested import file does not exist.")

        logging.basicConfig(filename='divlog.txt',
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)

        if len(self.num_list) == 0:
            logging.warning("num_list is empty")

        sum = 0
        try:
            for num in self.num_list:
                self.sum = self.sum + num
        except TypeError:
            logging.error("There is a TypeError")
            print("num_list must be a list containing variable type entries.")
        except ValueError:
            logging.error("There is a ValueError")
            print("The entries list must consist only of real numbers.")

        logging.info("All entries successfully added up.")

        return sum

    def MaxDiff(self):
        """ returns the MaxDiff value

        :param:  num_list: list of values
        :param:  i : the index in num_list
        :param:  j : the index i + 1 in num_list
        :returns: return the max two adjacent diff value from input num_list
        :raises: ImportError
        :raises: TypeError
        :raises: ValueError
        """

        try:
            import logging
        except ImportError:
            logging.error("No such file")
            print("No Imported file")

        logging.basicConfig(filename='divlog.txt',
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)

        if len(self.num_list) == 0:
            logging.warning('This is not a list')

        try:
            self.max_diff = self.num_list[1] - self.num_list[0]
            i = 0
            j = i + 1
            for i in self.num_list:
                for j in self.num_list:
                    if (j - i > self.max_diff):
                        self.max_diff = j - i
            return self.max_diff
        except TypeError:
            pass
        except ValueError:
            pass
        logging.info('Status quo')

    def findextremes(self):
        """ returns the smallest and largest elements in an inputted list
        :param: num_list
        :returns: the smallest and largest elements in input num_list
        :raises: TypeError: Input list must not be empty
        :raises: ValueError: Numbers in list must be real numbers
        :raises: ImportError: Numpy must be installed in Env
        """

        # Set up logger
        import logging
        log_format = '%(levelname)s %(asctime)s %(message)s'
        logging.basicConfig(filename='divlog.txt', format=log_format,
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG, filemode='w')
        logger = logging.getLogger()
        # Make sure list criteria are met
        try:
            self.check_input(self.num_list)
        except ValueError:
            logging.error('Input must be a list composed of real, '
                          'numeric entries')
            quit()
        except TypeError:
            logging.error('Input must be list with entries')
            quit()
        try:
            import numpy as np
        except ImportError:
            logging.error('Numpy must be installed in your local environment!')
        logger.info("# Find Minimum and Maximum")
        logger.debug('Input: %s', str(self.num_list))
        minimum = np.min(self.num_list)
        maximum = np.max(self.num_list)
        logging.info("# Return Minimum and Maximum")
        logger.debug('Output:%s,%s', str(minimum), str(maximum))
        return [minimum, maximum]

    def contains_imaginary(self):
        '''Checks if input contains imaginary numbers
        :param: num_list
        :returns: Boolean indicating if the input contains imaginary numbers
        '''
        import numpy as np
        is_real = np.isreal(self.num_list)
        if False in is_real:
            imaginary_elements = True
        else:
            imaginary_elements = False
        return imaginary_elements

    def check_list(self):
        '''Checks if input is a list
        :param: num_list
        :returns: Boolean indicating if the input data type is a list'''
        if type(self.num_list) == list:
            list_input = True
        else:
            list_input = False
        return list_input

    def check_input(self):
        '''Checks if the input meets all of the criteria required of minmax.py
         :param: num_list
         :raises: TypeError: If the input is not a list
         :raises: TypeError: If the input list has no entries
         :raises: ValueError: If the input list contains imaginary elements'''
        # Check that input is a list
        if self.check_list(self.num_list) is False:
            raise TypeError('Input must be a list')
        # Check that list has entries
        if len(self.num_list) == 0:
            raise TypeError('Input list is empty')
        # Check for imaginary numbers in list
        if self.contains_imaginary(self.num_list) is True:
            logging.error('Input list contains imaginary elements')
            raise ValueError('Input list contains imaginary elements!')
