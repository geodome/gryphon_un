#!/bin/python3

class member:

    def __init__(self,nickname,country):       ##nickname and country are all in string
        self.nickname = nickname
        self.country = country
        self.role = ""
        self.isVoting = None
        self.yes = 0
        self.no = 0
        self.total_motion = 0
        

    def present(self):
        self.isVoting = False
        self.role = "present"
        return (self.country + " is not voting", self.country + " is not voting") 

    def present_and_voting(self):
        self.isVoting = True
        self.role = "present and voting"
        return (self.country + " is voting", self.country + " is voting")

    def role_call(self, decision):
        decision = decision.lower()

        if Chairperson.rolecall() == True:
            if decision == "present":
                self.role = "present"
                return (self.role, self.role)

            elif decision == "present and voting":
                self.role = "present and voting"
                return (self.role, self.role)
            
    def point_of_personal_privilege(self):
        if self.canVoteSubstantive == True:
            #ret = True
            return (self.country + " has the rights to request",self.country + " has the rights to request" )

        else:
            #ret = False
            return (self.country + " has no rights to request",self.country + " has no rights to request" )



    def canVoteSubstantive(self):
        '''
        Checks if the member is allowed to vote for substantive votes or not
        '''
        if self.isVoting == False:
            ret = False

        elif self.isVoting == True:
            ret = True
        return ret 
        
    def vote(self,option):
        option = option.lower()
        if option == "yes":
            self.yes += 1 
            return ("You have voted yes", "")         ##(member, other member)

        elif option == "no":
            self.no += 1 
            return ("You have voted no", "")


    def view_status(self,country):
        global session 

        if session[members['country']] == True:
            return self.role

        else:
            return "Absent"
            

    def point_of_order(self):
        if self.canVoteSubstantive == True:
            #ret = True
            return (self.country + " has the rights to order",self.country + " has the rights to order" )

        else:
            #ret = False
            return (self.country + " has no rights to order",self.country + " has no rights to order" )


        
    def point_of_enquiry(self):
        if self.canVoteSubstantive == True:
            #ret = True
            return (self.country + " has the rights to enquire",self.country + " has the rights to enquire" )
            
        else:
            #ret = False
            return (self.country + " has no rights to enquire",self.country + " has no rights to enquire" )

    

    def right_of_reply(self):
        if self.canVoteSubstantive == True:
            #ret = True
            return (self.country + " has the rights to reply",self.country + " has the rights to reply" )

        else:
            #ret = False
            return (self.country + " has no rights to reply",self.country + " has no rights to reply" )


    def motion_to_close_debate(self):
        if self.canVoteSubstantive == True:
            #ret = True
            return (self.country + " has the rights to close debate",self.country + " has the rights to close debate" )

        else:
            #ret = False
            return (self.country + " has no rights to close debate",self.country + " has no rights to close debate" )        

    def motion_to_table_debate(self):
        if self.canVoteSubstantive == True:
            #ret = True
            return (self.country + " has the rights to table debate",self.country + " has the rights to table debate" )

        else:
            #ret = False
            return (self.country + " has no rights to table debate",self.country + " has no rights to table debate" )  

    def motion_to_resume_debate(self):
        if self.canVoteSubstantive == True:
            #ret = True
            return (self.country + " has the rights to resume debate",self.country + " has the rights to resume debate" )

        else:
            #ret = False
            return (self.country + " has no rights to resume debate",self.country + " has no rights to resume debate" )  




    def motion_to_introduce_amendment(self,arg):
        return ""

    def motion_to_introduce_working_paper(self):
        return ""



    def motion_to_introduce_unmoderated_caucus(self):
        return ""
    
    def motion_to_introduce_moderated_caucus(self):
        return ""

    def motion_to_change_speaking_time(self):
        return ""

    def motion_to_reorder_draft_resolutions(self):
        return ""

    def motion_to_divide_the_question(self):
        return ""

    def motion_to_roll_call(self):
        return ""

    def voting_result(self):
        '''
        Find out whether the vote is a majority or not
        '''
        total = self.yes + self.no
        majority = self.yes/total

        if majority>0.5 and majority<=1:
            ret = "Majority says yes"
            return ret                                 #(chairperson, member)

        elif majority>0 and majority<0.5: 
            ret = "Majority says no"
            return ret

        elif majority == 0.5:
            ret = "Its a tie"
            return ret

        else:
            ret = "Error in calculating the majority"
            return ret

        
    def submit_motion(self,motion):
        self.total_motion += 1 
        return (Motion + " is submitted by " + self.country, "Motion submitted")

    def main_agenda(self):
        global session 
        return session['agenda']

    def sub_agenda(self):
        global session 
        return session['sub_agenda']




