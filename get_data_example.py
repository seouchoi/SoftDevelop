#오직 실험용 코드(아무것도 아님)
from DBHandler.contest_DBhandler import Contest_DBHandler

con = Contest_DBHandler()

data = con.get_contest_by_category_id(3)
data.to_list()
print(len(data))