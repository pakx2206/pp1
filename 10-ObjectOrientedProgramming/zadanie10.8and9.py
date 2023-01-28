class Tv():
    def __init__(self) -> None:
        self.is_on = False
        self.channel_no = 1

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
    def set_channel(self,name):
        self.channel_no = name
    def show_status(self):
        if self.is_on:
            print("TV is on, channel",self.channel_no)
        else:
            print("TV is off")
    
        


x = Tv()
x.show_status()
x.turn_on()
x.show_status()
x.set_channel(5)
x.show_status()
x.turn_off()
x.show_status()
