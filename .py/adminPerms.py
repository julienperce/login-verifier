class AdminPerms():
    def __init__(self, hasAll, canRead, canWrite):
        self.hasAll = hasAll
        self.canRead = canRead
        self.canWrite = canWrite
    
    def sayPerms(self):
        print(f"I have the following perms, {self.hasAll}, {self.canRead}, {self.canWrite}")
    
    
admin1 = AdminPerms(True, True, True)
admin2 = AdminPerms(False, True, False)
