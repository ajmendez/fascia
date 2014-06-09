'''earth.py: get the clouds + earth image 
May 2014 -- Mendez

http://flatplanet.sourceforge.net/maps/night.html
http://flatplanet.sourceforge.net/maps/natural.html
http://wiki.birth-online.de/know-how/software/linux/xplanet

http://www.fourmilab.ch/fourmilog/archives/Monthly/2005/2005-05.html

http://mathematica.stackexchange.com/questions/3326/composition-how-to-make-a-day-and-night-world-map

'''

URL = 'http://xplanet.sourceforge.net.nyud.net:8080/clouds/tmp/201405310046.765843/clouds_2048.jpg'


class Earth(object):
    """Determine earth imaging"""
    def __init__(self):
        pass
    
    def update(self):
        pass
    
    def display(self):
        pass
    


def plot():
    import numpy as np
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
    from datetime import datetime
    # miller projection
    # map = Basemap(projection='mill',lon_0=180)
    map = Basemap(projection='kav7',lon_0=180)
    
    # plot coastlines, draw label meridians and parallels.
    map.drawcoastlines()
    map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
    # fill continents 'coral' (with zorder=0), color wet areas 'aqua'
    map.drawmapboundary(fill_color='aqua')
    map.fillcontinents(color='coral',lake_color='aqua')
    # shade the night areas, with alpha transparency so the
    # map shows through. Use current time in UTC.
    date = datetime.utcnow()
    CS=map.nightshade(date)
    plt.title('Day/Night Map for %s (UTC)' % date.strftime("%d %b %Y %H:%M:%S"))
    plt.show()



if __name__ == '__main__':
    # e = Earth()
    plot()
