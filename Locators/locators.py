class locators():
    # Login page webelements
    UserID = "uid"
    Pwd = "password"
    Loginbtn = "btnLogin"
    Resetbtn = "btnReset"

    # Manager Page or Landing page
    Heading_text = "//*[@class='heading3']"

    # New Customer page web elements
    Newcustomerlink = "/html/body/div[3]/div/ul/li[2]/a"
    custname = "name"
    Gendermale = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]"
    Genderfemale = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]"
    Dob = "dob"
    Address = "addr"
    City = "city"
    State = "state"
    Pin = "pinno"
    mobilenum = "telephoneno"
    emailid = "emailid"
    password_txt = "password"
    submit_btn = "sub"
    reset_btn = "res"
    Confirmmesg = "//*[contains(text(),'Customer Registered Successfully!!!')]"
    custid = "//*[@id='customer']/tbody/tr[4]/td[2]"

    # Edit Customer page web elements
    Editcustomerlink = "/html/body/div[2]/div/div/ul/li[3]/a"
    Edit_custid = "cusid"
    Edit_submit = "AccSubmit"
    Reset = "reset"
