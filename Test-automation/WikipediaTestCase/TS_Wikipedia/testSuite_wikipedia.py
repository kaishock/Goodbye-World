import unittest
from WikipediaTestCase.TC_polishSite.main_wikiPL import Wiki_PL
from WikipediaTestCase.TC_englishSite.main_wikiEN import Wiki_EN


#Preparing Test Cases
TC1 = unittest.TestLoader().loadTestsFromTestCase(Wiki_PL)
TC2 = unittest.TestLoader().loadTestsFromTestCase(Wiki_EN)

#Creating Test Suites
masterTestSuite = unittest.TestSuite([TC1, TC2])
polishWikipediaTestSuite = unittest.TestSuite([TC1])
englishWikipediaTestSuite = unittest.TestSuite([TC2])

unittest.TextTestRunner().run(masterTestSuite)
print("As part of the Test Suite performed test cases for both Polish and English Wikipedia")

#unittest.TextTestRunner().run(polishWikipediaTestSuite)
#print("As part of the Test Suite performed test cases for Polish Wikipedia")

#unittest.TextTestRunner().run(englishWikipediaTestSuite)
#print("As part of the Test Suite performed test cases for English Wikipedia")
