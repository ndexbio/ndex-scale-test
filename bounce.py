import ndex.client as nc
from networkn import NdexGraph
import thread
import copy
import json

def update_network(thread_name, G, network_id):
    ndex_dev = nc.Ndex("http://dev.ndexbio.org", username="david_test", password="david_test")
    # ndex_dev.set_debug_mode(True)
    G = copy.deepcopy(G)
    G.set_name('RAS: ' + network_id)
    for i in range(10000):
        print i, thread_name, network_id
        ndex_dev.update_cx_network(json.dumps(G.to_cx()), network_id)
        print 'done with', i, thread_name,
    print 'Thread ', thread_name, ' finished updating.'

def get_edges(thread_name, G, network_id):
    ndex_dev = nc.Ndex("http://public.ndexbio.org", username="drh", password="drh")
    # ndex_dev.set_debug_mode(True)
    route = "/network/%s/edge/asNetwork/0/500" % (network_id)
    for i in range(50000):
        ndex_dev.get(route)

ndex = nc.Ndex("http://public.ndexbio.org", username="drh", password="drh")
# ndex_dev = nc.Ndex("http://test.ndexbio.org", username="david_test", password="david_test")

noi_id = '50e3dff7-133e-11e6-a039-06603eb7f303'

noi_cx = ndex.get_network_as_cx_stream(noi_id).json()
noi = NdexGraph(noi_cx)

print 'start'
try:
    # DEV
    thread.start_new_thread(update_network, ('thread-1', noi, '65141932-397d-11e6-ab1d-06832d634f41'))
    thread.start_new_thread(update_network, ('thread-2', noi, '53a00511-397d-11e6-ab1d-06832d634f41'))
    thread.start_new_thread(update_network, ('thread-3', noi, '3db7a6e0-397d-11e6-ab1d-06832d634f41'))


    # TEST
    # thread.start_new_thread(update_network, ('thread-1', noi, '13e3356b-3990-11e6-a295-028f28cd6a5b'))
    # thread.start_new_thread(update_network, ('thread-2', noi, '1e6b21ac-3990-11e6-a295-028f28cd6a5b'))
    # thread.start_new_thread(update_network, ('thread-3', noi, '27eaecbd-3990-11e6-a295-028f28cd6a5b'))

    # PUBLIC
    # thread.start_new_thread(update_network, ('thread-1', noi, '7e4f833f-3991-11e6-805a-06603eb7f303'))
    # thread.start_new_thread(update_network, ('thread-2', noi, '8974c0f0-3991-11e6-805a-06603eb7f303'))
    # thread.start_new_thread(update_network, ('thread-3', noi, '9499fea1-3991-11e6-805a-06603eb7f303'))

    # thread.start_new_thread(get_edges, ('thread-4', noi, 'c12521b6-2f64-11e6-a3ba-06832d634f41'))
    # thread.start_new_thread(get_edges, ('thread-5', noi, 'd7f19e5a-2f64-11e6-a3ba-06832d634f41'))
    # thread.start_new_thread(get_edges, ('thread-6', noi, 'd1f1d248-2f64-11e6-a3ba-06832d634f41'))

except:
    print 'Error: Unable to launch threads'

print 'Done launching threads.'

while 1:
   pass



#
# for i in range(1000):
#     print i
#     ndex_dev.update_cx_network(noi.to_CX_stream(), noi_id)


# ndex_dev = nc.Ndex("http://test.ndexbio.org", username="drh", password="drh")
#
# noi.write_to('ras_machine.cx')
#
# noi.set_name("1. RAS machine")
# ndex.save_cx_stream_as_new_network(noi.to_cx_stream())
#
# noi.set_name("2. RAS machine")
# ndex.save_cx_stream_as_new_network(noi.to_cx_stream())
#
# noi.set_name("3. RAS machine")
# ndex.save_cx_stream_as_new_network(noi.to_cx_stream())





