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

class Display15:
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
        self.select_tools_probmap = [200,165]
        self.select_maximize_probemap_window = [1172,261]
        self.select_probemap_file = [921, 537]
        self.select_probemap_loadfile = [921,557]
        self.select_probemap_config_file_path = [1389,60]
        self.select_probemap_config_file = [355, 227]
        self.select_open_probemap_config_file = [1700,1096]
        self.select_best_fit_probmap = [1896, 85]
        self.select_ohm_icon_probemap = [1900,505]
        self.select_close_probemap = [1887,12]

        # Overnight Test Execution - 1st April 2024
        self.select_folder_icon = [213,78]
        self.select_to_delete_edit_path = [1458,80]
        self.select_to_write_file_name = [1385,1003]
        self.select_to_save = [1716,1098]
        self.select_to_record = [253,73]
        self.select_to_stop_recording = [104,75]
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
        self.select_to_write_file_name = [744,929]
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
        self.select_stopbutton = [87,58]

        # Number of times to run impedance, probemap, start and stop
        self.number_of_times_inner_loop = 18
        self.probemap_filename = "config"



