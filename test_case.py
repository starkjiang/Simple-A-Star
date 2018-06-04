import a_star as A



def test_2DGrid_1():
    """Example 1 (4 * 10 cells)"""



    a = A.Astar()
    obstacles = ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                 (1, 6), (1, 7), (1, 8), (1, 9))
    a.init_grid(10, 4, obstacles, (0, 9), (3, 9))
    path = a.solve()
    print(path)
    # self.assertEqual(path, [(0, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4),
    #                         (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0),
    #                         (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
    #                         (3, 9)])


def test_2DGrid_hammer_1():
    """With a hammer, equivalently, it has no obstacles in the grid for the robot"""



    a = A.Astar()
    obstacles = ()
    a.init_grid(10, 4, obstacles, (0, 9), (3, 9))
    path = a.solve()
    print(path)
    # self.assertEqual(len(path), 4)

def test_2DGrid_2():
    """Example 2 (11 * 14 cells)"""




    a = A.Astar()
    obstacles = ((0, 12), (1, 2), (1, 3), (1, 4), (1, 5), (1, 12), (2, 2), (2, 5), (2, 12),
                 (3, 2), (3, 5), (3, 12), (4, 2), (4, 3), (4, 4), (4, 5), (4, 7), (4, 12),
                 (5, 7), (5, 12), (6, 7), (6, 12), (7, 7), (8, 1), (8, 2), (8, 7), (8, 8),
                 (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (9, 2), (10, 0), (10, 1), (10, 2),
                 (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11),
                 (10, 12), (10, 13))
    a.init_grid(14, 11, obstacles, (1, 13), (9, 0))
    path = a.solve()
    print(path)
    # self.assertEqual(path, [(1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (6, 13), (7, 13), (7, 12),
    #                         (7, 11), (7, 10), (7, 9), (7, 8), (6, 8), (5, 8), (4, 8), (3, 8),
    #                         (3, 7), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (7, 5), (7, 4), (7, 3),
    #                         (7, 2), (7, 1), (7, 0), (8, 0), (9, 0)])

def test_2DGrid_hammer_2():
    """With hammer"""



    a = A.Astar()
    obstacles = ()
    a.init_grid(14, 11, obstacles, (1, 13), (0, 9))
    path = a.solve()
    print(path)
    # self.assertEqual(len(path), 24)

if __name__ == '__main__':
    print("start running...")
    test_2DGrid_1()
    test_2DGrid_hammer_1()
    test_2DGrid_2()
    test_2DGrid_hammer_2()
