from collections import deque, defaultdict
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """

        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                in_degree[recipe] += 1
        queue = deque(supplies)
        result = []
        while queue:
            ingredient = queue.popleft()
            if ingredient in recipes:
                result.append(ingredient)
            for recipe in graph[ingredient]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    queue.append(recipe)
        
        return result
        

            