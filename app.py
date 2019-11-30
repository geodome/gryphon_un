#!/bin/python3
import slack
from config import token
from parser import Parser
from chairperson import chairperson
from memberstate import memberstate

def GetChairParser(chairperson):
    p = Parser()
    p.addCommand("open session", chairperson.open_session)
    p.addCommand("close session", chairperson.close_session)
    p.addCommand("resume session", chairperson.resume_session)
    p.addCommand("table session", chairperson.suspend_session)
    p.addCommand("take attendance", chairperson.take_attendance)
    p.addCommand("open floor", chairperson.open_floor)
    p.addCommand("close floor", chairperson.close_floor)
    p.addCommand("add member <str> <str>", chairperson.add_member)
    p.addCommand("del motion <str>", chairperson.del_motion)
    p.addCommand("start timer <str> <str>", chairperson.start_timer)
    p.addCommand("set agenda <*>", chairperson.set_agenda)
    p.addCommand("close agenda", chairperson.close_agenda)
    return p 

def GetMemberStateParser(member):
    p = Parser()
    p.addCommand("present", member.present)
    p.addCommand("present and voting", member.present_and_voting)
    p.addCommand("point of personal privilege", member.point_of_personal_privilege)
    p.addCommand("point of order", member.point_of_order)
    p.addCommand("point of inquiry", member.point_of_enquiry)
    p.addCommand("right of reply", member.right_of_reply)
    p.addCommand("motion to close debate", member.motion_to_close_debate)
    p.addCommand("motion to table debate", member.motion_to_table_debate)
    p.addCommand("motion to resume debate", member.motion_to_resume_debate)
    p.addCommand("motion to introduce amendment <*>", member.motion_to_introduce_amendment)
    p.addCommand("motion to introduce working paper", member.motion_to_introduce_working_paper)
    p.addCommand("motion to introduce unmoderated caucus", member.motion_to_introduce_unmoderated_caucus)
    p.addCommand("motion to introduce moderated caucus", member.motion_to_introduce_moderated_caucus)
    p.addCommand("motion to change speaking time", member.motion_to_change_speaking_time)
    p.addCommand("motion to reorder draft resolutions", member.motion_to_reorder_draft_resolutions)
    p.addCommand("motion to divide the question", member.motion_to_divide_the_question)
    p.addCommand("motion to roll call", member.motion_to_roll_call)
    return p

def NewSession(chair):
    chairperson = ChairPerson(chair)
    chairparser = GetChairParser(chairperson)
    session = {}
    session["chairperson"] = ChairPerson(chair)
    session["parser"] = []
    session["memberstates"] = {"chairperon": MemberState(chair, "chair")}
    session["agenda"] = ""
    return session

def isMemberState(user):
    global session
    return user in session["memberstates"].keys()

@slack.RTMClient.run_on(event='message')
def chairperson_commands(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if session["chairperson"].isUser(data['user']):
        command = data.get('text', []).split()
        p = GetChairParser(session["chairperson"])
        msg1, msg2 = p.exec(command)
        channel_id = data['channel']
        thread_ts = data['ts']
        web_client.chat_postMessage(
            channel=channel_id,
            text=msg1,
            thread_ts=thread_ts
        )        
        web_client.chat_postMessage(
            channel="#general",
            text=msg2,
        )        

@slack.RTMClient.run_on(event='message')
def memberstate_commands(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if isMemberState(data['user']):
        command = data.get('text', []).split()
        p = GetMemberStateParser(data["user"])
        msg1, msg2 = p.exec(command)
        channel_id = data['channel']
        thread_ts = data['ts']
        web_client.chat_postMessage(
            channel=channel_id,
            text=msg1,
            thread_ts=thread_ts
        )        
        web_client.chat_postMessage(
            channel="#general",
            text=msg2,
        )        

session = NewSession(chair = "Donaldson Tan")
rtm_client = slack.RTMClient(token=token)
rtm_client.start() 

