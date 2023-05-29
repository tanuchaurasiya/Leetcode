class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b=big
        self.m=medium 
        self.s=small 
        

    def addCar(self, car: int) -> bool:
        if car==1:
            if self.b>0:
                self.b-=1
                return True
            else:
                return False

        if car==2:
            if self.m>0:
                self.m-=1
                return True
            else:
                return False

        if car==3:
            if self.s>0:
                self.s-=1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)