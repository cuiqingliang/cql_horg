from test_po.page.main import MianPage


class Test_Con:
    def setup(self):
        self.main=MianPage()
    def test_add_con(self):
        name='hh'
        account='12'
        phonenum='13211111111'
        ele=self.main.addcomtact_click().addcon(name,account,phonenum)
        ele.getcontact(name)
        assert ele
    def test_delete_con(self):
        name='hh'
        ele1=self.main.contact_click().delete_contact()
        ele1.delete_con(name).getcontact(name)