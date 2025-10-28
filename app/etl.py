import json
import os

class ETLPipeline:
    def __init__(self):
        pass

    def load_json(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)


    def get_first_field(self, data, field):
        if isinstance(data, list) and data:
            return data[0].get(field)
        elif isinstance(data, dict):
            return data.get(field)
        return None

    def get_version(self, data):
        if isinstance(data, dict) and "message" in data:
            messages = data["message"]
            if isinstance(messages, list) and messages:
                return messages[0].get("version")
        return None


    def run(self):
        whoami = self.load_json(os.path.join("mock_data", "input", "whoami.json"))
        vms_all = self.load_json(os.path.join("mock_data", "input", "vms_all.json"))
        vms_by_user = self.load_json(os.path.join("mock_data", "input", "vms_by_user.json"))
        vms_delete = self.load_json(os.path.join("mock_data", "input", "vms_delete.json"))
        vms_detail = self.load_json(os.path.join("mock_data", "input", "vms_detail.json"))
        vms_version = self.load_json(os.path.join("mock_data", "input", "vms_version.json"))
        vms_cluster = self.load_json(os.path.join("mock_data", "input", "vms_cluster.json"))

        record = {
            "username": self.get_first_field(whoami, "username"),
            "vm_id": self.get_first_field(vms_all, "vm_id"),
            "clusterid": self.get_first_field(vms_by_user, "clusterid"),
            "message": self.get_first_field(vms_delete, "message"),
            "podname": self.get_first_field(vms_detail, "podname"),
            "deployedvmstatus": self.get_first_field(vms_cluster, "deployedvmstatus"),
            "version": self.get_version(vms_version),
            "deployedvmtimestamp": self.get_first_field(vms_cluster, "deployedvmtimestamp")
        }

        with open("output.json", "w") as outfile:
            json.dump([record], outfile, indent=2)