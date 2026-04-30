class test:
    def get_data(self):
        return dict()
    

obj1 = test()
print(obj1.get_data())


class panch(test):
    def get_data(self):
        dictionary = super().get_data()
        return ("data from parent class: ", dictionary)

obj2 = panch()
print(obj2.get_data())