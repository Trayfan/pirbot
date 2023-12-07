from data.cords import Game, Item, Cords
from data.enums import ItemType, Location, Ticket
from client_interactions import get_cord_color, press_key, click


def get_location_by_cords(cords:Cords):
    possible_locations = [
        (Location.IcespireHaven, Cords(2700, 600)),
        (Location.BelmontPlains, Cords(1500, 2600)),
        (Location.ThundoriaCastle, Cords(700, 1700)),
        (Location.SacredForest, Cords(300, 1600)),
        (Location.ThundoriaHarbor, Cords(1000, 1300)),
        (Location.SacredSnowMountain, Cords(1000, 1000)),
        (Location.OasisHaven, Cords(900, 3000)),
        (Location.SouthernDesert, Cords(1400, 2900)),
        (Location.AndesForestHaven, Cords(1000, 2900)),
    ]
    result = (None, 10000)
    for loc in possible_locations:
        x_dif = abs(cords.x - loc[1].x)
        y_dif = abs(cords.y - loc[1].y)
        if x_dif + y_dif < result[1]:
            result = (loc[0], x_dif + y_dif)
    print(f"Локация копания сокровищ: {result[0].value}")
    return result[0]


def tp_to_location(location:Location):
    res = None
    for column in game.panel.slots[1]:
        if not column.item:
            continue
        if location in column.item.check_object.value:
            column.use()
            # invis.use()
            match location:
                case Location.BelmontPlains:
                    click(Cords(509, 693))
                    game.minimap.wait_running()
                case Location.ThundoriaCastle:
                    game.radar.go_to(Cords(753, 1638))
                    game.minimap.wait_running()
            res = True
            break
    if not res:
        print("Не нашли билет для телепорта!")
        exit()


def safe_point(location:Location):
    cords = None
    match location:
        case Location.SacredForest:
            cords = Cords()
        case Location.SacredSnowMountain:
            cords = Cords(987, 1022)
        case Location.IcespireHaven:
            cords = Cords(2728, 614)
    return cords
    
def dead():
    if get_cord_color(Cords(803, 609)) == (235, 235, 235):
        return True
    return False

game = Game()
# Устанавливаем за что отвечают ячейки
oss = game.inv.slots[0][0]
treasure_map = game.inv.slots[0][1]
ticket_argent = game.panel.slots[1][2]
ticket_icespire_haven = game.panel.slots[1][3]
ticket_abandon_mine = game.panel.slots[1][4]
ticket_thundoria_castle = game.panel.slots[1][5]
ticket_lone_tower = game.panel.slots[1][6]
ticket_thundoria_harbor = game.panel.slots[1][7]
ticket_sacred_snow_mountain = game.panel.slots[1][8]
ticket_oasis = game.panel.slots[1][9]
ticket_barren_cavern = game.panel.slots[1][10]
ticket_andes_forest_haven = game.panel.slots[1][11]
invis = game.panel.slots[0][0]

# Устанавливаем какой предмет лежит в ячейке
treasure_map.item = Item("treasure_map", ItemType.Disapear, treasure_map, treasure_map.get_color())
oss.item = Item("oss", ItemType.AnotherCell, treasure_map, oss.get_color())
ticket_argent.item = Item("ticket_argent", ItemType.Ticket, Ticket.ArgentCity, ticket_argent.get_color())
ticket_icespire_haven.item = Item("ticket_icespire_haven", ItemType.Ticket, Ticket.IcespireHaven, ticket_icespire_haven.get_color())
ticket_abandon_mine.item = Item("ticket_abandon_mine", ItemType.Ticket, Ticket.AbandonMine1, ticket_abandon_mine.get_color())
ticket_thundoria_castle.item = Item("ticket_thundoria_castle", ItemType.Ticket, Ticket.ThundoriaCastle, ticket_thundoria_castle.get_color())
ticket_lone_tower.item = Item("ticket_lone_tower", ItemType.Ticket, Ticket.LoneTower, ticket_lone_tower.get_color())
ticket_thundoria_harbor.item = Item("ticket_thundoria_harbor", ItemType.Ticket, Ticket.ThundoriaHarbor, ticket_thundoria_harbor.get_color())
ticket_sacred_snow_mountain.item = Item("ticket_sacred_snow_mountain", ItemType.Ticket, Ticket.SacredSnowMountain, ticket_sacred_snow_mountain.get_color())
ticket_oasis.item = Item("ticket_oasis", ItemType.Ticket, Ticket.OasisHaven, ticket_oasis.get_color())
ticket_barren_cavern.item = Item("ticket_barren_cavern", ItemType.Ticket, Ticket.BarrenCavern, ticket_barren_cavern.get_color())
ticket_andes_forest_haven.item = Item("ticket_andes_forest_haven", ItemType.Ticket, Ticket.AndesForestHaven, ticket_andes_forest_haven.get_color())
invis.item = Item("Invisible", ItemType.Buff, (Cords(409, 1155), (2, 3, 0)), invis.get_color())


while 1:
    game.inv.open()
    oss.use()
    cords = treasure_map.get_treasure_cords()
    location = get_location_by_cords(cords)
    tp_to_location(location)
    game.inv.open()
    game.radar.go_to(cords)
    game.minimap.wait_running()
    treasure_map.use()
    click(Cords(2514, 1371))
    if dead():
        click(Cords(720, 670))
        click(Cords(2514, 1371))
    ticket_argent.use()
