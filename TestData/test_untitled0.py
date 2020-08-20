# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:20:12 2020

@author: Woody
"""
import os

def example1():
    """
    Retrieve the current directory

    Returns:
        Current directory
    """
    current_path = os.getcwd()
    return current_path

def test_get_current_directory(monkeypatch):
    """
    GIVEN a monkeypatched version of os.getcwd()
    WHEN example1() is called
    THEN check the current directory returned
    """
    def mock_getcwd():
        return '/data/user/directory123'

    monkeypatch.setattr(os, 'getcwd', mock_getcwd)
    assert example1() == '/data/user/directory123'