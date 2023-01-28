class Tv():
    def __init__(self) -> None:
        self.is_on = False
        self.channel_names = []
        self.channel_no = 1

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channels(self, chanel):
        self.channel_names = chanel

    def show_channels(self):
        print("Channel list:")
        for i, x in enumerate(self.channel_names):
            print(i+1,".", x)

    def set_channel(self,name):
        self.channel_no = name

    def show_status(self):
        if self.is_on:
            print("TV is on, channel", self.channel_no, self.channel_names[self.channel_no-1])
        else:
            print("TV is off")


x = Tv()
x.turn_on()
x.show_channels()
x.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
x.show_channels()
x.show_status()
x.turn_off()
