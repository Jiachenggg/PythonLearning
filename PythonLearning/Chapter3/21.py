# 继承：一个类继承另外类的成员变量和成员方法

# 单继承：一个类继承另一个类
class Phone:
    IMEI = None  # 序列号
    producer = "HUAWEI"

    def call_by_4g(self):
        print("4G通话")


class Phone2023(Phone):
    face_id = "001"

    def call_by_5g(self):
        print("新功能：5G通话")


phone = Phone2023()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 多继承：一个类继承多个类，按照顺序依次继承
class NFCReader:
    nfc_type = "第五代"
    producer = "华为"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("开启红外遥控")


class Myphone(Phone, NFCReader, RemoteControl):
    pass  # pass占位语句，用来保证函数（方法）或类定义的完整性，表示无内容，为空


phone = Myphone()
phone.call_by_4g()
phone.read_card()
phone.control()
# 多继承中，如果父类有同名方法和属性，先继承的优先级高于后继承的优先级
print(phone.producer)
