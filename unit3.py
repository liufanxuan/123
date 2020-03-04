class circle:


    center = 0 + 0j

    radius = 0
  def __init__(self, x, y, r):

        self.center = complex(x, y)

        self.radius = abs(r)

    def print(self):

        x = self.center.real

        y = self.center.imag

        r = self.radius

        print("Center\t(%f,%f) \t Radius\t%f" % (x, y, r))



    # 计算两个圆之间的距离

    def Distance(self, cir2):

        c_1 = self.center

        c_2 = cir2.center

        r_1 = self.radius

        r_2 = cir2.radius



        return abs(c_1 - c_2) - (r_1 + r_2)



    # 判断对象是否和另一个circle对象clr2有重叠部分

    def OverLap(self, cir2):

        # 计算两个圆间的距离，若小于0则有重叠部分

        Dist = self.Distance(cir2)

        if Dist < 0:

            return True

        elif Dist >= 0:

            return False



    # 将此对象添加到列表c_list中,返回是否添加成功

    def Append_To(self, c_list):

        # 判断该圆是否和列表中其他圆有重合部分

        OverLap = False

        if len(c_list) == 0:

            c_list.append(self)

            return True

        else:

            for c in c_list:

                OverLap += self.OverLap(c)



            if not OverLap:

                c_list.append(self)

                return True

            else:

                return False



    # 判断该圆的圆心是否在其他的圆内

    def Center_Inside(self, c_list):

        if len(c_list) == 0:

            return False

        else:

            Inside = False

            for cir in c_list:

                c_1 = cir.center

                r_1 = cir.radius

                dis = abs(self.center - c_1)

                if dis <= r_1:

                    Inside += True

                    break

                else:

                    Inside += False



            return Inside



    # 计算最大可行半径

    def Max_Radius(self, c_list):

        x = self.center.real

        y = self.center.imag

        # 计算到边界的距离

        R_list = [1 - x, x + 1, 1 - y, y + 1]



        if not len(c_list) == 0:

            # 计算到其他各圆的距离

            for c in c_list:

                r = c.Distance(self) + self.radius

                R_list.append(r)

        # 从中取最小值，作为该圆的半径

        self.radius = min(R_list)





# 计算c_list中所有圆的r^2之和

def Total_R_Square(c_list):

    R2 = 0

    for c in c_list:

        R2 += c.radius**2



    return R2





# 输出c_list中所有圆的信息

def Print_All(c_list):

    for c in c_list:

        c.print()





# 计算在给定圆的数量的情况下，r^2最大时对应的圆的列表

# 返回这一列表

def Max_R_Square(circle_num):

    circle_list = []

    # 向列表中添加新圆，直到总数符合要求

    while len(circle_list) < circle_num:

        if len(circle_list) == 0:

            # 第一个圆，强制设定为单位圆

            x = 0

            y = 0

            r = 1

        else:

            # 随机下一个圆的圆心坐标

            import random

            x = random.uniform(-1, 1)

            y = random.uniform(-1, 1)

            r = 0



        cir = circle(x, y, r)

        # 判断随机生成的新圆心坐标是否在已经存在的圆内

        if not cir.Center_Inside(circle_list):

            # 若不在，则计算这个圆的最大半径，并添加进列表

            cir.Max_Radius(circle_list)

            cir.Append_To(circle_list)

    return circle_list





if __name__ == "__main__":

    circle_num = 1000

    c_list = Max_R_Square(circle_num)

    R2 = Total_R_Square(c_list)

    print("对应圆的参数")

    Print_All(c_list)



    print("sum r^2的最大值为\t", R2)
