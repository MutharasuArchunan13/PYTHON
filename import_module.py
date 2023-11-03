print("the module will be successfully imported")

def find_index(collections,target_value):
     """ To find the index value"""
     for index,value in enumerate(collections):
         if value == target_value:
     
            return index
 
     return 'target not found'