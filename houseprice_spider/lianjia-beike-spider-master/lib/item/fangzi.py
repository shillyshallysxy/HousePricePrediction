

class FangZi(object):
    def __init__(self, name='', pattern='', size='', price='', total_price='', orientation=''):
        # 房名
        self.name = name
        # 房间格局
        self.pattern = pattern
        self.size = size
        self.price = price
        self.total_price = total_price
        self.orientation = orientation

    def text(self):
        return self.name + "," + \
                self.pattern + "," + \
                self.size + "," + \
                self.price + "," + \
                self.total_price + "," + \
                self.orientation
