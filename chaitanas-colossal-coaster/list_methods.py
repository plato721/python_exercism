"""Functions to manage and organize queues at Chaitana's roller coaster."""
NORMAL_TYPE = 0
EXPRESS_TYPE = 1


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    queue_for_ticket = express_queue if is_express(ticket_type) else normal_queue
    return add_to_queue(person_name, queue_for_ticket)


def is_express(ticket_type):
    return ticket_type == EXPRESS_TYPE


def add_to_queue(person, queue):
    queue.append(person)
    return queue


def find_my_friend(queue, friend_name):
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    return queue.count(person_name)


def remove_the_last_person(queue):
    return queue.pop()


def sorted_names(queue):
    return sorted(queue)
