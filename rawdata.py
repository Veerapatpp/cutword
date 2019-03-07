import re
import sqlite3
def Writedata():
    try:
        db = "data/HomeAddress.sqlite3"
        with (sqlite3.connect(db)) as conn:
            sql_create = """
            CREATE TABLE `HomeAddress` (
                `id`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `HomeNo`	TEXT,
                `Alley`	TEXT,
                `Road`	TEXT,
                `District`	TEXT,
                `Province`	TEXT,
                `PostalCode`	TEXT
            );
                """
            conn.executescript(sql_create)

    except Exception as e:
        print("Error {0}".format(e))

def Insertdata(data):
    try:
        db = "data/HomeAddress.sqlite3"
        with (sqlite3.connect(db)) as conn:
            var_string = ','.join('?' * len(data))
            sql = """Insert into HomeAddress (Homeno,Alley,
            Road,District,Province,
            PostalCode) values (%s);""" % var_string

        conn.execute(sql,data)
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error {0}".format(e))

def Readdata() :
    with open("data/RawAddressData.txt", "r", encoding="UTF-8") as f:
        str = f.readlines()
        return str
def Postcode(data):
    if re.search("\d\d\d\d\d", data):
        x = re.search("\d\d\d\d\d", data)
        return x.group()
    else:
        return None
def Homecode(data):
    if re.search("^\d+/\d+-*\d*", data):
        Home = re.search("^\d+/\d+-*\d*", data)
    elif re.search("\s+\d+/\d+",data):
        Home = re.search("\s+\d+/\d+",data)
    elif re.search("\d+-\d+",data):
        Home = re.search("\d+-\d+",data)
    elif re.search("^\d+\s+/\s+\d+",data):
        Home = re.search("^\d+\s+/\s+\d+",data)
    elif re.search("^\d+",data):
        Home = re.search("^\d+",data)
    elif re.search("^\d",data):
        Home = re.search("^\d",data)
    else:
        return None
    return Home.group()
def Province(data):
    data_provice = ['นครราชสีมา','เชียงใหม่','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน','เพชรบูรณ์',
                    'ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช','สกลนคร',
                    'นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว','กาฬสินธุ์','อุทัยธานี',
                    'สุโขทัย','	แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร','นครพนม','สุพรรณบุรี','ฉะเชิงเทรา',
                    'มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร','ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ',
                    'พังงา','ยโสธร','หนองบัวลำภู','สระบุรี','ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา',
                    'สตูล','ชัยนาท','นครปฐม','นครนายก','ปัตตานี','กรุงเทพ','กรุงเทพมหานคร','กทม','ปทุมธานี','สมุทรปราการ','อ่างทอง',
                    'สมุทรสาคร','สิงห์บุรี','นนทบุรี','ภูเก็ต','สมุทรสงคราม']
    for i in data_provice:
        if re.search(i,data):
            Province=re.search(i,data)
            return Province.group()
            break
def District(data):
    if re.search("อ[.][ก-๙]+", data):
        dis =re.search("อ[.][ก-๙]+", data)
    elif re.search("อ[.]\s+[ก-๙]+", data):
        dis = re.search("อ[.]\s+[ก-๙]+", data)
    elif re.search("อำเภอ[ก-๙]+", data):
        dis = re.search("อำเภอ[ก-๙]+", data)
    elif re.search("อำเภอ\s+[ก-๙]+", data):
        dis = re.search("อำเภอ\s+[ก-๙]+", data)
    elif re.search("เขต[ก-๙]+", data):
        dis = re.search("เขต[ก-๙]+", data)
    elif re.search("เขต\s+[ก-๙]+",data):
        dis = re.search("เขต\s+[ก-๙]+",data)
    else:
        return None
    return dis.group()

def Alley(data):
    if re.search("ซอย\W\s\d+", data):
        Alley = re.search("ซอย\W\s\d+", data)
    elif re.search("ซ[.][ก-๙]+\s*\d*", data):
        Alley = re.search("ซ[.][ก-๙]+\s*\d*", data)
    elif re.search("ซ[.]\s+[ก-๙]+\s*\d*", data):
        Alley = re.search("ซ[.]\s+[ก-๙]+\s*\d*", data)
    elif re.search("ซอย[ก-๙]+\s*\d*", data):
        Alley = re.search("ซอย[ก-๙]+\s*\d*", data)
    elif re.search("ซอย\s+[ก-๙]+\s*\d*", data):
        Alley = re.search("ซอย\s+[ก-๙]+\s*\d*", data)
    elif re.search("ซอย[.][ก-๙]+\s*\d*", data):
        Alley = re.search("ซอย[.][ก-๙]+\s*\d*", data)
    elif re.search("ซอย[.]\s+[ก-๙]+\s*\d*", data) :
        Alley = re.search("ซอย[.]\s+[ก-๙]+\s*\d*", data)
    else:
        return None
    return Alley.group()
def Road(data):
    if re.search("ถ[.][ก-๙]+", data):
        Road=re.search("ถ[.][ก-๙]+", data)
    elif re.search("ถ[.][ก-๙]+\s*\d+", data):
        Road = re.search("ถ[.][ก-๙]+\s*\d+", data)
    elif re.search("ถนน[ก-๙]+", data):
        Road = re.search("ถนน[ก-๙]+", data)
    elif re.search("ถนน[ก-๙]+\s*\d+", data):
        Road = re.search("ถนน[ก-๙]+\s*\d+", data)
    else:
        return None
    return Road.group()
if __name__ == '__main__':
    data = Readdata()
    Homedata = []
    Writedata()
    for i in data:
        Homedata.append(Homecode(i))
        Homedata.append(Alley(i))
        Homedata.append(Road(i))
        Homedata.append(District(i))
        Homedata.append(Province(i))
        Homedata.append(Postcode(i))
        Insertdata(Homedata)
        Homedata = []
    print(Homedata)



