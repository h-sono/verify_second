#-*- coding: utf-8 -*-

# クラスに関するテスト
class ClsVerify1(object):

    def __init__(self, hoge_1):
        """
        コンストラクタ
        """
        self.hoge_1 = hoge_1
        self.hoge_2 = 10
        self.hoge_3 = u'コンストラクタ文字列1'

    def calc_1(self, add_num):
        """
        計算用関数1
        """
        result_1 = self.hoge_2 * 2
        result_2 = result_1 + self.hoge_1 + add_num

        return result_2

    def str_1(self):
        """
        文字列返却関数1
        """
        return u'文字列テスト1:' + self.hoge_3
