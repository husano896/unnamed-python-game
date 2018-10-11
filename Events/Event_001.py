import sys
sys.path.append('../')

from Game_System import Game_System

def Event_001():
    return [
        lambda: (Game_System.Event_Handler.Command_Message_WithName("事件運行測試", "明智")), 
        lambda: (Game_System.Event_Handler.Command_Message_WithName("欸超強欸這個", "名字")),
        lambda: (Game_System.Event_Handler.Command_Message_WithName("真的\n換行測試\n再換行測試\n換很多行測試", "名字三明治")),
        lambda: (print("Event_001 Complete."))
    ]
