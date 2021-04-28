import gspread


gc = gspread.service_account()

sht1 = gc.open_by_key('1CV9C2mWMOWzwS4yMN3dyYZl2fJSAtC_ropC2F3Ypai8')
worksheet = sht1.get_worksheet(0)

# With label
val = worksheet.get('A2:E')
print("aaaa")
for val_ in val:
    contact_name,contact_number,msg =val_[1],val_[2],val_[3]
    print(contact_name,contact_number,msg)
