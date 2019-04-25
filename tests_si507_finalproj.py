import unittest
from si507_finalproj import *
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
import csv
import wikipedia
import os
from flask import Flask, request, flash, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator


class Test(unittest.TestCase):
    def test_syriawardetails(self):
        self.wardetails_file = open('syriawardetails.csv','r')
        self.row_reader = self.wardetails_file.readlines()
        # print(self.row_reader)
        self.assertTrue(len(self.row_reader) > 200, "Testing that all the lines exist in the CSV")
        self.wardetails_file.close()

    def test_numrefugees(self):
        self.numrefugees_file = open('numrefugees.csv','r')
        self.row_reader = self.numrefugees_file.readlines()
        self.assertTrue(len(self.row_reader) > 100 , "Testing that there is a significant amount of dates in the numrefugees file")
        self.numrefugees_file.close()

    def test_numrefugees(self):
        self.numrefugees_file = open('numrefugees.csv','r')
        self.row_reader = self.numrefugees_file.readlines()
        self.assertTrue(len(self.row_reader) > 100 , "Testing that there is a significant amount of dates in the numrefugees file")
        self.numrefugees_file.close()


    def test_wikititle(self):
        self.assertEqual(title,"Timeline of the Syrian Civil War ", "Testing that the 'title' variable has the correct phrase. If this is not correct, the Wikipedia module will not find any of the files to scrape.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
