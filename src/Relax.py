class Relax:

    @staticmethod
    def relax(u, v, w):

        if v.distance > u.distance + w:
            v.distance = u.distance + w
            v.parent = u