class Relax:

    @staticmethod
    def relax(u, v, w):

        if v.get_distance() > u.get_distance() + w:
            v.set_distance(u.get_distance() + w)
            v.set_parent(u)