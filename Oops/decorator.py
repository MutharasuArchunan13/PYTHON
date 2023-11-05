#In java it's came to the concept of  annotations

class language:
    def __init__(self,lang,version):
        self.lang=lang
        self.version=version
        #self.learn='he learn ',self.lang,'in version',self.version
    @property
    def current_status(self):
        return    'he learn {}:{}'.format(self.lang,self.version)

    @property
    def language(self):
        return self.lang
    @language.setter
    def language(self,name):
        self.lang=name

obj=language('python','3.10.3')
obj.lang='java'
obj.language='java script'
print(obj.current_status)
print(obj.language)

