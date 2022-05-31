'''
visual of linked list as compared to dictionary
although this is not the exact representation.
'''

head = {
    "value":11,
    "next":{
            "value":23,
            "next":{
                    "value":7,
                    "next":{
                            "value":11,
                            "next":None
                        }
                }
        }
}

print(head["next"]["next"]["value"])


# This will only run witha linked list.
# print(myLinkedList.head.next.next.value)