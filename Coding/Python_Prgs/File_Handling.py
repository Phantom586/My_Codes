class Editor(object):
    """
        Parameters : f_name
        f_name = File Name with its Extension

    """
    print('Welcome to My Editor !!!')

    def __init__(self, f_name):
        self.f_name = f_name

    def Read_File(self):
        """
        Parameters : None
        Description :
            Displays the Content of the File.

        """
        with open(self.f_name) as f:
            for line in f:
                print(line, end='')

    def Extract_Data(self):
        """
        Parameters : None
        Description :
            Extracts the Data of the File in a List.

        """
        data = []
        with open(self.f_name) as f:
            for line in f:
                data.append(line)
        return data

    def Edit_File(self, string='', append=False, delete=False, line_no=0):
        """
            Parameters :
                string = [' '(Default)] The String to be Appended in the File.
                append = [False(Default)] To Append a string in the File.
                delete = [False(Default)] to Delete a Specific line from the File.
                line_no = [0(Default)]

            Description :
                line_no = No. of the Line you want to Delete.
                Helps you in Deleting the Unwanted Text from the File.

        """
        temp_data = []
        if append == True:
            with open(self.f_name, 'a') as f:
                f.write('\n')
                f.write(string)
        elif delete == True:
            with open(self.f_name) as f:
                for line in f:
                    temp_data.append(line)
            del (temp_data[line_no])
            with open(self.f_name, 'w+') as f:
                for i in temp_data:
                    f.write(i)

        with open(self.f_name) as f:
            for line in f:
                print(line, end='')
