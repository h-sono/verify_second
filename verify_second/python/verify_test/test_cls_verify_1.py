#-*- coding: utf-8 -*-
# pytest実行コマンド：$ pytest test_cls_verify_1.py
from verify_test.cls_verify_1 import ClsVerify1


class TestClsVerify1(object):

    def test_cls_verify_1_1(self):
        
        # インスタンス化
        cv = ClsVerify1(100)

        # 検証
        assert cv.calc_1(1) == 121

    def test_cls_verify_1_2(self):
        
        # インスタンス化
        cv = ClsVerify1(1)

        # 検証1
        assert cv.str_1() == u'文字列テスト1:コンストラクタ文字列1'
