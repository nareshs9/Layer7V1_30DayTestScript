#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
_______________________________________________________________________

PROJECT Layer 7 Version 1
_______________________________________________________________________

\file    Impedance_DataCollection.py

\Brief : Pyton script to automataically record data from Intan RHX software.

\author  Naresh Sambulu
_______________________________________________________________________

Requirements:
V1T-TMS-0005	The test measurement system automated data collection script shall have a capability to perform the following:
V1T-TMS-0005A    The script shall be able to launch and close the Intan RHX software.
V1T-TMS-0005B	The script shall be able to set notch filter to 60Hz.
V1T-TMS-0005C	The script shall be able to create log folder for every run.
V1T-TMS-0005D	The script shall be able to run impedance measurement test multiple times and save impedance measurement test results in the current log folder.
V1T-TMS-0005E	The script shall be able to capture required screens and save it in appropriate log folder.
V1T-TMS-0005F	The script shall be able to select “Sampling Rate” as 20KHz.
V1T-TMS-0005G	The script shall be able to create and select the appropriate log folder to save the output files on the compute unit that is being recorded.
V1T-TMS-0005H	The script shall be able to start and stop the recording on Intan RHX software.
V1T-TMS-0005I	The script shall be able to record and store output files for twenty seconds by default.
V1T-TMS-0005J	The script shall be able to provide an option for user to program the number of impedance test and data recording sessions.
"""
import pygetwindow
import pyautogui
from PIL import Image
import os
import time
from datetime import datetime
from supporting_packages_config import Display15
from supporting_packages_config import Display27
import shutil
import logging
import sys
import psutil
import subprocess

# logger: Hirearchical logging
logger = logging.getLogger(__name__)


class ImpedanceMeasurement:
    def __init__(self, path, app_loc, screens_path, config_ele, record_file_name, impedance_fname, data_recording, probemap):
        self.path = path
        self.app_loc = app_loc
        self.window = 0
        self.screens_path = screens_path
        self.config_ele = config_ele
        self.record_file_name = record_file_name
        self.impedance_fname = impedance_fname
        self.data_recording = data_recording
        self.probemap = probemap
    

    def startIntanRHX(self):
        logger.info("Starting Intan Application in 2 seconds which is located in %s", self.app_loc)
        time.sleep(2)
        
        # Start Intan RHX Application
        start_status = os.startfile(self.app_loc)
        
        time.sleep(3)
        self.window_titles = pygetwindow.getAllTitles()
        logger.info("All the list of windows that are open on this pc %s", self.window_titles)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        logger.info(self.window.title)

        #save first screen
        screenObj = ScreenCapture(self.screens_path, self.window, self.window.title, True)
        screen_saved = screenObj.saveScreenShots()
        logger.info("Screen record saved successfully %d", screen_saved)
        time.sleep(2)
        
        
        # click on open button of "Select Intan Controller"
        pyautogui.moveTo(self.config_ele.select_intan_ctrl_co_ordinates[0], self.config_ele.select_intan_ctrl_co_ordinates[1])
        time.sleep(2)
        test2 = pyautogui.click(x=self.config_ele.select_intan_ctrl_co_ordinates[0], y=self.config_ele.select_intan_ctrl_co_ordinates[1])
        time.sleep(10)
        self.window_titles = pygetwindow.getAllTitles()
        logger.info("list of windows that are open currently %s", self.window_titles)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        logger.info("Looking for main Intan RHX Application %s", self.window.title)
        pyautogui.moveTo(1084,595)
        #save second screen
        screenObj2 = ScreenCapture(self.screens_path, self.window, self.window.title, True)
        screen_saved = screenObj2.saveScreenShots()
        logger.info("Screen record saved successfully %d", screen_saved)
        

        # move to ok button to select 20Khz
        #pyautogui.moveTo(1084,595)
        pyautogui.moveTo(self.config_ele.ok_button_select_frequency[0], self.config_ele.ok_button_select_frequency[1])
        time.sleep(2)
        # click on ok button with 20KHz
        #click_ok = pyautogui.click(1084,585)
        test2 = pyautogui.click(x=self.config_ele.ok_button_select_frequency[0], y=self.config_ele.ok_button_select_frequency[1])

        time.sleep(10)
        self.window_titles = pygetwindow.getAllTitles()
        logger.info("Main Intan Controller %s", self.window_titles)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        logger.info("Looking for main Intan RHX Application Finally %s", self.window.title)
        #pyautogui.moveTo(1084,595)
        #save second screen
        screenObj3 = ScreenCapture(self.screens_path, self.window, self.window.title, True)
        screen_saved = screenObj3.saveScreenShots()

        #Verify all 8 ports connected and identified using Intan Software
        #move to verify number of ports connected
        logger.info("move to verify number of ports")
        logger.info("Co-ordinates to verify number of ports are %d, %d",self.config_ele.get_number_of_ports_connected[0], self.config_ele.get_number_of_ports_connected[1])
        pyautogui.moveTo(self.config_ele.get_number_of_ports_connected[0], self.config_ele.get_number_of_ports_connected[1])
        time.sleep(2)
        # click on to verify number of ports connected
        click_ok = pyautogui.click(self.config_ele.get_number_of_ports_connected[0], self.config_ele.get_number_of_ports_connected[1])

        time.sleep(5)
        self.window_titles = pygetwindow.getAllTitles()
        logger.info("Main Intan Application %s", self.window_titles)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        logger.info("Looking for number of ports connected %s", self.window.title)
        #pyautogui.moveTo(1084,595)
        #save second screen
        screenObj4 = ScreenCapture(self.screens_path, self.window, "Number_of_ports_connected", False)
        screen_saved = screenObj4.saveScreenShots()

        # Select "BW" on left pane and take screen capture
        # Move to "BW" option
        logger.info("Co-ordinates to move to BW %d, %d",self.config_ele.select_BW[0], self.config_ele.select_BW[1])
        pyautogui.moveTo(self.config_ele.select_BW[0], self.config_ele.select_BW[1])
        time.sleep(2)
        #click_ok = pyautogui.click(570,1094)
        click_ok = pyautogui.click(self.config_ele.select_BW[0], self.config_ele.select_BW[1])
        time.sleep(2)
        self.window_titles = pygetwindow.getAllTitles()
        #print("Main Intan Application %s", self.window_titles)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        #print("Looking for number of ports connected", self.window.title)

        screenObj4 = ScreenCapture(self.screens_path, self.window, "BW_Selected", False)
        screen_saved = screenObj4.saveScreenShots()

        # Select "NotchFilter" under "BW" pane and take screen capture
        pyautogui.moveTo(self.config_ele.select_Notch[0], self.config_ele.select_Notch[1])
        time.sleep(2)
        move_ok = pyautogui.click(self.config_ele.select_Notch[0], self.config_ele.select_Notch[1])
        time.sleep(2)
        self.window_titles = pygetwindow.getAllTitles()
        logger.info("- Notch Value %s", self.window_titles)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        logger.info("Looking notch value %s", self.window.title)

        #save second screen
        screenObj5 = ScreenCapture(self.screens_path, self.window, "Notch_Selected", False)
        screen_saved = screenObj5.saveScreenShots()

        click_ok = pyautogui.moveTo(self.config_ele.select_Notch_60Hz[0], self.config_ele.select_Notch_60Hz[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_Notch_60Hz[0], self.config_ele.select_Notch_60Hz[1])
        time.sleep(2)

        self.window = pygetwindow.getWindowsWithTitle('intan')[0]


        screenObj6 = ScreenCapture(self.screens_path, self.window, "Notch_60Hz_Selected", False)
        screen_saved = screenObj6.saveScreenShots()

        # Impedance Tab
        logger.info("Move and clickon Impedance tab")
        # move to impedance tab
        pyautogui.moveTo(self.config_ele.select_impedence_tab[0], self.config_ele.select_impedence_tab[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_impedence_tab[0], self.config_ele.select_impedence_tab[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Impedence_tab_Selected", False)
        screen_saved = screenObj.saveScreenShots()

        # select impedance frequency button
        logger.info("Move and clickon select impedance frequency tab")
        #move to frequency tab
        pyautogui.moveTo(self.config_ele.select_Impedence_Test_Button[0], self.config_ele.select_Impedence_Test_Button[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_Impedence_Test_Button[0], self.config_ele.select_Impedence_Test_Button[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Impedence_freq_btn_Selected", True)
        screen_saved = screenObj.saveScreenShots()

        # ok button pressed on frequency selection pop up
        logger.info("Select ok on Impedance frequency pop up")
        # move to impedance frequency popup
        pyautogui.moveTo(self.config_ele.select_ok_Impedence_Test[0], self.config_ele.select_ok_Impedence_Test[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_ok_Impedence_Test[0], self.config_ele.select_ok_Impedence_Test[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Frequency_selected_ok", False)
        screen_saved = screenObj.saveScreenShots()

        # Run Impedance test
        logger.info("Run Impedance Test")
        # move to run impedance test
        pyautogui.moveTo(self.config_ele.run_Impedence_measurement[0], self.config_ele.run_Impedence_measurement[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.run_Impedence_measurement[0], self.config_ele.run_Impedence_measurement[1])
        logger.info("Waiting 20 for impedance test to be completed....")
        time.sleep(30)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Impedance_Test_Screen", False)
        screen_saved = screenObj.saveScreenShots()

        # Save Impedance Results
        logger.info("Save Impedance Test Data")
        # move to save impedance results
        pyautogui.moveTo(self.config_ele.select_save_Impedence_Measurement[0], self.config_ele.select_save_Impedence_Measurement[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_save_Impedence_Measurement[0], self.config_ele.select_save_Impedence_Measurement[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('save')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Save", True)
        screen_saved = screenObj.saveScreenShots()

        # Delete Existing path in save impedance window
        logger.info("Delete the existing path")
        # move to delete existing path in save impedance window
        pyautogui.moveTo(self.config_ele.select_to_delete_edit_path[0], self.config_ele.select_to_delete_edit_path[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_to_delete_edit_path[0], self.config_ele.select_to_delete_edit_path[1])
        time.sleep(2)
        pyautogui.press('delete')
        time.sleep(2)
        pyautogui.write(self.path)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)



        click_ok = pyautogui.click(self.config_ele.select_to_write_file_name[0], self.config_ele.select_to_write_file_name[1])
        time.sleep(5)
        pyautogui.press('delete')
        pyautogui.write(self.impedance_fname)


        # save button pressed on save impedance window
        logger.info("Save the impedance file")
        click_ok = pyautogui.click(self.config_ele.select_to_save[0], self.config_ele.select_to_save[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "save4", True)
        screen_saved = screenObj.saveScreenShots()
        
        # Start and stop recording every 10 seconds to new file.
        
        logger.info("Click on folder icon")
        click_ok = pyautogui.click(self.config_ele.select_folder_icon[0], self.config_ele.select_folder_icon[1])
        #move_to = pyautogui.moveTo(200,145)
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('Select')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Record1", True)
        screen_saved = screenObj.saveScreenShots()
        move_to = pyautogui.moveTo(self.config_ele.select_to_delete_edit_path[0], self.config_ele.select_to_delete_edit_path[1])
        # Delete Existing path in save impedance window
        logger.info("Record: Delete the existing path")

        click_ok = pyautogui.click(self.config_ele.select_to_delete_edit_path[0], self.config_ele.select_to_delete_edit_path[1])
        time.sleep(2)
        pyautogui.press('delete')
        pyautogui.write(self.path)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('Select')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Record2", True)
        screen_saved = screenObj.saveScreenShots()


        # Give file name in known path into save impedance window
        logger.info("Record: Delete File name and give new file name")
        move_to = pyautogui.moveTo(self.config_ele.select_to_write_file_name[0], self.config_ele.select_to_write_file_name[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_to_write_file_name[0], self.config_ele.select_to_write_file_name[1])
        time.sleep(2)
        pyautogui.press('delete')
        pyautogui.write(self.record_file_name)
        self.window = pygetwindow.getWindowsWithTitle('Select')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Record3", True)
        screen_saved = screenObj.saveScreenShots()

        # save button pressed on save impedance window
        logger.info("Record: Save the impedance file")
        move_to = pyautogui.moveTo(self.config_ele.select_to_save[0], self.config_ele.select_to_save[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_to_save[0], self.config_ele.select_to_save[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Record4", True)
        screen_saved = screenObj.saveScreenShots()
        time.sleep(2)

        logger.info("click on start recording")
        move_to = pyautogui.moveTo(self.config_ele.select_to_record[0], self.config_ele.select_to_record[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_to_record[0], self.config_ele.select_to_record[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "Start Record", True)
        screen_saved = screenObj.saveScreenShots()
        
        #Wait for 20 seconds
        time.sleep(20)
       
        # During the recording
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "During Record", True)
        screen_saved = screenObj.saveScreenShots()

        logger.info("click on stop recording")
        move_to = pyautogui.moveTo(self.config_ele.select_to_stop_recording[0], self.config_ele.select_to_stop_recording[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_to_stop_recording[0], self.config_ele.select_to_stop_recording[1])
        time.sleep(7)


    def startstopplay(self):
        """
        This function will perform the following: a) Start Intan App b) Verify all ports c) Start play
        d) stop play e) Do not record anything f) close Intan App
        """
        logger.info("startstoprecording: Starting Intan Application to just start click on different ports to capture the screenshots %s", self.app_loc)
        time.sleep(2)
        
        # Start Intan RHX Application
        start_status = os.startfile(self.app_loc)
        
        time.sleep(3)
        self.window_titles = pygetwindow.getAllTitles()
        logger.info("startstoprecording: All the list of windows that are open on this pc %s", self.window_titles)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
              
        # click on open button of "Select Intan Controller"
        pyautogui.moveTo(self.config_ele.select_intan_ctrl_co_ordinates[0], self.config_ele.select_intan_ctrl_co_ordinates[1])
        time.sleep(2)
        test2 = pyautogui.click(x=self.config_ele.select_intan_ctrl_co_ordinates[0], y=self.config_ele.select_intan_ctrl_co_ordinates[1])
        time.sleep(10)
        self.window_titles = pygetwindow.getAllTitles()
        
        pyautogui.moveTo(self.config_ele.ok_button_select_frequency[0], self.config_ele.ok_button_select_frequency[1])
        time.sleep(2)
        # click on ok button with 20KHz
        #click_ok = pyautogui.click(1084,585)
        test2 = pyautogui.click(x=self.config_ele.ok_button_select_frequency[0], y=self.config_ele.ok_button_select_frequency[1])
        time.sleep(5)
        # click on ok button with 20KHz
        click_ok = pyautogui.click(1084,585)
        time.sleep(10)

        #Verify all 8 ports connected and identified using Intan Software
        #move to verify number of ports connected
        pyautogui.moveTo(self.config_ele.get_number_of_ports_connected[0], self.config_ele.get_number_of_ports_connected[1])
        time.sleep(2)
        # click on to verify number of ports connected
        click_ok = pyautogui.click(self.config_ele.get_number_of_ports_connected[0], self.config_ele.get_number_of_ports_connected[1])

        time.sleep(5)
        self.window_titles = pygetwindow.getAllTitles()
        logger.info("Main Intan Application %s", self.window_titles)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        logger.info("Looking for number of ports connected %s", self.window.title)
        #pyautogui.moveTo(1084,595)
        #save second screen
        screenObj4 = ScreenCapture(self.screens_path, self.window, "Number_of_ports_connected", False)
        screen_saved = screenObj4.saveScreenShots()

        # Select "BW" on left pane and take screen capture
        # Move to "BW" option
        pyautogui.moveTo(self.config_ele.select_BW[0], self.config_ele.select_BW[1])
        time.sleep(2)
        #click_ok = pyautogui.click(570,1094)
        click_ok = pyautogui.click(self.config_ele.select_BW[0], self.config_ele.select_BW[1])
        time.sleep(2)


        # Select "NotchFilter" under "BW" pane and take screen capture
        pyautogui.moveTo(self.config_ele.select_Notch[0], self.config_ele.select_Notch[1])
        time.sleep(2)
        #click_ok = pyautogui.click(570,1094)
        move_ok = pyautogui.click(self.config_ele.select_Notch[0], self.config_ele.select_Notch[1])
        time.sleep(2)
        

        # Select "NotchFilter" as 60Hz and take screen capture
        #click_ok = pyautogui.click(570,1094)
        click_ok = pyautogui.moveTo(self.config_ele.select_Notch_60Hz[0], self.config_ele.select_Notch_60Hz[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_Notch_60Hz[0], self.config_ele.select_Notch_60Hz[1])
        time.sleep(2)


        # Impedance Tab
        logger.info("Move and clickon Impedance tab")
        # move to impedance tab
        pyautogui.moveTo(self.config_ele.select_impedence_tab[0], self.config_ele.select_impedence_tab[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_impedence_tab[0], self.config_ele.select_impedence_tab[1])
        time.sleep(2)


        # select impedance frequency button
        logger.info("Move and clickon select impedance frequency tab")
        #move to frequency tab
        pyautogui.moveTo(self.config_ele.select_Impedence_Test_Button[0], self.config_ele.select_Impedence_Test_Button[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_Impedence_Test_Button[0], self.config_ele.select_Impedence_Test_Button[1])
        time.sleep(2)


        # ok button pressed on frequency selection pop up
        logger.info("Select ok on Impedance frequency pop up")
        # move to impedance frequency popup
        pyautogui.moveTo(self.config_ele.select_ok_Impedence_Test[0], self.config_ele.select_ok_Impedence_Test[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_ok_Impedence_Test[0], self.config_ele.select_ok_Impedence_Test[1])
        time.sleep(2)


        # Run Impedance test
        logger.info("Run Impedance Test")
        # move to run impedance test
        pyautogui.moveTo(self.config_ele.run_Impedence_measurement[0], self.config_ele.run_Impedence_measurement[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.run_Impedence_measurement[0], self.config_ele.run_Impedence_measurement[1])
        logger.info("Waiting 30 for impedance test to be completed....")
        time.sleep(30)

        # Capture probemap.
        logger.info("click on Tools button")
        move_to = pyautogui.moveTo(self.config_ele.select_tools[0], self.config_ele.select_tools[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_tools[0], self.config_ele.select_tools[1])
        time.sleep(2)

        logger.info("click on probemap button")
        move_to = pyautogui.moveTo(self.config_ele.select_tools_probemap[0], self.config_ele.select_tools_probemap[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_tools_probemap[0], self.config_ele.select_tools_probemap[1])
        time.sleep(2)
        #self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        #screenObj = ScreenCapture(self.screens_path, self.window, "PortA", True)
        #filename = "portA"+str(time.time())+".png"
        
        logger.info("click on maximize button")
        move_to = pyautogui.moveTo(self.config_ele.select_maximize_probemap_window[0], self.config_ele.select_maximize_probemap_window[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_maximize_probemap_window[0], self.config_ele.select_maximize_probemap_window[1])
        time.sleep(2)

        logger.info("click on file button")
        move_to = pyautogui.moveTo(self.config_ele.select_probemap_file[0], self.config_ele.select_probemap_file[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_probemap_file[0], self.config_ele.select_probemap_file[1])
        time.sleep(2)

        logger.info("click on loadfile button")
        move_to = pyautogui.moveTo(self.config_ele.select_probemap_loadfile[0], self.config_ele.select_probemap_loadfile[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_probemap_loadfile[0], self.config_ele.select_probemap_loadfile[1])
        time.sleep(2)

        logger.info("click on file path space")

        # Delete Existing path in save impedance window
        logger.info("Delete the existing path")
        # move to delete existing path in save impedance window
        pyautogui.moveTo(self.config_ele.select_to_delete_edit_path[0], self.config_ele.select_to_delete_edit_path[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_to_delete_edit_path[0], self.config_ele.select_to_delete_edit_path[1])
        time.sleep(2)
        pyautogui.press('delete')
        time.sleep(2)
        pyautogui.write(self.probemap)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        

        logger.info("click on select xml file")
        move_to = pyautogui.moveTo(self.config_ele.select_probemap_config_file[0], self.config_ele.select_probemap_config_file[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_probemap_config_file[0], self.config_ele.select_probemap_config_file[1])
        time.sleep(2)
        
        logger.info("click on open button")
        move_to = pyautogui.moveTo(self.config_ele.select_open_probemap_config_file[0], self.config_ele.select_open_probemap_config_file[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_open_probemap_config_file[0], self.config_ele.select_open_probemap_config_file[1])
        time.sleep(5)

        logger.info("click on best fit button")
        move_to = pyautogui.moveTo(self.config_ele.select_best_fit_probmap[0], self.config_ele.select_best_fit_probmap[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_best_fit_probmap[0], self.config_ele.select_best_fit_probmap[1])
        time.sleep(2)

        logger.info("click on Ohm symbol button")
        move_to = pyautogui.moveTo(self.config_ele.select_ohm_icon_probemap[0], self.config_ele.select_ohm_icon_probemap[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_ohm_icon_probemap[0], self.config_ele.select_ohm_icon_probemap[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('Probe Map')[0]
        
        screenObj = ScreenCapture(self.screens_path, self.window, "ProbeMap", True)
        screen_saved = screenObj.saveScreenShots()
        time.sleep(5)

        logger.info("click on close probemap")
        move_to = pyautogui.moveTo(self.config_ele.select_close_probemap[0], self.config_ele.select_close_probemap[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_close_probemap[0], self.config_ele.select_close_probemap[1])
        time.sleep(2)

        
        logger.info("click on play button")
        move_to = pyautogui.moveTo(self.config_ele.select_to_play[0], self.config_ele.select_to_play[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_to_play[0], self.config_ele.select_to_play[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "PortA", True)
        screen_saved = screenObj.saveScreenShots()

        """
        time.sleep(5)
        logger.info("click on scroll bar for first time")
        move_to = pyautogui.moveTo(self.config_ele.select_scrollbar[0], self.config_ele.select_scrollbar[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_scrollbar[0], self.config_ele.select_scrollbar[1])
        time.sleep(2)
        self.window = pygetwindow.getWindowsWithTitle('intan')[0]
        screenObj = ScreenCapture(self.screens_path, self.window, "PortA", True)
        screen_saved = screenObj.saveScreenShots()
       
        time.sleep(5)
        logger.info("click on scroll bar for second time")
        move_to = pyautogui.moveTo(self.config_ele.select_scrollbar[0], self.config_ele.select_scrollbar[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_scrollbar[0], self.config_ele.select_scrollbar[1])
        time.sleep(2)

        time.sleep(5)
        logger.info("click on scroll bar for third time")
        move_to = pyautogui.moveTo(self.config_ele.select_scrollbar[0], self.config_ele.select_scrollbar[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_scrollbar[0], self.config_ele.select_scrollbar[1])
        time.sleep(2)

        time.sleep(5)
        logger.info("click on port B")
        move_to = pyautogui.moveTo(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        move_to = pyautogui.moveTo(self.config_ele.select_portB[0], self.config_ele.select_portB[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_portB[0], self.config_ele.select_portB[1])
        time.sleep(2)

        logger.info("click on port C")
        move_to = pyautogui.moveTo(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        move_to = pyautogui.moveTo(self.config_ele.select_portC[0], self.config_ele.select_portC[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_portC[0], self.config_ele.select_portC[1])
        time.sleep(2)

        logger.info("click on port D")
        move_to = pyautogui.moveTo(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        move_to = pyautogui.moveTo(self.config_ele.select_portD[0], self.config_ele.select_portD[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_portD[0], self.config_ele.select_portD[1])
        time.sleep(2)

        logger.info("click on port E")
        move_to = pyautogui.moveTo(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        move_to = pyautogui.moveTo(self.config_ele.select_portE[0], self.config_ele.select_portE[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_portE[0], self.config_ele.select_portE[1])
        time.sleep(2)

        logger.info("click on port F")
        move_to = pyautogui.moveTo(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        move_to = pyautogui.moveTo(self.config_ele.select_portF[0], self.config_ele.select_portF[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_portF[0], self.config_ele.select_portF[1])
        time.sleep(2)

        logger.info("click on port G")
        move_to = pyautogui.moveTo(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        move_to = pyautogui.moveTo(self.config_ele.select_portG[0], self.config_ele.select_portG[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_portG[0], self.config_ele.select_portG[1])
        time.sleep(2)

        logger.info("click on port H")
        move_to = pyautogui.moveTo(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        move_to = pyautogui.moveTo(self.config_ele.select_portH[0], self.config_ele.select_portH[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_portH[0], self.config_ele.select_portH[1])
        time.sleep(2)
        """ # Remove comment later
        logger.info("stop the playing")
        move_to = pyautogui.moveTo(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_display_ports[0], self.config_ele.select_display_ports[1])
        time.sleep(2)
        move_to = pyautogui.moveTo(self.config_ele.select_stopbutton[0], self.config_ele.select_stopbutton[1])
        time.sleep(2)
        click_ok = pyautogui.click(self.config_ele.select_stopbutton[0], self.config_ele.select_stopbutton[1])
        time.sleep(10)
        


    def get_PID_SpecificProcess(self):
        process_Specific = []
        process_name = "IntanRHX.exe"
        for proc in psutil.process_iter():
            process = psutil.Process(proc.pid) # Get the process info using PID
            pname = process.name() # here is the process name
            #Print name
            if pname == process_name:
                logger.info("Yes, Identified the Intan Process ID")
                logger.info("Process id %d", process.pid)
                process_Specific.append(process)
                logger.info("Identified Intan Specific process ID's %s", process_Specific)

            else:
                print("Finding IntanRHX process ID to identify already running process")
        return process_Specific
    
class ScreenCapture:
    def __init__(self, screen_path, window, title, crop_screenshot=False):
        self.screen_path = screen_path
        self.window = window
        self.screen_name = title
        self.crop_screenshot = crop_screenshot

    def saveScreenShots(self):
        logger.info("This function will literally capture the screen shot and chops it to window level and save")
        logger.info("These are the parameters of window %s", self.window)
        ct = datetime.now().strftime("%Y%m%d-%H%M%S")
        screen_name = self.window.title
        left, top = self.window.topleft
        right, bottom = self.window.bottomright
        logger.info(" Actual co-ordinates are Left: %d, top:%d, right:%d, bottom:%d", left, top, right, bottom)
        screen_name = screen_name.replace(" ","")+ct+".png"
        add_bkslash = "\\"
        screen_name = add_bkslash+screen_name
        path = self.screen_path+screen_name
        pyautogui.screenshot(path)
        logger.info("Crop Screenshot value is set to:%s", self.crop_screenshot)
        if(self.crop_screenshot):
            img = Image.open(path)
            img = img.crop((left, top, right, bottom))
            img.save(path)
        
        return True


if __name__ == '__main__':
    global config
    version = "TMS_DataCollection_1.0"
    # Create a Directory to store impedance files
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    logger.info("Test Measurement System Data Collection Script version: %s", version)
    logger.info("The current time is %s", current_time)
    dir_path = os.getcwd()+"/Impedance"+current_time
    dir_status = os.mkdir(dir_path)
    dir_screenshots_path = dir_path+"/ScreenCaptures"+current_time
    dir_probemap_config_path = dir_path+"/config_probemap/"
    dir_probemap_config_path_status = os.mkdir(dir_probemap_config_path)
    # Copy probemap file from config folder to logs folder 
    # This is as an objective reference stating we used this file.

    #crate a log file
    log_filename = "Record_Data_log"+current_time+".log"
    logging.basicConfig(filename=dir_path+"/"+log_filename, level = logging.INFO)
    logger.info("Started logging")
    #Load the configuration file
    ScreenSize = sys.argv[2]
    if int(ScreenSize) == 27:
        config = Display27()
        logger.info("Screen Size provided by the user is %s", ScreenSize)
    if int(ScreenSize) == 15:
        config = Display15()
        logger.info("Screen Size provided by the user is %s", ScreenSize)

    #app_loc = config.intan_path
    logger.info("Intan is located in the path %s", config.intan_path)
    
    # Script version:
    logger.info("Impedance_DataCollection Script Version: %s", config.version)

    logger.info("argument list %s", sys.argv[1])
    logger.info("Recording started at %s", current_time)

    #Finding .xml file:
    src_folder = os.getcwd()+"/config/"
    for file_name in os.listdir(src_folder):
        #Construct full file path
        src_file_path = src_folder + file_name
        if os.path.isfile(src_file_path) and "Array" in file_name:
            shutil.copy(src_file_path, dir_probemap_config_path)
            logger.info("Copied the config file")



    dir_screenshots_path_status = os.mkdir(dir_screenshots_path)
    logger.info("Directory created  for Impedance measurement %s", dir_status)
    logger.info("Directory created for capturing screens %s", dir_screenshots_path)
    for i in range(0, int(sys.argv[1])):
        logger.info("Impedance and recording attempt number %s", i)
        impedance_file_name = "impedance"+str(i)
        Record_file_name = "Record"+str(i)
        intan_obj = ImpedanceMeasurement(path = dir_path, app_loc = config.intan_path, screens_path = dir_screenshots_path, config_ele = config, record_file_name = Record_file_name, impedance_fname = impedance_file_name, data_recording = "True", probemap = dir_probemap_config_path)
        # Look for any existing Intan RHX process running on this pc
        Intan_pid = intan_obj.get_PID_SpecificProcess()
        logger.info("Intan PID's are %s", Intan_pid)
        for i_pid in Intan_pid:
            logger.info("Terminating the process with ID %s", i_pid)
            i_pid.terminate()
            
        
        # Start Intan
        
        intan_obj.startIntanRHX()
        
        for j in range(0, config.number_of_times_inner_loop):
            logger.info("Start and stop playing will start in a moment")
            Intan_pid = intan_obj.get_PID_SpecificProcess()
            logger.info("Intan PID's are %s", Intan_pid)
            for j_pid in Intan_pid:
                logger.info("Terminating the process with ID %s", j_pid)
                j_pid.terminate()

            # Call the start and stop function
            intan_obj.startstopplay()

        logger.info("Waiting for 5 seconds... %s", str(i))
        time.sleep(5)
    
    