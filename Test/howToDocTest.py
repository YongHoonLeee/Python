class cal(object):
    def add_num_and_double(self, x, y):
        # 미리 실행시켜서 밑에 기대값을 적어놓는다.
        """Add num and make Double
        >>> c = cal()
        >>> c.add_num_and_double(1,1)
        4
        """
        # 만약 기대값과 다르다면 test Failed 가 뜨면서 값을 비교해준다 신기.
        result = x+y
        result += 2
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
