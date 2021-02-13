#!/usr/bin/env python3
# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
from password_generator import PasswordGenerator


def gen_pass():
    pw = PasswordGenerator()
    pw.minnumbers = 1
    pw.minuchars = 1
    pw.minlen = 20
    pw.maxlen = 20
    pw.excludeschars = "!$%^="

    return pw.generate()
