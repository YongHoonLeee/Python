import json


j = {
    "employee":
        [
            {"id": 111, "name": "Yonghoon"},
            {"id": 222, "name": "Nancy"}
        ]
}
# ' 으로 데이터 둘러짐 '
print(j)

print("##################")

# python 안에서 읽을때는 dump's'
# json format 으로 읽으면 "" 으로 둘러짐 그냥 print(j) 와 다른점
print(json.dumps(j))

# wirte json file Using json.dump   not dump's'
with open('./WebAndNetwork/test.json', 'w') as f:
    json.dump(j, f)

print("##################")

# read json file Using json.load    not load's'
with open('./WebAndNetwork/test.json', 'r') as f:
    print(json.load(f))

"""

<?xml version='1.0' encoding = 'utf-8'?>
<root>
    <employee>
        <employ>
            <id>111</id>
            <name>Yonghoon</name>
        </employ>
        <employ>
            <id>222</id>
            <name>Nancy</name>
        </employ>
    </employee>
<root>

{
    "employee":
        [
            {"id": 111, "name": "Yonghoon"},
            {"id": 222, "name": "Nancy"}
        ]
}
"""
