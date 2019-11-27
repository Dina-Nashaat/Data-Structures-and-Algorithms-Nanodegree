from collections import defaultdict
import re

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = ''

    def insert(self, resource):
        # Insert the node as before
        return self.children[resource]

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.not_found_handler = not_found_handler

    def insert(self, resources, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for idx, resource in enumerate(resources):
            if not (idx == len(resources) - 1 and resource == '/'):
                current_node = current_node.children[resource]

        current_node.handler = handler
        trailing_slash = current_node.insert('/')
        trailing_slash.handler = handler

    def find(self, resources):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for resource in resources:
            if resource not in current_node.children:
                return self.not_found_handler
            current_node = current_node.children[resource]
        if current_node.handler:
            return current_node.handler
        else:
            return self.not_found_handler
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(not_found_handler)
        self.routes.insert(['/'], 'root handler')

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the path parts
        # as a list to the RouteTrie
        resources = self.split_path(path)
        self.routes.insert(resources, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        resources = self.split_path(path)
        return self.routes.find(resources)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        resources = re.split(r'(\W)', path)
        return list(filter(None, resources))

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route


# some lookups with the expected output
print("==============================")
print("path => /home/about/")
router = Router("Not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about/", "about handler")  # add a route
print('lookup / =>', router.lookup("/")) # should print 'root handler'
print('lookup /home =>', router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print('lookup /home/about =>', router.lookup("/home/about")) # should print 'about handler'
print('lookup /home/about/ =>', router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print('lookup /home/about/me =>', router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

print("==============================")
print("path => /home/about")
router = Router("Not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
print('lookup / =>', router.lookup("/")) # should print 'root handler'
print('lookup /home =>', router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print('lookup /home/about =>', router.lookup("/home/about")) # should print 'about handler'
print('lookup /home/about/ =>', router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print('lookup /home/about/me =>', router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one