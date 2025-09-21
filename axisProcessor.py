class AxisProcessor:
    def __init__(self, parent_map):
        self.parent_map = parent_map

    def process(self, axis, current_data, identifier=None):

        if axis == 'child::/':
            return self.find_child(current_data, identifier)



        elif axis == 'parent::/':
            return self.find_parent(current_data, identifier)

        elif axis == 'ancestor::/':
            return self.find_ancestor(current_data, identifier)

        elif axis == 'ancestor_or_self::/':
            return self.find_ancestors_or_self(current_data, identifier)

        elif axis == 'descendant::/':
            return self.find_descendant(current_data, identifier)

        elif axis == 'descendant_or_self::/':
            return self.find_descendant_or_self(current_data, identifier)

        elif axis == 'following::/':
            return self.find_following(current_data, identifier)

        elif axis == 'following_sibling::/':
            return self.find_following_sibling(current_data, identifier)

        elif axis == 'preceding::/':
            return self.find_preceding(current_data, identifier)

        elif axis == 'preceding_sibling::/':
            return self.find_preceding_sibling(current_data, identifier)

    def find_child(self, current_data, identifier):
        """
        Рекурсивно ищет дочерние элементы в JSON данных по идентификатору 'label'.
        """
        results = []

        if isinstance(current_data, dict):
            # Если это словарь, проверяем ключ 'label' для поиска совпадений
            if 'label' in current_data and (identifier is None or current_data['label'] == identifier):
                results.append(current_data)

            # Рекурсивно проходим по всем значениям словаря
            for value in current_data.values():
                results.extend(self.find_child(value, identifier))

        elif isinstance(current_data, list):
            # Если это список, рекурсивно проходим по всем элементам
            for item in current_data:
                results.extend(self.find_child(item, identifier))

        return results
    def find_parent(self, current_data, identifier=None):
        """
        Ищет родителя для текущего элемента.
        Если указан идентификатор, находит родителя и затем выполняет поиск непосредственных детей
        с указанным идентификатором.
        """
        if isinstance(current_data, list):
            # Для списка ищем родителей всех элементов
            parents = [self.parent_map.get(item.get('label')) for item in current_data if isinstance(item, dict)]
        elif isinstance(current_data, dict) and 'label' in current_data:
            # Для одного элемента ищем его родителя
            parents = [self.parent_map.get(current_data['label'])]
        else:
            parents = []

        # Убираем пустые значения
        parents = [parent for parent in parents if parent]

        if identifier:
            # Если задан идентификатор, находим дочерние элементы только на один уровень ниже
            children = []
            for parent in parents:
                if 'value' in parent and isinstance(parent['value'], list):
                    # Ищем среди непосредственных детей
                    children.extend([child for child in parent['value'] if child.get('label') == identifier])
            return children
        else:
            # Если идентификатор не задан, возвращаем родителей
            return parents

    def find_ancestor(self, current_data, identifier=None):
        """
        Ищет всех предков для текущего элемента, начиная с его родителя и до самого верхнего уровня.
        """
        ancestors = []

        if isinstance(current_data, dict) and 'label' in current_data:
            # Получаем родителя текущего элемента
            parent = self.parent_map.get(current_data['label'])
            while parent:
                # Добавляем родителя в список предков
                ancestors.append(parent)

                # Получаем следующего предка (родителя родителя)
                parent = self.parent_map.get(parent.get('label'))

        elif isinstance(current_data, list):
            for item in current_data:
                # Для списка обрабатываем каждый элемент
                ancestors.extend(self.find_ancestor(item, identifier))

        if identifier:
            # Если задан идентификатор, ищем предков с данным идентификатором
            ancestors = [ancestor for ancestor in ancestors if 'label' in ancestor and ancestor['label'] == identifier]

        return ancestors

    def find_ancestors_or_self(self, current_data, identifier=None):
        """
        Ищет предков или сам текущий элемент, если задан идентификатор, или все предков,
        включая сам текущий элемент.
        Если задан идентификатор, ищем предков с этим идентификатором.
        """
        # Если задан идентификатор, ищем только предков, как в ancestor
        if identifier:
            return self.find_ancestor(current_data, identifier)

        ancestors = self.find_ancestor(current_data)

        if isinstance(current_data, dict) and 'label' in current_data:
            # Если это словарь и есть метка, добавляем сам текущий элемент
            ancestors.append(current_data)

        elif isinstance(current_data, list):
            # Если это список, добавляем все элементы списка
            for item in current_data:
                ancestors.extend(self.find_ancestors_or_self(item, identifier))

        return ancestors

    def find_descendant(self, current_data, identifier=None):
        """
        Ищет все потомки для текущего элемента, включая дочерние элементы, их потомков и т.д.
        Если задан идентификатор, ищем только потомков с этим идентификатором.
        """
        descendants = []

        if isinstance(current_data, dict) and 'label' in current_data:
            # Ищем дочерние элементы
            descendants.extend(self.find_child(current_data, identifier))

            # Рекурсивно ищем потомков среди дочерних элементов
            for value in current_data.values():
                descendants.extend(self.find_descendant(value, identifier))

        elif isinstance(current_data, list):
            # Для списка ищем потомков среди всех элементов
            for item in current_data:
                descendants.extend(self.find_descendant(item, identifier))

        return descendants

    def find_descendant_or_self(self, current_data, identifier=None):
        """
        Ищет все потомков для текущего элемента, включая дочерние элементы, их потомков и т.д.
        Также добавляет сам текущий элемент в результат.
        Если задан идентификатор, ищем только потомков с этим идентификатором.
        """
        descendants = []

        # Добавляем сам текущий элемент (self)
        if isinstance(current_data, dict) and 'label' in current_data:
            if identifier is None or current_data.get('label') == identifier:
                descendants.append(current_data)

        elif isinstance(current_data, list):
            for item in current_data:
                if isinstance(item, dict) and (identifier is None or item.get('label') == identifier):
                    descendants.append(item)

        # Рекурсивно ищем всех потомков (descendants)
        if isinstance(current_data, dict):
            for value in current_data.values():
                descendants.extend(self.find_descendant_or_self(value, identifier))
        elif isinstance(current_data, list):
            for item in current_data:
                descendants.extend(self.find_descendant_or_self(item, identifier))

        return descendants

    def find_following(self, current_data, identifier):
        all_nodes = self.in_order_traversal(current_data)
        following_nodes = []

        current_index = None
        for i, node in enumerate(all_nodes):
            if 'label' in node and node['label'] == identifier:
                current_index = i
                break

        if current_index is not None:
            following_nodes = all_nodes[current_index + 1:]

        return following_nodes

    def find_following_sibling(self, current_data, identifier):
        siblings = []

        parent = self.find_parent(current_data)
        if parent:
            parent = parent[0]  # Assuming a single parent
            if 'value' in parent and isinstance(parent['value'], list):
                found = False
                for child in parent['value']:
                    if found and (identifier is None or child.get('label') == identifier):
                        siblings.append(child)
                    if 'label' in child and child['label'] == identifier:
                        found = True

        return siblings

    def find_preceding(self, current_data, identifier):
        all_nodes = self.in_order_traversal(current_data)
        preceding_nodes = []

        current_index = None
        for i, node in enumerate(all_nodes):
            if 'label' in node and node['label'] == identifier:
                current_index = i
                break

        if current_index is not None:
            preceding_nodes = all_nodes[:current_index]

        return preceding_nodes

    def find_preceding_sibling(self, current_data, identifier):
        siblings = []

        parent = self.find_parent(current_data)
        if parent:
            parent = parent[0]  # Assuming a single parent
            if 'value' in parent and isinstance(parent['value'], list):
                for child in parent['value']:
                    if 'label' in child and child['label'] == identifier:
                        break
                    siblings.append(child)

        return siblings

    def in_order_traversal(self, current_data):
        nodes = []
        if isinstance(current_data, dict):
            if 'value' in current_data:
                if isinstance(current_data['value'], list):
                    for child in current_data['value']:
                        nodes.extend(self.in_order_traversal(child))
            nodes.append(current_data)
        elif isinstance(current_data, list):
            for item in current_data:
                nodes.extend(self.in_order_traversal(item))
        return nodes