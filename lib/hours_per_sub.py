total_hours_per_week = 39

class calculate_hours:
    labs = 0
    minor_subs = 0
    major_subs = 0
    """total hours per subject"""
    def calculate(self):
        total_hours_per_week = 39
        hours = ( total_hours_per_week- (self.labs*3 + self.minor_subs))/self.major_subs
        print(hours)
        per_sub = int(hours)
        extra = (hours % per_sub) * self.total_major_subs
        return per_sub, int(extra)+1