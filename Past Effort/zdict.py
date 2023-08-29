contacts = {
    803366472 :'John Doe', 703432302:'Jane Doe', 
    378232:'Anonymous',  7382032:'Unknown',
    485923:"N/A",893843:"No Name"
    }
removed_items = []
for key, value in list(contacts.items()):
    if len(str(key)) > 6:
        removed_items.append(f"{key} {value}")
        del contacts[key]
print("Removed contact numbers greater than 6 digits:", removed_items)