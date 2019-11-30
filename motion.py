

class motion:
    d = [('Point of Personal Privilege', 10), ('Point of Order', 20), ('Point of Parliamentary Inquiry', 30),
     ('Motion for Closure of the Debate', 40), ('Motion for Closure of the Debate', 50), ('Motion to Table the Debate', 60),
     ('Motion for Adjournment of the Meeting', 70), ('Motion for Suspension of the Meeting', 80), ('Motion to Resume Debate', 90),
     ('Motion to Introduce an Amendment', 100), ('Motion to Introduce a Working Paper', 110), ('Motion for Un-moderated Caucus', 120),
     ('Motion for Moderated Caucus', 130), ('Motion to Change the Speaking Time', 140), ('Motion to Open the Speaker´s List', 150),
     ('Motion to Reorder Draft Resolutions', 160), ('Motion to Divide the Question', 170), ('Motion for the Roll Call', 180)]

    def __init__(self):
        self.motions = []
        self.final = []

    def add_motion(self, item):
        self.motions.append(item)
        
    def sort_motion(self, lst):
        '''
        Sorts motions according to order of precedence.
        @parameter: list of motions
        @returns: sorted list of motions
        '''
        sorted_list = []
        for i in lst:
            for j in range(len(d)):
                if i in d[j]:
                    sorted_list.append(d[j][1])
        sorted_list.sort()
        for i in sorted_list:
            for j in range(len(d)):
                if i in d[j]:
                    self.final.append(d[j][0])            
        return self.final
                
    def delete(self, index):
        '''
        Delete motions based on their index (1st element is 1).
        @parameters: index to be removed
        '''
        self.final.pop(index-1)
        




