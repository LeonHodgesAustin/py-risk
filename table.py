import threading
import Queue


def table(args):
    '''
    Simple table for gamblers
    '''
    pool = []
    queue = Queue.Queue()
    player_results = []
    players_at_table = args[0]
    for i in range(players_at_table):
        t = threading.Thread(target=args[1], args=(args[2], queue))
        pool.append(t)
        t.start()
        response = queue.get()
        player_results.append(response)
    for thread in pool:
        thread.join()

    return player_results


def sequential(args):
    '''
    Simple table for gamblers
    '''
    player_results = []
    players_at_table = args[0]
    for i in range(players_at_table):
        player_results.append(args[1](args[2]))

    return player_results


def table_sequential(args):
    '''
    Simple table for gamblers
    '''
    pool = []
    queue = Queue.Queue()
    player_results = []
    players_at_table = args[0]
    for i in range(players_at_table):
        t = threading.Thread(target=sequential_queue, args=(args, queue))
        pool.append(t)
        t.start()
        response = queue.get()
        player_results.append(response)
    for thread in pool:
        thread.join()

    return player_results


def sequential_queue(args, queue):
    '''
    Simple table for gamblers
    '''
    player_results = []
    players_at_table = args[0]
    for i in range(players_at_table):
        player_results.append(args[1](args[2]))

    return player_results
