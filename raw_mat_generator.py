"""
Raw material 'bundles' and generatoers.

raw_mat_collection:
    name: string
    count: int
    cycle_created: int

raw_mat_manager:
    name: string
    produce_per_cycle: int
    ttl: int
    collection: list
    
    prod_cycle(): add a raw_mat_collection to the end of the self.collection
    rem_cycle(): remove raw_mat_collection older than ttl from self.collection
    cycle(current_cycle_no): calls prod_cycle and rem_cycle
    consume(amount_to_consume): tries to "consume" that amount and returns the attempt.  silently fails and just returns whatever it can get.
"""

class raw_mat_collection:
    def __init__(self, p_name="", p_count=0, p_cycle_created=0):
        self.name = p_name
        self.count = p_count
        self.cycle_created = p_cycle_created
    def __str__(self):
        return str((self.name, self.count, self.cycle_created))
    

class raw_mat_manager:
    """
    todo: implement sort on age by default instead of sorting by 
            whatever it'll sort right now.  If it sorts at all...
    """
    
    def __init__(self, p_name="", p_produce_per_cycle=0, p_ttl=0):
        self.name = p_name
        self.produce_per_cycle = p_produce_per_cycle
        self.ttl = p_ttl
        self.collection = []
    
    def prod_cycle(self, p_cycle_no=0):
        self.collection.append(raw_mat_collection(self.name,self.produce_per_cycle, p_cycle_no))
    
    def rem_cycle(self, p_cycle_no=0):
        for i in self.collection:
            if (p_cycle_no - i.cycle_created) > self.ttl:
                self.collection.remove(i)
    
    def cycle(self, p_cycle_no=0):
        self.rem_cycle(p_cycle_no)
        self.prod_cycle(p_cycle_no)
        
    
    def consume(self, p_count=0):
        to_consume = []
        to_mod = {}
        curr_needed = p_count
        gathered = 0
        i = 0
        ii = None
        try:
            while curr_needed > 0:
                ii = self.collection[i]
                if ii.count - curr_needed > 0:
                    to_mod[ii] = ii.count - curr_needed
                    gathered = gathered + curr_needed
                    curr_needed = 0
                else:
                    to_consume.append(ii)
                    gathered = gathered + ii.count
                    curr_needed = curr_needed - ii.count
                i = i + 1
        except:
            pass
        for i in to_consume:
            try:
                self.collection.remove(i)
            except:
                pass
        for i in to_mod.keys():
            i.count = to_mod[i]
        return gathered
    
    












