import openpyxl

def get_login_data():
    workbook = openpyxl.load_workbook(#paste the login excel file path present in test_data)
    sheet = workbook[]

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    return data