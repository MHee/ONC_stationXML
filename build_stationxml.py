# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 12:18:50 2017

@author: mheesema
"""

#%%
import obspy
ONC_CONTACTS=[obspy.station.util.Person(names=['Martin Heesemann',],
                                        agencies=['Ocean Networks Canada',],
                                        emails=['mheesema@uvic.ca','info@oceannetworks.ca'],
                                        phones=[]),]
                                        
ONC_OPS=obspy.station.util.Operator(agencies=['Ocean Networks Canada',],
                                    contacts=ONC_CONTACTS,
                                    website='http://www.oceannetworks.ca')
                                    

#%% Network
def get_base_inventory():
    """Return basic inventory class with empty NV network."""
    return obspy.read_inventory('NV_network_stationXML.xml', format='STATIONXML')

#%% Station
# http://docs.obspy.org/archive/0.10.2/_modules/obspy/station/station.html#Station
inv = get_base_inventory()    
NV = inv[0]
#Comment=obspy.station.util.Comment('This is a comment.')
#NV.comments.append(Comment)
description="""Broadband seismometer, current meter, and bottom pressure
    recorder installed close by ODP borehole 1026B, Cascadia Basin, eastern 
    flank of the Juan de Fuca Ridge."""
    
NC27 = obspy.station.Station('NC27',
                             latitude=47.7623, longitude=-127.7579, elevation=-2656.0,
                             vault='burried caisson', geology = 'pelagic sediments',
                             creation_date=obspy.UTCDateTime('2009-09-14'),
                             termination_date=None,
                             description=description,
                             start_date=obspy.UTCDateTime('2009-09-14'),
                             end_date=None,
                             restricted_status='open')

NC27.site=obspy.station.util.Site(name='Cascadia Basin', 
                                  description='NEPTUNE Observatory Cascadia Basin '+
                                              'site near ODP borehole 1026B.',
                                  town=None, county=None,
                                  region='Northeast Pacific, off Vancouver Island',
                                  country='Canada')
#NC27.equipments.append(obspy.station.util.Equipment(...))
#NC27.comments.append(Comment)
#NC27.data_availability...

NC27.operators.append(ONC_OPS)
NC27.external_references.append(obspy.station.util.ExternalReference(
               uri='http://dmas.uvic.ca/DataSearch?location=NC27',
               description='More details on Oceans 2.0'))

#%% Channel
# http://docs.obspy.org/archive/0.10.2/_modules/obspy/station/channel.html

NC27_HHZ=obspy.station.Channel(code='HHZ', location_code='', latitude=NC27.latitude, 
                       longitude=NC27.longitude, elevation=NC27.elevation, depth=0.5)
#%%

NV.stations.append(NC27)
inv.write('NV_TEST_stationXML.xml','STATIONXML')
