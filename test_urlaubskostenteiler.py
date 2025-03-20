# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 11:13:52 2025

@author: cleme
"""

import urlaubskostenteiler

def test_berechnung():
    teilnehmer = ["Alice", "Bob", "Charlie"]
    ausgaben = [
        {"bezahlt_von": "Alice", "betrag": 30, "beteiligt": ["Alice", "Bob", "Charlie"]},
        {"bezahlt_von": "Bob", "betrag": 20, "beteiligt": ["Bob", "Charlie"]}
    ]

    assert urlaubskostenteiler.berechnung(teilnehmer, ausgaben) == {
        "Alice": 20,  
        "Bob": 10,    
        "Charlie": -30  
    }
    
if __name__ == "__main__":
    import unittest
    unittest.main()