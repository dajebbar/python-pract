class TV:
    def __init__(self):
        self.is_on = False
        self.is_muted = False
        # Default list of channels
        self.channel_list = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 56 ]
        self.n_channels = len(self.channel_list)
        self.channel_index = 0
        # Constants
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        # self volume
        self.volume = self.VOLUME_MAXIMUM // 2
    
    def power(self):
        '''[Toggle the state of power to off if current state is on and vice-versa]'''
        self.is_on = not self.is_on
    
    def volume_up(self):
        '''[turn up the volume if power is on and mute is off]'''
        if not self.is_on:
            return
        # changing the volume while muted unmutes the sound
        if self.is_muted:
            self.is_muted = False
        # Raise volume
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1
    
    def volume_down(self):
        '''[lower the volume if power is on and mute is off]'''
        if not self.is_on:
            return
        # changing the volume while muted unmutes the sound
        if self.is_muted:
            self.is_muted = False
        # lower the volume
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1
    
    def channel_up(self):
        if not self.is_on:
            return
        
        if self.channel_index < self.n_channels:
            self.channel_index += 1
        else:
            self.channel_index = 0
    
    def channel_down(self):
        if not self.is_on:
            return
        
        if self.channel_index > 0:
            self.channel_index -= 1
        else:
            self.channel_index = 0
    
    def mute(self):
        if not self.is_on:
            return
        self.is_muted = not self.is_muted
    
    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)
    
    def show_info(self):
        print()
        print('TV Status:')
        if self.is_on:
            print('    TV is: On')
            print('    Channel is:', self.channel_list[self.channel_index])
            if self.is_muted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')


my_tv = TV()
my_tv.power()
my_tv.show_info()

for i in range(3):
    my_tv.volume_up()
    my_tv.channel_up()
# my_tv.set_channel(20)
my_tv.mute()
my_tv.show_info()
