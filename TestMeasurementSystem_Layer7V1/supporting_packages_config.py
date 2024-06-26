#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
_______________________________________________________________________
COPY RIGHT: PRECISION NEUROSCIENCE
_______________________________________________________________________

PROJECT LAYER 7 VERSION 1
_______________________________________________________________________

\file    supporting_packages_config.py

\Brief : General class to contains configuration parameters for version 1. 
        This file shall be used along with Impedance_DataCollectoin.py script.

\author  Naresh Sambulu
_______________________________________________________________________

"""

class Display15_Dell:
    def __init__(self):
        self.version = "1.0.0"
        self.intan_path = "C:\Program Files\Intan\IntanRHX.exe"
        self.timeout = 60
        self.select_intan_ctrl_co_ordinates = [1346, 642]
        self.ok_button_select_frequency = [1084,585]
        self.get_number_of_ports_connected = [570,1094]
        self.select_BW = [44,517]
        self.select_Notch = [167,683]
        self.select_Notch_60Hz = [167, 730]
        self.select_impedence_tab = [122,524]
        self.select_Impedence_Test_Button = [141,562]
        self.select_ok_Impedence_Test = [1026,641]
        self.run_Impedence_measurement = [132,644]
        self.select_save_Impedence_Measurement = [230,674]
        self.select_to_delete_edit_path = [1458,80]
        self.select_to_write_file_name = [1385,1003]
        self.select_to_save = [1716,1098]
        self.select_tools = [200, 45]
        self.select_tools_probemap = [200,165]
        self.select_maximize_probemap_window = [1172,261]
        self.select_probemap_file = [15, 45]
        self.select_probemap_loadfile = [19,69]
        self.select_probemap_config_file_path = [1465,68]
        self.select_probemap_config_file = [288, 200]
        self.select_open_probemap_config_file = [1682,1095]
        self.select_best_fit_probmap = [1899, 87]
        self.select_ohm_icon_probemap = [1900,497]
        self.select_close_probemap = [1883,9]

        # Overnight Test Execution - 1st April 2024
        self.select_folder_icon = [213,78]
        self.select_to_delete_edit_path = [1458,80]
        self.select_to_write_file_name = [1385,1003]
        self.select_to_save = [1716,1098]
        self.select_to_record = [253,73]
        self.select_to_play = [141,70]
        self.select_to_stop_recording = [118,86]
        self.select_close_intan_app = [1895,0]

        # startstoprecording parameters
        self.select_playbutton = [144,77]
        self.select_scrollbar = [1898, 1008]
        self.select_display_ports = [571, 1090]
        self.select_portB = [493,944]
        self.select_portC = [494,953]
        self.select_portD = [505,976]
        self.select_portE = [507,492]
        self.select_portF = [518,1007]
        self.select_portG = [527,1040]
        self.select_portH = [484,1036]
        self.select_stopbutton = [105,75]

        # Number of times to run impedance, probemap, start and stop
        self.number_of_times_inner_loop = 1
        self.probemap_filename = "config"



class Display27:
    def __init__(self):
        self.version = "1.0.0"
        self.intan_path = "C:\Program Files\Intan\IntanRHX.exe"
        self.timeout = 60
        self.select_intan_ctrl_co_ordinates = [1302, 585]
        self.ok_button_select_frequency = [1074,538]
        self.get_number_of_ports_connected = [454,992]
        self.select_BW = [35,443]
        self.select_Notch = [143,575]
        self.select_Notch_60Hz = [120, 616]
        self.select_impedence_tab = [117,442]
        self.select_Impedence_Test_Button = [102,471]
        self.select_ok_Impedence_Test = [1022,569]
        self.run_Impedence_measurement = [100,537]
        self.select_save_Impedence_Measurement = [155,571]
        self.select_to_delete_edit_path = [971,58]
        self.select_to_write_file_name = [744,929]
        self.select_to_save = [1748,994]
        self.select_tools = [176, 32]
        self.select_tools_probemap = [183,146]
        self.select_maximize_probemap_window = [1190,213]
        self.select_probemap_file = [17, 33]
        self.select_probemap_loadfile = [19,56]
        self.select_probemap_config_file_path = [1487,61]
        self.select_probemap_config_file = [274, 161]
        self.select_open_probemap_config_file = [1754,995]
        self.select_best_fit_probmap = [1896, 67]
        self.select_ohm_icon_probemap = [1897,414]
        self.select_close_probemap = [1896,7]

        # Overnight Test Execution - 1st April 2024
        self.select_folder_icon = [177,61]
        self.select_to_delete_edit_path = [1525,54]
        #self.select_to_write_file_name = [744,929]
        self.select_to_write_file_name = [2361,1309]
        self.select_to_save = [1733,1000]
        self.select_to_record = [210,59]
        self.select_to_play = [117,59]
        self.select_to_stop_recording = [88,63]
        self.select_close_intan_app = [1895,9]

        # startstoprecording parameters
        self.select_playbutton = [117,61]
        self.select_scrollbar = [1899, 897]
        self.select_display_ports = [642, 985]
        self.select_portB = [559,813]
        self.select_portC = [538,837]
        self.select_portD = [542,856]
        self.select_portE = [528,871]
        self.select_portF = [541,889]
        self.select_portG = [540,908]
        self.select_portH = [549,925]
        self.select_stopbutton = [88,63]

        # Number of times to run impedance, probemap, start and stop
        self.number_of_times_inner_loop = 1
        self.probemap_filename = "config"

class Display15_Lenovo:
    def __init__(self):
        self.version = "1.0.0"
        #Display settings:
        #Scale to 150%
        #2560*1600
        self.intan_path = "C:\Program Files\Intan\IntanRHX.exe"
        self.timeout = 60
        self.select_intan_ctrl_co_ordinates = [1700, 845]
        self.ok_button_select_frequency = [1431,803]
        self.get_number_of_ports_connected = [699,1464]
        self.select_BW = [55,630]
        self.select_Notch = [205,813]
        self.select_Notch_60Hz = [185, 880]
        self.select_impedence_tab = [139,625]
        self.select_Impedence_Test_Button = [203,671]
        self.select_ok_Impedence_Test = [1366,854]
        self.run_Impedence_measurement = [178,773]
        self.select_save_Impedence_Measurement = [179,808]
        self.select_to_delete_edit_path = [2046,74]
        #self.select_to_write_file_name = [2209,1358]
        #self.select_to_write_file_name = [2214,1303]
        #self.select_to_write_file_name = [2395,1294]
        #self.select_to_write_file_name = [2528,1314]
        self.select_to_write_file_name = [319,1305]
        self.select_to_save = [2291,1474]
        self.select_tools = [227, 49]
        self.select_tools_probemap = [238,200]
        self.select_maximize_probemap_window = [1477,451]
        self.select_probemap_file = [16, 44]
        self.select_probemap_loadfile = [31,79]
        self.select_probemap_config_file_path = [2000,79]
        self.select_probemap_config_file = [362, 237]
        self.select_open_probemap_config_file = [2299,1481]
        self.select_best_fit_probmap = [2537, 95]
        self.select_ohm_icon_probemap = [2535,586]
        self.select_close_probemap = [2523,12]

        # Overnight Test Execution - 1st April 2024
        self.select_folder_icon = [251,81]
        #self.select_to_delete_edit_path = [2046,74]
        #self.select_to_write_file_name = [2209,1358]
        #self.select_to_save = [2291,1474]
        #self.select_to_save = [2312,1306]
        self.select_to_record = [294,85]
        self.select_to_play = [163,83]
        self.select_to_stop_recording = [121,87]
        self.select_close_intan_app = [1895,9]

        # startstoprecording parameters
        self.select_playbutton = [117,61]
        self.select_scrollbar = [1899, 897]
        self.select_display_ports = [642, 985]
        self.select_portB = [559,813]
        self.select_portC = [538,837]
        self.select_portD = [542,856]
        self.select_portE = [528,871]
        self.select_portF = [541,889]
        self.select_portG = [540,908]
        self.select_portH = [549,925]
        self.select_stopbutton = [87,58]

        # Number of times to run impedance, probemap, start and stop
        self.number_of_times_inner_loop = 1
        self.probemap_filename = "config"


class Display12_Microsoft:
    def __init__(self):
        self.version = "1.0.0"
        #Display settings:
        #Scale to 150%
        #2560*1600
        self.intan_path = "C:\Program Files\Intan\IntanRHX.exe"
        self.timeout = 60
        self.select_intan_ctrl_co_ordinates = [1544, 804]
        self.ok_button_select_frequency = [1292,769]
        self.get_number_of_ports_connected = [699,1381]
        self.select_BW = [54,622]
        self.select_Notch = [205,815]
        self.select_Notch_60Hz = [172, 875]
        self.select_impedence_tab = [136,631]
        self.select_Impedence_Test_Button = [136,674]
        self.select_ok_Impedence_Test = [1202,812]
        self.run_Impedence_measurement = [132,770]
        self.select_save_Impedence_Measurement = [147,813]
        self.select_to_delete_edit_path = [1697,73]
        #self.select_to_write_file_name = [2209,1358]
        #self.select_to_write_file_name = [2214,1303]
        #self.select_to_write_file_name = [2395,1294]
        #self.select_to_write_file_name = [2528,1314]
        self.select_to_write_file_name = [1936,1279]
        self.select_to_save = [2008,1390]
        self.select_tools = [239, 51]
        self.select_tools_probemap = [241,207]
        self.select_maximize_probemap_window = [1323,412]
        self.select_probemap_file = [19, 47]
        self.select_probemap_loadfile = [13,79]
        self.select_probemap_config_file_path = [1767,65]
        self.select_probemap_config_file = [409, 211]
        self.select_open_probemap_config_file = [2014,1388]
        self.select_best_fit_probmap = [2225, 95]
        self.select_ohm_icon_probemap = [2230,586]
        self.select_close_probemap = [2218,12]

        # Overnight Test Execution - 1st April 2024
        self.select_folder_icon = [248,90]
        #self.select_to_delete_edit_path = [2046,74]
        #self.select_to_write_file_name = [2209,1358]
        #self.select_to_save = [2291,1474]
        #self.select_to_save = [2312,1306]
        self.select_to_record = [292,85]
        self.select_to_play = [162,85]
        self.select_to_stop_recording = [123,86]
        self.select_close_intan_app = [1895,9]

        # startstoprecording parameters
        self.select_playbutton = [117,61]
        self.select_scrollbar = [1899, 897]
        self.select_display_ports = [642, 985]
        self.select_portB = [559,813]
        self.select_portC = [538,837]
        self.select_portD = [542,856]
        self.select_portE = [528,871]
        self.select_portF = [541,889]
        self.select_portG = [540,908]
        self.select_portH = [549,925]
        self.select_stopbutton = [87,58]

        # Number of times to run impedance, probemap, start and stop
        self.number_of_times_inner_loop = 1
        self.probemap_filename = "config"

