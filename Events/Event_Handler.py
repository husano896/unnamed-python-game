import sys
sys.path.append('../')
from Game_System import Game_System
from Window_Message import Window_Message
from Window_Message_WithName import Window_Message_WithName
class Event_Handler:
    #Parallel_Events = []
    Current_Event = None
    Event_Pause = False
    Event_Counter = 0

    def Complete_Check(self):
        if (len(self.Current_Event) == self.Event_Counter):
            self.Current_Event = None
            self.Event_Counter = 0
            self.Event_Pause = False

    def Run_Event(self,ev):
        if (not self.Current_Event == None):
            print("Currently running event, aborted")
            print(ev)
            return
        self.Current_Event = ev
        self.Event_Counter = 0
        
        self.Continue_Event()
        
    def Continue_Event(self):
        if (self.Current_Event == None):
            print("Continuing no event, probably bug?")
            return
        
        self.Event_Pause = False
        while ((not self.Event_Pause) and self.Event_Counter < len(self.Current_Event)):
            self.Current_Event[self.Event_Counter]()
            
            self.Event_Counter +=1
        self.Complete_Check()
    
    def Command_Message(self, text = ""):
        return Window_Message(text = text)
    
    def Command_Message_WithName(self, text = "", name = "", FaceSet = {}):
        return Window_Message_WithName(text, name, FaceSet)

Game_System.Event_Handler = Event_Handler()
