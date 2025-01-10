g_evene_queue = []

def add_event(event):
    global g_evene_queue
    g_evene_queue.append(event)


def clear_events():
    global g_evene_queue
    g_evene_queue = []
    