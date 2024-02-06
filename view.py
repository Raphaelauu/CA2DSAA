from functions import functions
class view:
    def __init__(self):
        self.option = ''

    def main(self):
        while self.option != "6":
            menu = functions.read_text_file('menu.txt')
            print(menu)
            self.option = input("Enter choice: ")
            #if self.option == "1":
            #    options.option1()
            #elif self.option == "2":
            #    options.option2()
            #elif self.option == "3":
            #    options.option3()
            #elif self.option == "4":
            #    options.option4()
            #elif self.option == "5": 
            #    options.option5()
            if self.option == "6": 
                print('Bye, thanks for using ST1507 DSAA: Evaluating & Sorting Assignment Statements')
            else:
                print('Invalid choice. Please enter a valid option (1-6).\n')