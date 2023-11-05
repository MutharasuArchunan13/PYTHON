#there is three types of method available in python
#instance or regular method\

class study:
    """ If you want to access the method you have instance of a class otherwise you can't"""
    def __init__(self,status):
        self.status=status

    def start(self):
        return self.status

    semester_start='next monday'
    #class method is alternative constructor because you access the class data without crearting through this
    @classmethod
    def change(cls,status):
        study.semester_start=status

    #static methods are use for there in no bound,that's don't receive any arguments we can use classname directly access that
    @staticmethod
    def direct_change():
        return 'this is static king'

study_status=study('started')

print(study_status.start())
study.change('next tuesday')
print(study.semester_start)

print(study.direct_change())



