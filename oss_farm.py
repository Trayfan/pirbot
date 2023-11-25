from data.cords import Game, Item, Cords
from data.enums import ItemType, Location

# Очищаем файл логов
with open("test.log", "w") as f:
    pass

game = Game()
# Устанавливаем за что отвечают ячейки
oss = game.inv.slots[0][0]
treasure_map = game.inv.slots[0][1]
ticket_icespire_haven = game.panel.slots[1][3]

# Устанавливаем какой предмет лежит в ячейке
treasure_map.item = Item("treasure_map", ItemType.Disapear, (180, 152, 95), treasure_map)
oss.item = Item("oss", ItemType.AnotherCell, (211, 167, 59), treasure_map)
ticket_icespire_haven.item = Item("ticket_icespire_haven", ItemType.Ticket, (139, 40, 218), Location.IcespireHaven)

# ticket_icespire_haven = game.inv.slots[0][2]
# ticket_abandon_mine = game.inv.slots[0][3]
# ticket_thundoria_castle = game.inv.slots[0][4]
# ticket_lone_tower = game.inv.slots[0][5]
# ticket_thundoria_harbor = game.inv.slots[0][6]
# ticket_sacred_snow_mountain = game.inv.slots[0][7]
# ticket_oasis = game.inv.slots[1][0]
# ticket_barren_cavern = game.inv.slots[1][1]
# ticket_andes_forest_haven = game.inv.slots[1][2]


# game.inv.open()
# oss.use()
# print(oss.get_color())
# print(ticket_icespire_haven.get_color())
# ticket_icespire_haven.use()

# print(game.minimap.location)
game.radar.go_to(Cords(1234, 4312))