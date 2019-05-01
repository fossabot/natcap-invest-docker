# coding=UTF-8
# hardcoded demo runner script for the pollination model

import time
import sys
import logging
import natcap.invest.pollination

logging.basicConfig(stream=sys.stdout, level=logging.WARN)

def now():
    return int(time.time() * 1000.0)
start_ms = now()
print('[INFO] starting up')

args = {
    u'farm_vector_path': u'/data/pollination/farms.shp',
    u'guild_table_path': u'/data/pollination/guild_table.csv',
    u'landcover_biophysical_table_path': u'/data/pollination/landcover_biophysical_table.csv',
    u'landcover_raster_path': u'/data/pollination/landcover.tif',
    u'results_suffix': u'',
    u'workspace_dir': u'/workspace/pollination',
}

if __name__ == '__main__':
    print('[INFO] starting execution of pollination model')
    natcap.invest.pollination.execute(args)
    elapsed_time = now() - start_ms
    print('[INFO] finished execution of pollination model, elapsed time {}ms'.format(elapsed_time))
