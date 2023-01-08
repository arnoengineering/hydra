import numpy as np

r = 6371  # ave rad


def hav(x):
    return np.sin(x/2)**2


def lat_pars(la):
    p1 = [np.deg2rad(float(x)) for x in la.split(', ')]
    return p1


def hav_dist(p01_s, p02_s):
    p01 = lat_pars(p01_s)
    p02 = lat_pars(p02_s)
    d = np.arcsin(np.sqrt(hav(p02[0]-p01[0])+np.cos(p01[0])*np.cos(p02[0])*hav(p02[1]-p01[1])))*r*2
    print(d)
    return d


def drop_dist(dist):
    angle = dist/r
    print('angle ', angle)
    if angle >= np.pi/4:
        print('to far')
        return 0
    else:
        eq_drop = np.sqrt(2 * r**2 - 4 * r * np.cos(angle))*np.sin(angle)
        print('Equivilent Drop ', eq_drop)
        return eq_drop


def drop_angle(p01_s, p02_s):
    d = hav_dist(p01_s, p02_s)
    drop_dist(d)


def plot_d(p1, p2):
    # todo plot points--> then arc betwwen show angle, show rel drop, on eartth
    pass


p01_s1 = "-33.587991, 22.187726"  # SOH
p02_s1 = '53.527410, -113.528481'  # entrance to etlc
hav_dist(p01_s1, p02_s1)
