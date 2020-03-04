from models.item import Item

speakers = Item("https://www.johnlewis.com/sonos-one-gen-2-smart-speaker-with-voice-control/black/p4045151", "p", {"class": "price price--large"})
ipad = Item("https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-cellular-512gb/space-grey/p3834614", "p", {"class": "price price--large"})
tv= Item("https://www.johnlewis.com/toshiba-24wl3a63db-2019-led-hd-ready-720p-smart-tv-24-inch-with-freeview-hd-freeview-play-black/p4269742", "p",{"class": "price price--large"})

print('The price of the items are as follows:')
print('Speakers: ' + str(speakers.price_of_item()))
print('Ipad: ' + str(ipad.price_of_item()))
print('TV: ' + str(tv.price_of_item()))

ipad.save_to_mongo()
speakers.save_to_mongo()
tv.save_to_mongo()

all_items  = Item.all()


print(all_items)
print(all_items[0])
print(speakers.price_of_item())

