import time
from github.plant_ import combinatorics


class Plant:
    def __init__(self, rows, columns, duration):
        """
        :param rows: 行数
        :param columns: 列数
        :param duration: 最大连续种树数
        """
        self._rows = rows
        self._columns = columns
        self._duration = duration
        self._map = [[0 for _ in range(self._columns)] for _ in range(self._rows)]
        self._max_num = 0
        self._max_maps = []
        self._spend = 0
        self._found = False
        # self.map = [
        #     [1, 1, 0, 1],
        #     [0, 1, 0, 0],
        #     [0, 0, 0, 1],
        # ]
        # self.map = [
        #     [1, 0, 0, 1],
        #     [0, 0, 1, 0],
        #     [0, 1, 0, 1],
        # ]

    def __str__(self, map_=None):
        map_ = map_ or self._map
        str_ = []
        for row in map_:
            row_ = [str(i) for i in row]
            str_.append("\t".join(row_))
        return "\n".join(str_)

    def can_plant(self):
        def all_right(i, j):
            for k in range(self._duration):
                if not self._map[i][j + k]:
                    return False
            return True

        def all_down(i, j):
            for k in range(self._duration):
                if not self._map[i + k][j]:
                    return False
            return True

        def all_right_down(i, j):
            for k in range(self._duration):
                if not self._map[i + k][j + k]:
                    return False
            return True

        def all_left_down(i, j):
            for k in range(self._duration):
                if not self._map[i + k][j - k]:
                    return False
            return True

        right = self._columns - self._duration + 1
        down = self._rows - self._duration + 1
        left = self._duration - 2
        for i in range(self._rows):
            for j in range(self._columns):
                # 右
                if j < right:
                    if all_right(i, j):
                        return False
                    # 右下
                    if i < down and all_right_down(i, j):
                        return False
                # 下
                if i < down:
                    if all_down(i, j):
                        return False
                    # 左下
                    if j > left and all_left_down(i, j):
                        return False
        return True

    def tree_num(self):
        num = 0
        for i in range(self._rows):
            for j in range(self._columns):
                num += self._map[i][j]
        return num

    # 这个函数较下一个多 300% 耗时
    # def max_tree_num(self):
    #     if self._found:
    #         return self._max_num
    #     self._spend = time.time()
    #     for k in range(2 ** (self._rows * self._columns) - 1, -1, -1):
    #         for i in range(self._rows - 1, -1, -1):
    #             for j in range(self._columns - 1, -1, -1):
    #                 self._map[i][j] = k & 1
    #                 k = k >> 1
    #         # 这段代码较下一段多 50% 耗时
    #         # if self.can_plant():
    #         #     num = self.tree_num()
    #         #     if num > self._max_num:
    #         #         self._max_num = num
    #         #         self._max_maps = [copy.deepcopy(self.map_)]
    #         #     elif num == self._max_num:
    #         #         self._max_maps.append(copy.deepcopy(self.map_))
    #         num = self.tree_num()
    #         if num > self._max_num:
    #             if self.can_plant():
    #                 self._max_num = num
    #                 self._max_maps = [copy.deepcopy(self._map)]
    #         elif num == self._max_num:
    #             if self.can_plant():
    #                 self._max_maps.append(copy.deepcopy(self._map))
    #     self._found = True
    #     self._spend = time.time() - self._spend
    #     return self._max_num

    def max_tree_num(self):
        if self._found:
            return self._max_num
        self._spend = time.time()
        multi = self._rows * self._columns
        for k in range(self._rows * self._columns, 0, -1):
            print(f"尝试种 {k} 棵树...")
            maps = combinatorics.combination(multi, k)
            for m in maps:
                self._map = []
                for i in range(self._rows):
                    self._map.append(m[i * self._columns: (i + 1) * self._columns])
                if self.can_plant():
                    self._max_num = k
                    self._max_maps.append(self._map)
                    self._found = True
            if self._found:
                break
        self._spend = time.time() - self._spend
        return self._max_num

    def max_tree_maps(self):
        if not self._found:
            self.max_tree_num()
        return self._max_maps

    def show_all(self):
        if not self._found:
            self.max_tree_num()
        print(f"对于 {self._rows} x {self._columns} 的土地，最多连续数为 {self._duration} 的种树方法统计：")
        print(f"耗时 {self._spend:0.6f} s。")
        print(f"最多可以种 {self._max_num} 棵树，有 {len(self._max_maps)} 种种法。")
        print(f"具体种法如下：\n")
        for map_ in self._max_maps:
            print(self.__str__(map_) + "\n")


if __name__ == "__main__":
    p = Plant(5, 4, 3)
    p.show_all()
