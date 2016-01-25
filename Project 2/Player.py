class Player:
        def __init__(self, tile, texture, pn):
            self.MyTile = tile
            self.Texture = texture
            self.playerNumber = pn

        def Update(self, dice):
            for i in range(0, dice):
                self.MyTile[0]= self.MyTile[0] + 33

        def Draw(self, texture, pos, screen):
            screen.blit(texture, pos)

            

                            