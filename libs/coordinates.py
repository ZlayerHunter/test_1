import math
import re
from .utils import res_to_grad


class Coordinates:
    def __init__(self, lat=None, lon=None):
        self.set_coordinates = [lat, lon]
    
    @property
    def get_coordinates(self):
        return self._coordinates

    @property
    def get_lon(self):
        return self._coordinates[1]

    @property
    def get_lat(self):
        return self._coordinates[0]
    
    @get_coordinates.setter
    def set_coordinates(self, coord):
        def set_coord(coord: str) -> float:
            match_3 = re.compile('''(\d+)°(\d+)'(\d+|\d+.\d+)"''')
            match_1 = re.compile('''(\d+)° (\d+)' (\d+|\d+.\d+)"''')
            match_2 = re.compile("(\d+) (\d+) (\d+.\d+|\d+)")
            if res := match_1.match(coord):
                res = res_to_grad(res)
            elif res := match_2.match(coord):
                res = res_to_grad(res)
            elif res := match_3.match(coord):
                res = res_to_grad(res)
            return res
        result = []
        for elem in coord:
            if not isinstance(elem, (int, float, str)):
                raise AttributeError('''Input integer or string like DD.DDDDD or DD MM SS or DD° HH' SS"''')
            if isinstance(elem, (int, float)):
                result.append(elem)
            elif isinstance(elem, str):
                result.append(set_coord(elem))
        self._coordinates = result

    def __str__(self):
        return "Lat: {:.4f}, Lon: {:.4f}"\
                .format(*self._coordinates)

    def __sub__(self, obj):
        def get_dist(p_start, p_end):
            earth_radius = 6371000
            d_lat = math.radians(p_end.get_lat - p_start.get_lat)
            d_lon = math.radians(p_end.get_lon - p_start.get_lon)
            s_lat_r = math.radians(p_start.get_lat)
            e_lat_r = math.radians(p_end.get_lat)
            part_1 = math.sin(d_lat/2)**2
            part_2 = math.cos(s_lat_r) * math.cos(e_lat_r)
            part_3 = math.sin(d_lon/2)**2
            distance = part_1 + part_2 * part_3
            distance = 2 * math.atan2(distance**(0.5), (1 - distance)**(0.5))
            distance *= earth_radius
            return distance
        result = get_dist(self, obj)
        return result
