from compiler import compiler_query  # Импортируем функцию компиляции запроса
import json

with open('diameterJson.json', 'r') as file:
    data = json.load(file)

query2 = "/child::/AVP_2/ancestor::/AVP_2/following::/AVP_2.2.1.1"
query3 = "/child::/AVP_2.2/preceding_sibling::/AVP_2.2.1/child::/AVP_2.2.1"

request_child = "/child::/AVP_2.2"  # AVP_2.2.1, AVP_2.2.2
request_parent_not_iden = "/child::/AVP_2.2/parent::/AVP_2.2"  # AVP_2
request_parent = "/child::/AVP_2/parent::/AVPs"  # AVP_2.2.1
request_descendant_not_iden = "/child::/AVP_2/parent::/AVP_2.2.1/descendant::/"  # AVP_2.2.1, AVP_2.2.1.1
request_descendant = "/descendant::/AVP_2.2.1.1"  # AVP_2.2.1.1
request_descendant_or_self_not_iden = "/child::/AVP_2.2/parent::/AVP_2.2.1/descendant_or_self::/"  # AVP_2.2.1, AVP_2.2.1.1
request_descendant_or_self = "/child::/AVP_2.2/parent::/AVP_2.2.1/descendant_or_self::/AVP_2.2.1.1"  # AVP_2.2.1.1
request_ancestor_not_iden = "/child::/AVP_2.2.2/ancestor::/"  # AVP_2, AVPs

request_ancestor = "/child::/AVP_2.2/ancestor::/"  # AVP_2.2

request_following = "/child::/AVP_2/preceding::/AVP_2.2" # AVP
request_ancestor_or_self = ""

request_following_siblings = ""
request_preceding = ""
request_preceding_siblings = ""

print("Axis:")
print("----------------")

print(f"request_child                        -> {compiler_query(request_child, data)}")
print(f"request_parent_not_iden              -> {compiler_query(request_parent_not_iden, data)}")
print(f"request_parent                       -> {compiler_query(request_parent, data)}")
print(f"request_descendant_not_iden          -> {compiler_query(request_descendant_not_iden, data)}")
print(f"request_descendant                   -> {compiler_query(request_descendant, data)}")
print(f"request_descendant_or_self_not_iden  -> {compiler_query(request_descendant_or_self_not_iden, data)}")
print(f"request_descendant_or_self           -> {compiler_query(request_descendant_or_self, data)}")
print(f"request_ancestor_not_iden            -> {compiler_query(request_ancestor_not_iden, data)}")
print(f"request_ancestor                     -> {compiler_query(request_ancestor, data)}")
print(f"request_following                    -> {compiler_query(request_following, data)}")

print("----------------")

print("")
results = compiler_query(query2, data)
results3 = compiler_query(query3, data)
print(results)
print(results3)
