class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = "001"
clock1.price = 19.9
print(f"闹钟ID{clock1.id}，价格{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "002"
clock2.price = 19.9
print(f"闹钟ID{clock2.id}，价格{clock2.price}")
clock2.ring()
