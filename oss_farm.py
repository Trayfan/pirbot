from data.cords import Game


game = Game()
oss = game.inv.slots[0][0]
treasure_map = game.inv.slots[0][1]
ticket_icespire_haven = game.inv.slots[0][2]
ticket_abandon_mine = game.inv.slots[0][3]
ticket_thundoria_castle = game.inv.slots[0][4]
ticket_lone_tower = game.inv.slots[0][5]
ticket_thundoria_harbor = game.inv.slots[0][6]
ticket_sacred_snow_mountain = game.inv.slots[0][7]
ticket_oasis = game.inv.slots[1][0]
ticket_barren_cavern = game.inv.slots[1][1]
ticket_andes_forest_haven = game.inv.slots[1][2]


game.inv.open()

ticket_andes_forest_haven.use()
