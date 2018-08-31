"""
'actions' represent things that agents can do in a cell,
provided the agent can meet the cost. 

todo: lots
"""

class action:
    types = [
        "get_raw_mats",
        "store_raw_mats",
        "consume_mats"
    ]
    def __init__(self, p_action_type="get_raw_mats"):
        self.action_type = p_action_type
    
    def take_action(self, p_actor):
        pass
    
    def check_costs(self, p_actor):
        pass
    
