#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  22 16:10:00 2025

@Author: Caleb Kilonzi
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt

    Parameters
    ----------
    password : str
        The password to be hashed

    Returns
    -------
    bytes
        The salted, hashed password as a byte string
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password using bcrypt

    Parameters
    ----------
    hashed_password : bytes
        The hashed password to compare against
    password : str
        The password to be validated

    Returns
    -------
    bool
        True if the password matches the hashed password, False otherwise
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
