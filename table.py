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
