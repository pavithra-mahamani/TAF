from basetestcase import BaseTestCase


class XDCRNewBaseTest(BaseTestCase):

    def setUp(self):
        super(XDCRNewBaseTest, self).setUp()
        self.clusters = self.get_clusters()
        self.task = self.get_task()
        self.taskmgr = self.get_task_mgr()

    def tearDown(self):
        super(XDCRNewBaseTest, self).tearDown()
