class FairGroupper(object):
    def __init__(self, names):
        self.names = names
        self.weight = {}
        for k in names:
            self.weight.setdefault(k)
            self.weight[k]=0

    def random_group(self, group_count):
        pass
