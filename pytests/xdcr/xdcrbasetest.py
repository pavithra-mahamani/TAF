from basetestcase import BaseTestCase


class XDCRNewBaseTest(BaseTestCase):

    def setUp(self):
        super(XDCRNewBaseTest, self).setUp()
        self.clusters = self.get_clusters()
        for cluster in self.clusters:
            cluster_util = ClusterUtils(cluster, self.task_manager)
            cluster_util.add_all_nodes_then_rebalance(cluster.servers[1:])
        self.task = self.get_task()
        self.taskmgr = self.get_task_mgr()

    def tearDown(self):
        super(XDCRNewBaseTest, self).tearDown()
