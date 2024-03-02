# 封装：将现实世界事物在类中描述为属性和方法
class Phone:
    # 私有成员实际意义：在类中提供仅供内部使用的属性和方法，而不对外开放（类对象无法使用）

    # 私有成员变量
    __current_voltage = 0.5

    # 私有成员方法
    def __keep_sigle_core(self):
        print("使CPU以单核模式运行")

    # 类对象无法访问私有成员，类中的其他成员可以访问私有成员
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_sigle_core()


phone = Phone()

# print(phone.__current_voltage)
# phone.__keep_sigle_core
phone.call_by_5g()
