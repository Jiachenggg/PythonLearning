# 复写：对父类的成员属性或成员方法重新定义
class Phone:
    IMEI = None
    producer = "华为"

    def call_by_5g(self):
        print("使用5G通话")


class MyPhone(Phone):
    producer = "HUAWEI"  # 复写父类的成员

    def call_by_5g(self):
        print("使用5G+通话")
        # 在子类中调用父类成员

        # 方式1
        # print(f"父类厂商：{Phone.producer}")
        # Phone.call_by_5g(self)

        # 方式2
        print(f"父类厂商：{super().producer}")
        super().call_by_5g()


phone = MyPhone()
phone.call_by_5g()
print(phone.producer)
