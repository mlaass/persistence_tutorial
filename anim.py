from manimlib.imports import *
import shapely.wkt as wkt
from shapely.geometry import LineString
import json
import math

#lss = "LINESTRING (8.88 1608, 10.17 1608, 12.87 1608.3, 16.21 1608.57, 22.81 1608.95, 29.83 1609.28, 37.68 1609.6, 46.44 1609.93, 57.64 1610.3, 69.47 1610.58, 78.1 1610.53, 88.69 1610, 101.07 1608.4, 109.79 1606.6, 121.67 1603.4, 133.21 1599.42, 141.53 1596.05, 153 1590.92, 162.64 1586.1, 173.64 1582.12, 181.47 1582.13, 191.33 1582.33, 203.48 1582.91, 214.04 1583.51, 226.36 1584.2, 235.16 1584.7, 247.47 1585.34, 259.71 1585.5, 267.78 1584.42, 277.41 1581.02, 283.99 1576.41, 288.35 1571.68, 292.86 1563.76, 295.4 1556.06, 297.51 1547.87, 298.79 1543.07, 300.43 1536.84, 301.2 1533.72, 301.95 1530.37, 302.32 1528.2, 302.46 1527.36, 302.49 1527.13, 302.49 1527.13, 301.71 1526.92, 299.94 1526.49, 295.77 1525.49, 291.6 1524.5, 284.32 1522.91, 277.32 1521.58, 268.76 1520.02, 262.11 1518.81, 254.6 1517.47, 249.24 1516.51, 242.26 1515.26, 234.95 1513.97, 226.14 1512.74, 216.94 1511.92, 210.51 1511.45, 202.71 1510.79, 196.13 1510.21, 189.6 1509.66, 185.14 1509.89, 183.81 1511.07, 185.29 1513.16, 187.79 1515.08, 191.25 1517.3, 194.4 1519.28, 196.17 1520.35, 197.06 1520.86, 197.19 1520.93, 197.2 1520.93, 198.17 1521.49, 200.55 1521.88, 204.82 1521.88, 209.39 1521.88, 213.24 1521.88, 215.79 1521.88, 218.07 1521.88, 219.62 1521.88, 220.02 1521.88, 220.02 1521.88, 220.84 1521.88, 222.41 1521.91, 225.78 1523.02, 227.49 1523.7, 229.57 1524.58, 230.41 1525.01, 230.51 1525.06, 230.51 1525.06, 230.51 1525.06, 230.51 1525.06, 230.51 1525.06, 230.51 1525.06, 230.51 1525.06, 230.51 1525.06, 230.51 1525.06, 230.51 1525.06, 229.8 1525.84, 227.57 1528.09, 224.8 1530.78, 221.5 1533.49, 216.94 1536.37, 212.22 1537.2, 206.65 1535.7, 202.68 1534.41, 196.53 1532.74, 190.48 1531.14, 186.84 1530.21, 184.09 1529.68, 183.06 1530.54, 184.65 1533.3, 186.69 1536.05, 190.87 1541.22, 196.36 1547.59, 200.95 1552.77, 207.01 1559.48, 214.77 1568.02, 220.66 1574.43, 229.01 1583.5, 234.97 1589.97, 243.4 1599.03, 252.38 1607.49, 261.98 1613.04, 268.85 1614.87, 276.52 1614.89, 284.11 1612.4, 289.1 1608.38, 292.45 1603.14) "
# lss = "LINESTRING (8 1672, 8.2 1670.4, 3.89 1669.92, 1.13 1668.45, -1.38 1668.87, -0.98 1667, 1.25 1665.37, 5.08 1664.72, 10.39 1663.91, 16.96 1662.88, 24.51 1661.55, 25.87 1660.02, 25.87 1657.78, 25.87 1655.55, 25.87 1652.71, 25.87 1649.09, 25.87 1644.51, 26 1637.89, 26.27 1631.38, 25.93 1624.1, 24.73 1617.95, 21.69 1608.52, 17.92 1603.05, 12.98 1598.99, 8.06 1596.51, 0.09 1594.27, -7.44 1593.32, -17.05 1593.18, -26.1 1593.76, -37.41 1595.15, -47.71 1596.82, -60.18 1597.51, -71.05 1596.8, -80.11 1595.43, -92.64 1592.69, -103.09 1589.81, -113.31 1586.52, -123.32 1583.08, -135.01 1579.1, -145.15 1577.17, -156.92 1578.48, -166.97 1580.88, -177.07 1584.16, -189.43 1588.13, -200.51 1591.53, -213.45 1595.5, -224.53 1598.91, -236.9 1602.93, -246.06 1605.64, -260.59 1608.83, -271.41 1610.55, -282.19 1611.87, -291.15 1612.7, -301.92 1613.73, -314.42 1614.61, -326.87 1615.11, -337.52 1615.23, -346.37 1615.19, -358.73 1614.87, -369.29 1614.42, -381.61 1613.86, -392.18 1613.36, -404.5 1612.72, -413.31 1612.22, -423.87 1611.62, -436.19 1610.83, -446.74 1610.14, -459.06 1609.33, -467.86 1608.75, -478.41 1608.06, -490.73 1607.21, -494.25 1606.93, -513.58 1605.06, -525.85 1603.64, -536.36 1602.41, -545.52 1601.3, -549.46 1600.83, -558.24 1599.87, -564.23 1599.11, -570.63 1598.1, -577.37 1596.93, -586.39 1595.22, -594.93 1593.53, -604.05 1591.83, -612.04 1590.42, -621.69 1588.73, -631.39 1587.04, -642.98 1585.07, -653.14 1583.39, -663.49 1581.7, -675.66 1579.74, -686.08 1578.06, -698.25 1576.09, -706.94 1574.69, -719.1 1572.73, -729.52 1571.04, -741.67 1569.08, -753.83 1567.12, -762.51 1565.72, -772.93 1564.04, -785.1 1562.08, -793.79 1560.67, -805.95 1558.71, -814.64 1557.31, -826.87 1555.34, -837.3 1553.65, -849.47 1551.59, -858.14 1549.92, -870.28 1547.22, -882.48 1544.05, -891.38 1541.61, -904.11 1537.96, -915.32 1534.52, -924.89 1531.43, -940.6 1526.06, -950.67 1522.36, -965.1 1516.5, -977.65 1510.85, -992.29 1503.53, -1004.83 1496.63, -1017.37 1489.16, -1031.44 1479.77, -1040.08 1472.46, -1050.44 1461.53, -1057.93 1452.01, -1064.38 1443.42, -1069.96 1435.5, -1075.31 1425.52) "
lss = "LINESTRING (200.94 1672, 202.28 1672, 204.66 1672, 208.67 1672, 214.32 1671.99, 222.47 1671.99, 228.98 1671.99, 238.96 1671.98, 248.22 1671.97, 259.61 1671.87, 269.66 1671.22, 281.42 1668.97, 289.47 1666.18, 299.37 1659.94, 308.04 1652.21, 313.52 1646.01, 320.39 1636.2, 324.84 1628.51, 330.4 1617.11, 333.93 1608.84, 338.51 1597.19, 341.54 1588.82, 346 1575.35, 349.39 1563.22, 351.29 1554.35, 352.78 1541.8, 352.98 1532.74, 352.3 1519.98, 351.34 1511.01, 349.4 1498.58, 347.74 1486.15, 347.5 1477.12, 348.28 1464.37, 349.72 1453.42, 352.1 1440.97, 355.03 1428.77, 357.36 1420.16, 360.4 1409.94, 363.12 1398.05, 364.18 1387.59, 364.26 1378.7, 363.58 1366.24, 362.13 1353.78, 360.37 1343.15, 358.68 1334.37, 355.99 1322.2, 352.92 1310.18, 349.98 1299.98, 346.26 1288.18, 343.46 1279.81, 342.31 1276.47, 335.7 1258.22, 331.99 1248.3, 327.65 1236.73, 323.32 1225.16, 320.83 1216.79, 318.72 1204.58, 317.88 1195.68, 317.65 1192.08, 317.36 1186.73, 316.55 1160.29, 316.24 1151.49, 315.95 1146.18, 315.02 1133.84, 312.54 1115.98, 310.66 1107.05, 309.32 1101.74, 305.64 1089.64, 301.36 1077.92, 296.71 1066.46, 296.71 1066.46, 284.49 1049.21, 279.59 1045.19, 269.91 1039.31, 263.91 1036.52, 246.08 1030.12, 241.06 1028.42, 229.02 1024.44, 229.02 1024.44, 202.78 1015.92, 193.94 1013.08, 181.56 1009.11, 181.56 1009.11, 160.35 1002.29, 151.51 999.45, 139.13 995.47, 139.13 995.47, 115.91 988.33, 104.79 985.44, 91.45 983.14, 77.71 983.43, 65.63 983.99, 53.25 984.84, 39.03 987.11, 25.97 990.95, 18.87 993.5, 7.05 998.41, -4.27 1003.75, -15.23 1009.46, -21.5 1012.72, -32.79 1017.86, -42.55 1020.61, -53.4 1021.34, -56.41 1021.16, -66.79 1019.25, -80.1 1014.05, -90.46 1008.28, -91.94 1007.36, -102.26 1000.31, -111.22 994.56, -126.73 986.22, -134.11 981.8, -143.33 974.61, -144.55 973.48, -154.99 957.26, -155.85 953.24, -156.03 943.6, -153.67 932.12, -150.56 923.2, -147.32 915.61, -141.93 904.65, -137.03 895.26, -132.13 884.35, -132.14 876.32, -132.71 865, -133.99 855.08, -136.54 843.2, -139.02 834.56) "

def diff(v,w):
     return (v[0] - w[0], v[1] - w[1])

def dot(v,w):
    return v[0] * w[0] + v[1] * w[1]

def normalize(v):
    l = math.sqrt(v[0] * v[0] + v[1] * v[1])
    # if l== 0:
    #     l = 0.0000001
    return (v[0]/l, v[1]/l)

def to_deg(rad):
    return (rad * 180.0) / math.pi  

def lr_sgn(v,w):
    if ( v[0] * w[1] - v[1] * w[0]) < 0:
        return -1.0
    else:
        return 1.0
def preprocess(t):
    res = []
    for i in range(1,len(t)-1): 
        v = t[i]
        l = t[i-1]
        if v != l:
            res.append(v)
    return res

def traj_to_curve(traj):
    t = preprocess(traj)
    res = [0] * len(t)
    print(t)
    for i in range(1,len(t)-1):   
        print(i, t[i])
        v = t[i]
        last = t[i-1]
        v1 = diff(last, v)
        nex = t[i+1]
        v2 = diff(v, nex)
        
        v1 = normalize(v1)
        v2 = normalize(v2)
        
        value = dot(v1, v2)
        res[i] = to_deg( math.acos(value)*lr_sgn(v1, v2))
    return res

def extrema(curve):
    res_min=[]
    res_max=[]

    SEARCH_UNDECIDED = 0
    SEARCH_MIN = 1
    SEARCH_MAX = 2
    
    last_min = curve[0]
    last_max = curve[0]
    search = SEARCH_UNDECIDED
    
    for i, x in enumerate(curve):
        if(search == SEARCH_UNDECIDED):
            if(x > last_min):
                search = SEARCH_MAX
                last_max = x
                res_min.append(0)
        
            if(x < last_min):
                search = SEARCH_MIN
                last_min = x
                res_max.append(0)
        
        elif(search == SEARCH_MIN):
            if(x > last_min):
                search = SEARCH_MAX
                last_max = x
                res_min.append(i-1)
            else:
                last_min = x
            
        elif(search == SEARCH_MAX):
            if(x < last_max):
                search = SEARCH_MIN
                last_min = x
                res_max.append(i-1)
            else:
                last_max = x

    #add end, its either min or max
    if(curve[res_min[-1]] > curve[res_max[-1]]):
        res_max.append(len(curve)-1)
    else:
        res_min.append(len(curve)-1)
    
    return res_min, res_max

def persistence(curve):
    minima, maxima = extrema(curve)
    comps = [{"right": m, "left": m,"min": m, "max": m, "done": False} for m in minima]
    max_set = maxima
    active_comps = list(range(len(comps)))
    used = [-1] * len(curve)
    it = 0
    finished = False
    

    while not finished and len(active_comps) > 0:
        it+=1
        i = it % len(active_comps)
        #grow bars
        current_i = active_comps[i]
        c1 = comps[current_i]

        if(c1["left"] == 0 and c1["right"] == len(curve)-1):
            finished = True
            c1["done"] = True
            del active_comps[i]
    
            if c1["left"] in max_set:
                c1["max"] = c1["left"]
            elif c1["right"] in max_set:
                c1["max"] = c1["right"]           
        
        if not c1["done"]:
            l = c1["left"] - 1
            r = c1["right"] + 1

            #decide grow direction
            x = 0
            if l != -1 and (r == len(curve) or curve[l] < curve[r]) :
                c1["left"] = l
                x = l
            else:
                c1["right"] = r
                x = r
    
            x = min(max(0,x), len(curve)-1)     
    
            
            if x in max_set:
                c1["done"] = True
                c1["max"] = x
                #REMOVE
                del active_comps[i]
                #if max is already used
                if(used[x] != -1):                                          
                    #MERGE COMPONENTS
                    c2 = comps[used[x]]
                    m1 = c1["min"]
                    m2 = c2["min"]

                    if (c2["min"] > c1["min"]):
                        m1 = c2["min"]
                        m2 = c1["min"]
                    
                    
                    c2["left"] = min(c1["left"], c2["left"])
                    c2["right"] = max(c1["right"], c2["right"])
                    c2["min"] = m2
                    c2["max"] = -1
                    c2["done"] = False

                    #ADD
                    active_comps.append(used[x])
                    
                    c1["left"] = min(x, m1)
                    c1["right"] = max(x, m1)
                    c1["min"] = m1
                    
                    #REDUNDANT see above
                    c1["max"] = x
                    c1["done"] = True
                   
                used[x] = current_i
    bars = [[c["min"], c["max"]] for c in comps]
    return comps, bars

def make_traj(ls):
    b = ls.bounds
    traj = preprocess(ls.coords)
    print(b)
    sx = sz/(b[2]-b[0])
    sy = sz/(b[3]-b[1])
    data = [((c[0]-b[0])*sx, (c[1]-b[1])*sy) for c in traj]
    return data



def set_background(self, fill_color="#FFFFFF"):
    background = Rectangle(
    width = FRAME_WIDTH*5,
    height = FRAME_HEIGHT*5,
    stroke_width = 0,
    fill_opacity = 1, fill_color=fill_color)
    self.add(background)

class IntroScene(Scene):
    def construct(self):
        tum = SVGMobject("./resources/tum_logo.svg",color="#3070B3")
        bgdm = Text(r"Big Geospatial Data Managment", color="black")
        bgdm_www = Text(r"https://www.bgd.lrg.tum.de/", color="#3070B3")
        bgdm_www.scale(0.75)
        tum.scale_in_place(1.5)
        
        #self.add(tum.to_edge(UP))
        bgdm.next_to(tum, direction=DOWN, aligned_edge=DOWN, buff=1)
        bgdm_www.next_to(bgdm, direction=DOWN, aligned_edge=DOWN, buff=0.25)
        x = VGroup(bgdm, bgdm_www)
        set_background(self)
        self.play(Write(tum))
        self.play(Write(x))
        self.wait(2)

class FormulaScene(Scene):
    def construct(self):
        set_background(self)

        formula = Text(r"$\frac{3}{4}$", color="black")
        self.play(Write(formula))
        self.wait(3)

ls = wkt.loads(lss)
sz = 6
graph_timing=0.1
cutoff = 130




class SequencePlotTraj(GraphScene):
    def __init__(self, **kwargs):

        GraphScene.__init__(
            self,
            x_min=0,
            x_max=sz,
            y_min=0,
            y_max=sz,
            x_axis_height= sz,
            y_axis_height= sz,

           # graph_origin = [-5,0,0],
            **kwargs
        )

    def construct(self):
        # data = [(1,1), (2,2), (3,2), (5,4), (3,4), (4,1), (2,3)]

        set_background(self)
        data = make_traj(LineString(ls.coords[:cutoff]))[::-1]
        self.setup_axes()

        for i, dat in enumerate(data):
            s=self.coords_to_point(data[max(0,i-1)][0],data[max(0,i-1)][1])
            e=self.coords_to_point(dat[0],dat[1])


            dot = Dot(color="darkgray").move_to(e)
            line = Line(start=s, end=e, color="lightgray")
            x = VGroup(line,dot )
            self.play(Write(x), run_time=graph_timing)
        
        self.wait(3)
MIN_Y= 200
MAX_Y = -200
crv = traj_to_curve(ls.coords[:cutoff][::-1])
for c in crv:
    MIN_Y = min(MIN_Y, c)
    MAX_Y = max(MAX_Y, c)
class SequencePlotDeriv(GraphScene):
    def __init__(self, **kwargs):

        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=cutoff,
            y_min=MIN_Y,
            y_max=MAX_Y,
            graph_origin = [-5,0,0],
            x_tick_frequency=5,
            y_tick_frequency=10,
            y_axis_label=r"$\alpha$",
            x_axis_label=r"$i$",
            **kwargs
        )

    def construct(self):
        set_background(self)
        data = traj_to_curve(ls.coords[:cutoff][::-1])
        print(data)
        print("UP", UP, "DOWN", DOWN, "LEFT", LEFT, "RIGHT", RIGHT, "ORIGIN", ORIGIN)
        
        self.setup_axes()

        for i, dat in enumerate(data):
            s=self.coords_to_point(max(0,i-1),data[max(0,i-1)])
            e=self.coords_to_point(i,dat)


            dot = Dot(color="darkgray").move_to(e)
            line = Line(start=s, end=e, color="lightgray")
            x = VGroup(dot, line)
            self.play(Write(x), run_time=graph_timing)
        
        self.wait(3)
class SequencePlotMinMax(GraphScene):
    def __init__(self, **kwargs):

        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=cutoff,
            y_min=MIN_Y,
            y_max=MAX_Y,
            graph_origin = [-5,0,0],
            x_tick_frequency=5,
            y_tick_frequency=10,
            y_axis_label=r"$\alpha$",
            x_axis_label=r"$i$",
            **kwargs
        )

    def construct(self):
        set_background(self)
        data = traj_to_curve(ls.coords[:cutoff][::-1])
        minima, maxima = extrema(data)
        print(data)
        print("UP", UP, "DOWN", DOWN, "LEFT", LEFT, "RIGHT", RIGHT, "ORIGIN", ORIGIN)
        
        self.setup_axes()

        m1 = Dot(color="red").move_to(RIGHT*4+UP*2.5)
        label_min =  Text(r"minima", color="black").move_to(RIGHT*5+UP*2.5)
        m2 = Dot(color="green").move_to(RIGHT*4+UP*2)
        label_max =  Text(r"maxima", color="black").move_to(RIGHT*5.05+UP*2)
        self.add(m1)
        self.add(m2)
        self.add(label_min)
        self.add(label_max)

        for i, dat in enumerate(data):
            s=self.coords_to_point(max(0,i-1),data[max(0,i-1)])
            e=self.coords_to_point(i,dat)


            #dot = Dot(color="darkgray").move_to(e)
            line = Line(start=s, end=e, color="lightgray")
            #x = VGroup(dot, line)
            self.play(Write(line), run_time=graph_timing)
            if i in minima:
                m = Dot(color="red").move_to(e)
                self.play(Write(m), run_time=graph_timing)
            if i in maxima:
                m = Dot(color="green").move_to(e)
                self.play(Write(m), run_time=graph_timing)
        
        self.wait(3)


class SequencePlotSweepline(GraphScene):

    def __init__(self, **kwargs):

        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=cutoff,
            y_min=MIN_Y,
            y_max=MAX_Y,
            graph_origin = [-5,0,0],
            x_tick_frequency=5,
            y_tick_frequency=10,
            y_axis_label=r"$\alpha$",
            x_axis_label=r"$i$",
            **kwargs
        )

    def construct(self):
        set_background(self)
        data = traj_to_curve(ls.coords[:cutoff][::-1])
        minima, maxima = extrema(data)
        print(data)
        print("UP", UP, "DOWN", DOWN, "LEFT", LEFT, "RIGHT", RIGHT, "ORIGIN", ORIGIN)
        
        self.setup_axes()

        m1 = Dot(color="red").move_to(RIGHT*4+UP*2.5)
        label_min =  Text(r"minima", color="black").move_to(RIGHT*5+UP*2.5)
        m2 = Dot(color="green").move_to(RIGHT*4+UP*2)
        label_max =  Text(r"maxima", color="black").move_to(RIGHT*5.05+UP*2)
        self.add(m1)
        self.add(m2)
        self.add(label_min)
        self.add(label_max)

        comps, bars = persistence(data)

        min_y = 200
        max_y = -200
        for i, dat in enumerate(data):
            s=self.coords_to_point(max(0,i-1),data[max(0,i-1)])
            e=self.coords_to_point(i,dat)
            min_y = min(min_y, data[i])
            max_y = max(max_y, dat)


            #dot = Dot(color="darkgray").move_to(e)
            line = Line(start=s, end=e, color="lightgray")
            #x = VGroup(dot, line)
            self.add(line)
            if i in minima:
                m = Dot(color="red").move_to(e)
                self.add(m)
            if i in maxima:
                m = Dot(color="green").move_to(e)
                self.add(m)
        
        l1 = Line(start=self.coords_to_point(-5, min_y), end=self.coords_to_point(len(data)+5, min_y), color="black", stroke_width=7, stroke_opacity=0.75)
        # l2 = Line(start=self.coords_to_point(0, max_y), end=self.coords_to_point(len(data), max_y), color="black")
        self.play(Write(l1))
        ss= 1
        steps = range(int(min_y/ss)*ss, ss*2+int(max_y/ss)*ss, ss)
        abars = []
        vb = VGroup()
        # for b in bars:
        #     m = data[b[0]]
        #     mx = data[b[1]]
        #     bar = Line(start=self.coords_to_point(b[0], m), end=self.coords_to_point(b[0], mx), color="orange")
        #     marker = DashedLine(start=self.coords_to_point(b[0], mx), end=self.coords_to_point(b[1], mx), color="lightgray")
        #     self.add((bar))
        #     self.add((marker))
        steptime = 0.1
        for i in steps:
            l2 = Line(start=self.coords_to_point(-5, i), end=self.coords_to_point(len(data)+5, i), color="black", stroke_width=7, stroke_opacity=0.5)

            self.play(Transform(l1,l2), run_time= steptime)
            for b in bars:
                m = data[b[0]]
                mx = data[b[1]]
                if m > i-ss and m <= i:
                    #self.play(Write(bar), run_time= 0.1)
                    abars.append(b)
            
            vb2 = VGroup()
            for b in abars:
                bar = Line(start=self.coords_to_point(b[0], data[b[0]]), end=self.coords_to_point(b[0], min(data[b[1]], i)), color="black", stroke_width=7)#.add_tip(tip_length=0.2, at_start=True).add_tip(tip_length=2, at_start=False)
                vb2.add(bar)
                if data[b[1]] <= i:
                    marker = DashedLine(start=self.coords_to_point(b[0], data[b[1]] ), end=self.coords_to_point(b[1], data[b[1]] ), color="gray")
                    vb2.add(marker)
            self.remove(vb)
            self.add(vb2)
            vb = vb2
        self.play(FadeOut(l1), run_time=2)
        
        self.wait(3)
    
class SequencePlotGrowComponents(GraphScene, MovingCameraScene):
    def __init__(self, **kwargs):
        self.cutoff= int(32)

        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=self.cutoff,
            y_min=int(MIN_Y/15)*15,
            y_max=MAX_Y,
            graph_origin = [-5,0,0],
            x_tick_frequency=1,
            y_tick_frequency=15,
            y_labeled_nums=range(int(MIN_Y/15)*15,int(MAX_Y),15),
            y_axis_label=r"$\alpha$",
            x_axis_label=r"$i$",
            include_tip=True,
            **kwargs
        )
    def setup(self):
        GraphScene.setup(self)
    def construct(self):
        self.camera.frame.save_state()
        #self.play(Restore(self.camera.frame.scale(0.5)))
        set_background(self)
        data = traj_to_curve(ls.coords[:self.cutoff][::-1])
        minima, maxima = extrema(data)

        print(data)
        print("UP", UP, "DOWN", DOWN, "LEFT", LEFT, "RIGHT", RIGHT, "ORIGIN", ORIGIN)
        
        self.setup_axes(animate = False)

        m1 = Dot(color="red").move_to(RIGHT*4+UP*2.5)
        label_min =  Text(r"minima", color="black").move_to(RIGHT*5+UP*2.5)
        self.add(m1)
        self.add(label_min)
        m2 = Dot(color="green").move_to(RIGHT*4+UP*2)
        label_max =  Text(r"maxima", color="black").move_to(RIGHT*5.05+UP*2)
        self.add(m2)
        self.add(label_max)

        for i, dat in enumerate(data):
            s=self.coords_to_point(max(0,i-1),data[max(0,i-1)])
            e=self.coords_to_point(i,dat)


            #dot = Dot(color="darkgray").move_to(e)
            line = Line(start=s, end=e, color="lightgray")
            #x = VGroup(dot, line)
            self.add(line)
        
        for i in minima:
            e=self.coords_to_point(i,data[i])
            m = Dot(color="red").move_to(e)
            self.add(m)
        for i in maxima:
            e=self.coords_to_point(i,data[i])
            m = Dot(color="green").move_to(e)
            self.add(m)
        # persisitence algorithm
        curve = data

        comps = [{"right": m, "left": m,"min": m, "max": m, "done": False ,"v":VGroup()} for m in minima]
        max_set = maxima
        active_comps = list(range(len(comps)))
        used = [-1] * len(curve)
        it = 0
        finished = False
        label_iter =  Text(f"iteration: {it}", color="black").move_to(RIGHT*1+UP*2)
            
        #self.add(label_iter)
        cur = Dot(color="blue", fill_opacity=0.5, radius=DEFAULT_DOT_RADIUS*2.0).move_to(self.coords_to_point(0,curve[0]))
        status = VGroup(label_iter, cur)

        def set_status(s, status):
            self.remove(status)
            label_iter =  Text(s, color="black").move_to(LEFT*0.75+UP*3)
            label_iter.scale(0.8)
            status = VGroup(label_iter, cur)
            self.play(FadeIn(status), run_time=0.25)
            return status

        def make_v(c):
            color = "orange"
            # if c["done"]:
            #     color="black"
            s=self.coords_to_point(c["min"],curve[c["min"]])
            left = Line(start=s, end=self.coords_to_point(c["left"],curve[c["left"]]), color=color)
            right= Line(start=s, end=self.coords_to_point(c["right"],curve[c["right"]]), color=color)
            return VGroup(left, right)
        
        bars = []
        #TODO merge bars
        def add_bar(c):
            bars.append(c)
            x= -3.5+0.25*len(bars)
            
            l1 = Line(start= self.coords_to_point(c["min"],curve[c["min"]]),end= self.coords_to_point(c["max"],curve[c["max"]]), color="black")
            l2 = Line(start= self.coords_to_point(x,curve[c["min"]]),end= self.coords_to_point(x,curve[c["max"]]), color="black")
            self.play(ShowCreation(l1))
            self.play(Transform(l1, l2), run_time=1.5)
            c["bar"] = [l1,l2]
            return c
        

        while not finished and len(active_comps) > 0:
            # self.remove(label_iter)
            # self.remove(cur)
            it+=1
            i = it % len(active_comps)
            #grow bars
            current_i = active_comps[i]
            c1 = comps[current_i]
            cur = Dot(color="blue", fill_opacity=0.5, radius=DEFAULT_DOT_RADIUS*1.5).move_to(self.coords_to_point(c1["min"],curve[c1["min"]]))
            
            status = set_status(f"iteration: {it}\ncurrent component: {current_i}", status)

            if(c1["left"] == 0 and c1["right"] == len(curve)-1):
                finished = True
                c1["done"] = True
                del active_comps[i]
        
                if c1["left"] in max_set:
                    c1["max"] = c1["left"]
                elif c1["right"] in max_set:
                    c1["max"] = c1["right"]           
                c1 = add_bar(c1)
                status = set_status(f"iteration: {it}\nFinished!", status)
                print("Finished at: ", it)
            
            if not c1["done"]:
                l = c1["left"] - 1
                r = c1["right"] + 1
                status = set_status(f"iteration: {it}\ncurrent component: {current_i}", status)

                #decide grow direction
                x = 0
                if l != -1 and (r == len(curve) or curve[l] < curve[r]) :
                    c1["left"] = l
                    x = l
                else:
                    c1["right"] = r
                    x = r
        
                x = min(max(0,x), len(curve)-1)     
       
                
                if x in max_set:
                    
                    status = set_status(f"iteration: {it}\ncurrent component: {current_i}\nreached maximum -> Create Bar!", status)
                    c1["done"] = True
                    c1["max"] = x

                    self.remove(c1["v"])
                    c1["v"] = make_v(c1)
                    self.play(Write(c1["v"]))

                    #REMOVE
                    del active_comps[i]
                    c1 = add_bar(c1)

                    #if max is already used
                    if(used[x] != -1):   
                        
                        #MERGE COMPONENTS
                        status = set_status(f"iteration: {it}\ncurrent component: {current_i}\nmax is used -> merge", status)                     
                        c2 = comps[used[x]]
                        m1 = c1["min"]
                        m2 = c2["min"]

                        if (c2["min"] > c1["min"]):
                            m1 = c2["min"]
                            m2 = c1["min"]
                        
                        
                        c2["left"] = min(c1["left"], c2["left"])
                        c2["right"] = max(c1["right"], c2["right"])
                        c2["min"] = m2
                        c2["max"] = -1
                        c2["done"] = False

                        for b in c2["bar"]:
                            self.play(FadeOut(b))

                        #ADD
                        active_comps.append(used[x])
                        
                        c1["left"] = min(x, m1)
                        c1["right"] = max(x, m1)
                        c1["min"] = m1
                        
                        #REDUNDANT see above
                        c1["max"] = x
                        c1["done"] = True

                        self.play(FadeOut(c1["v"]))
                        self.play(FadeOut(c2["v"]))
                        c1["v"] = make_v(c1)
                        c2["v"] = make_v(c2)
                        self.play(Write(c1["v"]))
                        self.play(Write(c2["v"]))
                        
                    used[x] = current_i
                else:
                    self.remove(c1["v"])
                    c1["v"] = make_v(c1)
                    self.play(Write(c1["v"]))

        # self.play(Restore(self.camera.frame))
        self.wait(3)




