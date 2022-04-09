#under the hood

head = {
    "Value": 11,
    "next": {
        "Value": 3,
        "next": {
            "Value": 27,
            "next": {
                "Value": 7,
                "next": None
                }
            } 
        }
}

print(head['next']['next']['Value'])
# print(my_linked_list.head.next.next.value)