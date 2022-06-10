class FindSet:

    @staticmethod
    def find_set(s, x):
    
        target = None
        for e in s.s:
            if x in e:
                target = e
        return target