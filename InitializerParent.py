class ParentInitializer:
    def __init__(self, json_data):
        self.json_data = json_data
        self.parent_map = {}
        self.initialize_parent_links(self.json_data, None)

    def initialize_parent_links(self, data, parent=None):
        if isinstance(data, dict):
            if 'label' in data:
                self.parent_map[data['label']] = parent

            for key, value in data.items():
                self.initialize_parent_links(value, data)

        elif isinstance(data, list):
            for item in data:
                self.initialize_parent_links(item, parent)

    def get_parent_map(self):
        return self.parent_map