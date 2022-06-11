# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""test.py: test file."""

__author__		= 'Ritesh Dubal'


import os
import sys
import json
import time
import ast
import datetime
import pandas as pd
import requests
from collections import Counter
from math import sqrt
from scipy import spatial
from operator import itemgetter
sys.path.append('../')
from icrapp import common_util
from icrapp import models
from icrapp.icr import data_enrichment_util

pd.set_option('display.max_rows', 2000)

# labelsDict = {'undefined': 0, 'invoice_number': 1, 'date': 2, 'time': 3, 'total': 4, 'vendor.name': 5, 'vendor.phone_number': 6, 'vendor.vat_number': 7, 'vendor.email': 8, 'vendor.address': 9, 'meta_data.document_title': 10, 'customer.customer_name': 11, 'customer.phone_number': 12, 'generated_by.sales_person': 13, 'generated_by.sales_person_id': 14, 'payment.method': 15}

# # adidas - 
# # arr =  [{'xmin': 258, 'ymin': 161, 'xmax': 335, 'ymax': 188, 'lineNumber': 1, 'rd_b': 0.004560260567814112, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'adidas', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 245, 'ymin': 195, 'xmax': 348, 'ymax': 219, 'lineNumber': 2, 'rd_b': 0.004560260567814112, 'rd_r': 0.0, 'rd_t': -0.004560260567814112, 'rd_l': 0.0, 'nUpper': 8.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'NARAYANS', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 32, 'ymin': 226, 'xmax': 69, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.06775244325399399, 'rd_r': 0.009787928313016891, 'rd_t': 0.0, 'rd_l': 0.0, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'UGS', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 75, 'ymin': 226, 'xmax': 78, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.15374593436717987, 'rd_r': 0.032626427710056305, 'rd_t': 0.0, 'rd_l': -0.009787928313016891, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 98, 'ymin': 226, 'xmax': 176, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.0026058631483465433, 'rd_r': 0.02773246355354786, 'rd_t': 0.0, 'rd_l': -0.032626427710056305, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Ground', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 193, 'ymin': 226, 'xmax': 255, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.0026058631483465433, 'rd_r': 0.032626427710056305, 'rd_t': -0.004560260567814112, 'rd_l': -0.02773246355354786, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Floor', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 275, 'ymin': 226, 'xmax': 309, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.0026058631483465433, 'rd_r': 0.009787928313016891, 'rd_t': 0.0, 'rd_l': -0.032626427710056305, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 0.0, 'obj': '142', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 315, 'ymin': 226, 'xmax': 319, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.024755699560046196, 'rd_r': 0.03099510632455349, 'rd_t': 0.0, 'rd_l': -0.009787928313016891, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 338, 'ymin': 226, 'xmax': 428, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.0026058631483465433, 'rd_r': 0.02773246355354786, 'rd_t': 0.0, 'rd_l': -0.03099510632455349, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Phoenix', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 445, 'ymin': 226, 'xmax': 520, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.0026058631483465433, 'rd_r': 0.029363784939050674, 'rd_t': 0.0, 'rd_l': -0.02773246355354786, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Market', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 538, 'ymin': 226, 'xmax': 558, 'ymax': 256, 'lineNumber': 3, 'rd_b': 0.06775244325399399, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.029363784939050674, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Ci', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 98, 'ymin': 260, 'xmax': 215, 'ymax': 288, 'lineNumber': 4, 'rd_b': 0.024755699560046196, 'rd_r': 0.026101142168045044, 'rd_t': -0.0026058631483465433, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Velachery', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 231, 'ymin': 260, 'xmax': 282, 'ymax': 288, 'lineNumber': 4, 'rd_b': 0.024755699560046196, 'rd_r': 0.026101142168045044, 'rd_t': -0.0026058631483465433, 'rd_l': -0.026101142168045044, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Main', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 298, 'ymin': 260, 'xmax': 349, 'ymax': 288, 'lineNumber': 4, 'rd_b': 0.02410423383116722, 'rd_r': 0.009787928313016891, 'rd_t': -0.0026058631483465433, 'rd_l': -0.026101142168045044, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Road', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 355, 'ymin': 260, 'xmax': 359, 'ymax': 288, 'lineNumber': 4, 'rd_b': 0.06710097938776016, 'rd_r': 0.03099510632455349, 'rd_t': -0.0026058631483465433, 'rd_l': -0.009787928313016891, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 378, 'ymin': 260, 'xmax': 495, 'ymax': 288, 'lineNumber': 4, 'rd_b': 0.08925081789493561, 'rd_r': 0.0, 'rd_t': -0.0026058631483465433, 'rd_l': -0.03099510632455349, 'nUpper': 1.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Velachery', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 244, 'ymin': 294, 'xmax': 331, 'ymax': 318, 'lineNumber': 5, 'rd_b': 0.027361564338207245, 'rd_r': 0.0, 'rd_t': -0.024755699560046196, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Chennai', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 191, 'ymin': 326, 'xmax': 215, 'ymax': 352, 'lineNumber': 6, 'rd_b': 0.026058631017804146, 'rd_r': 0.032626427710056305, 'rd_t': -0.024755699560046196, 'rd_l': 0.0, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'PH', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 235, 'ymin': 326, 'xmax': 242, 'ymax': 352, 'lineNumber': 6, 'rd_b': 0.047557003796100616, 'rd_r': 0.004893964156508446, 'rd_t': -0.024755699560046196, 'rd_l': -0.032626427710056305, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 245, 'ymin': 325, 'xmax': 406, 'ymax': 353, 'lineNumber': 6, 'rd_b': 0.06905537098646164, 'rd_r': 0.0, 'rd_t': -0.02410423383116722, 'rd_l': -0.004893964156508446, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 11.0, 'nSpecial': 1.0, 'obj': '044-61153161', 'numLabel': 6, 'labelName': 'vendor.phone_number'}, {'xmin': 32, 'ymin': 360, 'xmax': 91, 'ymax': 390, 'lineNumber': 7, 'rd_b': 0.08729641884565353, 'rd_r': 0.05872756987810135, 'rd_t': -0.06775244325399399, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Email', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 127, 'ymin': 360, 'xmax': 281, 'ymax': 390, 'lineNumber': 7, 'rd_b': 0.06644950807094574, 'rd_r': 0.02773246355354786, 'rd_t': -0.027361564338207245, 'rd_l': -0.05872756987810135, 'nUpper': 0.0, 'nAlpha': 12.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'adioriginals', 'numLabel': 8, 'labelName': 'vendor.email'}, {'xmin': 298, 'ymin': 360, 'xmax': 563, 'ymax': 390, 'lineNumber': 7, 'rd_b': 0.06579804420471191, 'rd_r': 0.0, 'rd_t': -0.06775244325399399, 'rd_l': -0.02773246355354786, 'nUpper': 0.0, 'nAlpha': 17.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 3.0, 'obj': 'phoenix@europa.co.in', 'numLabel': 8, 'labelName': 'vendor.email'}, {'xmin': 150, 'ymin': 392, 'xmax': 214, 'ymax': 421, 'lineNumber': 8, 'rd_b': 0.04560260474681854, 'rd_r': 0.04893964156508446, 'rd_t': -0.026058631017804146, 'rd_l': 0.0, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'GSTIN', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 244, 'ymin': 391, 'xmax': 441, 'ymax': 421, 'lineNumber': 8, 'rd_b': 0.04560260474681854, 'rd_r': 0.0, 'rd_t': -0.06710097938776016, 'rd_l': -0.04893964156508446, 'nUpper': 8.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 7.0, 'nSpecial': 0.0, 'obj': '33ACCPR4059E1ZS', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 204, 'ymin': 425, 'xmax': 281, 'ymax': 453, 'lineNumber': 9, 'rd_b': 0.024755699560046196, 'rd_r': 0.03099510632455349, 'rd_t': -0.047557003796100616, 'rd_l': 0.0, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'RETAIL', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 300, 'ymin': 425, 'xmax': 388, 'ymax': 453, 'lineNumber': 9, 'rd_b': 0.04625407233834267, 'rd_r': 0.0, 'rd_t': -0.08925081789493561, 'rd_l': -0.03099510632455349, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'INVOICE', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 231, 'ymin': 459, 'xmax': 348, 'ymax': 485, 'lineNumber': 10, 'rd_b': 0.02540716528892517, 'rd_r': 0.0, 'rd_t': -0.06905537098646164, 'rd_l': 0.0, 'nUpper': 9.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'DUPLICATE', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 30, 'ymin': 492, 'xmax': 94, 'ymax': 521, 'lineNumber': 11, 'rd_b': 0.022149836644530296, 'rd_r': 0.026101142168045044, 'rd_t': -0.15374593436717987, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Place', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 110, 'ymin': 492, 'xmax': 133, 'ymax': 521, 'lineNumber': 11, 'rd_b': 0.0019543974194675684, 'rd_r': 0.02773246355354786, 'rd_t': -0.06644950807094574, 'rd_l': -0.026101142168045044, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'of', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 150, 'ymin': 491, 'xmax': 227, 'ymax': 521, 'lineNumber': 11, 'rd_b': 0.0019543974194675684, 'rd_r': 0.013050571084022522, 'rd_t': -0.04560260474681854, 'rd_l': -0.02773246355354786, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Supply', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 235, 'ymin': 491, 'xmax': 238, 'ymax': 520, 'lineNumber': 11, 'rd_b': 0.022149836644530296, 'rd_r': 0.009787928313016891, 'rd_t': -0.024755699560046196, 'rd_l': -0.013050571084022522, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 244, 'ymin': 491, 'xmax': 303, 'ymax': 520, 'lineNumber': 11, 'rd_b': 0.0026058631483465433, 'rd_r': 0.03425774723291397, 'rd_t': -0.06579804420471191, 'rd_l': -0.009787928313016891, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Tamil', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 324, 'ymin': 491, 'xmax': 374, 'ymax': 520, 'lineNumber': 11, 'rd_b': 0.0026058631483465433, 'rd_r': 0.026101142168045044, 'rd_t': -0.04560260474681854, 'rd_l': -0.03425774723291397, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Nadu', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 390, 'ymin': 491, 'xmax': 401, 'ymax': 520, 'lineNumber': 11, 'rd_b': 0.13159608840942383, 'rd_r': 0.026101142168045044, 'rd_t': 0.0, 'rd_l': -0.026101142168045044, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '&', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 417, 'ymin': 490, 'xmax': 441, 'ymax': 519, 'lineNumber': 11, 'rd_b': 0.13224755227565765, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.026101142168045044, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': '33', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 31, 'ymin': 524, 'xmax': 78, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.0032573288772255182, 'rd_r': 0.03425774723291397, 'rd_t': -0.08729641884565353, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Bill', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 99, 'ymin': 524, 'xmax': 123, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.0026058631483465433, 'rd_r': 0.011419249698519707, 'rd_t': -0.0019543974194675684, 'rd_l': -0.03425774723291397, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'No', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 130, 'ymin': 524, 'xmax': 135, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.047557003796100616, 'rd_r': 0.006525285542011261, 'rd_t': 0.0, 'rd_l': -0.011419249698519707, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 139, 'ymin': 524, 'xmax': 201, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.02540716528892517, 'rd_r': 0.011419249698519707, 'rd_t': -0.0019543974194675684, 'rd_l': -0.006525285542011261, 'nUpper': 1.0, 'nAlpha': 1.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 0.0, 'obj': 'S1602', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 208, 'ymin': 524, 'xmax': 213, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.02540716528892517, 'rd_r': 0.011419249698519707, 'rd_t': 0.0, 'rd_l': -0.011419249698519707, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 220, 'ymin': 524, 'xmax': 244, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.06775244325399399, 'rd_r': 0.008156606927514076, 'rd_t': -0.02540716528892517, 'rd_l': -0.011419249698519707, 'nUpper': 1.0, 'nAlpha': 1.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': 'T1', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 249, 'ymin': 524, 'xmax': 254, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.13485342264175415, 'rd_r': 0.006525285542011261, 'rd_t': -0.0026058631483465433, 'rd_l': -0.008156606927514076, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 258, 'ymin': 524, 'xmax': 325, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.0026058631483465433, 'rd_r': 0.008156606927514076, 'rd_t': -0.04625407233834267, 'rd_l': -0.006525285542011261, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 0.0, 'obj': 'SC969', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 330, 'ymin': 524, 'xmax': 335, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.2410423457622528, 'rd_r': 0.006525285542011261, 'rd_t': -0.0026058631483465433, 'rd_l': -0.008156606927514076, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 339, 'ymin': 524, 'xmax': 389, 'ymax': 550, 'lineNumber': 12, 'rd_b': 0.11205212026834488, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.006525285542011261, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': 'FY19', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 30, 'ymin': 555, 'xmax': 53, 'ymax': 584, 'lineNumber': 13, 'rd_b': 0.0032573288772255182, 'rd_r': 0.013050571084022522, 'rd_t': -0.022149836644530296, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Dt', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 61, 'ymin': 555, 'xmax': 64, 'ymax': 584, 'lineNumber': 13, 'rd_b': 0.02540716528892517, 'rd_r': 0.009787928313016891, 'rd_t': -0.0032573288772255182, 'rd_l': -0.013050571084022522, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 70, 'ymin': 554, 'xmax': 201, 'ymax': 585, 'lineNumber': 13, 'rd_b': 0.024755699560046196, 'rd_r': 0.026101142168045044, 'rd_t': -0.0026058631483465433, 'rd_l': -0.009787928313016891, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 2.0, 'obj': '02/02/2019', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 217, 'ymin': 554, 'xmax': 281, 'ymax': 583, 'lineNumber': 13, 'rd_b': 0.09055374562740326, 'rd_r': 0.026101142168045044, 'rd_t': -0.022149836644530296, 'rd_l': -0.026101142168045044, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '02:24', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 297, 'ymin': 554, 'xmax': 322, 'ymax': 583, 'lineNumber': 13, 'rd_b': 0.09055374562740326, 'rd_r': 0.0, 'rd_t': -0.0026058631483465433, 'rd_l': -0.026101142168045044, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'PM', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 31, 'ymin': 589, 'xmax': 121, 'ymax': 618, 'lineNumber': 14, 'rd_b': 0.024755699560046196, 'rd_r': 0.03099510632455349, 'rd_t': -0.0032573288772255182, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Cashier', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 140, 'ymin': 589, 'xmax': 162, 'ymax': 618, 'lineNumber': 14, 'rd_b': 0.024755699560046196, 'rd_r': 0.04730831831693649, 'rd_t': -0.02540716528892517, 'rd_l': -0.03099510632455349, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ID', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 191, 'ymin': 589, 'xmax': 361, 'ymax': 618, 'lineNumber': 14, 'rd_b': 0.09055374562740326, 'rd_r': 0.0, 'rd_t': -0.02540716528892517, 'rd_l': -0.04730831831693649, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': 'S1602.cashier', 'numLabel': 12, 'labelName': 'customer.phone_number'}, {'xmin': 32, 'ymin': 623, 'xmax': 82, 'ymax': 651, 'lineNumber': 15, 'rd_b': 0.04625407233834267, 'rd_r': 0.03425774723291397, 'rd_t': -0.02540716528892517, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Name', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 103, 'ymin': 623, 'xmax': 105, 'ymax': 651, 'lineNumber': 15, 'rd_b': 0.11074918508529663, 'rd_r': 0.009787928313016891, 'rd_t': -0.024755699560046196, 'rd_l': -0.03425774723291397, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 111, 'ymin': 623, 'xmax': 189, 'ymax': 651, 'lineNumber': 15, 'rd_b': 0.0032573288772255182, 'rd_r': 0.0, 'rd_t': -0.047557003796100616, 'rd_l': -0.009787928313016891, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'MERLIN', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 30, 'ymin': 656, 'xmax': 107, 'ymax': 682, 'lineNumber': 16, 'rd_b': 0.04820846766233444, 'rd_r': 0.02773246355354786, 'rd_t': -0.024755699560046196, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Mobile', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 124, 'ymin': 656, 'xmax': 147, 'ymax': 682, 'lineNumber': 16, 'rd_b': 0.04820846766233444, 'rd_r': 0.03425774723291397, 'rd_t': -0.024755699560046196, 'rd_l': -0.02773246355354786, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'No', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 168, 'ymin': 656, 'xmax': 171, 'ymax': 682, 'lineNumber': 16, 'rd_b': 0.08990228176116943, 'rd_r': 0.011419249698519707, 'rd_t': -0.0032573288772255182, 'rd_l': -0.03425774723291397, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 178, 'ymin': 654, 'xmax': 307, 'ymax': 682, 'lineNumber': 16, 'rd_b': 0.08990228176116943, 'rd_r': 0.0, 'rd_t': -0.06775244325399399, 'rd_l': -0.011419249698519707, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 10.0, 'nSpecial': 0.0, 'obj': '7338920514', 'numLabel': 12, 'labelName': 'customer.phone_number'}, {'xmin': 31, 'ymin': 722, 'xmax': 148, 'ymax': 748, 'lineNumber': 17, 'rd_b': 0.07035830616950989, 'rd_r': 0.04893964156508446, 'rd_t': -0.04625407233834267, 'rd_l': 0.0, 'nUpper': 2.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ArticleNo', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 178, 'ymin': 722, 'xmax': 228, 'ymax': 748, 'lineNumber': 17, 'rd_b': 0.21889251470565796, 'rd_r': 0.04730831831693649, 'rd_t': -0.09055374562740326, 'rd_l': -0.04893964156508446, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Size', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 257, 'ymin': 722, 'xmax': 308, 'ymax': 748, 'lineNumber': 17, 'rd_b': 0.06905537098646164, 'rd_r': 0.0701468214392662, 'rd_t': -0.09055374562740326, 'rd_l': -0.04730831831693649, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Desc', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 351, 'ymin': 722, 'xmax': 389, 'ymax': 748, 'lineNumber': 17, 'rd_b': 0.005211726296693087, 'rd_r': 0.004893964156508446, 'rd_t': -0.11205212026834488, 'rd_l': -0.0701468214392662, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'HSN', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 392, 'ymin': 722, 'xmax': 402, 'ymax': 748, 'lineNumber': 17, 'rd_b': 0.06905537098646164, 'rd_r': 0.0032626427710056305, 'rd_t': -0.13159608840942383, 'rd_l': -0.004893964156508446, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '/', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 404, 'ymin': 722, 'xmax': 442, 'ymax': 748, 'lineNumber': 17, 'rd_b': 0.005211726296693087, 'rd_r': 0.02446982078254223, 'rd_t': -0.13224755227565765, 'rd_l': -0.0032626427710056305, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SAC', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 457, 'ymin': 722, 'xmax': 561, 'ymax': 748, 'lineNumber': 17, 'rd_b': 0.005211726296693087, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.02446982078254223, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Division', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 31, 'ymin': 756, 'xmax': 68, 'ymax': 782, 'lineNumber': 18, 'rd_b': 0.19674266874790192, 'rd_r': 0.11092985421419144, 'rd_t': -0.04820846766233444, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Qty', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 136, 'ymin': 756, 'xmax': 174, 'ymax': 778, 'lineNumber': 18, 'rd_b': 0.048859935253858566, 'rd_r': 0.11582382023334503, 'rd_t': -0.04820846766233444, 'rd_l': -0.11092985421419144, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'MRP', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 245, 'ymin': 757, 'xmax': 281, 'ymax': 781, 'lineNumber': 18, 'rd_b': 0.11140064895153046, 'rd_r': 0.004893964156508446, 'rd_t': -0.13485342264175415, 'rd_l': -0.11582382023334503, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Tax', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 284, 'ymin': 757, 'xmax': 295, 'ymax': 780, 'lineNumber': 18, 'rd_b': 0.1543973982334137, 'rd_r': 0.08972267806529999, 'rd_t': -0.09055374562740326, 'rd_l': -0.004893964156508446, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 350, 'ymin': 756, 'xmax': 400, 'ymax': 779, 'lineNumber': 18, 'rd_b': 0.02671009860932827, 'rd_r': 0.026101142168045044, 'rd_t': -0.005211726296693087, 'rd_l': -0.08972267806529999, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Disc', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 416, 'ymin': 756, 'xmax': 427, 'ymax': 779, 'lineNumber': 18, 'rd_b': 0.2853420078754425, 'rd_r': 0.09298531711101532, 'rd_t': -0.005211726296693087, 'rd_l': -0.026101142168045044, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 484, 'ymin': 756, 'xmax': 559, 'ymax': 781, 'lineNumber': 18, 'rd_b': 0.027361564338207245, 'rd_r': 0.0, 'rd_t': -0.005211726296693087, 'rd_l': -0.09298531711101532, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Amount', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 29, 'ymin': 821, 'xmax': 107, 'ymax': 844, 'lineNumber': 19, 'rd_b': 0.15635178983211517, 'rd_r': 0.09298531711101532, 'rd_t': -0.11074918508529663, 'rd_l': 0.0, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 0.0, 'obj': 'BK7308', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 164, 'ymin': 820, 'xmax': 215, 'ymax': 846, 'lineNumber': 19, 'rd_b': 0.15570032596588135, 'rd_r': 0.029363784939050674, 'rd_t': -0.08990228176116943, 'rd_l': -0.09298531711101532, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'OSFM', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 233, 'ymin': 820, 'xmax': 320, 'ymax': 846, 'lineNumber': 19, 'rd_b': 0.15570032596588135, 'rd_r': 0.029363784939050674, 'rd_t': -0.08990228176116943, 'rd_l': -0.029363784939050674, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TREFOIL', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 338, 'ymin': 820, 'xmax': 362, 'ymax': 846, 'lineNumber': 19, 'rd_b': 0.09120520949363708, 'rd_r': 0.1549755334854126, 'rd_t': -0.02671009860932827, 'rd_l': -0.029363784939050674, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TR', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 457, 'ymin': 823, 'xmax': 508, 'ymax': 848, 'lineNumber': 19, 'rd_b': 0.003908794838935137, 'rd_r': 0.026101142168045044, 'rd_t': -0.027361564338207245, 'rd_l': -0.1549755334854126, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 0.0, 'obj': '6505', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 524, 'ymin': 823, 'xmax': 562, 'ymax': 848, 'lineNumber': 19, 'rd_b': 0.04625407233834267, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.026101142168045044, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ACC', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 33, 'ymin': 856, 'xmax': 37, 'ymax': 874, 'lineNumber': 20, 'rd_b': 0.15830619633197784, 'rd_r': 0.14681892096996307, 'rd_t': -0.07035830616950989, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '1', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 127, 'ymin': 853, 'xmax': 175, 'ymax': 880, 'lineNumber': 20, 'rd_b': 0.13289901614189148, 'rd_r': 0.11092985421419144, 'rd_t': -0.048859935253858566, 'rd_l': -0.14681892096996307, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 0.0, 'obj': '1299', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 243, 'ymin': 854, 'xmax': 307, 'ymax': 880, 'lineNumber': 20, 'rd_b': 0.1752443015575409, 'rd_r': 0.11419249325990677, 'rd_t': -0.06905537098646164, 'rd_l': -0.11092985421419144, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': 'GST12', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 377, 'ymin': 854, 'xmax': 428, 'ymax': 879, 'lineNumber': 20, 'rd_b': 0.027361564338207245, 'rd_r': 0.07340946048498154, 'rd_t': -0.06905537098646164, 'rd_l': -0.11419249325990677, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '0.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 473, 'ymin': 854, 'xmax': 560, 'ymax': 879, 'lineNumber': 20, 'rd_b': 0.04820846766233444, 'rd_r': 0.0, 'rd_t': -0.003908794838935137, 'rd_l': -0.07340946048498154, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '1299.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 296, 'ymin': 920, 'xmax': 372, 'ymax': 946, 'lineNumber': 21, 'rd_b': 0.04690553620457649, 'rd_r': 0.035889070481061935, 'rd_t': -0.2410423457622528, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Amount', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 394, 'ymin': 921, 'xmax': 396, 'ymax': 945, 'lineNumber': 21, 'rd_b': 0.0058631920255720615, 'rd_r': 0.1272430717945099, 'rd_t': -0.027361564338207245, 'rd_l': -0.035889070481061935, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 474, 'ymin': 919, 'xmax': 561, 'ymax': 948, 'lineNumber': 21, 'rd_b': 0.02540716528892517, 'rd_r': 0.0, 'rd_t': -0.04625407233834267, 'rd_l': -0.1272430717945099, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '1299.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 270, 'ymin': 952, 'xmax': 373, 'ymax': 980, 'lineNumber': 22, 'rd_b': 0.13224755227565765, 'rd_r': 0.03425774723291397, 'rd_t': -0.11140064895153046, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Discount', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 394, 'ymin': 954, 'xmax': 397, 'ymax': 980, 'lineNumber': 22, 'rd_b': 0.003908794838935137, 'rd_r': 0.18433931469917297, 'rd_t': -0.0058631920255720615, 'rd_l': -0.03425774723291397, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 510, 'ymin': 953, 'xmax': 561, 'ymax': 980, 'lineNumber': 22, 'rd_b': 0.026058631017804146, 'rd_r': 0.0, 'rd_t': -0.04820846766233444, 'rd_l': -0.18433931469917297, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '0.00', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 335, 'ymin': 986, 'xmax': 374, 'ymax': 1011, 'lineNumber': 23, 'rd_b': 0.1335504949092865, 'rd_r': 0.029363784939050674, 'rd_t': -0.09120520949363708, 'rd_l': 0.0, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ROD', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 392, 'ymin': 986, 'xmax': 396, 'ymax': 1009, 'lineNumber': 23, 'rd_b': 0.0065146577544510365, 'rd_r': 0.18597063422203064, 'rd_t': -0.003908794838935137, 'rd_l': -0.029363784939050674, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 510, 'ymin': 987, 'xmax': 560, 'ymax': 1014, 'lineNumber': 23, 'rd_b': 0.13224755227565765, 'rd_r': 0.0, 'rd_t': -0.02540716528892517, 'rd_l': -0.18597063422203064, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '0.00', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 256, 'ymin': 1017, 'xmax': 316, 'ymax': 1045, 'lineNumber': 24, 'rd_b': 0.1543973982334137, 'rd_r': 0.032626427710056305, 'rd_t': -0.1543973982334137, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Total', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 336, 'ymin': 1018, 'xmax': 372, 'ymax': 1045, 'lineNumber': 24, 'rd_b': 0.19804559648036957, 'rd_r': 0.035889070481061935, 'rd_t': -0.04690553620457649, 'rd_l': -0.032626427710056305, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Amt', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 394, 'ymin': 1019, 'xmax': 396, 'ymax': 1045, 'lineNumber': 24, 'rd_b': 0.11205212026834488, 'rd_r': 0.12561175227165222, 'rd_t': -0.0065146577544510365, 'rd_l': -0.035889070481061935, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 473, 'ymin': 1020, 'xmax': 560, 'ymax': 1045, 'lineNumber': 24, 'rd_b': 0.11205212026834488, 'rd_r': 0.0, 'rd_t': -0.026058631017804146, 'rd_l': -0.12561175227165222, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '1299.00', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 31, 'ymin': 1084, 'xmax': 65, 'ymax': 1110, 'lineNumber': 25, 'rd_b': 0.024755699560046196, 'rd_r': 0.02773246355354786, 'rd_t': -0.19674266874790192, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Tot', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 82, 'ymin': 1084, 'xmax': 133, 'ymax': 1110, 'lineNumber': 25, 'rd_b': 0.004560260567814112, 'rd_r': 0.006525285542011261, 'rd_t': -0.15635178983211517, 'rd_l': -0.02773246355354786, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Prod', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 137, 'ymin': 1084, 'xmax': 146, 'ymax': 1110, 'lineNumber': 25, 'rd_b': 0.06905537098646164, 'rd_r': 0.004893964156508446, 'rd_t': -0.13289901614189148, 'rd_l': -0.006525285542011261, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '/', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 149, 'ymin': 1084, 'xmax': 186, 'ymax': 1111, 'lineNumber': 25, 'rd_b': 0.11140064895153046, 'rd_r': 0.03425774723291397, 'rd_t': -0.21889251470565796, 'rd_l': -0.004893964156508446, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Qty', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 207, 'ymin': 1085, 'xmax': 210, 'ymax': 1111, 'lineNumber': 25, 'rd_b': 0.0, 'rd_r': 0.016313213855028152, 'rd_t': -0.15570032596588135, 'rd_l': -0.03425774723291397, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 220, 'ymin': 1085, 'xmax': 250, 'ymax': 1111, 'lineNumber': 25, 'rd_b': 0.15504886209964752, 'rd_r': 0.0, 'rd_t': -0.15570032596588135, 'rd_l': -0.016313213855028152, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 1.0, 'obj': '1/1', 'numLabel': 13, 'labelName': 'generated_by.sales_person'}, {'xmin': 29, 'ymin': 1117, 'xmax': 66, 'ymax': 1143, 'lineNumber': 26, 'rd_b': 0.02540716528892517, 'rd_r': 0.026101142168045044, 'rd_t': -0.15830619633197784, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Tax', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 82, 'ymin': 1117, 'xmax': 173, 'ymax': 1144, 'lineNumber': 26, 'rd_b': 0.04690553620457649, 'rd_r': 0.0, 'rd_t': -0.004560260567814112, 'rd_l': -0.026101142168045044, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Breakup', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 30, 'ymin': 1148, 'xmax': 80, 'ymax': 1172, 'lineNumber': 27, 'rd_b': 0.05081433057785034, 'rd_r': 0.24306687712669373, 'rd_t': -0.024755699560046196, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 229, 'ymin': 1149, 'xmax': 292, 'ymax': 1174, 'lineNumber': 27, 'rd_b': 0.15504886209964752, 'rd_r': 0.0, 'rd_t': -0.1752443015575409, 'rd_l': -0.24306687712669373, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '69.59', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 27, 'ymin': 1182, 'xmax': 78, 'ymax': 1208, 'lineNumber': 28, 'rd_b': 0.04820846766233444, 'rd_r': 0.24469821155071259, 'rd_t': -0.02540716528892517, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SGST', 'numLabel': 13, 'labelName': 'generated_by.sales_person'}, {'xmin': 228, 'ymin': 1183, 'xmax': 292, 'ymax': 1209, 'lineNumber': 28, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.13224755227565765, 'rd_l': -0.24469821155071259, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '69.59', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 27, 'ymin': 1216, 'xmax': 117, 'ymax': 1244, 'lineNumber': 29, 'rd_b': 0.0, 'rd_r': 0.02773246355354786, 'rd_t': -0.04690553620457649, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Payment', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 134, 'ymin': 1216, 'xmax': 225, 'ymax': 1244, 'lineNumber': 29, 'rd_b': 0.024755699560046196, 'rd_r': 0.04730831831693649, 'rd_t': -0.06905537098646164, 'rd_l': -0.02773246355354786, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Details', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 254, 'ymin': 1216, 'xmax': 385, 'ymax': 1246, 'lineNumber': 29, 'rd_b': 0.0, 'rd_r': 0.006525285542011261, 'rd_t': -0.1335504949092865, 'rd_l': -0.04730831831693649, 'nUpper': 2.0, 'nAlpha': 10.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CreditCard', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 389, 'ymin': 1217, 'xmax': 395, 'ymax': 1245, 'lineNumber': 29, 'rd_b': 0.0, 'rd_r': 0.009787928313016891, 'rd_t': -0.11205212026834488, 'rd_l': -0.006525285542011261, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 401, 'ymin': 1217, 'xmax': 478, 'ymax': 1245, 'lineNumber': 29, 'rd_b': 0.1100977212190628, 'rd_r': 0.011419249698519707, 'rd_t': -0.2853420078754425, 'rd_l': -0.009787928313016891, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'MASTER', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 485, 'ymin': 1217, 'xmax': 490, 'ymax': 1245, 'lineNumber': 29, 'rd_b': 0.0, 'rd_r': 0.029363784939050674, 'rd_t': -0.11205212026834488, 'rd_l': -0.011419249698519707, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 508, 'ymin': 1217, 'xmax': 518, 'ymax': 1245, 'lineNumber': 29, 'rd_b': 0.0, 'rd_r': 0.032626427710056305, 'rd_t': -0.13224755227565765, 'rd_l': -0.029363784939050674, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '=', 'numLabel': 13, 'labelName': 'generated_by.sales_person'}, {'xmin': 538, 'ymin': 1218, 'xmax': 585, 'ymax': 1246, 'lineNumber': 29, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.032626427710056305, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 0.0, 'obj': '1299', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 31, 'ymin': 1250, 'xmax': 64, 'ymax': 1273, 'lineNumber': 30, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.05081433057785034, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 1.0, 'obj': '.00', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 27, 'ymin': 1282, 'xmax': 131, 'ymax': 1307, 'lineNumber': 31, 'rd_b': 0.0, 'rd_r': 0.011419249698519707, 'rd_t': -0.04820846766233444, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Salesman', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 138, 'ymin': 1282, 'xmax': 141, 'ymax': 1307, 'lineNumber': 31, 'rd_b': 0.0, 'rd_r': 0.009787928313016891, 'rd_t': -0.024755699560046196, 'rd_l': -0.011419249698519707, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 13, 'labelName': 'generated_by.sales_person'}, {'xmin': 147, 'ymin': 1282, 'xmax': 225, 'ymax': 1307, 'lineNumber': 31, 'rd_b': 0.0, 'rd_r': 0.02446982078254223, 'rd_t': -0.11140064895153046, 'rd_l': -0.009787928313016891, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'STEVEN', 'numLabel': 13, 'labelName': 'generated_by.sales_person'}, {'xmin': 240, 'ymin': 1282, 'xmax': 318, 'ymax': 1307, 'lineNumber': 31, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.1543973982334137, 'rd_l': -0.02446982078254223, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'RENGMA', 'numLabel': 13, 'labelName': 'generated_by.sales_person'}, {'xmin': 227, 'ymin': 1349, 'xmax': 290, 'ymax': 1374, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': 0.02773246355354786, 'rd_t': -0.15504886209964752, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Thank', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 307, 'ymin': 1349, 'xmax': 344, 'ymax': 1374, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.19804559648036957, 'rd_l': -0.02773246355354786, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'You', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 280, 'ymin': 1412, 'xmax': 411, 'ymax': 1442, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.026101142168045044, 'rd_t': -0.15504886209964752, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 10.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Authorised', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 427, 'ymin': 1414, 'xmax': 544, 'ymax': 1444, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.1100977212190628, 'rd_l': -0.026101142168045044, 'nUpper': 1.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Signature', 'numLabel': 15, 'labelName': 'payment.method'}]

# # and - 00001.png
# # arr =  [{'xmin': 49, 'ymin': 94, 'xmax': 80, 'ymax': 111, 'lineNumber': 1, 'rd_b': 0.004830917809158564, 'rd_r': 0.01592356711626053, 'rd_t': 0.0, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Shop', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 85, 'ymin': 94, 'xmax': 122, 'ymax': 111, 'lineNumber': 1, 'rd_b': 0.004830917809158564, 'rd_r': 0.01592356711626053, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'online', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 127, 'ymin': 94, 'xmax': 137, 'ymax': 111, 'lineNumber': 1, 'rd_b': 0.004830917809158564, 'rd_r': 0.01592356711626053, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'at', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 142, 'ymin': 94, 'xmax': 143, 'ymax': 111, 'lineNumber': 1, 'rd_b': 0.047101449221372604, 'rd_r': 0.01592356711626053, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 148, 'ymin': 94, 'xmax': 257, 'ymax': 111, 'lineNumber': 1, 'rd_b': 0.004830917809158564, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 14.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 2.0, 'obj': 'www.andindia.com', 'numLabel': 8, 'labelName': 'vendor.email'}, {'xmin': 57, 'ymin': 115, 'xmax': 92, 'ymax': 131, 'lineNumber': 2, 'rd_b': 0.004830917809158564, 'rd_r': 0.012738853693008423, 'rd_t': -0.004830917809158564, 'rd_l': 0.0, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'OCHRE', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 96, 'ymin': 115, 'xmax': 116, 'ymax': 131, 'lineNumber': 2, 'rd_b': 0.004830917809158564, 'rd_r': 0.01592356711626053, 'rd_t': -0.004830917809158564, 'rd_l': -0.012738853693008423, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'AND', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 121, 'ymin': 115, 'xmax': 154, 'ymax': 131, 'lineNumber': 2, 'rd_b': 0.004830917809158564, 'rd_r': 0.01592356711626053, 'rd_t': -0.004830917809158564, 'rd_l': -0.01592356711626053, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'BLACK', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 159, 'ymin': 115, 'xmax': 200, 'ymax': 131, 'lineNumber': 2, 'rd_b': 0.022946860641241074, 'rd_r': 0.01592356711626053, 'rd_t': -0.004830917809158564, 'rd_l': -0.01592356711626053, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'PRIVATE', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 205, 'ymin': 115, 'xmax': 244, 'ymax': 131, 'lineNumber': 2, 'rd_b': 0.004830917809158564, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'LIMITED', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 79, 'ymin': 135, 'xmax': 95, 'ymax': 151, 'lineNumber': 3, 'rd_b': 0.05193236842751503, 'rd_r': 0.009554140269756317, 'rd_t': -0.004830917809158564, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Unit', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 98, 'ymin': 135, 'xmax': 112, 'ymax': 151, 'lineNumber': 3, 'rd_b': 0.009661835618317127, 'rd_r': 0.006369426846504211, 'rd_t': -0.004830917809158564, 'rd_l': -0.009554140269756317, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': 'No.', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 114, 'ymin': 135, 'xmax': 124, 'ymax': 151, 'lineNumber': 3, 'rd_b': 0.05193236842751503, 'rd_r': -0.006369426846504211, 'rd_t': -0.004830917809158564, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': '21', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 122, 'ymin': 150, 'xmax': 146, 'ymax': 160, 'lineNumber': 3, 'rd_b': -0.030193237587809563, 'rd_r': -0.06050955504179001, 'rd_t': -0.047101449221372604, 'rd_l': 0.006369426846504211, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Hosur', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 127, 'ymin': 135, 'xmax': 156, 'ymax': 151, 'lineNumber': 3, 'rd_b': 0.032608695328235626, 'rd_r': -0.01592356711626053, 'rd_t': 0.030193237587809563, 'rd_l': 0.06050955504179001, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Forum', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 151, 'ymin': 150, 'xmax': 175, 'ymax': 160, 'lineNumber': 3, 'rd_b': -0.001207729452289641, 'rd_r': -0.047770701348781586, 'rd_t': -0.022946860641241074, 'rd_l': 0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Road', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 160, 'ymin': 135, 'xmax': 213, 'ymax': 151, 'lineNumber': 3, 'rd_b': 0.05193236842751503, 'rd_r': 0.0, 'rd_t': -0.004830917809158564, 'rd_l': 0.047770701348781586, 'nUpper': 1.0, 'nAlpha': 10.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Koramangla', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 106, 'ymin': 159, 'xmax': 161, 'ymax': 174, 'lineNumber': 4, 'rd_b': 0.039855074137449265, 'rd_r': 0.009554140269756317, 'rd_t': -0.009661835618317127, 'rd_l': 0.0, 'nUpper': 9.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'BENGALURU', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 164, 'ymin': 159, 'xmax': 198, 'ymax': 174, 'lineNumber': 4, 'rd_b': 0.039855074137449265, 'rd_r': 0.0, 'rd_t': 0.001207729452289641, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 0.0, 'obj': '560095', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 127, 'ymin': 178, 'xmax': 180, 'ymax': 191, 'lineNumber': 5, 'rd_b': 0.04589372128248215, 'rd_r': 0.0, 'rd_t': -0.032608695328235626, 'rd_l': 0.0, 'nUpper': 9.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'KARNATAKA', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 88, 'ymin': 194, 'xmax': 115, 'ymax': 206, 'lineNumber': 6, 'rd_b': 0.001207729452289641, 'rd_r': 0.012738853693008423, 'rd_t': -0.05193236842751503, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Phone', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 119, 'ymin': 194, 'xmax': 134, 'ymax': 206, 'lineNumber': 6, 'rd_b': 0.04951690882444382, 'rd_r': 0.03184713423252106, 'rd_t': -0.05193236842751503, 'rd_l': -0.012738853693008423, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': 'No.', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 144, 'ymin': 194, 'xmax': 206, 'ymax': 206, 'lineNumber': 6, 'rd_b': 0.02777777798473835, 'rd_r': 0.0, 'rd_t': -0.05193236842751503, 'rd_l': -0.03184713423252106, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 11.0, 'nSpecial': 0.0, 'obj': '08291916230', 'numLabel': 6, 'labelName': 'vendor.phone_number'}, {'xmin': 80, 'ymin': 207, 'xmax': 110, 'ymax': 222, 'lineNumber': 7, 'rd_b': 0.030193237587809563, 'rd_r': 0.01592356711626053, 'rd_t': -0.039855074137449265, 'rd_l': 0.0, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'GSTIN', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 115, 'ymin': 207, 'xmax': 115, 'ymax': 222, 'lineNumber': 7, 'rd_b': 0.030193237587809563, 'rd_r': 0.019108280539512634, 'rd_t': -0.001207729452289641, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 121, 'ymin': 207, 'xmax': 215, 'ymax': 222, 'lineNumber': 7, 'rd_b': 0.030193237587809563, 'rd_r': 0.0, 'rd_t': -0.039855074137449265, 'rd_l': -0.019108280539512634, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '29AACCO8356L12S', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 112, 'ymin': 229, 'xmax': 131, 'ymax': 244, 'lineNumber': 8, 'rd_b': 0.02415458858013153, 'rd_r': 0.02229299396276474, 'rd_t': -0.04589372128248215, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Tax', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 138, 'ymin': 229, 'xmax': 186, 'ymax': 244, 'lineNumber': 8, 'rd_b': 0.0036231884732842445, 'rd_r': 0.0, 'rd_t': -0.02777777798473835, 'rd_l': -0.02229299396276474, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Invoice', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 21, 'ymin': 247, 'xmax': 55, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.002415458904579282, 'rd_r': 0.006369426846504211, 'rd_t': 0.0, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'involce', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 57, 'ymin': 247, 'xmax': 70, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.002415458904579282, 'rd_r': 0.006369426846504211, 'rd_t': 0.0, 'rd_l': -0.006369426846504211, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'No', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 72, 'ymin': 247, 'xmax': 79, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.021739130839705467, 'rd_r': 0.009554140269756317, 'rd_t': 0.0, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 82, 'ymin': 247, 'xmax': 94, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.021739130839705467, 'rd_r': 0.009554140269756317, 'rd_t': -0.030193237587809563, 'rd_l': -0.009554140269756317, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SB', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 97, 'ymin': 247, 'xmax': 99, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.04227053001523018, 'rd_r': 0.006369426846504211, 'rd_t': 0.0, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 101, 'ymin': 247, 'xmax': 116, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.021739130839705467, 'rd_r': 0.006369426846504211, 'rd_t': -0.030193237587809563, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 0.0, 'obj': '132', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 118, 'ymin': 247, 'xmax': 120, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.04227053001523018, 'rd_r': 0.0031847134232521057, 'rd_t': -0.04951690882444382, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 121, 'ymin': 247, 'xmax': 137, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.06521739065647125, 'rd_r': 0.0031847134232521057, 'rd_t': -0.030193237587809563, 'rd_l': -0.0031847134232521057, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Apr', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 138, 'ymin': 247, 'xmax': 140, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.08574879169464111, 'rd_r': 0.009554140269756317, 'rd_t': -0.0036231884732842445, 'rd_l': -0.0031847134232521057, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 143, 'ymin': 247, 'xmax': 177, 'ymax': 262, 'lineNumber': 9, 'rd_b': 0.021739130839705467, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '21-1426', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 20, 'ymin': 264, 'xmax': 46, 'ymax': 276, 'lineNumber': 10, 'rd_b': 0.004830917809158564, 'rd_r': 0.01592356711626053, 'rd_t': -0.002415458904579282, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Memo', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 51, 'ymin': 264, 'xmax': 65, 'ymax': 276, 'lineNumber': 10, 'rd_b': 0.004830917809158564, 'rd_r': 0.0541401281952858, 'rd_t': -0.002415458904579282, 'rd_l': -0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': 'No.', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 82, 'ymin': 264, 'xmax': 172, 'ymax': 276, 'lineNumber': 10, 'rd_b': 0.004830917809158564, 'rd_r': 0.0, 'rd_t': -0.02415458858013153, 'rd_l': -0.0541401281952858, 'nUpper': 1.0, 'nAlpha': 1.0, 'nSpaces': 0.0, 'nNumeric': 14.0, 'nSpecial': 1.0, 'obj': '296P2122-0000132', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 20, 'ymin': 280, 'xmax': 40, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.006038647145032883, 'rd_r': 0.012738853693008423, 'rd_t': -0.004830917809158564, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Date', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 44, 'ymin': 280, 'xmax': 45, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.028985507786273956, 'rd_r': 0.019108280539512634, 'rd_t': 0.0, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 51, 'ymin': 280, 'xmax': 60, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.04951690882444382, 'rd_r': 0.006369426846504211, 'rd_t': -0.004830917809158564, 'rd_l': -0.019108280539512634, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': '14', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 62, 'ymin': 280, 'xmax': 64, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.06884057819843292, 'rd_r': 0.006369426846504211, 'rd_t': 0.0, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 66, 'ymin': 280, 'xmax': 81, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.006038647145032883, 'rd_r': 0.006369426846504211, 'rd_t': -0.021739130839705467, 'rd_l': -0.006369426846504211, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Apr', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 83, 'ymin': 280, 'xmax': 85, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.028985507786273956, 'rd_r': 0.006369426846504211, 'rd_t': -0.021739130839705467, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 87, 'ymin': 280, 'xmax': 95, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.06884057819843292, 'rd_r': 0.01592356711626053, 'rd_t': -0.004830917809158564, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': '21', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 100, 'ymin': 280, 'xmax': 138, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.06884057819843292, 'rd_r': 0.019108280539512634, 'rd_t': -0.021739130839705467, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '06:18:31', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 144, 'ymin': 280, 'xmax': 157, 'ymax': 292, 'lineNumber': 11, 'rd_b': 0.006038647145032883, 'rd_r': 0.0, 'rd_t': -0.021739130839705467, 'rd_l': -0.019108280539512634, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'PM', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 23, 'ymin': 297, 'xmax': 65, 'ymax': 311, 'lineNumber': 12, 'rd_b': 0.07246376574039459, 'rd_r': 0.009554140269756317, 'rd_t': -0.006038647145032883, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Customer', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 68, 'ymin': 297, 'xmax': 95, 'ymax': 311, 'lineNumber': 12, 'rd_b': 0.08937197923660278, 'rd_r': -0.0031847134232521057, 'rd_t': -0.006038647145032883, 'rd_l': -0.009554140269756317, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Name', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 94, 'ymin': 297, 'xmax': 98, 'ymax': 311, 'lineNumber': 12, 'rd_b': 0.006038647145032883, 'rd_r': 0.009554140269756317, 'rd_t': -0.04227053001523018, 'rd_l': 0.0031847134232521057, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 101, 'ymin': 297, 'xmax': 137, 'ymax': 311, 'lineNumber': 12, 'rd_b': 0.04589372128248215, 'rd_r': 0.01592356711626053, 'rd_t': -0.04227053001523018, 'rd_l': -0.009554140269756317, 'nUpper': 3.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 2.0, 'obj': 'Ms.DR.', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 142, 'ymin': 297, 'xmax': 161, 'ymax': 311, 'lineNumber': 12, 'rd_b': 0.030193237587809563, 'rd_r': 0.019108280539512634, 'rd_t': -0.006038647145032883, 'rd_l': -0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Ivani', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 167, 'ymin': 297, 'xmax': 188, 'ymax': 311, 'lineNumber': 12, 'rd_b': 0.04589372128248215, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.019108280539512634, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Dash', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 21, 'ymin': 316, 'xmax': 63, 'ymax': 329, 'lineNumber': 13, 'rd_b': 0.050724636763334274, 'rd_r': 0.01592356711626053, 'rd_t': -0.028985507786273956, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Customer', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 68, 'ymin': 316, 'xmax': 95, 'ymax': 329, 'lineNumber': 13, 'rd_b': 0.06763284653425217, 'rd_r': 0.009554140269756317, 'rd_t': -0.028985507786273956, 'rd_l': -0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Mobile', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 98, 'ymin': 316, 'xmax': 99, 'ymax': 329, 'lineNumber': 13, 'rd_b': 0.1859903335571289, 'rd_r': 0.01592356711626053, 'rd_t': -0.006038647145032883, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 104, 'ymin': 316, 'xmax': 160, 'ymax': 329, 'lineNumber': 13, 'rd_b': 0.054347824305295944, 'rd_r': 0.0, 'rd_t': -0.06521739065647125, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 10.0, 'nSpecial': 0.0, 'obj': '8895831569', 'numLabel': 12, 'labelName': 'customer.phone_number'}, {'xmin': 43, 'ymin': 333, 'xmax': 80, 'ymax': 346, 'lineNumber': 14, 'rd_b': 0.07004830986261368, 'rd_r': 0.10191082954406738, 'rd_t': -0.04951690882444382, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Product', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 112, 'ymin': 333, 'xmax': 138, 'ymax': 347, 'lineNumber': 14, 'rd_b': 0.04589372128248215, 'rd_r': 0.041401274502277374, 'rd_t': -0.08574879169464111, 'rd_l': -0.10191082954406738, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Qty', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 151, 'ymin': 336, 'xmax': 177, 'ymax': 344, 'lineNumber': 14, 'rd_b': 0.006038647145032883, 'rd_r': 0.05095541477203369, 'rd_t': -0.030193237587809563, 'rd_l': -0.041401274502277374, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Rate', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 193, 'ymin': 335, 'xmax': 215, 'ymax': 344, 'lineNumber': 14, 'rd_b': 0.006038647145032883, 'rd_r': 0.06050955504179001, 'rd_t': 0.0, 'rd_l': -0.05095541477203369, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Disc', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 234, 'ymin': 335, 'xmax': 277, 'ymax': 344, 'lineNumber': 14, 'rd_b': 0.036231882870197296, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.06050955504179001, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Amount', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 37, 'ymin': 349, 'xmax': 75, 'ymax': 362, 'lineNumber': 15, 'rd_b': 0.06763284653425217, 'rd_r': 0.02866242080926895, 'rd_t': -0.06884057819843292, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Barcode', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 84, 'ymin': 349, 'xmax': 87, 'ymax': 362, 'lineNumber': 15, 'rd_b': 0.11835748702287674, 'rd_r': 0.03503184765577316, 'rd_t': -0.06884057819843292, 'rd_l': -0.02866242080926895, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 98, 'ymin': 349, 'xmax': 117, 'ymax': 362, 'lineNumber': 15, 'rd_b': 0.06763284653425217, 'rd_r': 0.012738853693008423, 'rd_t': -0.06884057819843292, 'rd_l': -0.03503184765577316, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'HSN', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 121, 'ymin': 349, 'xmax': 145, 'ymax': 362, 'lineNumber': 15, 'rd_b': 0.05193236842751503, 'rd_r': 0.025477707386016846, 'rd_t': -0.04589372128248215, 'rd_l': -0.012738853693008423, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Code', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 153, 'ymin': 349, 'xmax': 172, 'ymax': 362, 'lineNumber': 15, 'rd_b': 0.013285024091601372, 'rd_r': 0.012738853693008423, 'rd_t': -0.04589372128248215, 'rd_l': -0.025477707386016846, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'GST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 176, 'ymin': 349, 'xmax': 183, 'ymax': 362, 'lineNumber': 15, 'rd_b': 0.02777777798473835, 'rd_r': 0.02866242080926895, 'rd_t': -0.006038647145032883, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 192, 'ymin': 349, 'xmax': 214, 'ymax': 362, 'lineNumber': 15, 'rd_b': 0.014492753893136978, 'rd_r': 0.01592356711626053, 'rd_t': -0.006038647145032883, 'rd_l': -0.02866242080926895, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Style', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 219, 'ymin': 349, 'xmax': 232, 'ymax': 362, 'lineNumber': 15, 'rd_b': 0.026570048183202744, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': 'No.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 21, 'ymin': 371, 'xmax': 23, 'ymax': 381, 'lineNumber': 16, 'rd_b': 0.02777777798473835, 'rd_r': 0.041401274502277374, 'rd_t': -0.07246376574039459, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '1', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 36, 'ymin': 371, 'xmax': 66, 'ymax': 381, 'lineNumber': 16, 'rd_b': 0.0748792290687561, 'rd_r': 0.1719745248556137, 'rd_t': -0.050724636763334274, 'rd_l': -0.041401274502277374, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'DRESS', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 120, 'ymin': 374, 'xmax': 123, 'ymax': 380, 'lineNumber': 16, 'rd_b': 0.07729468494653702, 'rd_r': 0.07961783558130264, 'rd_t': -0.054347824305295944, 'rd_l': -0.1719745248556137, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '1', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 148, 'ymin': 373, 'xmax': 183, 'ymax': 383, 'lineNumber': 16, 'rd_b': 0.002415458904579282, 'rd_r': 0.09872611612081528, 'rd_t': -0.013285024091601372, 'rd_l': -0.07961783558130264, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '2,799.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 214, 'ymin': 374, 'xmax': 230, 'ymax': 381, 'lineNumber': 16, 'rd_b': 0.02777777798473835, 'rd_r': 0.03821656107902527, 'rd_t': -0.014492753893136978, 'rd_l': -0.09872611612081528, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '0.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 242, 'ymin': 374, 'xmax': 275, 'ymax': 382, 'lineNumber': 16, 'rd_b': 0.026570048183202744, 'rd_r': 0.0, 'rd_t': -0.036231882870197296, 'rd_l': -0.03821656107902527, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '2,799.00', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 33, 'ymin': 385, 'xmax': 73, 'ymax': 398, 'lineNumber': 17, 'rd_b': 0.054347824305295944, 'rd_r': 0.009554140269756317, 'rd_t': -0.08937197923660278, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '89051344', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 76, 'ymin': 385, 'xmax': 98, 'ymax': 398, 'lineNumber': 17, 'rd_b': 0.07608695328235626, 'rd_r': 0.01592356711626053, 'rd_t': -0.06763284653425217, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 0.0, 'obj': '10645', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 103, 'ymin': 385, 'xmax': 143, 'ymax': 398, 'lineNumber': 17, 'rd_b': 0.1026570051908493, 'rd_r': 0.012738853693008423, 'rd_t': -0.04589372128248215, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '62044990', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 147, 'ymin': 385, 'xmax': 165, 'ymax': 398, 'lineNumber': 17, 'rd_b': 0.009661835618317127, 'rd_r': 0.01592356711626053, 'rd_t': -0.002415458904579282, 'rd_l': -0.012738853693008423, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'GST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 170, 'ymin': 385, 'xmax': 177, 'ymax': 398, 'lineNumber': 17, 'rd_b': 0.02415458858013153, 'rd_r': 0.006369426846504211, 'rd_t': -0.02777777798473835, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': '12', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 179, 'ymin': 385, 'xmax': 186, 'ymax': 398, 'lineNumber': 17, 'rd_b': 0.02415458858013153, 'rd_r': 0.01592356711626053, 'rd_t': 0.0, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 191, 'ymin': 384, 'xmax': 264, 'ymax': 398, 'lineNumber': 17, 'rd_b': 0.022946860641241074, 'rd_r': 0.0, 'rd_t': -0.026570048183202744, 'rd_l': -0.01592356711626053, 'nUpper': 8.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 0.0, 'obj': 'SS21AN093DRLV', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 21, 'ymin': 404, 'xmax': 24, 'ymax': 416, 'lineNumber': 18, 'rd_b': 0.05314009636640549, 'rd_r': 0.03821656107902527, 'rd_t': -0.02777777798473835, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '2', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 36, 'ymin': 404, 'xmax': 53, 'ymax': 416, 'lineNumber': 18, 'rd_b': 0.08091787248849869, 'rd_r': 0.21337579190731049, 'rd_t': -0.07004830986261368, 'rd_l': -0.03821656107902527, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TOP', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 120, 'ymin': 405, 'xmax': 123, 'ymax': 412, 'lineNumber': 18, 'rd_b': 0.3055555522441864, 'rd_r': 0.08598726242780685, 'rd_t': -0.05193236842751503, 'rd_l': -0.21337579190731049, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '1', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 150, 'ymin': 406, 'xmax': 184, 'ymax': 415, 'lineNumber': 18, 'rd_b': 0.0036231884732842445, 'rd_r': 0.09554140269756317, 'rd_t': -0.009661835618317127, 'rd_l': -0.08598726242780685, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '1,799.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 214, 'ymin': 404, 'xmax': 230, 'ymax': 413, 'lineNumber': 18, 'rd_b': 0.08574879169464111, 'rd_r': 0.03503184765577316, 'rd_t': -0.02777777798473835, 'rd_l': -0.09554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '0.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 241, 'ymin': 404, 'xmax': 275, 'ymax': 415, 'lineNumber': 18, 'rd_b': 0.032608695328235626, 'rd_r': 0.0, 'rd_t': -0.026570048183202744, 'rd_l': -0.03503184765577316, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '1,799.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 33, 'ymin': 418, 'xmax': 97, 'ymax': 431, 'lineNumber': 19, 'rd_b': 0.06280193477869034, 'rd_r': 0.02229299396276474, 'rd_t': -0.06763284653425217, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 13.0, 'nSpecial': 0.0, 'obj': '8905134414613', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 104, 'ymin': 418, 'xmax': 143, 'ymax': 431, 'lineNumber': 19, 'rd_b': 0.06280193477869034, 'rd_r': 0.012738853693008423, 'rd_t': -0.06763284653425217, 'rd_l': -0.02229299396276474, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '62043990', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 147, 'ymin': 418, 'xmax': 165, 'ymax': 431, 'lineNumber': 19, 'rd_b': 0.20169082283973694, 'rd_r': 0.012738853693008423, 'rd_t': -0.0036231884732842445, 'rd_l': -0.012738853693008423, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'GST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 169, 'ymin': 418, 'xmax': 177, 'ymax': 431, 'lineNumber': 19, 'rd_b': 0.0640096589922905, 'rd_r': 0.006369426846504211, 'rd_t': -0.02415458858013153, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': '12', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 179, 'ymin': 418, 'xmax': 186, 'ymax': 431, 'lineNumber': 19, 'rd_b': 0.32125604152679443, 'rd_r': 0.01592356711626053, 'rd_t': -0.02415458858013153, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 191, 'ymin': 417, 'xmax': 256, 'ymax': 431, 'lineNumber': 19, 'rd_b': 0.03864734247326851, 'rd_r': 0.0, 'rd_t': -0.022946860641241074, 'rd_l': -0.01592356711626053, 'nUpper': 10.0, 'nAlpha': 10.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': 'SS21ANOGSTLV', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 21, 'ymin': 443, 'xmax': 46, 'ymax': 454, 'lineNumber': 20, 'rd_b': 0.03502415493130684, 'rd_r': 0.01592356711626053, 'rd_t': -0.0748792290687561, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Total', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 51, 'ymin': 443, 'xmax': 52, 'ymax': 454, 'lineNumber': 20, 'rd_b': 0.09541063010692596, 'rd_r': 0.21337579190731049, 'rd_t': -0.054347824305295944, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 119, 'ymin': 444, 'xmax': 124, 'ymax': 451, 'lineNumber': 20, 'rd_b': 0.1775362342596054, 'rd_r': 0.3407643437385559, 'rd_t': -0.07729468494653702, 'rd_l': -0.21337579190731049, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '2', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 231, 'ymin': 442, 'xmax': 276, 'ymax': 454, 'lineNumber': 20, 'rd_b': 0.036231882870197296, 'rd_r': 0.0, 'rd_t': -0.032608695328235626, 'rd_l': -0.3407643437385559, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '4,598.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 19, 'ymin': 460, 'xmax': 40, 'ymax': 472, 'lineNumber': 21, 'rd_b': 0.04589372128248215, 'rd_r': 0.012738853693008423, 'rd_t': -0.05314009636640549, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Net', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 44, 'ymin': 460, 'xmax': 85, 'ymax': 474, 'lineNumber': 21, 'rd_b': 0.07125604152679443, 'rd_r': 0.01592356711626053, 'rd_t': -0.11835748702287674, 'rd_l': -0.012738853693008423, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Payable', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 90, 'ymin': 461, 'xmax': 93, 'ymax': 473, 'lineNumber': 21, 'rd_b': 0.08574879169464111, 'rd_r': 0.4490445852279663, 'rd_t': -0.07608695328235626, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 234, 'ymin': 463, 'xmax': 275, 'ymax': 473, 'lineNumber': 21, 'rd_b': 0.047101449221372604, 'rd_r': 0.0, 'rd_t': -0.03864734247326851, 'rd_l': -0.4490445852279663, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '4598.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 21, 'ymin': 483, 'xmax': 31, 'ymax': 495, 'lineNumber': 22, 'rd_b': 0.05917874351143837, 'rd_r': 0.0031847134232521057, 'rd_t': -0.03502415493130684, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Rs', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 32, 'ymin': 483, 'xmax': 35, 'ymax': 495, 'lineNumber': 22, 'rd_b': 0.09661835432052612, 'rd_r': 0.012738853693008423, 'rd_t': -0.06280193477869034, 'rd_l': -0.0031847134232521057, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 39, 'ymin': 483, 'xmax': 59, 'ymax': 495, 'lineNumber': 22, 'rd_b': 0.09661835432052612, 'rd_r': 0.012738853693008423, 'rd_t': -0.08091787248849869, 'rd_l': -0.012738853693008423, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Four', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 63, 'ymin': 483, 'xmax': 105, 'ymax': 495, 'lineNumber': 22, 'rd_b': 0.12439613789319992, 'rd_r': 0.019108280539512634, 'rd_t': -0.1859903335571289, 'rd_l': -0.012738853693008423, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Thousand', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 111, 'ymin': 483, 'xmax': 127, 'ymax': 495, 'lineNumber': 22, 'rd_b': 0.14130434393882751, 'rd_r': 0.019108280539512634, 'rd_t': -0.1026570051908493, 'rd_l': -0.019108280539512634, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Five', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 133, 'ymin': 483, 'xmax': 167, 'ymax': 496, 'lineNumber': 22, 'rd_b': 0.14130434393882751, 'rd_r': 0.019108280539512634, 'rd_t': -0.06280193477869034, 'rd_l': -0.019108280539512634, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Hundred', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 173, 'ymin': 484, 'xmax': 198, 'ymax': 496, 'lineNumber': 22, 'rd_b': 0.12318840622901917, 'rd_r': 0.012738853693008423, 'rd_t': -0.0640096589922905, 'rd_l': -0.019108280539512634, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Ninety', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 202, 'ymin': 484, 'xmax': 205, 'ymax': 496, 'lineNumber': 22, 'rd_b': 0.14009661972522736, 'rd_r': 0.0031847134232521057, 'rd_t': 0.0, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 206, 'ymin': 484, 'xmax': 227, 'ymax': 496, 'lineNumber': 22, 'rd_b': 0.12318840622901917, 'rd_r': 0.01592356711626053, 'rd_t': -0.08574879169464111, 'rd_l': -0.0031847134232521057, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Eight', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 232, 'ymin': 484, 'xmax': 250, 'ymax': 496, 'lineNumber': 22, 'rd_b': 0.043478261679410934, 'rd_r': 0.0, 'rd_t': -0.036231882870197296, 'rd_l': -0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Only', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 24, 'ymin': 510, 'xmax': 45, 'ymax': 518, 'lineNumber': 23, 'rd_b': 0.11231884360313416, 'rd_r': 0.5955414175987244, 'rd_t': -0.04589372128248215, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Cash', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 232, 'ymin': 512, 'xmax': 271, 'ymax': 520, 'lineNumber': 23, 'rd_b': 0.032608695328235626, 'rd_r': 0.0, 'rd_t': -0.047101449221372604, 'rd_l': -0.5955414175987244, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '4.600.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 21, 'ymin': 533, 'xmax': 45, 'ymax': 541, 'lineNumber': 24, 'rd_b': 0.11835748702287674, 'rd_r': 0.01592356711626053, 'rd_t': -0.07125604152679443, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Cash', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 50, 'ymin': 533, 'xmax': 66, 'ymax': 541, 'lineNumber': 24, 'rd_b': 0.1497584581375122, 'rd_r': 0.5286624431610107, 'rd_t': -0.09541063010692596, 'rd_l': -0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Paid', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 232, 'ymin': 532, 'xmax': 271, 'ymax': 541, 'lineNumber': 24, 'rd_b': 0.06884057819843292, 'rd_r': 0.0, 'rd_t': -0.043478261679410934, 'rd_l': -0.5286624431610107, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '4,600,00', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 21, 'ymin': 544, 'xmax': 58, 'ymax': 558, 'lineNumber': 25, 'rd_b': 0.15338164567947388, 'rd_r': 0.01592356711626053, 'rd_t': -0.05917874351143837, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Balance', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 63, 'ymin': 544, 'xmax': 93, 'ymax': 558, 'lineNumber': 25, 'rd_b': 0.04830917716026306, 'rd_r': 0.5095541477203369, 'rd_t': -0.08574879169464111, 'rd_l': -0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Refund', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 253, 'ymin': 547, 'xmax': 271, 'ymax': 555, 'lineNumber': 25, 'rd_b': 0.07004830986261368, 'rd_r': 0.0, 'rd_t': -0.032608695328235626, 'rd_l': -0.5095541477203369, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '2.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 23, 'ymin': 575, 'xmax': 47, 'ymax': 588, 'lineNumber': 26, 'rd_b': 0.1473429948091507, 'rd_r': 0.02229299396276474, 'rd_t': -0.09661835432052612, 'rd_l': 0.0, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'GST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 54, 'ymin': 575, 'xmax': 101, 'ymax': 589, 'lineNumber': 26, 'rd_b': 0.0917874425649643, 'rd_r': 0.0, 'rd_t': -0.09661835432052612, 'rd_l': -0.02229299396276474, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Summary', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 20, 'ymin': 598, 'xmax': 72, 'ymax': 609, 'lineNumber': 27, 'rd_b': 0.10628019273281097, 'rd_r': 0.041401274502277374, 'rd_t': -0.12439613789319992, 'rd_l': 0.0, 'nUpper': 2.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': 'Taxable.Am', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 85, 'ymin': 598, 'xmax': 108, 'ymax': 609, 'lineNumber': 27, 'rd_b': 0.10628019273281097, 'rd_r': 0.02229299396276474, 'rd_t': -0.04830917716026306, 'rd_l': -0.041401274502277374, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'COST', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 115, 'ymin': 598, 'xmax': 119, 'ymax': 609, 'lineNumber': 27, 'rd_b': 0.0917874425649643, 'rd_r': 0.04458598792552948, 'rd_t': -0.1775362342596054, 'rd_l': -0.02229299396276474, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 133, 'ymin': 598, 'xmax': 174, 'ymax': 609, 'lineNumber': 27, 'rd_b': 0.03502415493130684, 'rd_r': 0.04458598792552948, 'rd_t': -0.20169082283973694, 'rd_l': -0.04458598792552948, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'COSTA', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 188, 'ymin': 598, 'xmax': 212, 'ymax': 609, 'lineNumber': 27, 'rd_b': 0.10628019273281097, 'rd_r': 0.02229299396276474, 'rd_t': -0.12318840622901917, 'rd_l': -0.04458598792552948, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SOST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 219, 'ymin': 598, 'xmax': 223, 'ymax': 609, 'lineNumber': 27, 'rd_b': 0.0917874425649643, 'rd_r': 0.02229299396276474, 'rd_t': -0.12318840622901917, 'rd_l': -0.02229299396276474, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 230, 'ymin': 598, 'xmax': 271, 'ymax': 609, 'lineNumber': 27, 'rd_b': 0.03502415493130684, 'rd_r': 0.0, 'rd_t': -0.06884057819843292, 'rd_l': -0.02229299396276474, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SOSTA', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 25, 'ymin': 611, 'xmax': 59, 'ymax': 620, 'lineNumber': 28, 'rd_b': 0.12560386955738068, 'rd_r': 0.13694266974925995, 'rd_t': -0.11231884360313416, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '4,105.34', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 102, 'ymin': 612, 'xmax': 118, 'ymax': 619, 'lineNumber': 28, 'rd_b': 0.09420289844274521, 'rd_r': 0.09235668927431107, 'rd_t': -0.14130434393882751, 'rd_l': -0.13694266974925995, 'nUpper': 1.0, 'nAlpha': 1.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 1.0, 'obj': '6.0C', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 147, 'ymin': 613, 'xmax': 173, 'ymax': 620, 'lineNumber': 28, 'rd_b': 0.07850241661071777, 'rd_r': 0.10191082954406738, 'rd_t': -0.14130434393882751, 'rd_l': -0.09235668927431107, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '246.33', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 205, 'ymin': 612, 'xmax': 221, 'ymax': 619, 'lineNumber': 28, 'rd_b': 0.07971014827489853, 'rd_r': 0.07643312215805054, 'rd_t': -0.14009661972522736, 'rd_l': -0.10191082954406738, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '6.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 245, 'ymin': 613, 'xmax': 272, 'ymax': 621, 'lineNumber': 28, 'rd_b': 0.07729468494653702, 'rd_r': 0.0, 'rd_t': -0.07004830986261368, 'rd_l': -0.07643312215805054, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '246.33', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 25, 'ymin': 639, 'xmax': 59, 'ymax': 647, 'lineNumber': 29, 'rd_b': 0.09299516677856445, 'rd_r': 0.2802547812461853, 'rd_t': -0.11835748702287674, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 2.0, 'obj': '4,105.34', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 147, 'ymin': 638, 'xmax': 173, 'ymax': 647, 'lineNumber': 29, 'rd_b': 0.07608695328235626, 'rd_r': 0.2261146456003189, 'rd_t': -0.03502415493130684, 'rd_l': -0.2802547812461853, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '246.33', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 244, 'ymin': 638, 'xmax': 270, 'ymax': 646, 'lineNumber': 29, 'rd_b': 0.047101449221372604, 'rd_r': 0.0, 'rd_t': -0.03502415493130684, 'rd_l': -0.2261146456003189, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '246.33', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 64, 'ymin': 665, 'xmax': 77, 'ymax': 678, 'lineNumber': 30, 'rd_b': 0.022946860641241074, 'rd_r': 0.01592356711626053, 'rd_t': -0.1497584581375122, 'rd_l': 0.0, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CIN', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 82, 'ymin': 665, 'xmax': 83, 'ymax': 678, 'lineNumber': 30, 'rd_b': 0.03864734247326851, 'rd_r': 0.025477707386016846, 'rd_t': -0.0917874425649643, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 91, 'ymin': 665, 'xmax': 219, 'ymax': 678, 'lineNumber': 30, 'rd_b': 0.00845410581678152, 'rd_r': 0.0, 'rd_t': -0.3055555522441864, 'rd_l': -0.025477707386016846, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 15.0, 'nSpecial': 0.0, 'obj': 'U18209MH2018PTC318048', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 38, 'ymin': 685, 'xmax': 94, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.030193237587809563, 'rd_r': -0.14012739062309265, 'rd_t': -0.15338164567947388, 'rd_l': 0.0, 'nUpper': 2.0, 'nAlpha': 10.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': 'Regd.Office', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 50, 'ymin': 697, 'xmax': 75, 'ymax': 711, 'lineNumber': 31, 'rd_b': 0.03140096738934517, 'rd_r': 0.006369426846504211, 'rd_t': -0.10628019273281097, 'rd_l': 0.14012739062309265, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'MIDC', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 77, 'ymin': 697, 'xmax': 77, 'ymax': 711, 'lineNumber': 31, 'rd_b': 0.047101449221372604, 'rd_r': 0.019108280539512634, 'rd_t': -0.022946860641241074, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 83, 'ymin': 697, 'xmax': 112, 'ymax': 711, 'lineNumber': 31, 'rd_b': 0.015700483694672585, 'rd_r': -0.0573248416185379, 'rd_t': -0.10628019273281097, 'rd_l': -0.019108280539512634, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Rabale', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 94, 'ymin': 685, 'xmax': 97, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.013285024091601372, 'rd_r': 0.012738853693008423, 'rd_t': -0.00845410581678152, 'rd_l': 0.0573248416185379, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 101, 'ymin': 685, 'xmax': 117, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.030193237587809563, 'rd_r': -0.009554140269756317, 'rd_t': -0.0917874425649643, 'rd_l': -0.012738853693008423, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Plot', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 114, 'ymin': 697, 'xmax': 116, 'ymax': 711, 'lineNumber': 31, 'rd_b': 0.03140096738934517, 'rd_r': 0.012738853693008423, 'rd_t': -0.09420289844274521, 'rd_l': 0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 120, 'ymin': 697, 'xmax': 138, 'ymax': 711, 'lineNumber': 31, 'rd_b': -0.03140096738934517, 'rd_r': -0.05095541477203369, 'rd_t': 0.0, 'rd_l': -0.012738853693008423, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Navi', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 122, 'ymin': 685, 'xmax': 132, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.04589372128248215, 'rd_r': 0.019108280539512634, 'rd_t': 0.03140096738934517, 'rd_l': 0.05095541477203369, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'No', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 138, 'ymin': 685, 'xmax': 143, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.030193237587809563, 'rd_r': -0.0031847134232521057, 'rd_t': 0.0, 'rd_l': -0.019108280539512634, 'nUpper': 1.0, 'nAlpha': 1.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'R', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 142, 'ymin': 697, 'xmax': 179, 'ymax': 711, 'lineNumber': 31, 'rd_b': -0.01690821163356304, 'rd_r': -0.10191082954406738, 'rd_t': -0.32125604152679443, 'rd_l': 0.0031847134232521057, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Mumbai', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 147, 'ymin': 685, 'xmax': 181, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.013285024091601372, 'rd_r': -0.012738853693008423, 'rd_t': -0.07850241661071777, 'rd_l': 0.10191082954406738, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '84771/1', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 177, 'ymin': 697, 'xmax': 181, 'ymax': 711, 'lineNumber': 31, 'rd_b': 0.015700483694672585, 'rd_r': 0.0031847134232521057, 'rd_t': 0.01690821163356304, 'rd_l': 0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 182, 'ymin': 685, 'xmax': 183, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.04589372128248215, 'rd_r': -0.0031847134232521057, 'rd_t': 0.0, 'rd_l': -0.0031847134232521057, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 182, 'ymin': 697, 'xmax': 201, 'ymax': 711, 'lineNumber': 31, 'rd_b': -0.001207729452289641, 'rd_r': -0.041401274502277374, 'rd_t': -0.10628019273281097, 'rd_l': 0.0031847134232521057, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'India', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 188, 'ymin': 685, 'xmax': 206, 'ymax': 699, 'lineNumber': 31, 'rd_b': -0.002415458904579282, 'rd_r': -0.009554140269756317, 'rd_t': -0.07971014827489853, 'rd_l': 0.041401274502277374, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TTC', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 203, 'ymin': 697, 'xmax': 207, 'ymax': 711, 'lineNumber': 31, 'rd_b': -0.001207729452289641, 'rd_r': 0.009554140269756317, 'rd_t': 0.002415458904579282, 'rd_l': 0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 210, 'ymin': 685, 'xmax': 223, 'ymax': 699, 'lineNumber': 31, 'rd_b': -0.002415458904579282, 'rd_r': -0.041401274502277374, 'rd_t': -0.0917874425649643, 'rd_l': -0.009554140269756317, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Ind', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 210, 'ymin': 697, 'xmax': 243, 'ymax': 711, 'lineNumber': 31, 'rd_b': 0.015700483694672585, 'rd_r': -0.041401274502277374, 'rd_t': 0.002415458904579282, 'rd_l': 0.041401274502277374, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 0.0, 'obj': '400701', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 230, 'ymin': 685, 'xmax': 250, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.013285024091601372, 'rd_r': 0.006369426846504211, 'rd_t': -0.07729468494653702, 'rd_l': 0.041401274502277374, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Area', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 252, 'ymin': 685, 'xmax': 255, 'ymax': 699, 'lineNumber': 31, 'rd_b': 0.030193237587809563, 'rd_r': 0.0, 'rd_t': -0.047101449221372604, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 23, 'ymin': 710, 'xmax': 39, 'ymax': 723, 'lineNumber': 32, 'rd_b': 0.032608695328235626, 'rd_r': -0.05095541477203369, 'rd_t': -0.1473429948091507, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'The', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 23, 'ymin': 724, 'xmax': 30, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.028985507786273956, 'rd_r': 0.01592356711626053, 'rd_t': -0.12560386955738068, 'rd_l': 0.05095541477203369, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'to', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 35, 'ymin': 724, 'xmax': 62, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.015700483694672585, 'rd_r': -0.06369426846504211, 'rd_t': -0.09299516677856445, 'rd_l': -0.01592356711626053, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'House', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 42, 'ymin': 710, 'xmax': 82, 'ymax': 723, 'lineNumber': 32, 'rd_b': -0.015700483694672585, 'rd_r': -0.047770701348781586, 'rd_t': -0.03864734247326851, 'rd_l': 0.06369426846504211, 'nUpper': 0.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'products', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 67, 'ymin': 724, 'xmax': 75, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.028985507786273956, 'rd_r': 0.012738853693008423, 'rd_t': -0.030193237587809563, 'rd_l': 0.047770701348781586, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'of', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 79, 'ymin': 724, 'xmax': 99, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': -0.0541401281952858, 'rd_t': -0.015700483694672585, 'rd_l': -0.012738853693008423, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Anita', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 82, 'ymin': 710, 'xmax': 85, 'ymax': 723, 'lineNumber': 32, 'rd_b': 0.04589372128248215, 'rd_r': 0.006369426846504211, 'rd_t': 0.015700483694672585, 'rd_l': 0.0541401281952858, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '/', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 87, 'ymin': 710, 'xmax': 118, 'ymax': 723, 'lineNumber': 32, 'rd_b': 0.032608695328235626, 'rd_r': -0.041401274502277374, 'rd_t': -0.013285024091601372, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'designs', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 105, 'ymin': 724, 'xmax': 136, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.028985507786273956, 'rd_r': -0.041401274502277374, 'rd_t': -0.030193237587809563, 'rd_l': 0.041401274502277374, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Dongre', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 123, 'ymin': 710, 'xmax': 170, 'ymax': 723, 'lineNumber': 32, 'rd_b': 0.01690821163356304, 'rd_r': -0.09235668927431107, 'rd_t': -0.07608695328235626, 'rd_l': 0.041401274502277374, 'nUpper': 0.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'purchased', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 141, 'ymin': 724, 'xmax': 171, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': 0.009554140269756317, 'rd_t': -0.030193237587809563, 'rd_l': 0.09235668927431107, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Private', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 710, 'xmax': 184, 'ymax': 723, 'lineNumber': 32, 'rd_b': 0.032608695328235626, 'rd_r': -0.025477707386016846, 'rd_t': -0.013285024091601372, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'by', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 176, 'ymin': 724, 'xmax': 207, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': -0.06369426846504211, 'rd_t': -0.015700483694672585, 'rd_l': 0.025477707386016846, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Limited', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 187, 'ymin': 710, 'xmax': 203, 'ymax': 723, 'lineNumber': 32, 'rd_b': 0.01690821163356304, 'rd_r': 0.012738853693008423, 'rd_t': 0.001207729452289641, 'rd_l': 0.06369426846504211, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'you', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 207, 'ymin': 710, 'xmax': 221, 'ymax': 723, 'lineNumber': 32, 'rd_b': 0.01690821163356304, 'rd_r': -0.02866242080926895, 'rd_t': 0.001207729452289641, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'are', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 212, 'ymin': 724, 'xmax': 227, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': -0.006369426846504211, 'rd_t': -0.015700483694672585, 'rd_l': 0.02866242080926895, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'and', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 225, 'ymin': 710, 'xmax': 274, 'ymax': 724, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': -0.13694266974925995, 'rd_t': -0.013285024091601372, 'rd_l': 0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 11.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'proprietary', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 231, 'ymin': 724, 'xmax': 233, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': 0.009554140269756317, 'rd_t': 0.0, 'rd_l': 0.13694266974925995, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '/', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 236, 'ymin': 724, 'xmax': 245, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.015700483694672585, 'rd_r': 0.012738853693008423, 'rd_t': 0.0, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'or', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 249, 'ymin': 724, 'xmax': 258, 'ymax': 737, 'lineNumber': 32, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.030193237587809563, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'its', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 23, 'ymin': 737, 'xmax': 75, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.001207729452289641, 'rd_r': 0.01592356711626053, 'rd_t': -0.03140096738934517, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 12.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'subsidiaries', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 80, 'ymin': 737, 'xmax': 95, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.01592356711626053, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'and', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 100, 'ymin': 737, 'xmax': 118, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.012738853693008423, 'rd_t': -0.03140096738934517, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'may', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 122, 'ymin': 737, 'xmax': 134, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.014492753893136978, 'rd_r': 0.01592356711626053, 'rd_t': -0.04589372128248215, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'not', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 139, 'ymin': 737, 'xmax': 149, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.001207729452289641, 'rd_r': 0.01592356711626053, 'rd_t': -0.01690821163356304, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'be', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 154, 'ymin': 737, 'xmax': 171, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.001207729452289641, 'rd_r': 0.0031847134232521057, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'rent', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 172, 'ymin': 737, 'xmax': 173, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.006369426846504211, 'rd_t': 0.0, 'rd_l': -0.0031847134232521057, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 175, 'ymin': 737, 'xmax': 189, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.014492753893136978, 'rd_r': 0.0031847134232521057, 'rd_t': -0.04589372128248215, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'out', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 190, 'ymin': 737, 'xmax': 191, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.012738853693008423, 'rd_t': 0.0, 'rd_l': -0.0031847134232521057, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 195, 'ymin': 737, 'xmax': 209, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.014492753893136978, 'rd_r': 0.006369426846504211, 'rd_t': -0.01690821163356304, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'sub', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 211, 'ymin': 737, 'xmax': 212, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.006369426846504211, 'rd_t': -0.01690821163356304, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 214, 'ymin': 737, 'xmax': 223, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.009554140269756317, 'rd_t': 0.0, 'rd_l': -0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'let', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 226, 'ymin': 737, 'xmax': 226, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.01592356711626053, 'rd_t': 0.0, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 231, 'ymin': 737, 'xmax': 273, 'ymax': 749, 'lineNumber': 33, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'subjected', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 23, 'ymin': 750, 'xmax': 31, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': -0.025477707386016846, 'rd_t': -0.032608695328235626, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'to', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 23, 'ymin': 761, 'xmax': 54, 'ymax': 776, 'lineNumber': 34, 'rd_b': -0.03140096738934517, 'rd_r': -0.06050955504179001, 'rd_t': -0.028985507786273956, 'rd_l': 0.025477707386016846, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'without', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 35, 'ymin': 750, 'xmax': 44, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.0031847134232521057, 'rd_t': -0.015700483694672585, 'rd_l': 0.06050955504179001, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 're', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 45, 'ymin': 750, 'xmax': 46, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.009554140269756317, 'rd_t': -0.001207729452289641, 'rd_l': -0.0031847134232521057, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 49, 'ymin': 750, 'xmax': 64, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': -0.01592356711626053, 'rd_t': 0.03140096738934517, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'sale', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 59, 'ymin': 761, 'xmax': 71, 'ymax': 776, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': -0.006369426846504211, 'rd_t': -0.028985507786273956, 'rd_l': 0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'the', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 69, 'ymin': 750, 'xmax': 77, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': -0.006369426846504211, 'rd_t': -0.047101449221372604, 'rd_l': 0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'or', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 75, 'ymin': 761, 'xmax': 95, 'ymax': 776, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': -0.041401274502277374, 'rd_t': -0.04589372128248215, 'rd_l': 0.006369426846504211, 'nUpper': 0.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'prior', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 82, 'ymin': 750, 'xmax': 137, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': -0.12101911008358002, 'rd_t': -0.032608695328235626, 'rd_l': 0.041401274502277374, 'nUpper': 0.0, 'nAlpha': 13.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'redistributed', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 99, 'ymin': 761, 'xmax': 129, 'ymax': 776, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.012738853693008423, 'rd_t': -0.028985507786273956, 'rd_l': 0.12101911008358002, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'written', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 133, 'ymin': 761, 'xmax': 167, 'ymax': 776, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': -0.08280254900455475, 'rd_t': -0.014492753893136978, 'rd_l': -0.012738853693008423, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'consent', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 141, 'ymin': 750, 'xmax': 147, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.01592356711626053, 'rd_t': -0.001207729452289641, 'rd_l': 0.08280254900455475, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'in', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 152, 'ymin': 750, 'xmax': 166, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.01592356711626053, 'rd_t': -0.001207729452289641, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'any', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 171, 'ymin': 750, 'xmax': 203, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': -0.09235668927431107, 'rd_t': -0.032608695328235626, 'rd_l': -0.01592356711626053, 'nUpper': 0.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'manner', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 761, 'xmax': 189, 'ymax': 776, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.02229299396276474, 'rd_t': -0.014492753893136978, 'rd_l': 0.09235668927431107, 'nUpper': 0.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'from', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 196, 'ymin': 761, 'xmax': 205, 'ymax': 776, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.009554140269756317, 'rd_t': -0.014492753893136978, 'rd_l': -0.02229299396276474, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'us', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 208, 'ymin': 750, 'xmax': 258, 'ymax': 762, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.015700483694672585, 'rd_l': -0.009554140269756317, 'nUpper': 0.0, 'nAlpha': 10.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'whatsoever', 'numLabel': 8, 'labelName': 'vendor.email'}]

# # aldo - 00002.pdf
# arr =  [{'xmin': 742, 'ymin': 156, 'xmax': 957, 'ymax': 203, 'lineNumber': 1, 'rd_b': 0.010454545728862286, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ALDO', 'numLabel': 5, 'labelName': 'vendor.name'}, {'xmin': 669, 'ymin': 249, 'xmax': 730, 'ymax': 267, 'lineNumber': 2, 'rd_b': 0.01772727258503437, 'rd_r': 0.008235294371843338, 'rd_t': 0.0, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Major', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 744, 'ymin': 249, 'xmax': 816, 'ymax': 267, 'lineNumber': 2, 'rd_b': 0.0013636363437399268, 'rd_r': 0.012352941557765007, 'rd_t': -0.010454545728862286, 'rd_l': -0.008235294371843338, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Brands', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 837, 'ymin': 249, 'xmax': 842, 'ymax': 267, 'lineNumber': 2, 'rd_b': 0.0011363636003807187, 'rd_r': 0.0035294117406010628, 'rd_t': 0.0, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 848, 'ymin': 249, 'xmax': 901, 'ymax': 267, 'lineNumber': 2, 'rd_b': 0.05818181857466698, 'rd_r': 0.004705882165580988, 'rd_t': 0.0, 'rd_l': -0.0035294117406010628, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'INDIA', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 909, 'ymin': 249, 'xmax': 912, 'ymax': 267, 'lineNumber': 2, 'rd_b': 0.4840908944606781, 'rd_r': 0.012352941557765007, 'rd_t': 0.0, 'rd_l': -0.004705882165580988, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 933, 'ymin': 249, 'xmax': 965, 'ymax': 267, 'lineNumber': 2, 'rd_b': 0.05818181857466698, 'rd_r': 0.004705882165580988, 'rd_t': 0.0, 'rd_l': -0.012352941557765007, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Pvt', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 973, 'ymin': 249, 'xmax': 978, 'ymax': 267, 'lineNumber': 2, 'rd_b': 0.1556818187236786, 'rd_r': 0.0035294117406010628, 'rd_t': 0.0, 'rd_l': -0.004705882165580988, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 984, 'ymin': 249, 'xmax': 1030, 'ymax': 267, 'lineNumber': 2, 'rd_b': 0.1786363571882248, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.0035294117406010628, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': 'Ltd.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 767, 'ymin': 273, 'xmax': 810, 'ymax': 290, 'lineNumber': 3, 'rd_b': 0.012500000186264515, 'rd_r': 0.010588235221803188, 'rd_t': -0.0013636363437399268, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Tax', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 828, 'ymin': 272, 'xmax': 929, 'ymax': 291, 'lineNumber': 3, 'rd_b': 0.0459090918302536, 'rd_r': 0.0, 'rd_t': -0.0011363636003807187, 'rd_l': -0.010588235221803188, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Invoice', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 173, 'ymin': 345, 'xmax': 200, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.0011363636003807187, 'rd_r': 0.012352941557765007, 'rd_t': 0.0, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 2.0, 'nSpecial': 0.0, 'obj': '23', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 221, 'ymin': 345, 'xmax': 316, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.008181817829608917, 'rd_r': 0.010588235221803188, 'rd_t': 0.0, 'rd_l': -0.012352941557765007, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Ground', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 334, 'ymin': 345, 'xmax': 412, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.008181817829608917, 'rd_r': 0.0035294117406010628, 'rd_t': 0.0, 'rd_l': -0.010588235221803188, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Floor', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 418, 'ymin': 345, 'xmax': 423, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.02090909145772457, 'rd_r': 0.014705882407724857, 'rd_t': 0.0, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 448, 'ymin': 345, 'xmax': 527, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.02090909145772457, 'rd_r': 0.010588235221803188, 'rd_t': 0.0, 'rd_l': -0.014705882407724857, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Forum', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 545, 'ymin': 345, 'xmax': 606, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.02818181738257408, 'rd_r': 0.004117647185921669, 'rd_t': 0.0, 'rd_l': -0.010588235221803188, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Mall', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 613, 'ymin': 345, 'xmax': 618, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.16318181157112122, 'rd_r': 0.014705882407724857, 'rd_t': 0.0, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 643, 'ymin': 345, 'xmax': 721, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.02818181738257408, 'rd_r': 0.011176470667123795, 'rd_t': -0.01772727258503437, 'rd_l': -0.014705882407724857, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Hosur', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 740, 'ymin': 345, 'xmax': 803, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.03500000014901161, 'rd_r': 0.0029411765281111, 'rd_t': -0.012500000186264515, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Road', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 808, 'ymin': 345, 'xmax': 813, 'ymax': 369, 'lineNumber': 4, 'rd_b': 0.03500000014901161, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 172, 'ymin': 374, 'xmax': 347, 'ymax': 399, 'lineNumber': 5, 'rd_b': 0.0013636363437399268, 'rd_r': 0.0, 'rd_t': -0.0011363636003807187, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 11.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Koramangala', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 172, 'ymin': 405, 'xmax': 250, 'ymax': 425, 'lineNumber': 6, 'rd_b': 0.008409091271460056, 'rd_r': 0.011176470667123795, 'rd_t': -0.008181817829608917, 'rd_l': 0.0, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'GSTIN', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 269, 'ymin': 405, 'xmax': 310, 'ymax': 425, 'lineNumber': 6, 'rd_b': 0.015454545617103577, 'rd_r': 0.014705882407724857, 'rd_t': -0.0013636363437399268, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': 'No.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 335, 'ymin': 405, 'xmax': 575, 'ymax': 425, 'lineNumber': 6, 'rd_b': 0.015454545617103577, 'rd_r': 0.0, 'rd_t': -0.008181817829608917, 'rd_l': -0.014705882407724857, 'nUpper': 8.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 7.0, 'nSpecial': 0.0, 'obj': '29AACCM4949B1ZG', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 171, 'ymin': 462, 'xmax': 313, 'ymax': 490, 'lineNumber': 7, 'rd_b': 0.0006818181718699634, 'rd_r': 0.011176470667123795, 'rd_t': -0.008409091271460056, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Corporate', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 332, 'ymin': 461, 'xmax': 442, 'ymax': 488, 'lineNumber': 7, 'rd_b': 0.0011363636003807187, 'rd_r': 0.0058823530562222, 'rd_t': -0.02090909145772457, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Address', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 452, 'ymin': 461, 'xmax': 455, 'ymax': 486, 'lineNumber': 7, 'rd_b': 0.001590909087099135, 'rd_r': 0.0, 'rd_t': -0.02090909145772457, 'rd_l': -0.0058823530562222, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 174, 'ymin': 493, 'xmax': 215, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.001590909087099135, 'rd_r': 0.004705882165580988, 'rd_t': -0.0006818181718699634, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 0.0, 'obj': '907', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 223, 'ymin': 493, 'xmax': 228, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.008409091271460056, 'rd_r': 0.014705882407724857, 'rd_t': 0.0, 'rd_l': -0.004705882165580988, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 253, 'ymin': 493, 'xmax': 266, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.001590909087099135, 'rd_r': 0.011176470667123795, 'rd_t': 0.0, 'rd_l': -0.014705882407724857, 'nUpper': 1.0, 'nAlpha': 1.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'B', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 285, 'ymin': 493, 'xmax': 348, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.001590909087099135, 'rd_r': 0.0029411765281111, 'rd_t': -0.015454545617103577, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Wing', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 353, 'ymin': 493, 'xmax': 358, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.008409091271460056, 'rd_r': 0.015882352367043495, 'rd_t': -0.015454545617103577, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 385, 'ymin': 493, 'xmax': 429, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.008409091271460056, 'rd_r': 0.011176470667123795, 'rd_t': -0.0011363636003807187, 'rd_l': -0.015882352367043495, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '9th', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 448, 'ymin': 493, 'xmax': 526, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.001590909087099135, 'rd_r': 0.0035294117406010628, 'rd_t': -0.001590909087099135, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Floor', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 532, 'ymin': 493, 'xmax': 537, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.03068181872367859, 'rd_r': 0.014117646962404251, 'rd_t': 0.0, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 12, 'labelName': 'customer.phone_number'}, {'xmin': 561, 'ymin': 493, 'xmax': 655, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.001590909087099135, 'rd_r': 0.012352941557765007, 'rd_t': -0.02818181738257408, 'rd_l': -0.014117646962404251, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Mittal', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 676, 'ymin': 493, 'xmax': 818, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.001590909087099135, 'rd_r': 0.0035294117406010628, 'rd_t': -0.02818181738257408, 'rd_l': -0.012352941557765007, 'nUpper': 1.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Commercia', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 824, 'ymin': 493, 'xmax': 829, 'ymax': 516, 'lineNumber': 8, 'rd_b': 0.09840909391641617, 'rd_r': 0.0, 'rd_t': -0.0459090918302536, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 173, 'ymin': 523, 'xmax': 217, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.02340909093618393, 'rd_r': 0.011176470667123795, 'rd_t': -0.001590909087099135, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '4th', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 236, 'ymin': 523, 'xmax': 298, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.04568181931972504, 'rd_r': 0.011176470667123795, 'rd_t': -0.001590909087099135, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Near', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 317, 'ymin': 523, 'xmax': 411, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.02340909093618393, 'rd_r': 0.012352941557765007, 'rd_t': -0.001590909087099135, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Mittal', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 432, 'ymin': 523, 'xmax': 592, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.0011363636003807187, 'rd_r': 0.002352941082790494, 'rd_t': -0.001590909087099135, 'rd_l': -0.012352941557765007, 'nUpper': 1.0, 'nAlpha': 10.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Commercial', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 596, 'ymin': 523, 'xmax': 601, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.10704545676708221, 'rd_r': 0.014705882407724857, 'rd_t': -0.001590909087099135, 'rd_l': -0.002352941082790494, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 626, 'ymin': 523, 'xmax': 736, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.05318181961774826, 'rd_r': 0.0029411765281111, 'rd_t': -0.001590909087099135, 'rd_l': -0.014705882407724857, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Andheri', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 741, 'ymin': 523, 'xmax': 753, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.053409092128276825, 'rd_r': 0.002352941082790494, 'rd_t': -0.03500000014901161, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 757, 'ymin': 523, 'xmax': 835, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.06113636493682861, 'rd_r': 0.011176470667123795, 'rd_t': -0.03500000014901161, 'rd_l': -0.002352941082790494, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Kurla', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 854, 'ymin': 523, 'xmax': 917, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.06113636493682861, 'rd_r': 0.0029411765281111, 'rd_t': -0.05818181857466698, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Road', 'numLabel': 14, 'labelName': 'generated_by.sales_person_id'}, {'xmin': 922, 'ymin': 523, 'xmax': 927, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.4272727370262146, 'rd_r': 0.014117646962404251, 'rd_t': 0.0, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 14, 'labelName': 'generated_by.sales_person_id'}, {'xmin': 951, 'ymin': 523, 'xmax': 1061, 'ymax': 548, 'lineNumber': 9, 'rd_b': 0.1377272754907608, 'rd_r': 0.015882352367043495, 'rd_t': -0.05818181857466698, 'rd_l': -0.014117646962404251, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Andheri', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1088, 'ymin': 524, 'xmax': 1092, 'ymax': 544, 'lineNumber': 9, 'rd_b': 0.42818182706832886, 'rd_r': 0.0035294117406010628, 'rd_t': 0.0, 'rd_l': -0.015882352367043495, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 1098, 'ymin': 524, 'xmax': 1159, 'ymax': 544, 'lineNumber': 9, 'rd_b': 0.06181818246841431, 'rd_r': 0.004117647185921669, 'rd_t': 0.0, 'rd_l': -0.0035294117406010628, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'East', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 1166, 'ymin': 524, 'xmax': 1170, 'ymax': 544, 'lineNumber': 9, 'rd_b': 0.09272727370262146, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 171, 'ymin': 553, 'xmax': 265, 'ymax': 577, 'lineNumber': 10, 'rd_b': 0.04681818187236786, 'rd_r': 0.012941176071763039, 'rd_t': -0.008409091271460056, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Mumbai', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 287, 'ymin': 553, 'xmax': 379, 'ymax': 577, 'lineNumber': 10, 'rd_b': 0.016818182542920113, 'rd_r': 0.004117647185921669, 'rd_t': -0.008409091271460056, 'rd_l': -0.012941176071763039, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 0.0, 'obj': '400059', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 386, 'ymin': 553, 'xmax': 390, 'ymax': 577, 'lineNumber': 10, 'rd_b': 0.038863636553287506, 'rd_r': 0.015882352367043495, 'rd_t': -0.008409091271460056, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ',', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 417, 'ymin': 553, 'xmax': 493, 'ymax': 577, 'lineNumber': 10, 'rd_b': 0.05431818217039108, 'rd_r': 0.0, 'rd_t': -0.0011363636003807187, 'rd_l': -0.015882352367043495, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'India', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 172, 'ymin': 651, 'xmax': 298, 'ymax': 669, 'lineNumber': 11, 'rd_b': 0.025909090414643288, 'rd_r': 0.0117647061124444, 'rd_t': -0.02340909093618393, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Customer', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 318, 'ymin': 651, 'xmax': 347, 'ymax': 669, 'lineNumber': 11, 'rd_b': 0.018409090116620064, 'rd_r': 0.005294117610901594, 'rd_t': -0.02340909093618393, 'rd_l': -0.0117647061124444, 'nUpper': 1.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'No', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 356, 'ymin': 651, 'xmax': 375, 'ymax': 669, 'lineNumber': 11, 'rd_b': 0.018409090116620064, 'rd_r': 0.015882352367043495, 'rd_t': -0.016818182542920113, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 2.0, 'obj': '.:', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 402, 'ymin': 651, 'xmax': 557, 'ymax': 669, 'lineNumber': 11, 'rd_b': 0.06454545259475708, 'rd_r': 0.0, 'rd_t': -0.03068181872367859, 'rd_l': -0.015882352367043495, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 10.0, 'nSpecial': 0.0, 'obj': '9986758771', 'numLabel': 12, 'labelName': 'customer.phone_number'}, {'xmin': 174, 'ymin': 749, 'xmax': 284, 'ymax': 767, 'lineNumber': 12, 'rd_b': 0.011136363260447979, 'rd_r': 0.011176470667123795, 'rd_t': -0.04568181931972504, 'rd_l': 0.0, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'RECEIPT', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 303, 'ymin': 750, 'xmax': 333, 'ymax': 766, 'lineNumber': 12, 'rd_b': 0.003863636404275894, 'rd_r': 0.004705882165580988, 'rd_t': -0.018409090116620064, 'rd_l': -0.011176470667123795, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'NO', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 341, 'ymin': 750, 'xmax': 361, 'ymax': 767, 'lineNumber': 12, 'rd_b': 0.003409090917557478, 'rd_r': 0.015294117853045464, 'rd_t': -0.018409090116620064, 'rd_l': -0.004705882165580988, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 2.0, 'obj': '.:', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 387, 'ymin': 748, 'xmax': 543, 'ymax': 768, 'lineNumber': 12, 'rd_b': 0.057045456022024155, 'rd_r': 0.0, 'rd_t': -0.038863636553287506, 'rd_l': -0.015294117853045464, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 10.0, 'nSpecial': 0.0, 'obj': '5580004778', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 174, 'ymin': 783, 'xmax': 250, 'ymax': 800, 'lineNumber': 13, 'rd_b': 0.02659090980887413, 'rd_r': 0.012941176071763039, 'rd_t': -0.04681818187236786, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Store', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 272, 'ymin': 783, 'xmax': 299, 'ymax': 800, 'lineNumber': 13, 'rd_b': 0.04227272793650627, 'rd_r': 0.005294117610901594, 'rd_t': -0.025909090414643288, 'rd_l': -0.012941176071763039, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ID', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 308, 'ymin': 783, 'xmax': 311, 'ymax': 800, 'lineNumber': 13, 'rd_b': 0.049772728234529495, 'rd_r': 0.015294117853045464, 'rd_t': -0.003863636404275894, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 6, 'labelName': 'vendor.phone_number'}, {'xmin': 337, 'ymin': 782, 'xmax': 395, 'ymax': 799, 'lineNumber': 13, 'rd_b': 0.0427272729575634, 'rd_r': 0.14235293865203857, 'rd_t': -0.003409090917557478, 'rd_l': -0.015294117853045464, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 0.0, 'obj': '8258', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 637, 'ymin': 782, 'xmax': 697, 'ymax': 800, 'lineNumber': 13, 'rd_b': 0.003863636404275894, 'rd_r': 0.005294117610901594, 'rd_t': -0.05318181961774826, 'rd_l': -0.14235293865203857, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Till', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 706, 'ymin': 782, 'xmax': 710, 'ymax': 799, 'lineNumber': 13, 'rd_b': 0.034090910106897354, 'rd_r': 0.014705882407724857, 'rd_t': 0.0, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 735, 'ymin': 783, 'xmax': 778, 'ymax': 800, 'lineNumber': 13, 'rd_b': 0.03386363759636879, 'rd_r': 0.0, 'rd_t': -0.053409092128276825, 'rd_l': -0.014705882407724857, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 0.0, 'obj': '558', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 176, 'ymin': 816, 'xmax': 331, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.025909090414643288, 'rd_r': 0.014117646962404251, 'rd_t': -0.011136363260447979, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 2.0, 'obj': '13-04-2021', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 355, 'ymin': 816, 'xmax': 430, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.05659090727567673, 'rd_r': 0.12117647379636765, 'rd_t': -0.05431818217039108, 'rd_l': -0.014117646962404251, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '15:09', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 636, 'ymin': 817, 'xmax': 746, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.02545454539358616, 'rd_r': 0.012941176071763039, 'rd_t': -0.003863636404275894, 'rd_l': -0.12117647379636765, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Cashier', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 768, 'ymin': 817, 'xmax': 795, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.05659090727567673, 'rd_r': 0.004705882165580988, 'rd_t': -0.06113636493682861, 'rd_l': -0.012941176071763039, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ID', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 803, 'ymin': 817, 'xmax': 807, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.07977272570133209, 'rd_r': 0.014705882407724857, 'rd_t': 0.0, 'rd_l': -0.004705882165580988, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 12, 'labelName': 'customer.phone_number'}, {'xmin': 832, 'ymin': 817, 'xmax': 907, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.02545454539358616, 'rd_r': 0.12941177189350128, 'rd_t': -0.06113636493682861, 'rd_l': -0.014705882407724857, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 0.0, 'obj': '55894', 'numLabel': 14, 'labelName': 'generated_by.sales_person_id'}, {'xmin': 1127, 'ymin': 816, 'xmax': 1237, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.026136362925171852, 'rd_r': 0.011176470667123795, 'rd_t': -0.06181818246841431, 'rd_l': -0.12941177189350128, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Cashier', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1256, 'ymin': 817, 'xmax': 1318, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.02545454539358616, 'rd_r': 0.005294117610901594, 'rd_t': 0.0, 'rd_l': -0.011176470667123795, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Name', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1327, 'ymin': 818, 'xmax': 1330, 'ymax': 837, 'lineNumber': 14, 'rd_b': 0.048636361956596375, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ':', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 172, 'ymin': 917, 'xmax': 314, 'ymax': 939, 'lineNumber': 15, 'rd_b': 0.0181818176060915, 'rd_r': 0.0, 'rd_t': -0.02659090980887413, 'rd_l': 0.0, 'nUpper': 8.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ITEM_NAME', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 172, 'ymin': 951, 'xmax': 234, 'ymax': 969, 'lineNumber': 16, 'rd_b': 0.019090909510850906, 'rd_r': 0.14941176772117615, 'rd_t': -0.025909090414643288, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CODE', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 488, 'ymin': 953, 'xmax': 535, 'ymax': 969, 'lineNumber': 16, 'rd_b': 0.011363636702299118, 'rd_r': 0.06470588594675064, 'rd_t': -0.06454545259475708, 'rd_l': -0.14941176772117615, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'HSN', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 645, 'ymin': 949, 'xmax': 691, 'ymax': 975, 'lineNumber': 16, 'rd_b': 0.02545454539358616, 'rd_r': 0.005294117610901594, 'rd_t': -0.02545454539358616, 'rd_l': -0.06470588594675064, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'QTY', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 700, 'ymin': 949, 'xmax': 705, 'ymax': 975, 'lineNumber': 16, 'rd_b': 0.07136363536119461, 'rd_r': 0.002352941082790494, 'rd_t': 0.0, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 709, 'ymin': 949, 'xmax': 755, 'ymax': 975, 'lineNumber': 16, 'rd_b': 0.01772727258503437, 'rd_r': 0.0029411765281111, 'rd_t': -0.034090910106897354, 'rd_l': -0.002352941082790494, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'pcs', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 760, 'ymin': 949, 'xmax': 771, 'ymax': 975, 'lineNumber': 16, 'rd_b': 0.04113636538386345, 'rd_r': 0.0017647058703005314, 'rd_t': -0.03386363759636879, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '/', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 774, 'ymin': 949, 'xmax': 853, 'ymax': 975, 'lineNumber': 16, 'rd_b': 0.32318180799484253, 'rd_r': 0.0035294117406010628, 'rd_t': -0.09840909391641617, 'rd_l': -0.0017647058703005314, 'nUpper': 0.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'pairs', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 859, 'ymin': 949, 'xmax': 864, 'ymax': 975, 'lineNumber': 16, 'rd_b': 0.3302272856235504, 'rd_r': 0.06058823689818382, 'rd_t': -0.02545454539358616, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 967, 'ymin': 952, 'xmax': 1014, 'ymax': 969, 'lineNumber': 16, 'rd_b': 0.06522727012634277, 'rd_r': 0.05058823525905609, 'rd_t': -0.1556818187236786, 'rd_l': -0.06058823689818382, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'MRP', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1100, 'ymin': 952, 'xmax': 1163, 'ymax': 967, 'lineNumber': 16, 'rd_b': 0.019090909510850906, 'rd_r': 0.002352941082790494, 'rd_t': -0.026136362925171852, 'rd_l': -0.05058823525905609, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'DISC', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1167, 'ymin': 952, 'xmax': 1177, 'ymax': 967, 'lineNumber': 16, 'rd_b': 0.01931818202137947, 'rd_r': 0.03529411926865578, 'rd_t': -0.09272727370262146, 'rd_l': -0.002352941082790494, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1237, 'ymin': 949, 'xmax': 1365, 'ymax': 974, 'lineNumber': 16, 'rd_b': 0.040909089148044586, 'rd_r': 0.029411764815449715, 'rd_t': -0.02545454539358616, 'rd_l': -0.03529411926865578, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'DISC_AMT', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1415, 'ymin': 951, 'xmax': 1527, 'ymax': 972, 'lineNumber': 16, 'rd_b': 0.0181818176060915, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.029411764815449715, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'NET_AMT', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 172, 'ymin': 986, 'xmax': 299, 'ymax': 1006, 'lineNumber': 17, 'rd_b': 0.018409090116620064, 'rd_r': 0.020588235929608345, 'rd_t': -0.04227272793650627, 'rd_l': 0.0, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TAX_RATE', 'numLabel': 6, 'labelName': 'vendor.phone_number'}, {'xmin': 334, 'ymin': 987, 'xmax': 381, 'ymax': 1003, 'lineNumber': 17, 'rd_b': 0.019090909510850906, 'rd_r': 0.0, 'rd_t': -0.0427272729575634, 'rd_l': -0.020588235929608345, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TAX', 'numLabel': 2, 'labelName': 'date'}, {'xmin': 175, 'ymin': 1019, 'xmax': 299, 'ymax': 1038, 'lineNumber': 18, 'rd_b': 0.011136363260447979, 'rd_r': 0.0029411765281111, 'rd_t': -0.0181818176060915, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '30144078', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 304, 'ymin': 1019, 'xmax': 316, 'ymax': 1038, 'lineNumber': 18, 'rd_b': 0.011136363260447979, 'rd_r': 0.0029411765281111, 'rd_t': -0.049772728234529495, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 321, 'ymin': 1019, 'xmax': 495, 'ymax': 1038, 'lineNumber': 18, 'rd_b': 0.003409090917557478, 'rd_r': 0.002352941082790494, 'rd_t': -0.057045456022024155, 'rd_l': -0.0029411765281111, 'nUpper': 11.0, 'nAlpha': 11.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TRIPLESPINE', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 499, 'ymin': 1019, 'xmax': 511, 'ymax': 1038, 'lineNumber': 18, 'rd_b': 0.011136363260447979, 'rd_r': 0.0035294117406010628, 'rd_t': -0.011363636702299118, 'rd_l': -0.002352941082790494, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 517, 'ymin': 1019, 'xmax': 560, 'ymax': 1038, 'lineNumber': 18, 'rd_b': 0.018409090116620064, 'rd_r': 0.002352941082790494, 'rd_t': 0.0, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 0.0, 'obj': '969', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 564, 'ymin': 1019, 'xmax': 576, 'ymax': 1038, 'lineNumber': 18, 'rd_b': 0.011136363260447979, 'rd_r': 0.0017647058703005314, 'rd_t': 0.0, 'rd_l': -0.002352941082790494, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 579, 'ymin': 1019, 'xmax': 608, 'ymax': 1038, 'lineNumber': 18, 'rd_b': 0.034090910106897354, 'rd_r': 0.0, 'rd_t': -0.10704545676708221, 'rd_l': -0.0017647058703005314, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'NS', 'numLabel': 9, 'labelName': 'vendor.address'}, {'xmin': 176, 'ymin': 1053, 'xmax': 300, 'ymax': 1073, 'lineNumber': 19, 'rd_b': 0.010454545728862286, 'rd_r': 0.0882352963089943, 'rd_t': -0.019090909510850906, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '15609539', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 450, 'ymin': 1053, 'xmax': 573, 'ymax': 1073, 'lineNumber': 19, 'rd_b': 0.0181818176060915, 'rd_r': 0.1052941158413887, 'rd_t': -0.003409090917557478, 'rd_l': -0.0882352963089943, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '61159990', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 752, 'ymin': 1053, 'xmax': 761, 'ymax': 1068, 'lineNumber': 19, 'rd_b': 0.0427272729575634, 'rd_r': 0.1052941158413887, 'rd_t': -0.01772727258503437, 'rd_l': -0.1052941158413887, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '1', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 940, 'ymin': 1053, 'xmax': 1047, 'ymax': 1071, 'lineNumber': 19, 'rd_b': 0.06545454263687134, 'rd_r': 0.028235293924808502, 'rd_t': -0.1786363571882248, 'rd_l': -0.1052941158413887, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '1499.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1095, 'ymin': 1051, 'xmax': 1170, 'ymax': 1072, 'lineNumber': 19, 'rd_b': 0.018636364489793777, 'rd_r': 0.0035294117406010628, 'rd_t': -0.019090909510850906, 'rd_l': -0.028235293924808502, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '50.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1176, 'ymin': 1052, 'xmax': 1187, 'ymax': 1071, 'lineNumber': 19, 'rd_b': 0.018863637000322342, 'rd_r': 0.0394117645919323, 'rd_t': -0.01931818202137947, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1254, 'ymin': 1051, 'xmax': 1346, 'ymax': 1071, 'lineNumber': 19, 'rd_b': 0.04204545542597771, 'rd_r': 0.05058823525905609, 'rd_t': -0.048636361956596375, 'rd_l': -0.0394117645919323, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '749.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1432, 'ymin': 1052, 'xmax': 1523, 'ymax': 1070, 'lineNumber': 19, 'rd_b': 0.018863637000322342, 'rd_r': 0.0, 'rd_t': -0.0181818176060915, 'rd_l': -0.05058823525905609, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '749.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 173, 'ymin': 1087, 'xmax': 234, 'ymax': 1106, 'lineNumber': 20, 'rd_b': 0.010909090749919415, 'rd_r': 0.0058823530562222, 'rd_t': -0.018409090116620064, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CGST', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 244, 'ymin': 1087, 'xmax': 248, 'ymax': 1106, 'lineNumber': 20, 'rd_b': 0.018636364489793777, 'rd_r': 0.004117647185921669, 'rd_t': -0.011136363260447979, 'rd_l': -0.0058823530562222, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 7, 'labelName': 'vendor.vat_number'}, {'xmin': 255, 'ymin': 1087, 'xmax': 314, 'ymax': 1106, 'lineNumber': 20, 'rd_b': 0.0029545454308390617, 'rd_r': 0.0035294117406010628, 'rd_t': -0.011136363260447979, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '2.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 320, 'ymin': 1087, 'xmax': 331, 'ymax': 1106, 'lineNumber': 20, 'rd_b': 0.0029545454308390617, 'rd_r': 0.004117647185921669, 'rd_t': 0.0, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 338, 'ymin': 1087, 'xmax': 342, 'ymax': 1106, 'lineNumber': 20, 'rd_b': 0.018636364489793777, 'rd_r': 0.016470588743686676, 'rd_t': -0.019090909510850906, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 370, 'ymin': 1086, 'xmax': 445, 'ymax': 1106, 'lineNumber': 20, 'rd_b': 0.0029545454308390617, 'rd_r': 0.03235294297337532, 'rd_t': -0.05659090727567673, 'rd_l': -0.016470588743686676, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '17.85', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 500, 'ymin': 1087, 'xmax': 560, 'ymax': 1108, 'lineNumber': 20, 'rd_b': 0.0181818176060915, 'rd_r': 0.006470588035881519, 'rd_t': -0.011136363260447979, 'rd_l': -0.03235294297337532, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 571, 'ymin': 1087, 'xmax': 574, 'ymax': 1108, 'lineNumber': 20, 'rd_b': 0.03386363759636879, 'rd_r': 0.004117647185921669, 'rd_t': -0.011136363260447979, 'rd_l': -0.006470588035881519, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 581, 'ymin': 1087, 'xmax': 640, 'ymax': 1108, 'lineNumber': 20, 'rd_b': 0.0181818176060915, 'rd_r': 0.0035294117406010628, 'rd_t': -0.16318181157112122, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '2.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 646, 'ymin': 1087, 'xmax': 657, 'ymax': 1108, 'lineNumber': 20, 'rd_b': 0.041363637894392014, 'rd_r': 0.004117647185921669, 'rd_t': -0.02545454539358616, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 664, 'ymin': 1087, 'xmax': 668, 'ymax': 1108, 'lineNumber': 20, 'rd_b': 0.0181818176060915, 'rd_r': 0.015294117853045464, 'rd_t': 0.0, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 694, 'ymin': 1086, 'xmax': 769, 'ymax': 1106, 'lineNumber': 20, 'rd_b': 0.05772727355360985, 'rd_r': 0.0, 'rd_t': -0.05659090727567673, 'rd_l': -0.015294117853045464, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '17.85', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 175, 'ymin': 1119, 'xmax': 299, 'ymax': 1139, 'lineNumber': 21, 'rd_b': 0.011136363260447979, 'rd_r': 0.0029411765281111, 'rd_t': -0.010454545728862286, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '30014002', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 304, 'ymin': 1119, 'xmax': 316, 'ymax': 1139, 'lineNumber': 21, 'rd_b': 0.011136363260447979, 'rd_r': 0.002352941082790494, 'rd_t': -0.0029545454308390617, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 320, 'ymin': 1119, 'xmax': 398, 'ymax': 1139, 'lineNumber': 21, 'rd_b': 0.011136363260447979, 'rd_r': 0.002352941082790494, 'rd_t': -0.0029545454308390617, 'rd_l': -0.002352941082790494, 'nUpper': 5.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'LILLY', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 402, 'ymin': 1119, 'xmax': 414, 'ymax': 1139, 'lineNumber': 21, 'rd_b': 0.011136363260447979, 'rd_r': 0.0029411765281111, 'rd_t': -0.0029545454308390617, 'rd_l': -0.002352941082790494, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 419, 'ymin': 1119, 'xmax': 527, 'ymax': 1139, 'lineNumber': 21, 'rd_b': 0.018863637000322342, 'rd_r': 0.0, 'rd_t': -0.018409090116620064, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 2.0, 'obj': '100-6.5', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 176, 'ymin': 1154, 'xmax': 299, 'ymax': 1173, 'lineNumber': 22, 'rd_b': 0.011136363260447979, 'rd_r': 0.0882352963089943, 'rd_t': -0.010909090749919415, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '15855511', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 449, 'ymin': 1153, 'xmax': 572, 'ymax': 1173, 'lineNumber': 22, 'rd_b': 0.011136363260447979, 'rd_r': 0.10647058486938477, 'rd_t': -0.0181818176060915, 'rd_l': -0.0882352963089943, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '64029990', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 753, 'ymin': 1156, 'xmax': 762, 'ymax': 1171, 'lineNumber': 22, 'rd_b': 0.050227273255586624, 'rd_r': 0.10470588505268097, 'rd_t': -0.04113636538386345, 'rd_l': -0.10647058486938477, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '1', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 940, 'ymin': 1154, 'xmax': 1047, 'ymax': 1173, 'lineNumber': 22, 'rd_b': 0.0925000011920929, 'rd_r': 0.028235293924808502, 'rd_t': -0.1377272754907608, 'rd_l': -0.10470588505268097, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '8999.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1095, 'ymin': 1154, 'xmax': 1170, 'ymax': 1173, 'lineNumber': 22, 'rd_b': 0.018863637000322342, 'rd_r': 0.0035294117406010628, 'rd_t': -0.018636364489793777, 'rd_l': -0.028235293924808502, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '40.10', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1176, 'ymin': 1154, 'xmax': 1186, 'ymax': 1173, 'lineNumber': 22, 'rd_b': 0.018863637000322342, 'rd_r': 0.03529411926865578, 'rd_t': -0.018863637000322342, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1246, 'ymin': 1154, 'xmax': 1354, 'ymax': 1174, 'lineNumber': 22, 'rd_b': 0.2779545485973358, 'rd_r': 0.03529411926865578, 'rd_t': -0.040909089148044586, 'rd_l': -0.03529411926865578, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '3609.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1414, 'ymin': 1153, 'xmax': 1522, 'ymax': 1174, 'lineNumber': 22, 'rd_b': 0.018636364489793777, 'rd_r': 0.0, 'rd_t': -0.018863637000322342, 'rd_l': -0.03529411926865578, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '5390.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 1188, 'xmax': 235, 'ymax': 1211, 'lineNumber': 23, 'rd_b': 0.010227272287011147, 'rd_r': 0.006470588035881519, 'rd_t': -0.011136363260447979, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 246, 'ymin': 1188, 'xmax': 249, 'ymax': 1211, 'lineNumber': 23, 'rd_b': 0.017954545095562935, 'rd_r': 0.004705882165580988, 'rd_t': -0.018636364489793777, 'rd_l': -0.006470588035881519, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 257, 'ymin': 1188, 'xmax': 315, 'ymax': 1211, 'lineNumber': 23, 'rd_b': 0.0024999999441206455, 'rd_r': 0.0035294117406010628, 'rd_t': -0.011136363260447979, 'rd_l': -0.004705882165580988, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '9.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 321, 'ymin': 1188, 'xmax': 332, 'ymax': 1211, 'lineNumber': 23, 'rd_b': 0.0024999999441206455, 'rd_r': 0.004117647185921669, 'rd_t': -0.011136363260447979, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 339, 'ymin': 1188, 'xmax': 343, 'ymax': 1211, 'lineNumber': 23, 'rd_b': 0.017954545095562935, 'rd_r': 0.015882352367043495, 'rd_t': -0.018636364489793777, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 370, 'ymin': 1188, 'xmax': 461, 'ymax': 1211, 'lineNumber': 23, 'rd_b': 0.017954545095562935, 'rd_r': 0.03235294297337532, 'rd_t': -0.011136363260447979, 'rd_l': -0.015882352367043495, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '411.10', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 516, 'ymin': 1188, 'xmax': 576, 'ymax': 1209, 'lineNumber': 23, 'rd_b': 0.0029545454308390617, 'rd_r': 0.006470588035881519, 'rd_t': -0.0181818176060915, 'rd_l': -0.03235294297337532, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 587, 'ymin': 1188, 'xmax': 590, 'ymax': 1209, 'lineNumber': 23, 'rd_b': 0.018409090116620064, 'rd_r': 0.005294117610901594, 'rd_t': -0.034090910106897354, 'rd_l': -0.006470588035881519, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 599, 'ymin': 1188, 'xmax': 656, 'ymax': 1209, 'lineNumber': 23, 'rd_b': 0.04159091040492058, 'rd_r': 0.004117647185921669, 'rd_t': -0.0181818176060915, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '9.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 663, 'ymin': 1188, 'xmax': 673, 'ymax': 1209, 'lineNumber': 23, 'rd_b': 0.018409090116620064, 'rd_r': 0.004117647185921669, 'rd_t': -0.0181818176060915, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 680, 'ymin': 1188, 'xmax': 684, 'ymax': 1209, 'lineNumber': 23, 'rd_b': 0.08454545587301254, 'rd_r': 0.016470588743686676, 'rd_t': 0.0, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 712, 'ymin': 1188, 'xmax': 803, 'ymax': 1209, 'lineNumber': 23, 'rd_b': 0.27000001072883606, 'rd_r': 0.0, 'rd_t': -0.07977272570133209, 'rd_l': -0.016470588743686676, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '411.10', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 175, 'ymin': 1222, 'xmax': 299, 'ymax': 1242, 'lineNumber': 24, 'rd_b': 0.010909090749919415, 'rd_r': 0.0029411765281111, 'rd_t': -0.011136363260447979, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '30144078', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 304, 'ymin': 1222, 'xmax': 316, 'ymax': 1242, 'lineNumber': 24, 'rd_b': 0.010909090749919415, 'rd_r': 0.002352941082790494, 'rd_t': -0.0024999999441206455, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 320, 'ymin': 1222, 'xmax': 415, 'ymax': 1242, 'lineNumber': 24, 'rd_b': 0.010909090749919415, 'rd_r': 0.0017647058703005314, 'rd_t': -0.0024999999441206455, 'rd_l': -0.002352941082790494, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'PESWEN', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 418, 'ymin': 1222, 'xmax': 430, 'ymax': 1242, 'lineNumber': 24, 'rd_b': 0.018863637000322342, 'rd_r': 0.0029411765281111, 'rd_t': -0.018863637000322342, 'rd_l': -0.0017647058703005314, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 435, 'ymin': 1222, 'xmax': 478, 'ymax': 1242, 'lineNumber': 24, 'rd_b': 0.026136362925171852, 'rd_r': 0.0029411765281111, 'rd_t': -0.011136363260447979, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 0.0, 'obj': '410', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 483, 'ymin': 1222, 'xmax': 495, 'ymax': 1242, 'lineNumber': 24, 'rd_b': 0.05409090965986252, 'rd_r': 0.0017647058703005314, 'rd_t': 0.0, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 498, 'ymin': 1222, 'xmax': 527, 'ymax': 1242, 'lineNumber': 24, 'rd_b': 0.010909090749919415, 'rd_r': 0.0, 'rd_t': -0.0029545454308390617, 'rd_l': -0.0017647058703005314, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'NS', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 175, 'ymin': 1256, 'xmax': 298, 'ymax': 1276, 'lineNumber': 25, 'rd_b': 0.018636364489793777, 'rd_r': 0.08941176533699036, 'rd_t': -0.010227272287011147, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '61294321', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 450, 'ymin': 1257, 'xmax': 573, 'ymax': 1275, 'lineNumber': 25, 'rd_b': 0.003409090917557478, 'rd_r': 0.1052941158413887, 'rd_t': -0.03386363759636879, 'rd_l': -0.08941176533699036, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '61159990', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 752, 'ymin': 1256, 'xmax': 761, 'ymax': 1273, 'lineNumber': 25, 'rd_b': 0.26249998807907104, 'rd_r': 0.1052941158413887, 'rd_t': -0.0427272729575634, 'rd_l': -0.1052941158413887, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '1', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 940, 'ymin': 1256, 'xmax': 1047, 'ymax': 1276, 'lineNumber': 25, 'rd_b': 0.07659091055393219, 'rd_r': 0.028235293924808502, 'rd_t': -0.06522727012634277, 'rd_l': -0.1052941158413887, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '1499.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1095, 'ymin': 1256, 'xmax': 1170, 'ymax': 1275, 'lineNumber': 25, 'rd_b': 0.2549999952316284, 'rd_r': 0.0035294117406010628, 'rd_t': -0.018863637000322342, 'rd_l': -0.028235293924808502, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '50.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1176, 'ymin': 1256, 'xmax': 1187, 'ymax': 1275, 'lineNumber': 25, 'rd_b': 0.2620454430580139, 'rd_r': 0.0394117645919323, 'rd_t': -0.018863637000322342, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1254, 'ymin': 1256, 'xmax': 1346, 'ymax': 1275, 'lineNumber': 25, 'rd_b': 0.2620454430580139, 'rd_r': 0.05058823525905609, 'rd_t': -0.04204545542597771, 'rd_l': -0.0394117645919323, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '749.50', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 1432, 'ymin': 1256, 'xmax': 1523, 'ymax': 1274, 'lineNumber': 25, 'rd_b': 0.01931818202137947, 'rd_r': 0.0, 'rd_t': -0.018636364489793777, 'rd_l': -0.05058823525905609, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '749.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 1290, 'xmax': 235, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.0058823530562222, 'rd_t': -0.010909090749919415, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 245, 'ymin': 1290, 'xmax': 249, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.004117647185921669, 'rd_t': -0.017954545095562935, 'rd_l': -0.0058823530562222, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 256, 'ymin': 1290, 'xmax': 315, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.0035294117406010628, 'rd_t': -0.010909090749919415, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '2.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 321, 'ymin': 1290, 'xmax': 332, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.004117647185921669, 'rd_t': -0.010909090749919415, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 10, 'labelName': 'meta_data.document_title'}, {'xmin': 339, 'ymin': 1290, 'xmax': 343, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.016470588743686676, 'rd_t': -0.017954545095562935, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 371, 'ymin': 1290, 'xmax': 446, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.03117647022008896, 'rd_t': -0.017954545095562935, 'rd_l': -0.016470588743686676, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '17.85', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 499, 'ymin': 1290, 'xmax': 559, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.00318181817419827, 'rd_r': 0.0058823530562222, 'rd_t': -0.010909090749919415, 'rd_l': -0.03117647022008896, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 569, 'ymin': 1290, 'xmax': 573, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.004117647185921669, 'rd_t': -0.003409090917557478, 'rd_l': -0.0058823530562222, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 580, 'ymin': 1290, 'xmax': 639, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.06136363744735718, 'rd_r': 0.0035294117406010628, 'rd_t': -0.018409090116620064, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '2.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 645, 'ymin': 1290, 'xmax': 656, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.004117647185921669, 'rd_t': -0.041363637894392014, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 663, 'ymin': 1290, 'xmax': 667, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.018409090116620064, 'rd_r': 0.016470588743686676, 'rd_t': -0.018409090116620064, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 695, 'ymin': 1289, 'xmax': 770, 'ymax': 1311, 'lineNumber': 26, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.07136363536119461, 'rd_l': -0.016470588743686676, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '17.85', 'numLabel': 11, 'labelName': 'customer.customer_name'}, {'xmin': 176, 'ymin': 1325, 'xmax': 494, 'ymax': 1346, 'lineNumber': 27, 'rd_b': 0.030454546213150024, 'rd_r': 0.0035294117406010628, 'rd_t': -0.018863637000322342, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 17.0, 'nSpecial': 2.0, 'obj': '30174087-471_045-000', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 500, 'ymin': 1325, 'xmax': 511, 'ymax': 1346, 'lineNumber': 27, 'rd_b': 0.010454545728862286, 'rd_r': 0.002352941082790494, 'rd_t': -0.00318181817419827, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '-', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 515, 'ymin': 1325, 'xmax': 543, 'ymax': 1346, 'lineNumber': 27, 'rd_b': 0.030454546213150024, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.002352941082790494, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'NS', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 175, 'ymin': 1358, 'xmax': 348, 'ymax': 1377, 'lineNumber': 28, 'rd_b': 0.02340909093618393, 'rd_r': 0.05882352963089943, 'rd_t': -0.018636364489793777, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 11.0, 'nSpecial': 0.0, 'obj': '71699832521', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 448, 'ymin': 1357, 'xmax': 572, 'ymax': 1377, 'lineNumber': 28, 'rd_b': 0.05363636463880539, 'rd_r': 0.10647058486938477, 'rd_t': -0.026136362925171852, 'rd_l': -0.05882352963089943, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 8.0, 'nSpecial': 0.0, 'obj': '34051000', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 753, 'ymin': 1360, 'xmax': 762, 'ymax': 1377, 'lineNumber': 28, 'rd_b': 0.0, 'rd_r': 0.10941176116466522, 'rd_t': -0.05772727355360985, 'rd_l': -0.10647058486938477, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '1', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 948, 'ymin': 1359, 'xmax': 1039, 'ymax': 1378, 'lineNumber': 28, 'rd_b': 0.053409092128276825, 'rd_r': 0.23176470398902893, 'rd_t': -0.06545454263687134, 'rd_l': -0.10941176116466522, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '950.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1433, 'ymin': 1359, 'xmax': 1523, 'ymax': 1379, 'lineNumber': 28, 'rd_b': 0.0229545459151268, 'rd_r': 0.0, 'rd_t': -0.01931818202137947, 'rd_l': -0.23176470398902893, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '950.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 1392, 'xmax': 235, 'ymax': 1415, 'lineNumber': 29, 'rd_b': 0.037727274000644684, 'rd_r': 0.0058823530562222, 'rd_t': -0.018409090116620064, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 245, 'ymin': 1392, 'xmax': 249, 'ymax': 1415, 'lineNumber': 29, 'rd_b': 0.08022727072238922, 'rd_r': 0.004705882165580988, 'rd_t': -0.018409090116620064, 'rd_l': -0.0058823530562222, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 257, 'ymin': 1392, 'xmax': 315, 'ymax': 1415, 'lineNumber': 29, 'rd_b': 0.08022727072238922, 'rd_r': 0.0035294117406010628, 'rd_t': -0.018409090116620064, 'rd_l': -0.004705882165580988, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '9.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 321, 'ymin': 1392, 'xmax': 332, 'ymax': 1415, 'lineNumber': 29, 'rd_b': 0.11522727459669113, 'rd_r': 0.004117647185921669, 'rd_t': -0.018409090116620064, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 339, 'ymin': 1392, 'xmax': 343, 'ymax': 1415, 'lineNumber': 29, 'rd_b': 0.014772727154195309, 'rd_r': 0.015882352367043495, 'rd_t': -0.018409090116620064, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 370, 'ymin': 1392, 'xmax': 446, 'ymax': 1415, 'lineNumber': 29, 'rd_b': 0.08022727072238922, 'rd_r': 0.03176470473408699, 'rd_t': -0.018409090116620064, 'rd_l': -0.015882352367043495, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '72.46', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 500, 'ymin': 1392, 'xmax': 560, 'ymax': 1413, 'lineNumber': 29, 'rd_b': 0.053409092128276825, 'rd_r': 0.006470588035881519, 'rd_t': -0.010454545728862286, 'rd_l': -0.03176470473408699, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 571, 'ymin': 1392, 'xmax': 574, 'ymax': 1413, 'lineNumber': 29, 'rd_b': 0.060681819915771484, 'rd_r': 0.005294117610901594, 'rd_t': -0.018409090116620064, 'rd_l': -0.006470588035881519, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 583, 'ymin': 1392, 'xmax': 640, 'ymax': 1413, 'lineNumber': 29, 'rd_b': 0.0688636377453804, 'rd_r': 0.0035294117406010628, 'rd_t': -0.04159091040492058, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '9.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 646, 'ymin': 1392, 'xmax': 657, 'ymax': 1413, 'lineNumber': 29, 'rd_b': 0.10886363685131073, 'rd_r': 0.004117647185921669, 'rd_t': -0.018409090116620064, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 664, 'ymin': 1392, 'xmax': 668, 'ymax': 1413, 'lineNumber': 29, 'rd_b': 0.14272727072238922, 'rd_r': 0.015882352367043495, 'rd_t': -0.018409090116620064, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 695, 'ymin': 1392, 'xmax': 771, 'ymax': 1413, 'lineNumber': 29, 'rd_b': 0.2740909159183502, 'rd_r': 0.0, 'rd_t': -0.050227273255586624, 'rd_l': -0.015882352367043495, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '72.46', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 173, 'ymin': 1480, 'xmax': 298, 'ymax': 1504, 'lineNumber': 30, 'rd_b': 0.02545454539358616, 'rd_r': 0.015882352367043495, 'rd_t': -0.030454546213150024, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Subtotal', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 325, 'ymin': 1480, 'xmax': 329, 'ymax': 1504, 'lineNumber': 30, 'rd_b': 0.10863636434078217, 'rd_r': 0.0029411765281111, 'rd_t': -0.02340909093618393, 'rd_l': -0.015882352367043495, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '(', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 334, 'ymin': 1480, 'xmax': 444, 'ymax': 1504, 'lineNumber': 30, 'rd_b': 0.09545454382896423, 'rd_r': 0.0117647061124444, 'rd_t': -0.014772727154195309, 'rd_l': -0.0029411765281111, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'without', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 464, 'ymin': 1480, 'xmax': 510, 'ymax': 1504, 'lineNumber': 30, 'rd_b': 0.0956818163394928, 'rd_r': 0.0035294117406010628, 'rd_t': -0.05409090965986252, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'tax', 'numLabel': 3, 'labelName': 'time'}, {'xmin': 516, 'ymin': 1480, 'xmax': 520, 'ymax': 1504, 'lineNumber': 30, 'rd_b': 0.20999999344348907, 'rd_r': 0.5288235545158386, 'rd_t': -0.030454546213150024, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': ')', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1419, 'ymin': 1480, 'xmax': 1525, 'ymax': 1502, 'lineNumber': 30, 'rd_b': 0.0181818176060915, 'rd_r': 0.0, 'rd_t': -0.0229545459151268, 'rd_l': -0.5288235545158386, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '6800.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 172, 'ymin': 1581, 'xmax': 218, 'ymax': 1597, 'lineNumber': 31, 'rd_b': 0.011590909212827682, 'rd_r': 0.17529411613941193, 'rd_t': -0.037727274000644684, 'rd_l': 0.0, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TAX', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 516, 'ymin': 1581, 'xmax': 627, 'ymax': 1598, 'lineNumber': 31, 'rd_b': 0.08068181574344635, 'rd_r': 0.010588235221803188, 'rd_t': -0.06136363744735718, 'rd_l': -0.17529411613941193, 'nUpper': 7.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TAXABLE', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 645, 'ymin': 1581, 'xmax': 692, 'ymax': 1598, 'lineNumber': 31, 'rd_b': 0.18863636255264282, 'rd_r': 0.14235293865203857, 'rd_t': -0.08454545587301254, 'rd_l': -0.010588235221803188, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'AMT', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 934, 'ymin': 1580, 'xmax': 996, 'ymax': 1598, 'lineNumber': 31, 'rd_b': 0.011136363260447979, 'rd_r': 0.2182352989912033, 'rd_t': -0.0925000011920929, 'rd_l': -0.14235293865203857, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'RATE', 'numLabel': 13, 'labelName': 'generated_by.sales_person'}, {'xmin': 1367, 'ymin': 1582, 'xmax': 1414, 'ymax': 1599, 'lineNumber': 31, 'rd_b': 0.18136364221572876, 'rd_r': 0.009999999776482582, 'rd_t': 0.0, 'rd_l': -0.2182352989912033, 'nUpper': 3.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'TAX', 'numLabel': 13, 'labelName': 'generated_by.sales_person'}, {'xmin': 1431, 'ymin': 1582, 'xmax': 1527, 'ymax': 1599, 'lineNumber': 31, 'rd_b': 0.00318181817419827, 'rd_r': 0.0, 'rd_t': -0.0181818176060915, 'rd_l': -0.009999999776482582, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'AMOUNT', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 1616, 'xmax': 235, 'ymax': 1633, 'lineNumber': 32, 'rd_b': 0.011590909212827682, 'rd_r': 0.18529412150382996, 'rd_t': -0.02545454539358616, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 550, 'ymin': 1613, 'xmax': 657, 'ymax': 1634, 'lineNumber': 32, 'rd_b': 0.08659090846776962, 'rd_r': 0.15941175818443298, 'rd_t': -0.05363636463880539, 'rd_l': -0.18529412150382996, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '1427.62', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 928, 'ymin': 1613, 'xmax': 987, 'ymax': 1633, 'lineNumber': 32, 'rd_b': 0.01068181823939085, 'rd_r': 0.004117647185921669, 'rd_t': -0.07659091055393219, 'rd_l': -0.15941175818443298, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '2.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 994, 'ymin': 1613, 'xmax': 1004, 'ymax': 1633, 'lineNumber': 32, 'rd_b': 0.00318181817419827, 'rd_r': 0.2611764669418335, 'rd_t': -0.053409092128276825, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1448, 'ymin': 1613, 'xmax': 1524, 'ymax': 1633, 'lineNumber': 32, 'rd_b': 0.00318181817419827, 'rd_r': 0.0, 'rd_t': -0.00318181817419827, 'rd_l': -0.2611764669418335, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '35.69', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 1648, 'xmax': 234, 'ymax': 1664, 'lineNumber': 33, 'rd_b': 0.011590909212827682, 'rd_r': 0.18647058308124542, 'rd_t': -0.011590909212827682, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 551, 'ymin': 1648, 'xmax': 658, 'ymax': 1668, 'lineNumber': 33, 'rd_b': 0.16568182408809662, 'rd_r': 0.15882353484630585, 'rd_t': -0.053409092128276825, 'rd_l': -0.18647058308124542, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '1427.62', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 928, 'ymin': 1647, 'xmax': 988, 'ymax': 1667, 'lineNumber': 33, 'rd_b': 0.010909090749919415, 'rd_r': 0.0035294117406010628, 'rd_t': -0.011136363260447979, 'rd_l': -0.15882353484630585, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '2.50', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 994, 'ymin': 1647, 'xmax': 1004, 'ymax': 1667, 'lineNumber': 33, 'rd_b': 0.0029545454308390617, 'rd_r': 0.26058822870254517, 'rd_t': -0.00318181817419827, 'rd_l': -0.0035294117406010628, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 1447, 'ymin': 1647, 'xmax': 1523, 'ymax': 1667, 'lineNumber': 33, 'rd_b': 0.00318181817419827, 'rd_r': 0.0, 'rd_t': -0.00318181817419827, 'rd_l': -0.26058822870254517, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '35.69', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 1684, 'xmax': 235, 'ymax': 1701, 'lineNumber': 34, 'rd_b': 0.03750000149011612, 'rd_r': 0.1858823597431183, 'rd_t': -0.011590909212827682, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'CGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 551, 'ymin': 1680, 'xmax': 658, 'ymax': 1701, 'lineNumber': 34, 'rd_b': 0.1581818163394928, 'rd_r': 0.15882353484630585, 'rd_t': -0.060681819915771484, 'rd_l': -0.1858823597431183, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '5372.88', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 928, 'ymin': 1680, 'xmax': 986, 'ymax': 1700, 'lineNumber': 34, 'rd_b': 0.0, 'rd_r': 0.004117647185921669, 'rd_t': -0.01068181823939085, 'rd_l': -0.15882353484630585, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '9.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 993, 'ymin': 1680, 'xmax': 1003, 'ymax': 1700, 'lineNumber': 34, 'rd_b': 0.003409090917557478, 'rd_r': 0.2523529529571533, 'rd_t': -0.0029545454308390617, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 1432, 'ymin': 1681, 'xmax': 1524, 'ymax': 1702, 'lineNumber': 34, 'rd_b': 0.0029545454308390617, 'rd_r': 0.0, 'rd_t': -0.00318181817419827, 'rd_l': -0.2523529529571533, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '483.56', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 174, 'ymin': 1715, 'xmax': 234, 'ymax': 1732, 'lineNumber': 35, 'rd_b': 0.03681818023324013, 'rd_r': 0.18647058308124542, 'rd_t': -0.011590909212827682, 'rd_l': 0.0, 'nUpper': 4.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'SGST', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 551, 'ymin': 1716, 'xmax': 658, 'ymax': 1735, 'lineNumber': 35, 'rd_b': 0.1574999988079071, 'rd_r': 0.15941175818443298, 'rd_t': -0.0688636377453804, 'rd_l': -0.18647058308124542, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '5372.88', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 929, 'ymin': 1715, 'xmax': 987, 'ymax': 1734, 'lineNumber': 35, 'rd_b': 0.0, 'rd_r': 0.004117647185921669, 'rd_t': -0.010909090749919415, 'rd_l': -0.15941175818443298, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 3.0, 'nSpecial': 1.0, 'obj': '9.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 994, 'ymin': 1715, 'xmax': 1004, 'ymax': 1734, 'lineNumber': 35, 'rd_b': 0.15068182349205017, 'rd_r': 0.251764714717865, 'rd_t': -0.003409090917557478, 'rd_l': -0.004117647185921669, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '%', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 1432, 'ymin': 1715, 'xmax': 1524, 'ymax': 1734, 'lineNumber': 35, 'rd_b': 0.007499999832361937, 'rd_r': 0.0, 'rd_t': -0.0029545454308390617, 'rd_l': -0.251764714717865, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 5.0, 'nSpecial': 1.0, 'obj': '483.56', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 172, 'ymin': 1768, 'xmax': 249, 'ymax': 1786, 'lineNumber': 36, 'rd_b': 0.03795454651117325, 'rd_r': 0.0117647061124444, 'rd_t': -0.08022727072238922, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Total', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 269, 'ymin': 1768, 'xmax': 362, 'ymax': 1786, 'lineNumber': 36, 'rd_b': 0.05159090831875801, 'rd_r': 0.012352941557765007, 'rd_t': -0.08022727072238922, 'rd_l': -0.0117647061124444, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Amount', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 383, 'ymin': 1768, 'xmax': 446, 'ymax': 1786, 'lineNumber': 36, 'rd_b': 0.03136363625526428, 'rd_r': 0.5717647075653076, 'rd_t': -0.08022727072238922, 'rd_l': -0.012352941557765007, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Paid', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 1418, 'ymin': 1767, 'xmax': 1525, 'ymax': 1787, 'lineNumber': 36, 'rd_b': 0.14568181335926056, 'rd_r': 0.0, 'rd_t': -0.007499999832361937, 'rd_l': -0.5717647075653076, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '7839.00', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 172, 'ymin': 1866, 'xmax': 266, 'ymax': 1884, 'lineNumber': 37, 'rd_b': 0.029318181797862053, 'rd_r': 0.0, 'rd_t': -0.03750000149011612, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Tender', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 171, 'ymin': 1894, 'xmax': 283, 'ymax': 1918, 'lineNumber': 38, 'rd_b': 0.027272727340459824, 'rd_r': 0.17529411613941193, 'rd_t': -0.03681818023324013, 'rd_l': 0.0, 'nUpper': 5.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'MyGyFTR', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 581, 'ymin': 1892, 'xmax': 688, 'ymax': 1914, 'lineNumber': 38, 'rd_b': 0.12454545497894287, 'rd_r': 0.0, 'rd_t': -0.10886363685131073, 'rd_l': -0.17529411613941193, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '7750.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 172, 'ymin': 1922, 'xmax': 347, 'ymax': 1943, 'lineNumber': 39, 'rd_b': 0.022045454010367393, 'rd_r': 0.012352941557765007, 'rd_t': -0.11522727459669113, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 11.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Transaction', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 368, 'ymin': 1924, 'xmax': 412, 'ymax': 1943, 'lineNumber': 39, 'rd_b': 0.00909090880304575, 'rd_r': 0.004705882165580988, 'rd_t': -0.09545454382896423, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ref', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 420, 'ymin': 1924, 'xmax': 424, 'ymax': 1943, 'lineNumber': 39, 'rd_b': 0.009318182244896889, 'rd_r': 0.014117646962404251, 'rd_t': -0.03136363625526428, 'rd_l': -0.004705882165580988, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 448, 'ymin': 1925, 'xmax': 477, 'ymax': 1944, 'lineNumber': 39, 'rd_b': 0.00909090880304575, 'rd_r': 0.005294117610901594, 'rd_t': -0.0956818163394928, 'rd_l': -0.014117646962404251, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'no', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 486, 'ymin': 1925, 'xmax': 489, 'ymax': 1944, 'lineNumber': 39, 'rd_b': 0.00909090880304575, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 172, 'ymin': 1953, 'xmax': 234, 'ymax': 1971, 'lineNumber': 40, 'rd_b': 0.08386363834142685, 'rd_r': 0.20411764085292816, 'rd_t': -0.03795454651117325, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Cash', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 581, 'ymin': 1953, 'xmax': 656, 'ymax': 1972, 'lineNumber': 40, 'rd_b': 0.11136363446712494, 'rd_r': 0.0, 'rd_t': -0.08068181574344635, 'rd_l': -0.20411764085292816, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 4.0, 'nSpecial': 1.0, 'obj': '89.00', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 172, 'ymin': 1982, 'xmax': 347, 'ymax': 2003, 'lineNumber': 41, 'rd_b': 0.07659091055393219, 'rd_r': 0.012352941557765007, 'rd_t': -0.10863636434078217, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 11.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Transaction', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 368, 'ymin': 1983, 'xmax': 412, 'ymax': 2003, 'lineNumber': 41, 'rd_b': 0.07659091055393219, 'rd_r': 0.005294117610901594, 'rd_t': -0.00909090880304575, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'ref', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 421, 'ymin': 1984, 'xmax': 424, 'ymax': 2003, 'lineNumber': 41, 'rd_b': 0.08954545110464096, 'rd_r': 0.014705882407724857, 'rd_t': -0.009318182244896889, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 449, 'ymin': 1984, 'xmax': 477, 'ymax': 2003, 'lineNumber': 41, 'rd_b': 0.09659090638160706, 'rd_r': 0.005294117610901594, 'rd_t': -0.00909090880304575, 'rd_l': -0.014705882407724857, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'no', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 486, 'ymin': 1984, 'xmax': 489, 'ymax': 2003, 'lineNumber': 41, 'rd_b': 0.08954545110464096, 'rd_r': 0.0, 'rd_t': -0.00909090880304575, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '.', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 174, 'ymin': 2013, 'xmax': 235, 'ymax': 2034, 'lineNumber': 42, 'rd_b': 0.08250000327825546, 'rd_r': 0.010588235221803188, 'rd_t': -0.029318181797862053, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Item', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 253, 'ymin': 2013, 'xmax': 397, 'ymax': 2034, 'lineNumber': 42, 'rd_b': 0.08250000327825546, 'rd_r': 0.10823529213666916, 'rd_t': -0.05159090831875801, 'rd_l': -0.010588235221803188, 'nUpper': 1.0, 'nAlpha': 9.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Purchased', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 581, 'ymin': 2015, 'xmax': 590, 'ymax': 2031, 'lineNumber': 42, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.08659090846776962, 'rd_l': -0.10823529213666916, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 1.0, 'nSpecial': 0.0, 'obj': '4', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 171, 'ymin': 2038, 'xmax': 249, 'ymax': 2066, 'lineNumber': 43, 'rd_b': 0.08977272361516953, 'rd_r': 0.012352941557765007, 'rd_t': -0.027272727340459824, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Total', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 270, 'ymin': 2040, 'xmax': 379, 'ymax': 2069, 'lineNumber': 43, 'rd_b': 0.08159090578556061, 'rd_r': 0.11882352828979492, 'rd_t': -0.022045454010367393, 'rd_l': -0.012352941557765007, 'nUpper': 1.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Savings', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 581, 'ymin': 2041, 'xmax': 688, 'ymax': 2061, 'lineNumber': 43, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.14272727072238922, 'rd_l': -0.11882352828979492, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 6.0, 'nSpecial': 1.0, 'obj': '5108.00', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 172, 'ymin': 2340, 'xmax': 249, 'ymax': 2359, 'lineNumber': 44, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.08386363834142685, 'rd_l': 0.0, 'nUpper': 1.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'Terms', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 269, 'ymin': 2340, 'xmax': 316, 'ymax': 2359, 'lineNumber': 44, 'rd_b': 0.023181818425655365, 'rd_r': 0.011176470667123795, 'rd_t': -0.07659091055393219, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'and', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 335, 'ymin': 2340, 'xmax': 493, 'ymax': 2359, 'lineNumber': 44, 'rd_b': 0.023181818425655365, 'rd_r': 0.0, 'rd_t': -0.07659091055393219, 'rd_l': -0.011176470667123795, 'nUpper': 0.0, 'nAlpha': 10.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'conditions', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 226, 'ymin': 2397, 'xmax': 234, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.012941176071763039, 'rd_t': -0.08250000327825546, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': '•', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 256, 'ymin': 2397, 'xmax': 315, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.012941176071763039, 'rd_t': -0.08250000327825546, 'rd_l': -0.012941176071763039, 'nUpper': 1.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'This', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 337, 'ymin': 2397, 'xmax': 462, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.00863636378198862, 'rd_r': 0.012941176071763039, 'rd_t': -0.08954545110464096, 'rd_l': -0.012941176071763039, 'nUpper': 0.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'document', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 484, 'ymin': 2397, 'xmax': 510, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.08954545110464096, 'rd_l': -0.012941176071763039, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'is', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 531, 'ymin': 2397, 'xmax': 560, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.011176470667123795, 'rd_t': -0.16568182408809662, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'to', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 579, 'ymin': 2397, 'xmax': 609, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.1581818163394928, 'rd_l': -0.011176470667123795, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'be', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 629, 'ymin': 2397, 'xmax': 740, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.27000001072883606, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'treated', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 760, 'ymin': 2397, 'xmax': 787, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.32318180799484253, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'as', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 808, 'ymin': 2397, 'xmax': 853, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0011363636003807187, 'rd_r': 0.012352941557765007, 'rd_t': 0.0, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'tax', 'numLabel': 4, 'labelName': 'total'}, {'xmin': 874, 'ymin': 2397, 'xmax': 982, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.4840908944606781, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'invoice', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1002, 'ymin': 2397, 'xmax': 1031, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0011363636003807187, 'rd_r': 0.0117647061124444, 'rd_t': -0.15068182349205017, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'to', 'numLabel': 1, 'labelName': 'invoice_number'}, {'xmin': 1051, 'ymin': 2397, 'xmax': 1080, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': 0.0, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'be', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1100, 'ymin': 2397, 'xmax': 1193, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.2549999952316284, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'extent', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1214, 'ymin': 2397, 'xmax': 1243, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': 0.0, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'of', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1264, 'ymin': 2397, 'xmax': 1357, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.2779545485973358, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'supply', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1377, 'ymin': 2397, 'xmax': 1405, 'ymax': 2423, 'lineNumber': 45, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.18136364221572876, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'of', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 255, 'ymin': 2428, 'xmax': 365, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.08159090578556061, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 7.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'taxable', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 386, 'ymin': 2428, 'xmax': 462, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.09659090638160706, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'goods', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 483, 'ymin': 2428, 'xmax': 529, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.010588235221803188, 'rd_t': -0.20999999344348907, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'and', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 547, 'ymin': 2428, 'xmax': 608, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.1574999988079071, 'rd_l': -0.010588235221803188, 'nUpper': 0.0, 'nAlpha': 4.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'bill', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 629, 'ymin': 2428, 'xmax': 658, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.18863636255264282, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'of', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 679, 'ymin': 2428, 'xmax': 772, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.011176470667123795, 'rd_t': -0.26249998807907104, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'supply', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 791, 'ymin': 2428, 'xmax': 820, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.0011363636003807187, 'rd_l': -0.011176470667123795, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'to', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 840, 'ymin': 2428, 'xmax': 885, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.3302272856235504, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 3.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'the', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 906, 'ymin': 2428, 'xmax': 998, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.012941176071763039, 'rd_t': -0.4272727370262146, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'extent', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 1020, 'ymin': 2428, 'xmax': 1048, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.0011363636003807187, 'rd_l': -0.012941176071763039, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'of', 'numLabel': 15, 'labelName': 'payment.method'}, {'xmin': 1069, 'ymin': 2428, 'xmax': 1162, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.42818182706832886, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'supply', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1182, 'ymin': 2428, 'xmax': 1210, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.012352941557765007, 'rd_t': -0.2620454430580139, 'rd_l': -0.0117647061124444, 'nUpper': 0.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'of', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1231, 'ymin': 2428, 'xmax': 1358, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.011176470667123795, 'rd_t': -0.2620454430580139, 'rd_l': -0.012352941557765007, 'nUpper': 0.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'exempted', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1377, 'ymin': 2428, 'xmax': 1453, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.0058823530562222, 'rd_t': -0.14568181335926056, 'rd_l': -0.011176470667123795, 'nUpper': 0.0, 'nAlpha': 5.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'goods', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 1463, 'ymin': 2428, 'xmax': 1466, 'ymax': 2457, 'lineNumber': 46, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': 0.0, 'rd_l': -0.0058823530562222, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 226, 'ymin': 2461, 'xmax': 234, 'ymax': 2477, 'lineNumber': 47, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.08977272361516953, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': '•', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 254, 'ymin': 2461, 'xmax': 284, 'ymax': 2477, 'lineNumber': 47, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.023181818425655365, 'rd_l': -0.0117647061124444, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'NO', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 304, 'ymin': 2461, 'xmax': 430, 'ymax': 2477, 'lineNumber': 47, 'rd_b': 0.0, 'rd_r': 0.011176470667123795, 'rd_t': -0.023181818425655365, 'rd_l': -0.0117647061124444, 'nUpper': 8.0, 'nAlpha': 8.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'EXCHANGE', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 449, 'ymin': 2461, 'xmax': 479, 'ymax': 2477, 'lineNumber': 47, 'rd_b': 0.0, 'rd_r': 0.0117647061124444, 'rd_t': -0.00863636378198862, 'rd_l': -0.011176470667123795, 'nUpper': 2.0, 'nAlpha': 2.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'NO', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 499, 'ymin': 2462, 'xmax': 592, 'ymax': 2478, 'lineNumber': 47, 'rd_b': 0.0, 'rd_r': 0.005294117610901594, 'rd_t': -0.12454545497894287, 'rd_l': -0.0117647061124444, 'nUpper': 6.0, 'nAlpha': 6.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 0.0, 'obj': 'REFUND', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 601, 'ymin': 2462, 'xmax': 605, 'ymax': 2478, 'lineNumber': 47, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.11136363446712494, 'rd_l': -0.005294117610901594, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 0.0, 'nSpecial': 1.0, 'obj': '.', 'numLabel': 0, 'labelName': 'undefined'}, {'xmin': 771, 'ymin': 2619, 'xmax': 927, 'ymax': 2638, 'lineNumber': 48, 'rd_b': 0.0, 'rd_r': 0.0, 'rd_t': -0.2740909159183502, 'rd_l': 0.0, 'nUpper': 0.0, 'nAlpha': 0.0, 'nSpaces': 0.0, 'nNumeric': 10.0, 'nSpecial': 0.0, 'obj': '5580004778', 'numLabel': 1, 'labelName': 'invoice_number'}]

# def word2vec(word):
# 	# count the characters in word
# 	cw = Counter(word)
# 	# precomputes a set of the different characters
# 	sw = set(cw)
# 	# precomputes the "length" of the word vector
# 	lw = sqrt(sum(c*c for c in cw.values()))

# 	# return a tuple
# 	return cw, sw, lw

# def cosdis(v1, v2):
# 	# which characters are common to the two words?
# 	common = v1[1].intersection(v2[1])
# 	# by definition of cosine distance we have
# 	return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]


# def find_similarity_from_words(words, corpusWords):
# 	try:
# 		probability = {}
# 		for word in words:
# 			maxScore = 0.0
# 			for corpusWord in corpusWords:
# 				word2vecW = word2vec(word.lower())
# 				word2vecCW = word2vec(corpusWord.lower())
# 				score = cosdis(word2vecW, word2vecCW)*100
# 				if maxScore < score:
# 					maxScore = score
# 			probability[word] = maxScore

# 		scores = [{k:v} for k,v in probability.items()]
# 		return scores
# 	except Exception as e:
# 		raise e

# # stores
# # words = ["OCHRE", "AND", "BLACK", "involce", "No", "Memo", "No.", "Date"]
# # corpusWords=['adidas', 'ALDO', 'ARROW', 'and']
# # print("scores : ", find_similarity_from_words(words, corpusWords))



# def find_similarity_from_corpus(words, corpusWords):
# 	try:
# 		probability = {}
# 		for corpusWord in corpusWords:
# 			maxScore = 0.0
# 			for word in words:
# 				word2vecW = word2vec(word.lower())
# 				word2vecCW = word2vec(corpusWord.lower())
# 				score = cosdis(word2vecW, word2vecCW)*100
# 				if maxScore < score:
# 					maxScore = score
# 			probability[corpusWord] = maxScore

# 		scores = [{k:v} for k,v in probability.items()]
# 		return scores
# 	except Exception as e:
# 		raise e

# # address
# words = ["23", "Ground", "Floor", ",", "Forum", "Mall", ",", "Hosur", "Road", ",", "Koramangala", "GSTIN"]
# corpusWords = [
# "Forum Koramangala",
# "High Street Phoenix",
# "Phoenix Marketcity Bangalore",
# "Phoenix Marketcity Kurla",
# "Phoenix Marketcity Pune",
# "Phoenix Marketcity and Palladium Tamil Nadu Chennai",
# "Phoenix Palassio Lucknow",
# "Phoenix Palladium Mumbai",
# "Treasure Island Mall",
# "Treasure Island Next Mall"
# ]
# words = [" ".join(words)]
# print("scores : ", find_similarity_from_corpus(words, corpusWords))


# def test():
# 	df = pd.DataFrame(arr)

# 	mainDict = data_enrichment_util.visualize_test_data_labels(df, labelsDict)
# 	print("json : ", json.dumps(mainDict, indent=4))

# 	for key,value in mainDict.items():
# 		# print("key, value : ", key, value)
# 		if key == "vendor":
# 			for vKey, vValue in value.items():
# 				if vKey == "name":
# 					print("vValue : ", vValue)
# 					for index, objs, pos, lineNumber in zip(vValue['index'], vValue['objs'], vValue['pos'], vValue['lineNumber']):
# 						print(">>> : ", index, objs, pos, lineNumber)


# # test()



###########
# d = {11.0: 1, 0.0: 5, 4039.0: 1, 2.36: 2, 9971.0: 2, 9.0: 3, -1.0: 1, 440.0: 4, 550.0: 1, 110.0: 1, 9148078240.0: 1}

# newd = {k:v for k,v in d.items() if not(k == 0 or k == 0.0 or k < 0 or k < 0.0)}
# print("newd : ", newd)
# # for k,v in d.items():
# # 	if not (k == 0 or k == 0.0 or k < 0 or k < 0.0):
# # 		newd.update({k:v})
# maxTotalValueFreqKey = max(newd, key=newd.get)
# print(newd[maxTotalValueFreqKey])

# for k,v in newd.items():
# 	if v == newd[maxTotalValueFreqKey]:
# 		print("k : ", k)


# # minValue = 0.0
# # print("maxTotalValueFreqKey : ", d[maxTotalValueFreqKey])
# # if maxTotalValueFreq <= minValue:


# # df = pd.DataFrame(d.items(), columns=['values','frequency'])
# # print(df)





# # def find():
# # 	maxTotalValue = 0.0
# # 	mostRepeated = d[maxTotalValueFreqKey]

# # 	for k,v in d.items():
# # 		if v == mostRepeated:
# # 			if k > 0.0:
# # 				mostRepeated = mostRepeated - 1
# # 			else:
# # 				print("k : ", k)
# # 				maxTotalValue = k

# # 	print("maxTotalValue : ", maxTotalValue)
# # 	# if maxTotalValueFreqKey <= 0.0:
# # 	# 	maxTotalValueFreqKey = maxTotalValueFreqKey - 1
# # 	# 	print("maxTotalValueFreqKey : ", maxTotalValueFreqKey)
# # 	# for k,v in d.items():

# # find()



#########
# mainDict = {'vendor': {'name': {'index': [0, 1, 2, 8, 9, 12, 13, 32, 46, 51, 52, 53, 69, 70, 81, 82, 94, 302, 303, 304, 305, 306, 307], 'objs': ['TAX', 'INVOICE', '/', '(', 'FU', 'LTD', ')', ':', 'DESC', 'AMT', 'JOM', 'COSTX', 'WHITE', '1', 'NAVY', '1', '1', 'will', 'shortly', 'policy', 'SMS', '.', '"'], 'pos': [[238, 233, 288, 279], [311, 233, 431, 279], [439, 233, 450, 279], [401, 284, 413, 325], [413, 284, 444, 325], [662, 284, 711, 325], [716, 284, 725, 325], [397, 532, 407, 571], [97, 734, 165, 771], [788, 732, 837, 769], [167, 777, 218, 828], [432, 783, 518, 824], [236, 1035, 326, 1076], [471, 1040, 476, 1071], [252, 1134, 325, 1173], [472, 1138, 477, 1169], [471, 1237, 476, 1270], [426, 4350, 553, 4395], [602, 4351, 843, 4397], [390, 4395, 597, 4447], [642, 4397, 735, 4448], [756, 4398, 770, 4447], [786, 4399, 800, 4448]], 'lineNumber': [1, 1, 1, 2, 2, 2, 2, 7, 10, 10, 11, 11, 15, 15, 17, 17, 19, 68, 68, 69, 69, 69, 69], 'scores': [{'lifestyle': 56.61385170722979}, {'pantaloons': 50.0}, {'big bazaar': 35.35533905932738}, {'croma': 40.0}, {'hamleys': 57.14285714285714}, {'burger king': 34.42651863295481}, {'h & m': 16.90308509457033}, {'reliance trends': 60.0}, {'starmark': 43.64357804719848}, {'max': 28.86751345948129}]}, 'address': {'index': [17, 18, 19, 20, 21, 22, 23], 'objs': [',', 'NO.142', 'VELACHERY', ',', 'VELACHERY', 'MAIN', 'ROAD'], 'pos': [[570, 336, 581, 377], [594, 336, 693, 377], [201, 384, 359, 425], [361, 385, 370, 424], [395, 383, 552, 424], [573, 383, 636, 423], [661, 383, 728, 422]], 'lineNumber': [3, 3, 4, 4, 4, 4, 4], 'scores': [{'Phoenix Marketcity and Palladium Chennai': 46.423834544262974}, {'Phoenix Marketcity Bangalore': 41.60251471689219}, {'Phoenix Palladium Mumbai': 42.42640687119285}]}, 'phone_number': {'index': [30], 'objs': ['3088420084'], 'pos': [[453, 484, 627, 523]], 'lineNumber': [6]}, 'gst_number': {'index': [39], 'objs': ['33AADCB1093NIZN'], 'pos': [[238, 580, 499, 621]], 'lineNumber': [8]}, 'email': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}}, 'total': {'index': [184, 191], 'objs': ['6850.60', '6850.60'], 'pos': [[753, 2236, 873, 2274], [752, 2385, 873, 2422]], 'lineNumber': [39, 42]}, 'invoice_number': {'index': [230, 231], 'objs': ['2541029000003822', 'Auth'], 'pos': [[520, 3299, 800, 3342], [765, 3451, 835, 3493]], 'lineNumber': [52, 53]}, 'date': {'index': [], 'objs': [], 'pos': [], 'lineNumber': [], 'dateValue': []}, 'time': {'index': [249], 'objs': ['20:50'], 'pos': [[573, 3651, 656, 3696]], 'lineNumber': [56], 'timeValue': ['20:50:00']}}
# indexLabels = {}

# for key,value in mainDict.items():
# 	if key == 'invoice_number' or key == 'total' or key == 'date' or key == 'time':
# 		if len(mainDict[key]['index']) > 0:
# 			for i, index in enumerate(mainDict[key]['index']):
# 				indexLabels.update({index:key})
# 	if key == 'vendor':
# 		for vKey,vValue in mainDict[key].items():
# 			if vKey == 'name' or vKey == 'address' or vKey == 'phone_number' or vKey == 'gst_number' or vKey == 'email' or vKey == 'website':
# 				if len(mainDict[key][vKey]['index']) > 0:
# 					for i, index in enumerate(mainDict[key][vKey]['index']):
# 						indexLabels.update({index:str(key+'.'+vKey)})


# print("indexLabels : ", indexLabels)
#########

# mallsAddress = common_util.read_configuration()["mallsCollection"]

# df = pd.DataFrame(mallsAddress)
# data = "TAX INVOICE/BILL OF SUPPLY\nBIG BAZAAR (FUTUBE RETAIL LTD)\nPHOENIX MARKET CITY, NO 142\nVELACHERY, VELACHERY MAIN ROAD\nCHENNAI - 600042\nTel No: 808842008\nHELFLINE: 1300 286 2255\nGST TIN:33AACC81083NIZN N.E,F 01.07.2017\nCIN NC: \u201e51909MH2007P.C218269\nITEM DESC\nHSN\nQTY DISC INT NET AMT\nCGSTX SAS\"\n%\n-\n1\n0\n---1\nL.CO,FLDNM,32,TINT\n6204 Pcs\nPersnl Acc Insurance\n9971 Pcs\nSPECIAL BENEFIT\n9971 Pos\nSUBTOTAL\nRs.\n500 00- 1299.00\n6\na 00 2.36\n9\n2.36-\na\n1299.00\n--- 1\n9\n\u0700\nTOTAL\nICICI\n1299.00\n1299.00\nYour Mobile Number\n6000000000\nHas Been Registered\nwith Big Bazaar\nPIECES PURCHASED: 1 DISC ITENS: 1\nTOTAL SAVING: 500.00\nTOTAL COUPON SAVINGS: 500.0)\n4810749980\n: 300.0)\nGST\nCGST\nSGST\nBASE AMT\n1159.82\n1153.82\nTAK 1,29T\n69.59\n69.50\nTax Invoice Numbes - 2541028000030929\nAuth Sign\nCH:99959233 Hrarind Ranalingan\nTILL NO.26 NEMO NO.1030929 7:52588\nSt.2541 16/03,21 16:26\nNet Amount is inclusive of all taxes\nTotal Savirgs add to ciscount over MRP\nand additiona pronations.\nSR N Ibu\nNow also shop online\n@shop.bigbazaar.com\nGet Free Home Delivery\non orders over Rs.500\n\"Insurance policy\noffer is exclusive for\nFuture Pay Members Only;\nT&C Apply. Eligible\nCustomers will shortly\nreceive policy SMS.\n"
# # data = ".\nTAX INVOICE/BILL OF SUPPLY\nBIG BAZAAR (FUTURE RETAIL LTD\nPHOENIX MARKET CITY,NO. 142\nVELACHERY, VELACHERY MAIN ROAD\nCHENNAI - 600042\nTel No: 8088420084\nHELPLINE: 1800 266 2255\nGSI TIN:33AADCB 109GNIZM W.E.F 01.07.2017\nCIN NO:L51909MH2007PLC268269\nNET AMT\nITEM DESC\nHSN UOM\nQTY DISC AMT\nCGSTX SGST\n4pc kitchen tools\n8215 Pcs\nScotch Brite, Scruber\n9603 Pcs\nFNFDS MAYO VEG 250g\n2103 Pcs\nAMUL CAFE BT 200ml\n2202\nPcs\ntis\nSTR CNTREIBLE\n3924\nCONTAINERSET GOOMLX3\n3924 Pcs\nPersnl Acc Insurance\n9971 Pcs\nSPECIAL BENEFIT\n9971 Pcs\nSUBTOTAL\nRs.\n1\nton\n99.00\n6\n6\n0.00 35.00\n9\n0.00\n69.00\n6 6.\n1 0.00 25.00\n66\n150.00- 149,00\n9\n9.\n1 90.00- 109.00\n9 29\n0.00 2.36\n9 9\n- 1 0.00 2.36-\ng\n9\n486.00\nTOTAL\nHDFC\n486.00\n486.00\nYour Mobile Number\n8608950762\nHas Been Registered\nwith Big Bazaar\nPIECES PURCHASED: 6. DISC ITEMS: 3\nTOTAL SAVING: 381.00\nGST.\nCGST\nSGST\nBASE AMT\n420.64\n420.64\nTAX ANT\n32.69\n32:69\nTax Invoice Number - 2541028000000788\nAuth Sign\nCH:528197 Priyanga Durairaj\nTILL NO.28 MEMO NO.0006188 Tr:47043\nSt:2541 03/07/21 15:44\n.Net Amount is inclusive of all taxes\nTotal Savings add to discount over MRP\nand additional Promotions.\nNow also shop online\n@ shop.bigbazaar.com\nGet Free Home Delivery\non orders over Rs.999\n\"Insurance policy\noffer is exclusive for\nFuture Pay Members Only;\nT&C Apply. Eligible\nCustomers will shortly\nreceive policy SMS.\"\n"
# # data = "TAX INVOICE/BILL OF SUPPLY\nBIG BAZAAR (FUTURE RETAIL LTD)\nLG-29, BIGBAZAAR PHOENIX MARKET CITY\nOPP TO BBMP OFFICE MAHADEVAPURA-BLR 48\nTel No. - 08088420130/1800 266 2255\nFor Koryo : 18005725555/08033166512\nGSI TIN:29AADCB1093N1ZC W.E.F 01.07.2017\nCIN NO:151909MH2007PLC268269\nITEM DESC\nHSN UOM\nQTY DISC AMT NET AMT\nCGSTX SGST\n323\nSS IB Tope 14 cm\n1323 Pcs\nNILG BANANA SLTD 339\n2106 Pcs\nS Kadai 20 cm\nPcs\nMADHUR SUGAR 1kg\n1701 Pcs\nPersnl Acc Insurance\n0971 Pcs\nSPECIAL BENEFIT\n5971 Pcs\nSUBTOTAL\n1\n6\n1\n6\n1\n6\n1\n0\n-1\n9\n- 1\n9\nRs.\n226.00-\n299.00\n6\n0.00 20.00\n6\n325.00- 450.00\n6\n47.00-\n0\n0.00 2.36\n9\n0.00\n2.36-\n9\n769.00\nTOTAL\nSBI\n769.00\n769.00\nYour Mobile Number\n9742931421\nHas Been Registered\nwith Big Bazaar\nPIECES PURCHASED: 4 DISC ITEMS: 3\nTOTAL SAVING: 611.00\nGST\nCGST\nSGST\nBASE AMT - TAX AMT\n686.60 41.20\n686.60 41.20\nTax Invoice Number - 4993034000010928\nAuth Sign\nCH:99953222 Mallikarjun.D.Y\nTILL NO.34 MEMO NO.0010938 Tr:53235\nSt:4993 24/07/21 20:09\nNet Amount is inclusive of all taxes\nTotal Savings add to discount over MRP\nand additional Promotions.\nNow also shop online\n@shop.bigbazaar.com\nGet Free Home Delivery\non orders over Rs.500\n\"Insurance policy\noffer is exclusive for\nPuture Pay Members Only:\nT&C Apply. Eligible\nCustomers will shortly\nCeciveli SMA\n"
# print()
# print("df : ")
# print(df)

# data = data.replace("\n", " ")
# print("data : ", data)

# # vendor_alias = df['vendor.alias']
# # vendor_alias = list(set(vendor_alias.tolist()))
# # print("vendor_alias : ", vendor_alias)
# # print()

# # scores = data_enrichment_util.find_similarity_from_corpus(words=data, corpusWords=vendor_alias)
# # print("scores : ", scores)


# # vendor_address = df['vendor.address']
# # vendor_address = list(set(vendor_address.tolist()))
# # print("vendor_address : ", vendor_address)
# # print()

# # scores = data_enrichment_util.find_similarity_from_corpus(words=data, corpusWords=vendor_address)
# # print("scores : ", scores)

# vendor_malls = []
# for index, row in df.iterrows():
# 	mall = row['vendor.malls']
# 	address = row['vendor.address']
# 	if address in data.lower():
# 		if mall not in vendor_malls:
# 			vendor_malls.append(mall)

# print(vendor_malls)


# # for index, address in enumerate(vendor_address):
# # 	if address in data.lower():
# # 		print("yess : ", index, address)
# # 		vendor_malls.vendor_malls
# # 	else:
# # 		print("no : ", index, address)



#########
# rawDataDir = "/home/ritesh/OCR/icr-microservice/data/001_media/"
# filePaths = common_util.get_files_from_directory_subdirectory(rawDataDir, fileExtAllow=common_util.read_configuration()['typeOfMediaAllow'])
# print("filePaths : ", len(filePaths))

# # response = {'vendor': {'name': {'index': [0, 1, 5, 6, 7, 10, 11, 12, 19, 25, 28, 37, 38, 49, 50, 57, 58, 63, 65, 123, 136], 'objs': ['TAX', 'INVOICE', 'SUPPLY', 'BIG', 'BAZAAR', 'RETAIL', 'LTD', 'PHOENIX', 'VELACHERY', 'CHENNAI', 'Tel', 'GST', 'TIN', 'ITEM', 'DESC', 'HSV', 'JOM', 'KNI', 'TRS', 'UTL', 'TOTAL'], 'pos': [[288, 214, 339, 257], [362, 214, 479, 257], [644, 214, 748, 257], [252, 262, 303, 299], [322, 262, 427, 299], [587, 263, 688, 300], [716, 263, 760, 300], [286, 309, 409, 348], [250, 358, 407, 399], [374, 410, 495, 453], [357, 460, 404, 499], [144, 562, 193, 599], [219, 562, 264, 599], [44, 710, 121, 749], [142, 709, 208, 748], [41, 761, 104, 802], [215, 763, 264, 802], [52, 915, 110, 958], [128, 915, 174, 958], [101, 1423, 150, 1458], [119, 1624, 202, 1663]], 'lineNumber': [1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 6, 8, 8, 10, 10, 11, 11, 13, 13, 23, 26], 'scores': {'big bazaar': 88.45379626717033, 'lifestyle': 80.06407690254358, 'reliance trends': 73.48469228349535, 'hamleys': 68.37634587578276, 'starmark': 66.66666666666667}}, 'address': {'index': [22, 24, 25, 27, 31, 32, 34], 'objs': ['VELACHE', 'ROAD', 'CHENNAI', '600042', '10884200184', 'HELPLINE', '1800'], 'pos': [[447, 358, 572, 399], [712, 358, 781, 399], [374, 410, 495, 453], [552, 410, 655, 453], [499, 460, 671, 501], [303, 510, 439, 551], [483, 510, 548, 549]], 'lineNumber': [4, 4, 5, 5, 6, 7, 7]}, 'phone_number': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}, 'gst_number': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}, 'email': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}}, 'total': {'index': [135, 137, 139], 'objs': ['2416.00', '2416.00', '2416.00'], 'pos': [[791, 1519, 913, 1561], [792, 1624, 915, 1663], [791, 1674, 914, 1713]], 'lineNumber': [25, 26, 27]}, 'invoice_number': {'index': [71, 87, 102, 109, 116, 126, 128, 143, 144, 146, 160, 161, 163, 164, 179, 185, 209], 'objs': ['0.00', '0.00', '0.00', '0.00', '0.00', '20X20', '0.00', '9791017207', 'Registered', 'Been', '2299.82', '58.09', '2299.82', '58.09', 'NO.0003259', '2541', 'online'], 'pos': [[634, 915, 704, 954], [635, 1017, 704, 1050], [635, 1116, 704, 1151], [635, 1218, 704, 1259], [633, 1319, 702, 1354], [297, 1422, 382, 1457], [632, 1420, 701, 1458], [295, 1876, 642, 1923], [505, 1923, 855, 1978], [329, 1929, 465, 1980], [328, 2240, 449, 2279], [560, 2236, 645, 2275], [328, 2292, 449, 2331], [558, 2291, 643, 2331], [464, 2876, 637, 2918], [270, 2928, 332, 2967], [631, 3189, 841, 3241]], 'lineNumber': [13, 15, 17, 19, 21, 23, 23, 29, 29, 30, 34, 34, 35, 35, 39, 40, 44]}, 'date': {'index': [], 'objs': [], 'pos': [], 'lineNumber': [], 'dateValue': []}, 'time': {'index': [187], 'objs': ['17:47'], 'pos': [[606, 2930, 688, 2975]], 'lineNumber': [40], 'timeValue': ['17:47:00']}, 'ocrTexts': '3\nTAX INVOICE/BILL OF SUPPLY\nBIG BAZAAR (FUPURE RETAIL LTD\nPHOENIX MARKET CITY, NO. 142\nVELACHERY, VELACHE Y MAIN ROAD\nCHENNAI - 600042\nTel No: 10884200184\nHELPLINE: 1800 266 2255\nGST TIN:33AADCB 1093NIZN W.E.F 01.07.2017\nCIN NO:L51909/2007PLC268269\nITEM DESC\nHSV JOM\nQ"Y DISC AMT NET AMT\nCOSTS SGST\nRs.\n799.00\n999.00\n1\n2.5\n1\n2,5\n1\n2.5\n599.00\nKNI,TRS, 33, LTGRY\n6203 cs\nKNI,SHRT, 40-SF,BLACK\n5205 cs\nXNI,SHRT, 40-SF,BLACK\n6205\nPersni Aco insurance\n9971 Pcs\nSPECIAL BENEFIT\n2971 cs\nHM UTL PLN CL 20X20\n4202 cs\nSUBTOTAL\n0.00\n2.5\n0.00\n2.5\n0.00\n2.5\n0.00\n9\n0.00\n9\n0.00\n6\n2.36\n9\n2.36-\n9\n1\n6\n19.00\n2416.00\nU\nTOTAL\nICICI\n2416.00\n2416.00\nYour Mobile Number\n9791017207\nHas Been Registered\nwith Big Bazaar\nPIECES PURCHASED: 4\nS BASE AMT\nCGST 2299.82\nSGST 2299.82\n- TAX AMT\n58.09\n58.09\nTax Invoice Number - 2541029000003259\nAuth Sign\nCH:371501 Kumari K\nTILL NO.29 MEMO NO.0003259 Tr:7465\nSt:2541 16/09/21 17:47\nNet Amount is inclusive of all taxes\nTotal Savings add to discount over MRP\nand additional Promoticns.\nwi...d\nNow also shop online\n@ shop.bigbazaar.com\nGet Free Home Delivery\non orders over Rs.500\n"Insurance policy\noffer is exclusive for\nFuture Pay Members Only;\nT&C Apply. Eligible\nCustomers will shortly\nreceive policy SMS.\n', 'mall': 'Phoenix Marketcity and Palladium Chennai'}


# testedData = []

# for index,filePath in enumerate(filePaths):
# 	if index == 15 or index == 17:
# 		print()
# 		print("#"*100)
# 		sTs = time.time()

# 		directoryName,fileName,_,extension = common_util.get_file_info(filePath)
# 		print("", index, common_util.get_file_info(filePath))

# 		hostUrl = 'http://127.0.0.1:5000'
# 		method = 'POST'
# 		api = '/api/v1/icr/scan/'

# 		fileFp = open(filePath,'rb')

# 		if extension == '.pdf' or extension == '.PDF':
# 			fileType = 'application/'+extension
# 		elif extension in ['.jpeg', '.jpg', '.png']:
# 			fileType = 'image/'+extension

# 		files = [
# 			('image', (fileName, fileFp, fileType))
# 		]

# 		url = hostUrl+api
# 		try:
# 			response = requests.request("POST", url, files=files)
# 			response = response.json()
# 			status_code = response['status']
# 			print("{} | {} ".format(status_code, response))
# 		except requests.exceptions.ConnectionError as errh:
# 			print("http_error : ", errh)
# 		except requests.exceptions.ConnectionError as errc:
# 			print("connection_error : ", errc)
# 		except Exception as e:
# 			print("error : ", e)
# 			exc_type, exc_obj, exc_tb = sys.exc_info()
# 			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
# 			print(exc_type, fname, exc_tb.tb_lineno)

# 		fileFp.close()

# 		if status_code == 200:
# 			response = response['data']
# 			responseData = {}
# 			responseData['file'] = fileName
# 			responseData['vendorname'] = directoryName
			
# 			for key,value in response.items():	
# 				if key == 'total':
# 					responseData[key] = ''
# 					if len(response[key]['objs']) > 0:
# 						responseData[key] = response[key]['objs']

# 				if key == 'date':
# 					responseData[key] = ''
# 					if len(response[key]['dateValue']) > 0:
# 						responseData[key] = response[key]['dateValue']

# 				if key == 'time':
# 					responseData[key] = ''
# 					if len(response[key]['timeValue']) > 0:
# 						responseData[key] = response[key]['timeValue']

# 				if key == 'invoice_number':
# 					responseData[key] = ''
# 					if len(response[key]['objs']) > 0:
# 						responseData[key] = response[key]['objs']

# 				if key == 'vendor':
# 					for vKey,vValue in response[key].items():
# 						if vKey == 'name':
# 							responseData[key+'.'+vKey] = ''
# 							responseData[key+'.'+vKey+'.'+'scores'] = ''
# 							if len(response[key][vKey]['objs']) > 0:	
# 								responseData[key+'.'+vKey] = response[key][vKey]['objs']
# 								responseData[key+'.'+vKey+'.'+'scores'] = response[key][vKey]['scores']
						
# 						if vKey == 'address' or vKey == 'phone_number' or vKey == 'gst_number' or vKey == 'email':
# 							responseData[key+'.'+vKey] = ''
# 							if len(response[key][vKey]['objs']) > 0:	
# 								responseData[key+'.'+vKey] = response[key][vKey]['objs']

# 				if key == 'mall':
# 					responseData[key] = response[key]
				
# 				if key == 'ocrTexts':
# 					responseData[key] = response[key]
# 			eTs = time.time()
# 			responseData['timeTaken'] = eTs-sTs
# 			# print("responseData : ", responseData)
			
# 			testedData.append(responseData)



# print("testedData : ", testedData)

# df = pd.DataFrame(testedData)
# df.to_csv('tested_data.csv')



#########
# mainDict = {
#         "vendor": {
#             "name": {
#                 "index": [
#                     0,
#                     1,
#                     2,
#                     3,
#                     4,
#                     5,
#                     8,
#                     12,
#                     283,
#                     286,
#                     287,
#                     295
#                 ],
#                 "objs": [
#                     "Tax",
#                     "Invoice",
#                     "ADITYA",
#                     "BIRLA",
#                     "FASHION",
#                     "AND",
#                     "Pantaloons",
#                     "Velachery",
#                     "signatory",
#                     "For",
#                     "any",
#                     "new"
#                 ],
#                 "pos": [
#                     [
#                         767,
#                         140,
#                         810,
#                         158
#                     ],
#                     [
#                         828,
#                         139,
#                         929,
#                         158
#                     ],
#                     [
#                         506,
#                         169,
#                         613,
#                         187
#                     ],
#                     [
#                         630,
#                         169,
#                         718,
#                         187
#                     ],
#                     [
#                         736,
#                         169,
#                         858,
#                         187
#                     ],
#                     [
#                         875,
#                         169,
#                         927,
#                         187
#                     ],
#                     [
#                         788,
#                         197,
#                         910,
#                         215
#                     ],
#                     [
#                         496,
#                         264,
#                         640,
#                         292
#                     ],
#                     [
#                         352,
#                         2004,
#                         494,
#                         2032
#                     ],
#                     [
#                         286,
#                         2033,
#                         331,
#                         2062
#                     ],
#                     [
#                         351,
#                         2033,
#                         396,
#                         2062
#                     ],
#                     [
#                         1001,
#                         2033,
#                         1047,
#                         2062
#                     ]
#                 ],
#                 "lineNumber": [
#                     1,
#                     1,
#                     2,
#                     2,
#                     2,
#                     2,
#                     3,
#                     4,
#                     43,
#                     44,
#                     44,
#                     44
#                 ],
#                 "scores": {
#                     "pantaloons": 100.0,
#                     "big bazaar": 73.7864787372622,
#                     "hamleys": 68.37634587578276,
#                     "max": 66.66666666666667,
#                     "reliance trends": 66.33249580710799
#                 }
#             },
#             "address": {
#                 "index": [
#                     53,
#                     54,
#                     56
#                 ],
#                 "objs": [
#                     "L.B.S",
#                     "Road",
#                     "Kurla"
#                 ],
#                 "pos": [
#                     [
#                         172,
#                         472,
#                         249,
#                         498
#                     ],
#                     [
#                         269,
#                         472,
#                         332,
#                         498
#                     ],
#                     [
#                         367,
#                         472,
#                         444,
#                         498
#                     ]
#                 ],
#                 "lineNumber": [
#                     10,
#                     10,
#                     10
#                 ]
#             },
#             "phone_number": {
#                 "index": [],
#                 "objs": [],
#                 "pos": [],
#                 "lineNumber": []
#             },
#             "gst_number": {
#                 "index": [
#                     21
#                 ],
#                 "objs": [
#                     "33AAECP2371C1ZW"
#                 ],
#                 "pos": [
#                     [
#                         336,
#                         296,
#                         575,
#                         315
#                     ]
#                 ],
#                 "lineNumber": [
#                     5
#                 ]
#             },
#             "email": {
#                 "index": [],
#                 "objs": [],
#                 "pos": [],
#                 "lineNumber": []
#             }
#         },
#         "total": {
#             "index": [
#                 147
#             ],
#             "objs": [
#                 "1390.00"
#             ],
#             "pos": [
#                 [
#                     1418,
#                     1288,
#                     1525,
#                     1307
#                 ]
#             ],
#             "lineNumber": [
#                 26
#             ]
#         },
#         "invoice_number": {
#             "index": [
#                 120,
#                 126,
#                 139,
#                 145
#             ],
#             "objs": [
#                 "16.55",
#                 "16.55",
#                 "16.55",
#                 "16.55"
#             ],
#             "pos": [
#                 [
#                     371,
#                     1067,
#                     446,
#                     1089
#                 ],
#                 [
#                     695,
#                     1066,
#                     770,
#                     1087
#                 ],
#                 [
#                     371,
#                     1169,
#                     446,
#                     1192
#                 ],
#                 [
#                     696,
#                     1169,
#                     771,
#                     1191
#                 ]
#             ],
#             "lineNumber": [
#                 22,
#                 22,
#                 25,
#                 25
#             ]
#         },
#         "date": {
#             "index": [
#                 86
#             ],
#             "objs": [
#                 "21-10-2021"
#             ],
#             "pos": [
#                 [
#                     175,
#                     797,
#                     331,
#                     817
#                 ]
#             ],
#             "lineNumber": [
#                 16
#             ],
#             "dateValue": [
#                 "2021-10-21"
#             ]
#         },
#         "time": {
#             "index": [
#                 87
#             ],
#             "objs": [
#                 "18:44"
#             ],
#             "pos": [
#                 [
#                     354,
#                     797,
#                     429,
#                     817
#                 ]
#             ],
#             "lineNumber": [
#                 16
#             ],
#             "timeValue": [
#                 "18:44:00"
#             ]
#         },
#         "ocrTexts": "Tax Invoice\nADITYA BIRLA FASHION AND RETAIL LIMITED\nPantaloons\nPhoenix Market City Velachery Main Road Velachery Chennai-600042\nGSTIN No. 33AAECP2371C1ZW\nCompany PAN: AAECP2371C\nCorporate Address:\nPiramal Agastya Corporate Park, Bldg \"A\",\n4th & 5th Floor, Unit No. 401, 403, 501 and 502,\nL.B.S Road, Kurla Mumbai-400070 Maharashtra, India\nCIN : L18101MH2007PLC233901\nCustomer Name: Garima Sinha\nCustomer No.: 9769906550\nRECEIPT NO.: P067303121000880\nStore ID : P067\nTill: P067303\n21-10-2021 18:44\nCashier ID: 270784\nCashier Name: Uma\nHSN\nQTY\nMRP\nDISC%\nDISC_AMT\nNET_AMT\nITEM_NAME\nEAN_CODE\nTAX_RATE TAX\nAMANTE LINGERIE\n8 903129202978\nCGST (2.50%) 16.55\nAMANTE LINGERIE\n8903129203050\nCGST (2.50%) 16.55\n695.00\n695.00\n62121000\n1\nSGST (2.50%) 16.55\n695.00\n695.00\n62121000\n1\nSGST (2.50%) 16.55\nTotal\n1390.00\nTender\nHDFC Card\nTransaction ref. no.\nItem Purchased\n1390.00\nP067-P067303-1341 L: 1\n2\nTAX\nCGST\nTAXABLE AMT\n1323.80\n1323.80\nRATE\n2.50%\n2.50%\nTAX AMOUNT\n33.10\n33.10\nSGST\nFor any queries, please call Customer Care 1800 103 7527\nJoin us on www.facebook.com/pantaloons and www.instagram.com/pantaloonsfashion.\nFor points balance SMS \"MYGC\" to \"575758\"\n*GST invoice for Input tax credit are not allowed for return and exchange.\n*Net Amt. Inclusive of applicable taxes\nThis document is to be treated as tax invoice to the extent of supply of taxable\ngoods and bill of supply to the extent of supply of exempted goods\nSale is Ex-showroom\nThis is a computer generated invoice & should be treated as signed by an\nauthorized signatory\nNote : For any query / Suggestion, please refer to new registered office address\nmentioned on front side of the invoice.\nP067303121000880\nNAMASTE ! !\n",
#         "mall": "Phoenix Marketcity and Palladium Chennai"
#     }



# displayMainDict = {}
# for key,value in mainDict.items():
# 	if key == 'vendor':
# 		for vKey,vValue in mainDict[key].items():
# 			if vKey == 'name' or vKey == 'address' or vKey == 'phone_number' or vKey == 'gst_number' or vKey == 'email':
# 				for iVKey,iVValue in mainDict[key][vKey].items():
# 					if iVKey not in ['index','pos','lineNumber']:
# 						if key not in (displayMainDict.keys()):
# 							displayMainDict.update({key:{vKey:{iVKey:iVValue}}})
# 						else:
# 							displayMainDict[key].update({vKey:{iVKey:iVValue}})
# 	if key == 'total' or key == 'invoice_number' or key == 'date' or key == 'time':
# 		for oKey,oValue in mainDict[key].items():
# 			if oKey not in ['index', 'pos', 'lineNumber']:
# 				displayMainDict.update({key:{oKey:oValue}})
# 	if key == 'ocrTexts' or key == 'mall':
# 		displayMainDict.update({key:value})


# print("")
# print("")
# print("displayMainDict : ", displayMainDict)




#########

# ocrDict = {
# 	"store_name" : store_name,
# 	"time_errorCode" : time_errorCode,
# 	"bill_time" : bill_time,
# 	"date_errorCode" : date_errorCode,
# 	"bill_date" : bill_date,
# 	"invoice_number_errorCode" : invoice_number_errorCode,
# 	"bill_number" : bill_number,
# 	"total_errorCode" : total_errorCode,
# 	"bill_total" : bill_total,
# 	"final_errorCode" : final_errorCode,
# 	"retailer_id" : str(store_id),
# 	"mallId" : '',
# 	"mobile_number" : mobile_number,
# 	"mobile_errorCode" : mobile_errorCode
# }

# output_dict = {
# 	"store_name": store_name, 
# 	"keyword":keyword, 
# 	"raw_data": img_to_text_data[0], 
# 	"cleaned_data":cleaned_data, 
# 	"base64_data":base64_data, 
# 	"final_errorCode":final_errorCode, 
# 	"errorCode":errorCode, 
# 	"bill_time":bill_time, 
# 	"time_errorCode":time_errorCode, 
# 	"bill_date":bill_date, 
# 	"date_errorCode":date_errorCode, 
# 	"bill_number":bill_number,
# 	"invoice_number_errorCode":invoice_number_errorCode, 
# 	"bill_total":bill_total, 
# 	"total_errorCode":total_errorCode, 
# 	"img_file_to_text_time":img_file_to_text_time, 
# 	"logic_time":logic_time, 
# 	"database_gcp_cleaning_time":database_gcp_cleaning_time, 
# 	"database_time":database_time, 
# 	"file_location":str(file_location)
# }

# errorCodes = ''



# mainDict = {'vendor': {'name': {'scores': {'big bazaar': 88.45379626717033, 'lifestyle': 80.06407690254358, 'reliance trends': 73.48469228349535, 'hamleys': 68.37634587578276, 'starmark': 66.66666666666667}}, 'address': {'objs': ['MARKET', 'CITY', 'NO.142']}, 'phone_number': {'objs': ['8088420084']}, 'gst_number': {'objs': []}, 'email': {'objs': []}}, 'total': {'objs': ['522.00', '522.00', '522.00']}, 'invoice_number': {'objs': ['497.18', '497.18', 'over', 'over']}, 'date': {'dateValue': ['2021-08-09', '2021-11-08']}, 'time': {'timeValue': []}, 'ocrTexts': 'TAX INVOICE/BILL OF SUPPLY\nBIG BAZAAR (FUTURE RETAIL LTD)\nPHOENIX MARKET CITY,NO.142\nVELACHERY, VELACHERY MAIN ROAD\nCHENNAI:- 600042\nTel No: 8088420084\nHELPLINE: 1800 266 2255\nGST TIN:33AADCB 1093N1ZN W.E.F 01.07.2017\nCIN NO:L51909MH2C07PLC268269\nITEM DESC\nSN VOM\nQTY DISC AMT NET AMT\nCGSTX SGST%\nRS.\n240.00\n30,00\n27.00\n170.00\nPRIST GOLD PRM 200g\n9019 Pcs\nCAVIN BTSCH TP 180ml\n2202 Pcs\nHERS MSK ALMOND 200m\n2202 Pcs\nAPPLE SHIMLA PKD EA\n3081 Pcs\nHED POPCORN HAY&CH01P\n1704 Pcs\nRDIND PORN MGC MSL 1P\n2106 Pcs\nBersnl Acc Insurance\n9971 Pcs\nSPECIAL BENEFIT\n9971 Pcs\nSUBTOTAL\n2 0.00\n2.5 2,5\n1 5.00-\n6 6\n1 8.00-\n6 6\n2 0.00\n0 0\n1 0.00\n99\n1\n6 6\n0.00\n9 9\n-1 0.00\n9\n30.00\n0.00\n25.00\n2.36\n2.36-\nco\n522.00\n-\nWOW!\nTOTAL\nCASH\n522.00\n522.00\nYour Mobile Number\n6000000000\nHas Been Registered\nwith Big Bazaar\nPIECES PURCHASED: 8 DISC ITEMS: 2\nTOTAL SAVING: 13.00\nGST BASE AMT\nCGST 497.18\nSGST 497.18\nTAX AMT\n12.40\n12.40\nTax Invoice Number - 2541006000061373\nIMPER\nAuth Sign\nCH:464618 knand D\nTILL NO.6 MEMO NO.0061373 Tr:51754\nSt:2541 08/09/21 19:11\nNet Amount is inclusive of all taxes\nTotal Savings add to discount over MRP\nand additional Promotions.\n-\nNow also shop online\n@ shop.bigbazaar.com\nGet Free Home Delivery\non orders over Rs.500\n"Insurance policy\noffer is exclusive for\nFuture Pay Members Only;\nT&C Apply. Eligible\nCustomers will shortly\nreceive policy SMS.\n', 'mall': 'Phoenix Marketcity and Palladium Chennai'}
# print("mainDict : ", mainDict)

# def find_mallId(mainDict, errorCodes):
# 	try:
# 		mallId = ''
# 		mallErrorCodeSuccess = '146'
# 		mallErrorCodeError = '147'

# 		malls = common_util.read_configuration()['vendorAddress']
# 		mall = mainDict['mall'] if 'mall' in mainDict.keys() else ''

# 		if mall != '':
# 			if mall in malls:
# 				mallId = str(malls.index(mall)+1)
# 				errorCodes += mallErrorCodeSuccess
# 			else:
# 				errorCodes += mallErrorCodeError
# 		else:
# 			errorCodes += mallErrorCodeError
# 		return mallId, errorCodes
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_mallId')
# 		raise e


# def find_storename(mainDict, errorCodes):
# 	try:
# 		storename = ''
# 		storenameErrorCodeSuccess = '4'
# 		storenameErrorCodeError = '5'

# 		if 'vendor' in mainDict.keys():
# 			if 'name' in mainDict['vendor'].keys():
# 				if 'scores' in mainDict['vendor']['name'].keys():
# 					scores = mainDict['vendor']['name']['scores']
# 					if len(scores) > 0:
# 						storename = max(scores, key=scores.get)

# 		if storename != '':
# 			errorCodes += ","+storenameErrorCodeSuccess
# 		else:
# 			errorCodes += ","+storenameErrorCodeError
# 		return storename, errorCodes
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_storename')
# 		raise e


# def find_time(mainDict, errorCodes):
# 	try:
# 		billTime = ''
# 		timeErrorCode = ''
# 		billTimeErrorCodeSuccess = '65'
# 		billTimeErrorCodeError = '66'

# 		if 'time' in mainDict.keys():
# 			if 'timeValue' in mainDict['time'].keys():
# 				timeValue = mainDict['time']['timeValue']
# 				if len(timeValue) > 0:
# 					billTime = timeValue[0]

# 		if billTime != '':
# 			errorCodes += ","+billTimeErrorCodeSuccess
# 			timeErrorCode = billTimeErrorCodeSuccess
# 		else:
# 			errorCodes += ","+billTimeErrorCodeError
# 			timeErrorCode = billTimeErrorCodeError
# 		return billTime, timeErrorCode, errorCodes
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_time')
# 		raise e


# def find_date(mainDict, errorCodes):
# 	try:
# 		billDate = ''
# 		dateErrorCode = ''
# 		billDateErrorCodeSuccess = '62'
# 		billDateErrorCodeError = '63'

# 		if 'date' in mainDict.keys():
# 			if 'dateValue' in mainDict['date'].keys():
# 				dateValue = mainDict['date']['dateValue']
# 				if len(dateValue) > 0:
# 					billDate = dateValue[0]

# 		if billDate != '':
# 			errorCodes += ","+billDateErrorCodeSuccess
# 			dateErrorCode = billDateErrorCodeSuccess
# 		else:
# 			errorCodes += ","+billDateErrorCodeError
# 			dateErrorCode = billDateErrorCodeError
# 		return billDate, dateErrorCode, errorCodes
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_date')
# 		raise e


# def find_invoicenumber(mainDict, errorCodes):
# 	try:
# 		billNumber = ''
# 		billNumberErrorCode = ''
# 		billNumberErrorCodeSuccess = '46'
# 		billNumberErrorCodeError = '51'

# 		if 'invoice_number' in mainDict.keys():
# 			invoice_numbers = mainDict['invoice_number']['objs']
# 			if len(invoice_numbers) > 0:
# 				invoiceNumberFreq = {i:invoice_numbers.count(i) for i in invoice_numbers}
# 				billNumber = max(invoiceNumberFreq, key=invoiceNumberFreq.get)

# 		if billNumber != '':
# 			errorCodes += ","+billNumberErrorCodeSuccess
# 			billNumberErrorCode = billNumberErrorCodeSuccess
# 		else:
# 			errorCodes += ","+billNumberErrorCodeError
# 			billNumberErrorCode = billNumberErrorCodeError

# 		return billNumber, billNumberErrorCode, errorCodes
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_invoicenumber')
# 		raise e


# def find_total(mainDict, errorCodes):
# 	try:
# 		billTotal = ''
# 		billTotalErrorCode = ''
# 		billTotalErrorCodeSuccess = '18'
# 		billTotalErrorCodeError = '21'

# 		if 'total' in mainDict.keys():
# 			totals = mainDict['total']['objs']
# 			if len(totals) > 0:
# 				totalFreq = {i:totals.count(i) for i in totals}
# 				billTotal = max(totalFreq, key=totalFreq.get)

# 		if billTotal != '':
# 			errorCodes += ","+billTotalErrorCodeSuccess
# 			billTotalErrorCode = billTotalErrorCodeSuccess
# 		else:
# 			errorCodes += ","+billTotalErrorCodeError
# 			billTotalErrorCode = billTotalErrorCodeError

# 		return billTotal, billTotalErrorCode, errorCodes
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_total')
# 		raise e


# def find_mobilenumber(mainDict, errorCodes):
# 	try:
# 		mobileNumber = ''
# 		mobileNumberErrorCode = ''
# 		mobileNumberErrorCodeSuccess = '151'
# 		mobileNumberErrorCodeError = '150'

# 		if mobileNumber != '':
# 			errorCodes += ","+mobileNumberErrorCodeSuccess
# 			mobileNumberErrorCode = mobileNumberErrorCodeSuccess
# 		else:
# 			errorCodes += ","+mobileNumberErrorCodeError
# 			mobileNumberErrorCode = mobileNumberErrorCodeError

# 		return mobileNumber, mobileNumberErrorCode, errorCodes
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_mobilenumber')
# 		raise e


# print()
# print()
# mallId, errorCodes = find_mallId(mainDict, errorCodes)
# storename, errorCodes = find_storename(mainDict, errorCodes)
# billTime, timeErrorCode, errorCodes = find_time(mainDict, errorCodes)
# billDate, dateErrorCode, errorCodes = find_date(mainDict, errorCodes)
# billNumber, billNumberErrorCode, errorCodes = find_invoicenumber(mainDict, errorCodes)
# billTotal, billTotalErrorCode, errorCodes = find_total(mainDict, errorCodes)
# mobileNumber, mobileNumberErrorCode, errorCodes = find_mobilenumber(mainDict, errorCodes)



# print("mallId : ", mallId)
# print("storename : ", storename)
# print("billTime : ", billTime)
# print("timeErrorCode : ", timeErrorCode)
# print("billDate : ", billDate)
# print("dateErrorCode : ", dateErrorCode)
# print("billNumber : ", billNumber)
# print("billNumberErrorCode : ", billNumberErrorCode)
# print("billTotal : ", billTotal)
# print("billTotalErrorCode : ", billTotalErrorCode)
# print("mobileNumber : ", mobileNumber)
# print("mobileNumberErrorCode : ", mobileNumberErrorCode)
# print("errorCodes : ", errorCodes)


# # storeDict =  {'ocrData': {'mallId': '1', 'store_name': 'big bazaar', 'retailer_id': '', 'bill_time': '', 'time_errorCode': '66', 'bill_date': '2021-08-09', 'date_errorCode': '62', 'bill_number': '497.18', 'invoice_number_errorCode': '46', 'bill_total': '522.00', 'total_errorCode': '18', 'mobile_number': '', 'mobile_errorCode': '150', 'final_errorCode': ''}, 'icrData': {'metaFile': {'filename': '100003.jpeg', 'extension': '.jpeg', 'visualizationFilePath': '/home/ritesh/OCR/icr-microservice/data/008_visualize_test_enrich_data/2021_11_08_16_33_24_896016.png'}, 'icr': {'vendor': {'name': {'scores': {'big bazaar': 88.45379626717033, 'lifestyle': 80.06407690254358, 'reliance trends': 73.48469228349535, 'hamleys': 68.37634587578276, 'starmark': 66.66666666666667}}, 'address': {'objs': ['MARKET', 'CITY', 'NO.142']}, 'phone_number': {'objs': ['8088420084']}, 'gst_number': {'objs': []}, 'email': {'objs': []}}, 'total': {'objs': ['522.00', '522.00', '522.00']}, 'invoice_number': {'objs': ['497.18', '497.18', 'over', 'over']}, 'date': {'dateValue': ['2021-08-09', '2021-11-08']}, 'time': {'timeValue': []}, 'ocrTexts': 'TAX INVOICE/BILL OF SUPPLY\nBIG BAZAAR (FUTURE RETAIL LTD)\nPHOENIX MARKET CITY,NO.142\nVELACHERY, VELACHERY MAIN ROAD\nCHENNAI:- 600042\nTel No: 8088420084\nHELPLINE: 1800 266 2255\nGST TIN:33AADCB 1093N1ZN W.E.F 01.07.2017\nCIN NO:L51909MH2C07PLC268269\nITEM DESC\nSN VOM\nQTY DISC AMT NET AMT\nCGSTX SGST%\nRS.\n240.00\n30,00\n27.00\n170.00\nPRIST GOLD PRM 200g\n9019 Pcs\nCAVIN BTSCH TP 180ml\n2202 Pcs\nHERS MSK ALMOND 200m\n2202 Pcs\nAPPLE SHIMLA PKD EA\n3081 Pcs\nHED POPCORN HAY&CH01P\n1704 Pcs\nRDIND PORN MGC MSL 1P\n2106 Pcs\nBersnl Acc Insurance\n9971 Pcs\nSPECIAL BENEFIT\n9971 Pcs\nSUBTOTAL\n2 0.00\n2.5 2,5\n1 5.00-\n6 6\n1 8.00-\n6 6\n2 0.00\n0 0\n1 0.00\n99\n1\n6 6\n0.00\n9 9\n-1 0.00\n9\n30.00\n0.00\n25.00\n2.36\n2.36-\nco\n522.00\n-\nWOW!\nTOTAL\nCASH\n522.00\n522.00\nYour Mobile Number\n6000000000\nHas Been Registered\nwith Big Bazaar\nPIECES PURCHASED: 8 DISC ITEMS: 2\nTOTAL SAVING: 13.00\nGST BASE AMT\nCGST 497.18\nSGST 497.18\nTAX AMT\n12.40\n12.40\nTax Invoice Number - 2541006000061373\nIMPER\nAuth Sign\nCH:464618 knand D\nTILL NO.6 MEMO NO.0061373 Tr:51754\nSt:2541 08/09/21 19:11\nNet Amount is inclusive of all taxes\nTotal Savings add to discount over MRP\nand additional Promotions.\n-\nNow also shop online\n@ shop.bigbazaar.com\nGet Free Home Delivery\non orders over Rs.500\n"Insurance policy\noffer is exclusive for\nFuture Pay Members Only;\nT&C Apply. Eligible\nCustomers will shortly\nreceive policy SMS.\n', 'mall': 'Phoenix Marketcity and Palladium Chennai'}, 'createdAt': datetime.datetime(2021, 11, 8, 16, 33, 24, 950388), 'updatedAt': datetime.datetime(2021, 11, 8, 16, 33, 24, 950388)}}
# # print("storeDict : ", storeDict)


#########

# pmpc_1 = {"Lifestyle":1520,"Big Bazaar":899,"H&M":486,"Max":329,"Zara":314,"Reliance Digital":314,"Pantaloons":306,"Shoppers Stop":299,"Croma":272,"Luxe":268,"RMKV":253,"Reliance Trends":251,"Kakada Ramprasad":180,"Burger King":174,"Marks & Spencer":168,"Jockey":151,"Starmark":142,"Miniso":134,"Aptronix":129,"OnePlus":127}
# pmb_2 = {"Big Bazaar":437,"Lifestyle":373,"Max":271,"Reliance Trendz":246,"Zara":222,"Home Centre":202,"Reliance Digital":198,"Marks & Spencer":173,"Pantaloons":146,"Show Off":102,"Parking":96,"Tata Cha":92,"Domino's Pizza":78,"Miniso":74,"Fab India":71,"Manyavar & Mohey":70,"Tanishq":70,"Burger King":69,"Malabar Gold":65,"Mad Over Donuts":63}
# ppm_3 = {"Zara":245,"H&M":241,"Lifestyle":209,"Marks & Spencer":116,"Tanishq":88,"Pantaloons":80,"Foodhall":63,"Reliance Digital":62,"Mcdonald's":60,"Tommy Hilfiger":48,"Gucci":41,"Sephora":41,"Global Desi":41,"Home Centre":40,"Croma":38,"Malabar Gold":37,"Jack & Jones":33,"Hamleys":32,"Calvin Klein Jeans":31,"Fabindia":30}
# pmk_4 = {"Lifestyle":623,"H&M":399,"Reliance Smart":253,"Reliance Trends":237,"Zara":216,"Pantaloons":215,"Westside":192,"Max":136,"Marks & Spencer":120,"Reliance Digital":99,"Croma":95,"Timezone":72,"Tanishq":71,"Burger King":65,"Home Centre":62,"Miniso":61,"McDonalds":59,"KFC":57,"Mr. DIY":54,"Naturals":50}
# pmp_5 = {"Westside":277,"Lifestyle":206,"H&M":153,"Market 99":139,"Zara":129,"Malabar Gold & Diamonds":121,"Reliance Digital":111,"Reliance Trends":93,"Ajmal Perfumes":85,"Adidas":77,"Croma":71,"Vans":65,"Marks & Spencer":58,"Pantaloons":54,"Diesel":52,"UNI":49,"Max":46,"Tanishq":44,"RPPMSL (FBB":44,"Mad Over Donuts":43}
# ppl_6 = {"Big Bazaar":133,"KFC":74,"Reliance Digital":69,"Lifestyle":57,"H&M":46,"Miniso":36,"Shoppers Stop":34,"Subway":31,"Milk Shake & Co":31,"Asia Seven Express":27,"Max":27,"Reliance Trends":25,"Pantaloons":24,"Westside":22,"Market 99":18,"Stelatoes":18,"Street Foods By Punjab Grill":18,"Café Coffee Tree":15,"Home Centre":15,"Tanishq":14}


#########


# # mainDict = {'vendor': {'name': {'index': [1, 2, 3, 4, 5, 6, 7, 8, 27, 40, 46, 49, 53, 62, 76, 80, 176, 203, 220, 343, 346, 374, 375, 377, 401, 402, 403, 404, 406, 408, 409, 422, 424, 428, 430, 446, 453, 454, 458], 'objs': ['TAX', 'INVOICE', 'AMAR', 'COMMUNICATION', 'PVT', 'LTD', 'Phoenix', 'Market', 'Post', 'Customer', 'GSTIN', 'PAN', 'Invoice', 'Order', 'Invoice', 'Customer', 'IGST', 'TCS', 'PAY', 'promotional', 'benefits', 'are', 'accepted', 'IRP', 'invoice', 'and', 'your', 'GSTIN', 'rejected', 'IRP', 'portal', 'and', 'Code', 'scenarios', 'B2C', 'input', 'PVT', 'LTD', 'franchise'], 'pos': [[909, 238, 999, 275], [1016, 238, 1214, 275], [243, 393, 332, 421], [342, 393, 614, 421], [626, 393, 680, 421], [691, 393, 746, 421], [245, 440, 353, 475], [365, 440, 464, 475], [245, 478, 303, 510], [245, 618, 379, 646], [245, 665, 336, 692], [245, 714, 304, 741], [245, 848, 342, 875], [245, 940, 326, 968], [245, 1082, 342, 1112], [245, 1128, 379, 1158], [325, 2939, 392, 2964], [243, 3173, 298, 3200], [426, 3407, 480, 3433], [1130, 4137, 1282, 4173], [1408, 4137, 1509, 4173], [923, 4211, 962, 4244], [973, 4211, 1085, 4244], [1133, 4211, 1176, 4244], [1042, 4249, 1129, 4280], [1141, 4249, 1185, 4280], [1194, 4249, 1251, 4280], [1261, 4249, 1343, 4280], [1383, 4249, 1484, 4280], [1533, 4249, 1576, 4280], [1586, 4249, 1659, 4280], [769, 4285, 813, 4316], [871, 4285, 932, 4316], [1053, 4285, 1170, 4316], [1189, 4285, 1238, 4316], [695, 4323, 759, 4354], [593, 4400, 643, 4430], [653, 4400, 703, 4430], [926, 4400, 1040, 4430]], 'lineNumber': [2, 2, 3, 3, 3, 3, 4, 4, 5, 8, 9, 10, 11, 13, 16, 17, 38, 43, 48, 58, 58, 60, 60, 60, 61, 61, 61, 61, 61, 61, 61, 62, 62, 62, 62, 63, 64, 64, 64], 'scores': {'shoppers stop': 86.60254037844386, 'kakada ramprasad': 84.9207775608447, 'zara': 83.33333333333334, 'starmark': 82.49579113843056, 'pantaloons': 78.82407813680821}}, 'address': {'index': [9, 11, 14, 16, 19, 20, 22, 23, 26, 27, 29, 35, 36, 37], 'objs': ['City', 'Unit', 'G18A', 'No.106', 'Whitefiled', 'Road', 'Opposite', 'Mahadevapura', 'Mahadevapura', 'Post', 'Bangalore', '9620060280', 'Customer', 'Support'], 'pos': [[475, 440, 529, 475], [549, 440, 607, 475], [669, 440, 743, 475], [763, 440, 860, 475], [934, 440, 1075, 475], [1088, 440, 1155, 475], [1176, 440, 1297, 475], [1309, 440, 1515, 475], [1615, 440, 1821, 475], [245, 478, 303, 510], [314, 478, 453, 510], [433, 525, 603, 554], [245, 571, 379, 605], [391, 571, 499, 605]], 'lineNumber': [4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 7, 7]}, 'phone_number': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}, 'gst_number': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}, 'email': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}}, 'total': {'index': [194], 'objs': ['17598.00'], 'pos': [[1753, 3077, 1878, 3104]], 'lineNumber': [41]}, 'invoice_number': {'index': [112, 114], 'objs': ['HSNCODE', '85171211'], 'pos': [[1573, 1546, 1721, 1573], [1744, 1546, 1877, 1573]], 'lineNumber': [24, 24]}, 'date': {'index': [], 'objs': [], 'pos': [], 'lineNumber': [], 'dateValue': []}, 'time': {'index': [57], 'objs': ['16:05:45'], 'pos': [[608, 848, 725, 875]], 'lineNumber': [11], 'timeValue': ['16:05:45']}, 'ocrTexts': 'וח\nTAX INVOICE\nAMAR COMMUNICATION PVT LTD\nPhoenix Market City, Unit No-G18A, No.106/107 Whitefiled Road, Opposite Mahadevapura CMC, Mahadevapura\nPost, Bangalore\nPh. No.: +91 9620060280\nCustomer Support: service.in@xiaomi.com\nCustomer HotLine: 1800 103 6286\nGSTIN: 29AALCA2177L1Z6\nPAN NO.: AALCA2177L\nInvoice Date: 2021-09-05 16:05:45\nInvoice NO.: SMN0090092100080\nOrder NO.: SA1217462351682515\nCust. Name: Romash\nCust. PH: 7019474773\nInvoice Reference number:\nCustomer Address:\nSupply Type Code:B2C\nDocument Type Code: Invoice\nRCM: NO\nDescription\nRedmi Note 105 Deep Sea Blue 6GB64GB\nSN: 31996/G1SW12128\nIMEI: 865008051510623\nHSNCODE: 85171211\nSGST %\nMRP\n16999\nGST%\n9%\n9%\nCGST\n1143.99\nSGST\n1143.99\nQTY\n1\nTotal(incl.tax)\n14999\nDescription\nRedmi Earphones Blue\nGoodsID: 28323\nHSNCODE: 85183000\nMRP\n599\nCGST%\n9%\nSGST %\n9%\nCGST\n30.43\nSGST\n30.43\nQTY\n1\nTotal(incl.tax)\n399\nSUB TOTAL:\n13049.16\nTotal GST Tax:\nTotal IGST:\nTotal SGST:\nTotal CGST:\nMRP(INCL GST TAX):\nTotal(INCL GST TAX):\nTCS:\nMI EXCHANGE:\nDISCOUNT:\nGRAND TOTAL:\nPAYMENT:\nAMAZON PAY:\n2347.00\n0.00\n1174.42\n1174.42\n17598.00\n15398.00\n0.00\n0.00\n-2200.00\n15398.00\n15398.00\nThis is a computer generated invoice, so no signature is required\nAMAR COMMUNICATION PVT LTD\nNo.155/2,HBR Layout, Kacharakanahalli,\nnur\nMain Road, St Thomas Town Post, Bangalore\nTerms and conditions:\n1.Product once sold will not be returned or exchanged Under any circumstance.\n2.Please visit nearby Authorised Service centre in case of DOA for authorization and replacement.\n3.Keep a copy of this invoice to claim any future serve on the product at our service centers.\n4.By making this purchase, you consent to the store sharing the information provided by you with Xiaomi Technology India\nPrivate Limited.\n5.You consent to Xiaomi using this information to send you any promotional offers or benefits, to send you surveys or\nfeedback requests, or for any other reason related to your order.\n6.It is also highlighted that only active GSTINs are accepted by IRP portal for IRN generation. Thus, in case status of your\nGSTIN is cancelled or inactive at the time of issuance of invoice and your GSTIN is rejected by IRP portal, we shall not be\nable to issue B2B invoice with IRN and QR Code. In such scenarios, B2C invoice would be raised by us basis which you\nwould not be eligible to avail input tax credit.\n(AMAR COMMUNICATION PVT LTD is an authorized franchise holder of Mi products.)\n'}
# # ocrTexts = mainDict['ocrTexts']
# ocrTexts = 'ZARA\nTAX INVOICE\nInditex Trent Retail India Pvt Ltd\nAmbience Corporate Office Tower 2\nLevel 8 an Plot No. 3, Unit No. 1\n(office 1)\nAmbience Island, NH-8, Gurgaon 122002,\nHaryana, India\nCIN: 074900HR2009FTC043768\nTel: +91 124 497 3500\nFax: +91 124 497 3510\nwww.zara.com/in\nGSTIN: 33AACCI15660129\nPhoenix Marketcity Mall Chennai\nUG-17, Upper Ground Floor Plot in\nNorthern and Western part of old door\nno. 66 New door no. 142, Velachery\nSaidapet Taluk TAMIL NADU 600042\nTel: 044-66716216/217/218/219\nStore: 9184 CHE-PHOENIX MARKET\nDate: 08-08-2021\nTime: 11:58\nInvoice: 9184-01-S127295\nTrans: 480301\n3840\nTSP CODE QTY\nPRICE\nAMOUNT\nT\nSMS 640299 1 3,990.00 3,990.00 p\n10001337 1232182001042 RUNNING SHOES\n3,381.36 Central tax9.00% 304.32\n3,381.36 State tax 9.00% 304.32\nSMC 620530 1 2,790.00 2.790.00 p\n10002367 0754545771005 SHIRT\n2,491.08 Central tax6.00% 149.46\n2,491.08 State tax 6.00% 149.46\nSMC 6203431 2,990.00 2,990.00 P\n10003330 0070651540746 TROUSERS\n2,669.66 Central tax6.00% 160.17\n2,669.66 State tax 6.00% 160.17\nSMC 620520 1 2,990.00 2,990.00 P\n10004360 0097532040305 SHIRT\n2,669.66 Central tax6.00% 160.17\n2,669.66 State tax 6.00% 160.17\nSMS 640299 1 2,990.00 2,990.00 P\n10005323 1220372204042 SPORT SHOES\n2,533.90 Central tax9.00% 228.05\n2,533.90 State-tax 9.00% 228.05\nTOTAL\n5\n15,750.00\nWirecard\nINR 15, 750.00\nCard Number :\n************5795\nVISA\nExp. Date: XXXX\nMID:\nBATCH NUM: 224\nBILL NUM:\nAPPR. CODE: 873754\nDate: 08-08-2021\nTID: 41833208\nINV. NUM: 6402\n0918401127295\nRRN: 000000006656\nTime: 11:58:11\nTotal Net\nCentral tax 9.00%\n5,915.26\n532.37\nTotal Net\nState tax 9.00%\n5,915.26\n532.37\nTotal Net\nCentral tax 6.00%\n7,830.40\n469.80\nTotal Net\nState tax 6.00%\n7,830.40\n469.80\n*****\nTHANKS FOR YOUR VISIT\n*****\nNote: Unless otherwise stated, tax on\nthis invoice is not payable under\nreverse charge.\nThis is a computer generated invoice\nand hence does not require any\nsignature\nEmployee: 3840\n9184-01-S127295\nTrans: 480301\n'
# ocrTexts = ocrTexts.replace("\n", " ")

# mallsAddressArr = common_util.read_configuration()["mallsCollection"]

# mallsDict = {}

# for index, rows in enumerate(mallsAddressArr):
# 	count = 0
# 	for address in rows['vendor.address']:
# 		print("address : ", address)
# 		address = address.lower()
# 		if address in ocrTexts.lower():
# 			count += 1
# 			mallsDict.update({rows['vendor.mall']:count})

# mallStr = ''
# if len(mallsDict) > 0:
# 	mallStr = max(mallsDict, key=mallsDict.get)
# print("mallStr : ", mallStr)


#########

# mainDict =  {'vendor': {'name': {'index': [0, 1, 5, 6, 10, 11, 13, 24, 27, 47, 70], 'objs': ['TAX', 'INVOICE', 'SUPPLY', 'BIG', 'RETAIL', 'LTD', 'VELACHERY', 'CHENNAI', 'Tel', 'ITEM', 'Persnl'], 'pos': [[250, 160, 300, 200], [323, 160, 439, 200], [604, 160, 707, 200], [214, 203, 263, 244], [547, 204, 648, 247], [677, 205, 722, 246], [218, 292, 372, 333], [338, 336, 459, 373], [324, 382, 366, 419], [38, 605, 104, 645], [33, 873, 133, 917]], 'lineNumber': [1, 1, 1, 2, 2, 2, 3, 4, 5, 8, 13], 'scores': {'reliance digital': 84.86684247915055, 'lifestyle': 80.06407690254358, 'reliance trends': 73.48469228349535, 'mi': 70.71067811865474, 'miniso': 70.71067811865474}}, 'address': {'index': [14, 16, 17, 18, 23], 'objs': ['PHOENIX', 'MARKET', 'VELACHERY', 'CITY', 'ROAD'], 'pos': [[249, 246, 369, 292], [391, 247, 494, 293], [410, 292, 565, 333], [515, 248, 585, 293], [674, 292, 743, 333]], 'lineNumber': [3, 3, 3, 3, 3]}, 'phone_number': {'index': [30], 'objs': ['968420984'], 'pos': [[458, 382, 638, 421]], 'lineNumber': [5]}, 'gst_number': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}, 'email': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}}, 'total': {'index': [66, 87], 'objs': ['1299.00', '1299.00'], 'pos': [[745, 788, 867, 830], [744, 1152, 863, 1189]], 'lineNumber': [11, 18]}, 'invoice_number': {'index': [118, 120, 122], 'objs': ['4810749980', '500.00', 'BASE'], 'pos': [[100, 1662, 275, 1701], [488, 1663, 594, 1707], [312, 1754, 381, 1793]], 'lineNumber': [27, 27, 28]}, 'date': {'index': [], 'objs': [], 'pos': [], 'lineNumber': [], 'dateValue': []}, 'time': {'index': [154], 'objs': ['16:26'], 'pos': [[579, 2335, 659, 2374]], 'lineNumber': [35], 'timeValue': ['16:26:00']}, 'ocrTexts': 'TAX INVOICE/BILL OF SUPPLY\nBIG BAZAAR (FUTUBE RETAIL LTD)\nPHOENIX MARKET CITY, NO 142\nVELACHERY, VELACHERY AIN ROAD\nCHENNAI - 600042\nTel No: 968420984\nHELFLINE: 1800 286 2255\nGST TIN:33AACC81083NIZHNE,F 01.07.2017\nCIN NC:.51909MH2007P_C288269\nITEM DESC\nHSN\nQTY DISC «NT NET AMT\nCG973 SGS %\nRs.\n500 00- 1299.00\n)\nLCO,FLDNM,32,TINY\n6204 PCS\nPersnl Acc Insurance\n9971 Pos\nSPECIAL BENEFIT\n9971 Pos\nSUBTOTA\n1\n6\n--- 1\n9\n2.36\n0 00\n2.36-\n1299.00\nqYw-\nIP\nTOTAL\nICICI\n1299.00\n1299.00\nYour Mobile Number\n6000000000\nHas Been Registered\nwith Big Bazaar\nPIECES PURCHASED: | DISC ITENS: 1\nTOTAL SAVING: 500.00\nTOTAL COUPON SAVINGS: 500.0)\n4810749980\n: 500.00\n.\nGST\nCAST\nSGST\nBASE AMT\n1959.82\n1759.87\nTAK 2015\n69.50\n69.59\nTax Invoice Yune 2541020000030929\nNumber\nAuth Sign\nCH:99959239 Aravind Ramalingam\nTILL NO.26 NEMO NO.0030929 :52.688\nSt:2541 16 09:21 16:26\nNet Amount is inclusive of all taxes\nTotal Savirgs adu to ciscount over MRP\nand additional Promotions.\n4. OR\nNow also shop online\n@shop.bigbazaar.corn\nGet Free Home Delivery\non orders over Rs.500\nIN\nL\n"Insurance policy\noffer is exclusive for\nFuture Pay Members Only;\nT&C Apply. Eligible\nCustomers will shortly.\nreceive policy SMS.\n1\n', 'mall': 'Phoenix Marketcity and Palladium Chennai'}
# print()
# print("mainDict : ", mainDict)
# displayMainDict = {}
# for key,value in mainDict.items():
# 	if key == 'vendor':
# 		for vKey,vValue in mainDict[key].items():
# 			if vKey == 'name' or vKey == 'address' or vKey == 'phone_number' or vKey == 'gst_number' or vKey == 'email':
# 				for iVKey,iVValue in mainDict[key][vKey].items():
# 					if iVKey not in ['index','pos','lineNumber']:
# 						if key not in (displayMainDict.keys()):
# 							displayMainDict.update({key:{vKey:{iVKey:iVValue}}})
# 						else:
# 							if vKey not in (displayMainDict[key].keys()):
# 								displayMainDict[key].update({vKey:{iVKey:iVValue}})
# 							else:
# 								displayMainDict[key][vKey].update({iVKey:iVValue})

# 	if key == 'total' or key == 'invoice_number' or key == 'date' or key == 'time':
# 		for oKey,oValue in mainDict[key].items():
# 			if oKey not in ['index', 'pos', 'lineNumber']:
# 				displayMainDict.update({key:{oKey:oValue}})
# 	if key == 'ocrTexts' or key == 'mall':
# 		displayMainDict.update({key:value})
# print()
# print("displayMainDict : ", displayMainDict)

#########

# import re
# from nltk.corpus import stopwords


# ocrTexts = "ZARA\nTAX INVOICE\nInditex Trent Retail India Pvt Ltd\nAmbience Corporate Office Tower 2\nLevel 8 on Plot No. 3, Unit No. 1\nCoffice 1)\nAmbience Island, NH-8, Gurgaon 122002,\nHaryana, India\nCIN: U74900HR 2009FTC043768\nTel: +91 124 497 3500\nFax: +91 124 497 3510\nwww.zara.com/in\nGSTIN: 29AACCI1566Q1ZY\nPhoenix Marketcity Mall\nUG-04 and 07 Dyavasandra Phase-I\nIndustrial Area, Krishnarajapuran\nHobli Bangalore South KARNATAKA 560048\nTel: 080-67266121/22/24\nStore: 9218 BAN-PHOENIX MAR\nDate: 23-09-2021\nTime: 15:40\nInvoice: 9218-02-5057378\nTrans: 73067\n8457\nPRICE\nTSP CODE QTY\nAMOUNT\nT\n106 60\nSMC 611020 1 1,990.00 1,990.00 P\n10001646 0328430780002 SWEATER\n1,776.80 Central tax6.00%\n1,776.80 State tax 6.00% 106 60\nSMC 620342 1 2,990.00 990.00 P\n10002676 0084037580040 TROUSERS\n2,669.66 Central tax6.00% 160 17\n2,669.66 State tax 6.00% 160 17\nSMS 640291 1\n3,990.00 3,990.00 P\n100036391200582010040 ANKLE BOOT\n3,381.36 Central tax9.00%\n304.32\n3,381.36 State tax 9.00%\n304 32\nTOTAL\n8,970.00\nPinelabs\nINR 8,970.00\nCard Number :\n************2789\nMASTERCARD\nExp. Date: XXXX\n"
# vendorNames = ["big bazaar","burger king","croma","dominos","hamleys","hennes & mauritz","kakada ramprasad","kfc","lifestyle","luxe","marks & spencer","max","mi","miniso","mobitech creations","pantaloons","reliance digital","reliance trends","rmkv silks","starmark","shoppers stop","tanishq","tablez & toyz","westside","zara"]


# cachedStopWords = stopwords.words("english")
# print("cachedStopWords : ", cachedStopWords)
# pattern = re.compile(r'\b(' + r'|'.join(cachedStopWords) + r')\b\s*')
# text = pattern.sub('', ocrTexts.lower())
# print("text : ", text)
# corpus = text.replace("\n", " ")
# print("corpus : ", corpus)


# from sentence_transformers import SentenceTransformer
# import scipy.spatial

# embedder = SentenceTransformer('bert-base-nli-mean-tokens')

# # # Corpus with example sentences
# # corpus = ['A man is eating a food.',
# #           'A man is eating a piece of bread.',
# #           'The girl is carrying a baby.',
# #           'A man is riding a horse.',
# #           'A woman is playing violin.',
# #           'Two men pushed carts through the woods.',
# #           'A man is riding a white horse on an enclosed ground.',
# #           'A monkey is playing drums.',
# #           'A cheetah is running behind its prey.'
# #           ]
# corpus_embeddings = embedder.encode([corpus])
# print("corpus_embeddings : ", corpus_embeddings)

# # # Query sentences:
# # queries = ['A man is eating pasta.', 'Someone in a gorilla costume is playing a set of drums.', 'A cheetah chases prey on across a field.']
# queries = vendorNames
# query_embeddings = embedder.encode(queries)

# # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
# closest_n = 5
# for query, query_embedding in zip(queries, query_embeddings):
# 	distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]

# 	results = zip(range(len(distances)), distances)
# 	results = sorted(results, key=lambda x: x[1])

# 	print("\n\n======================\n\n")
# 	print("Query:", query)


#########


# # ocrTexts = "ZARA\nTAX INVOICE\nInditex Trent Retail India Pvt Ltd\nAmbience Corporate Office Tower 2\nLevel 8 on Plot No. 3, Unit No. 1\nCoffice 1)\nAmbience Island, NH-8, Gurgaon 122002,\nHaryana, India\nCIN: U74900HR 2009FTC043768\nTel: +91 124 497 3500\nFax: +91 124 497 3510\nwww.zara.com/in\nGSTIN: 29AACCI1566Q1ZY\nPhoenix Marketcity Mall\nUG-04 and 07 Dyavasandra Phase-I\nIndustrial Area, Krishnarajapuran\nHobli Bangalore South KARNATAKA 560048\nTel: 080-67266121/22/24\nStore: 9218 BAN-PHOENIX MAR\nDate: 23-09-2021\nTime: 15:40\nInvoice: 9218-02-5057378\nTrans: 73067\n8457\nPRICE\nTSP CODE QTY\nAMOUNT\nT\n106 60\nSMC 611020 1 1,990.00 1,990.00 P\n10001646 0328430780002 SWEATER\n1,776.80 Central tax6.00%\n1,776.80 State tax 6.00% 106 60\nSMC 620342 1 2,990.00 990.00 P\n10002676 0084037580040 TROUSERS\n2,669.66 Central tax6.00% 160 17\n2,669.66 State tax 6.00% 160 17\nSMS 640291 1\n3,990.00 3,990.00 P\n100036391200582010040 ANKLE BOOT\n3,381.36 Central tax9.00%\n304.32\n3,381.36 State tax 9.00%\n304 32\nTOTAL\n8,970.00\nPinelabs\nINR 8,970.00\nCard Number :\n************2789\nMASTERCARD\nExp. Date: XXXX\n"
# # ocrTexts = "ZARA\nTAX INVOICE\nInditex Trent Retail India Pvt Ltd\nAmbience Corporate Office Tower 2\nLevel 8 on Plot No. 3, Unit No.1\nCoffice 1)\nAmbience Island, NH-8, Gurgaon 122002,\nHaryana, India\nCIN: 0749001R 2009FTC043768\nTel: +91 124 497 3500\nFax: +91 124 497 3510\nwww.zara.com/in\nGSTIN: 29AACCI1566Q1ZY\nPhoenix Marketcity Mall\nUG-04 and 07 Dyavasandra Phase-Il\nIndustrial Area, Krishnarajapuran\nHobli Bangalore South KARNATAKA 560048\nTel: 080-67266121/22/24\nStore: 9218 BAN-PHOENIX MAR\nDate: 21-08-2021\nTime: 12:33\nInvoice: 9218-02-5054649\nTrans: 69526\n8457\nTSP CODE QTY\nPRICE\nAMOUNT\nT\nSMC 6103431 1,990.00 1.990.00 P\n100019390076130440105 BERMUDA\n1,776.80 Central tax6.00% 106 60\n1.776.80 State tax 6.00% 106 60\nSMC 6109101 1,990.00 1,990.00 P\n10002969 0622430081103 T-SHIRT\n1,776.80 Central tax6.00% 106 60\n1.776.80 State tax 6.00%\n106.60\nTOTAL\n2\n3.980.00\nWirecard\nINR 3,980.00\nCard Number\n************074\nVISA\nExp. Date: XXXX\nMID:\nBATCH NUM: 183\nBILL NUM\nAPPR. CODE: 775452\nDate: 21-08-2021\nTID: 41833174\nINV. NUM 8'22\n0921802054649\nRRN: 000000008974\nTime: 12 33 24\nTotal Net\nCentral tax 6.00%\n3,553.60\n213.20\nTotal Net\nState tax 6.00%\n3,553.60\n213.20\nTHANKS FOR YOUR VISIT\n*****\nNote: Unless otherwise stated, tax on\nthis invoice is not payable under\nreverse charge\nThis is a computer generated invoice\nand hence does not require any\nsignature\n"
# # ocrTexts = "וח\nTAX INVOICE\nUnbox Gadgets Pvt Ltd\nUnit LG23, S.No.207, Lower Ground Floor, Phoenix Marketcity, Viman Nagar Road, Viman Nagar, Pune-411014\nPh. No.: 9067905915\nCustomer Support: service.in@xiaomi.com\nCustomer HotLine: 1800 103 6286\nGSTIN: 27AACCU1521H1ZM\nPAN NO.: AACCU1521H\nInvoice Date: 2021-10-30 15:41:33\nInvoice NO.: SMN0013102100475\nOrder NO.: SA1218002224249806\nCust. Name: BHAIRAVNATH SAND SUPPLIERS\nCust. PH: 8669886969\nInvoice Reference number:\nCustomer Address:\nSupply Type Code:B2B\nDocument Type Code: Invoice\nNO\nGST NO.: 27AOPPP1722F1ZV\nDescription\nRedmi 9 Activ Carbon black 4GB64GB\nSN: 36650/D1 WF00722\nIMEI: 862968058549697\nHSNCODE: 85171211\nMRP\n10999\nCGST%\n9%\nSGST %\n9%\nCGST\n648.22\nSGST\n648.22\nQTY\n1\nTotal(incl.tax)\n8499\nDescription\nMi KN95 Protective Mask Pack of 2 White\nGoodsID: 30101\nHSNCODE: 63079090\nMRP\n500\nCGST%\n2.5%\nSGST %\n2.5%\nCGST\n1.19\nSGST\n1.19\nQTY\n1\nTotal(incl.tax)\n50\nDescription\nMi Smart LED Desk Lamp 1s White\nGoodsID: 23578\nHSNCODE: 94052010\nMRP\n2999\nCGST%\n9%\nSGST %\n9%\nCGST\n221.11\nSGST\n221.11\nQTY\n1\nTotal(incl.tax)\n2899\nSUB TOTAL:\nTotal GST Tax:\nTotal IGST:\nTotal SGST:\nTotal CGST:\nMRP(INCL GST TAX):\nTotal(INCL GST TAX):\nTCS:\nMI EXCHANGE:\nDISCOUNT:\nGRAND TOTAL:\nPAYMENT:\nCARD:\nProcessing Fee:\n9706.96\n1740.00\n0.00\n870.52\n870.52\n14498.00\n11448.00\n0.00\n0.00\n-3050.00\n11448.00\n11448.00\n0.00\nThis is a computer generated invoice, so no signature is required\nUnbox Gadgets Pvt Ltd\nH.No.2-56/2-33, Plot No. 1303,SY.No.11,Khanampet, Ayyappa Society, Madhapur, Hyderabad\nTerms and conditions:\n1. Product once sold will not be returned or exchanged Under any circumstance.\n2. Please visit nearby Authorised Service centre in case of DOA for authorization and replacement.\n3.Keep a copy of this invoice to claim any future serve on the product at our service centers.\n4.By making this purchase, you consent to the store sharing the information provided by you with Xiaomi Technology India\nPrivate Limited\n5.You consent to Xiaomi using this information to send you any promotional offers or benefits, to send you surveys or\nfeedback requests, or for any other reason related to your order.\n6.It is also highlighted that only active GSTINs are accepted by IRP portal for IRN generation. Thus, in case status of your\nGSTIN is cancelled or inactive at the time of issuance of invoice and your GSTIN is rejected by IRP portal, we shall not be\nable to issue B2B invoice with IRN and QR Code. In such spenarios, B2C invoice would be raised by us basis which you\nwould not be eligible to avail input tax credit\n(Unbox Gadgets Pvt Ltd is an authorized franchise holder of Mi products.)\n"
# vendorNames = ["big bazaar","burger king","croma","dominos","hamleys","hennes & mauritz","kakada ramprasad","kfc","lifestyle","luxe","marks & spencer","max","mi","miniso","mobitech creations","pantaloons","reliance digital","reliance trends","rmkv silks","starmark","shoppers stop","tanishq","tablez & toyz","westside","zara"]

# # text = (ocrTexts.replace("\n", " ")).lower()
# # print("text : ", text)
# # words = ['INVOICE', 'Inditex', 'Trent', 'Ltd', 'Ambience', 'Corporate', 'Office', 'Tower', 'Level', 'Ambience', 'CIN', 'GSTIN', 'Industrial', 'Time', 'Trans', 'TSP', 'CODE', 'SMC']
# # print()
# # print (">> : ", data_enrichment_util.find_similarity_from_corpus(words=words, corpusWords=common_util.read_configuration()["vendorNames"], top=5))


# df = pd.read_csv('/home/ritesh/OCR/icr-microservice/icrapp/tested_data.csv')
# print("df : ", df, df.columns)

# counts = {'yes':0, 'no':0}
# for index, row in df.iterrows():
# 	print()
# 	print()
# 	vendorName = row['vendorname']
# 	vendorNameArr = row['vendor.name']
# 	ocrTexts = row['ocrTexts']
# 	scores = row['vendor.name.scores']
# 	if pd.notnull(scores):
# 		scores = ast.literal_eval(row['vendor.name.scores'])
# 	else:
# 		scores = {}
# 	if pd.notnull(vendorNameArr):
# 		vendorNameArr = ast.literal_eval(row['vendor.name'])
# 	else:
# 		vendorNameArr = []
# 	vendorNameArr = [item for item in vendorNameArr if len(item) > 2]
# 	scores = data_enrichment_util.find_similarity_from_corpus(words=vendorNameArr, corpusWords=common_util.read_configuration()["vendorNames"], top=5)
# 	vendorNameStr = ''
# 	if len(scores.keys()) > 0:
# 		vendorNameStr = max(scores, key=scores.get)
# 	print("TRUE vendorName : ", vendorName)
# 	print("vendorNameStr : ", vendorNameStr)
# 	print("vendorNameArr : ", vendorNameArr, type(vendorNameArr))
# 	if vendorName == vendorNameStr:
# 		yesCount = counts['yes']
# 		counts.update({'yes':yesCount+1})
# 	else:
# 		noCount = counts['no']
# 		counts.update({'no':noCount+1})

# 	# print(">>> : ", data_enrichment_util.find_similarity_from_corpus(words=vendorNameArr, corpusWords=common_util.read_configuration()["vendorNames"], top=5))
# print("counts : ", counts)

# # {'yes': 158, 'no': 255}


#########

# ocrTexts = ocrTexts.replace("\n", " ")
# print("ocrTexts : ", ocrTexts)


# def find_vendorNames():
# 	try:
# 		vendorNameScores = {}

# 		ocrTexts = "TAX INVOICE/BILL OF SUPPLY\nBIG BAZAAR (FUTURE RETAIL LTD)\nLG-29, BIGBAZAAR PHOENIX MARKET CITY\nOPP TD BBMP OFFICE MAHADEVAPURA-BLR 48\nTel No. - 08088420130/1800 266 2255\nFor Koryo : 18005725555/00033166512\nGST TIN:29AADCB1093N1ZC W.E.F 01.07.2017\nCIN NO:151909HH2007PLC268269\nITEM DESC\nHSN LOM\nQTY DISC AMT NET AMT\nCGSTX SGST\nR6\n198.00\n2.5\n0.00\n2.5\n30.00\n110.00\n0.00\n149.00\n0.00\n50.00\n--------\n131.00-\nBOOOOO08FO\n129.00\nKH-KANKIES-POS, WHT\n6213 Pcs\nLOTTE CHOCO PI 3369\n1905 Рcs\nDisney Kitchen Set\n9503 Pos\nHERS CKS N CRM 33.69\n1806 Pos\nkitchen tools set of\n8215\nPos\nBIG1 A4 Note Book\n4820\nPcs\nBIG1 A4 Note Book\n4820 Pcs\nNI.GR PNUT BAR 1000\n2106 Pcs\nPOSTER COLOR 14\n3213\n2013\nPos\nHM UTL PLN CL 20X20\n4202 Pcs\nPersnl Acc Insurance\n9971 PCS\nSPECIAL BENEFIT\n9971 Рcs\nSUBTOTAL\n100.00\n0.00\n0.00\n6\n100.00\n6\n11.67-\n2.5\n0.00\n9\n0.00\n23.33\n%\n6\n1\n2.5\n1\n9\n1\n6\n-1\n9\n-1\n9\n195.00\n19.00\n2.36\n0.00\n9\n0.00\n9\n2.36-\n973.33\nTOTAL\nREWARD\nAXIS\n973.33\n558.75\n414.58\nYour Mobile Number\n9591520163\nHas Been Registered\nwith Big Bazaar\nPIECES PURCHASED: 11 DISC ITEMS: 4\nTOTAL SAVING: 322.67\nGST\nCGST\nSGST\nBASE AMT - TAX AMT\n866.09 53.61\nB66.09 53.61\nTax Invoice Number\n4993015000025172\nAuth Sign\nCH:502594 Vijay\nTILL NO.15 MEMO ND.0025172 Tr:21514\nSt: 4983 23/09/21 16:05\nNet Amount is inclusive of all taxes\nTotal Savings add to discount over MRP\nand additional Promotions.\nNow also shop online\n@shop.bigbazaar.com\nGet Free Home Delivery\non orders over Rs.500\n"
# 		ocrTexts = ocrTexts.replace("\n", " ")
		
# 		vendorNamesArr = common_util.read_configuration()["vendorNames"]

# 		for index, rows in enumerate(vendorNamesArr):
# 			count = 0
# 			if rows in ocrTexts.lower():
# 				count += 1
# 				vendorNameScores.update({rows:count})

# 		return vendorNameScores
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_malls')
# 		raise e

# find_vendorNames()


#########


# _path = common_util._get_path_constants(_dir='data')
# inputImagePath = _path['inputImagePath']
# ocrJsonPath = _path['ocrJsonPath']

# directoryName = "big_bazaar"
# fileName = "100003"
# imageFileExtension = ".jpeg"

# imageFilePath = inputImagePath+"/"+directoryName+"/"+fileName+imageFileExtension
# ocrJsonFilePath = ocrJsonPath+"/"+directoryName+"/"+fileName+".json"
# print("imageFilePath : ", imageFilePath)
# print("ocrJsonFilePath : ", ocrJsonFilePath)

# allPageData = common_util.read_json_file(ocrJsonFilePath)
# print("allPageData : ", allPageData)

# for index, pageData in enumerate(allPageData):
# 	if "full_text_annotation" not in pageData:
# 		raise
# 	if "text_annotations" not in pageData:
# 		raise

# 	fullTexts = pageData["full_text_annotation"]
# 	texts = pageData["text_annotations"]
# 	print()
# 	print()
# 	print()
# 	print("fullTexts : ", fullTexts)
# 	print()
# 	print()
# 	print("texts : ", texts)


#########

# mallStr = None
# mallsDict = {}

# # ocrTexts = "TAX INVOICE\nADITYA BIRLA FASHION AND RETAIL LIMITED\nPantalons Division\nFF & ST. PHOENIX PALASSIO MALL, Bonti Nega\nExtension,\nSector 7. Lucknow - 228010\nPhone: 8929001623\nCorporate Address:\nPiramal Nastya Corporate Park, Blog \"A\",\n4th & 5th Floor, LBS Road, Kuria\nMulbai-400070 Maharashtra, India\nCIN NO: L1810112007PLC233901\nGSTIN NO: DAAECP237ICIZN\nPAN: MAECP2371C\nRECEIPT NO:P414304121001148\nStore Id: P414 1111 P414304\nCashier : 373032\nDate 26-12-2021 Tine 16:50\nCashier Name: Ashutosh singh\nEAN CODE\nHSN\nTAX RATE\nOTY\nITEM NAM\n.\nWR\nVALUE\nDISC : DISC AMT\nNET_AMT\n650.00\n2901030368741 1.00 650.00\n33049110 LAKME-BODY CARE\n18.00\n800.00\n550.00\n800.00\n8901030817589 1.00\n33041000 LAKME LIP CARE\n18.00\nB00.00\n599.00\n8901030793974 1.00 599.00\n33049910 LAKME SKIN CARE\n18.00:\n599.00\n499.00\n499.00\n8906090490221 1.00\n33049990 SUGAR LIP CARE\n18.00:\n499.00\n999.00\n999.00\n8906090499699 1.00\n330499e0 SUGAR SKIN CARE\n18.000\n999.00\n7.00\n125\n1.00 7.00\n48194000 15*12-4.75 brown pla\n18.00\n7.00\nTotal\n3,554.00\n----\nTender\nUBI Card\n3,554.00\nTXN ref.no: P414-414304-164051736\n6851 L: 1\nRoundott Amount\n0.00\nIten(s) Purchased : 5.00\nItem(s) Returned: 0.00\nTax Details\nTAX TAXABLE AMT\nDEST 3.011.82\nSGST\n3,011.82\nRATE\n9.00\n9.00\nTAM AMOUNT\n271.07\n271.07\nFor any queries, please call\nCustomer Care-1800-103 7527\nJoin us on www.facebook.com/pantaloons,\nFor points balance SMS \"MYGC' to '575758\nNet Ant. Inclusive of applicable taxes.\nThis document is to be treated as tax\ninvoice to the extent of supply of\ntaxable gooxts and bill of supply to the\nextent of Bepted goods.\nSale Is Ex-show room\nThis is a computer Denerated involce &\nshould be treated as signed by an\nauthorised\nsignatory.\nNote: For buy Query / Suggestions, please\nmention on front side of the invoice\nrefer to the now registered oftice address\nP.1.0. TERMS & CONDITIONS\n"
# # ocrTexts = "R TAU\nAditya Birla Fashion and Retail Ltd.\n(Formerly known as\nPantaloons Fashion Reta Ltd.)\nai\nLOUIS PHILIPPE UNIT NO\nFIRST FLC\nR SECTOR 1 MONAGAR BROMBOE\nIX MARKETCITY\nLUCINOW226010) er crest.\nPhone-0522-6/89049\nReg office: piramal Agastya Corporate\nPark\nBuilding 'A', 4th and Sth Floor,\nunit No. 401, 403, 501, 502,\nL.B.S. Road, Kurla,\nMumbai -400070\nGSTIN NO: 09AAECP237) CAZN\nCIN NO:\nPAN: AAECP25710\nGenisice\nThithic\nCusty Name u BHESMEC BUNGU SRINATRA\nPAN NO\nGST Bill No: 137520.1121003772\nDate: 12/26/2021 1 Time: 13:25\nPRODUCT DTLS\nQTY\nRATE\nVALUE\n8905462423195 1 2,999.00 2,999.0\nLPSFMCLPX80429\n042\nFULL CUT AWAY PERFECT SHIRT 042 F : :\nHSNCODE 62052000\nTotal disc 43.31%\n-1,299.C\nNo. of produces\nTotaT MRP upper crest. 2,999.C\nsub total (Excl. of Tax) 1,517.&\nTax\n182.1\nDiscounts\n1,299.0\nTotal\n1,700.C\nTender\nInnoviti card\n1,700.0\nTXN ref.no: 13752-13752001-14193 1:1\nTotal Savings\n1,299.C\nGST Summary\nTAXCOMPONENT\nCGST\nSGST\nTAX % TAXBasis Total Am\n6.00 ,517.86 91.07\n6.00 1,517, 86 91.07\nComo hahaha\nTotal GST\nTes Personper finant.\nSales\nRizwan\n*1375201121003772\"\nsignature\nNo. of PH\nprin\n"
# # ocrTexts = "Philippe\nCOUIS PHILIPPE ONLIJ 17 IRST FLC\nLGION CUMTI WASIO Wor\nIX MARKETIT\nPhony 072 0789099\nReg officia Upwat Abdieyal corporate\nPark\nBuilding 'A', 4th and 5th Floor,\nUnit No. 401, 403, 501, 502,\nL.B.S. Road, Kurla,\nMumbai -400070\nGSTIN NO: 09AAECP2371CIZN\nCIN NO:\nPAN: AAECP23710\nTAQ Invoice\ncust. Peamer O Melide Singh\nCus PAN NO\nGST 61 NEP1373301€7100189\nDate: 12/26/2021 1 Time: 17:05\nPRODUCT DTLS QTY RATE\nVALUE\n8905462241508 1 8,999.00 8,999.C\nLPBZMRGHT74667\n104\nCOPY OF 104 : : 104\nHSNCODE 62033100\nகட்டபொக்காக\nPhilippe\nNo. of products\n1.0\nTotal MRP\nSub tota\n.\nTax\nbischdanes upper crest. 0.0\nTotal\n8,999.0\nTender\nInnoviti Card\n8,999.C\nTXN ref.no: 13752-13752001-142 14 L:1\nTotal savings\n0.0\nGST Summary\nTAXCOMPONENT TAX % TAXBasis Total An\nCGST\n6.00 8,034.82 482.09\nSGST\n6.00 8,034.82 482.09\nTotal GST\n964,18\nStoria\nSales\nDespois vires\nShilippe\n*1375201 121003789*\nsignature\n10\nof Print\n2\n"
# # ocrTexts = "மகம்\nPhilippe\nAditya Birla Fashion\nand Retail Ltd.\n(Formerly known as\nPantaloons Fashion retail Ltd.)\nLOUIS PHILIPPE UNIT NO. F-17 FIRST FLC\nR SECTOR -7 COMTI NAGARE STENSTON PHOE\nIX MARKETCITY\nphone\n0522-6789049\nReg Office : Pahat Aga's eyal corporate\nPark\nBuilding 'A', 4th and 5th Floor,\nUnit No. 401, 403, 501, 502,\nL.B.S. Road, Kurla,\nMumbai -400070\nGSTIN NO: 09AAECP2371cizn\nCIN NO:\nPAN: AAECP23710\nTay Invoice\ncust. Name: Obokst singh\nCust. NO\nGSTE TRANSP1975 10 1521608189\nDate: 12/25/2021 1 Time: 17:05\nPRODUCT DTLS QTY RATE VALUE\n8905462241508 1 8,999.00 8,999.0\nLPBZMRGHT74667\n104\nCOPY OF 104 : : 104\nHSNCODE 62033100\nPhilippe\nNO\nsub toa xeradabrera\nNo. of Products\n1.0\nMRP\n,999.C.\nFax)\n384.8\n964.1\nDiscounts upper crest. 0.0\nTotal\n8,999.0\nTender\nInnoviti card\n8,999.C\nTXN ref.no: 13752-13752001-14214 L: 1\nTotal savings\n0.C\nGST summary\nTAXCOMPONENT TAX % TAXBasis Total An\nCGST\n6.00 8,034.82 482.09\nSGST\n6.00 8,034.82 482.09\nTotal GST\n964.18\nsales\npersonis virenare\nScopri Bebelippe\n10DL BIBI\n*1375201 121003789*\nsignature\nNo. of Print\n: 2\n"
# # ocrTexts = "no\nSecond FIDE\nknow-226010\nwearepeppermint in\nTo F NO! 1800-212-1984\nGTIN: DOMAECP32061\nCIN: 010101N2007PTC129420\nTax Invoice / Bill of supply\nReceipt No.\n1003987\nDate\n26-12-2021\nCustomer\nSONAM\nPhone\n9889329707\nLoyalty Points 4\nItem\nHSN\nDescription\nDise\nRSP Qty\nMRP\nTotal Tax\n1399.00\n8905385071800 Top\n0\n30.00 979.30 1\n979.30 S5\n8905385069272 Top\n1299.00\n0\n30.00 909.30 1 909.30 S5\n8905385068121 Top\n1349.00\nO\n30.00 944.30 1 944.30 S5\n8905385070278 Jacke 1699.00\n0\n30.00 1189.30 1 1189.30 s12\nSub Total\nGST\nNet Amount\n26-12-2021\n262.32\n4022.00\nPaid By: Cash\nTotal Savings:\nSales Person:\n4022.00\n3759.68\n0\nTax Details\nTax Desc\nTaxable\nS5 CGST 2.58 2698.00\nS12 CGST 68 61.88\nS5 SGST 2.5 2698.00\nS12 SGST 68 1061.88\nTotal Tax\nTax\n67.45\n63.71\n67.45\n63.71\n262.32\nThank You for shopping With Us\nMerchandise can be exchanged\nwithin 30 days from the date of\npurchase provided the merchandise\nis unused and in saleable\ncondition, along with original\nproduct tag and invoice as proof\nof purchase.\nDue to implementation of GST,\nsuch exchange is permitted only\n"
# # ocrTexts = "IA MARKET\nPhilippe\nLOUTO PRITIS UNIT WOT17 FINT FLC\nPEGION MTI WAGOWO Wor\navis\nPhon0922 9789099\nReg offlidiar p-pilar Ageleyal corporate\nPark\nBuilding 'A', 4th and 5th Floor,\nUnit No. 401, 403, 501, 502,\nL.B.S, Road, Kurla,\nMumbai -400040\nGSTIN NO: 09AAECP2371CIZN\nCIN NO:\nPAN: AAECP23710\nJAQ Invoice\nCust. Naller mobile Bagh\nCus PAN NO\nGST Napp/1011100189\nDate: 12/26/2021 1 Time: 17:05\nPRODUCT DTLS QTY RATE VALUE\n8905462241508 1 8,999.00 8.999.C\nLPBZMRGHT74667 104\nCOPY OF 104: 104\nHSNCODE 62033100\nNo. of products\n1.0\nTotal MRP\n999.c\nSub tota consisteradhit\nKUA.\nTax\n-964.1\nDiscounts upper crest. 0.0\nTotal\n8.999.C\nTender\nInnoviti card\n8,999.C\nTXN ref.no: 13752-13752001-14214 1:1\nTotal savings\n0.C\nGST Summary\nTAXCOMPONENT TAX % TAXBasis Total Am\nCGST\n6.00 8,034.82 482.09\nSGST\n6.00 8.034.82 482.09\nTotal GST\n964.18\nLouis SA helippe\nSales\nDespois\n*1375201 121003789*\nsignature\n10\nof Print\n2\n"
# ocrTexts = "Aditya Birla Fashion and Retail Ltd.\n(Formerly khown as\nPantaloon Fusion Roca Ltd.)\nLOUIS PHSUPPE UNIT NO BST FLC\nR SECTOR 1 ANINAGAR\nBOY 2010\nIX MARKETCITY\nLUCKNOW220019) er crest.\nPhone-0522-6789049\nReo office: Piramal Agastya Corporate\nPark\nBuilding 'A', 4th and Sth Floor,\nunit No. 401, 403, 501, 502,\nL.3.5, Road, Kurla,\nMumbai -400070\nGSTIN NO: 09AAECP2373E12N\nPAN: AAECP7719\nTas/mabice\nCust home u PBRESHEC BUNGU SRINATRA\n. PAN NO\nGST Bill No: 1375201121003772\nDate: 12/26/2021\nTime: 13:25\nCIN NO:\nPhilippines\nPRODUCT DTLS\nQTY\nRATE\nVALUE\n8905462423195 1 2,999.00 2,999.0\nLPSFMCL PX80429\n042\nFULL CUT AWAY PERFECT SHIRT 042 F: :\nHSNCODE 62052000\nTotal disc 43.31%\n-1,299.C\n\"Pogos Prilippe\nSub totai ERP. @of farsst.\nNo. of produces\nС\nTota MRP\n2,999.0\nTax) 1,517.2\nTax\n182.)\nDiscounts\n1,299.0\nTotal\n1,700.C\nTender\nInnoviti Card\n1,700.C\nTXN ref.no: 13752-13752001-14193 L:1\nTotal Savings\n1,299.C\nGST\nSummary\nTAXCOMPONENT\nCGST\nSGST\nTAX % TAXBasis Total Ant\n6.00 517.86 91.07\n6.00 T.517.86 91.07\nEd Sheeran\nTotal GST\naTeb Cersemper fiscant.\nSales Person\n#1375201 121003772\nSignature\nNO\nof\nPrint\nin\n"
# ocrTexts = ocrTexts.replace("\n", " ")


# mallsAddressArr = common_util.read_configuration()['icrParams']['mallsCollection']

# for index, rows in enumerate(mallsAddressArr):
# 	count = 0
# 	for address in rows['vendor.address']:
# 		address = address.lower()
# 		if address in ocrTexts.lower():
# 			count += 1
# 			print("address : ", address)
# 			mallsDict.update({rows['vendor.mall']:count})

# print("mallsDict : ", mallsDict)

# if len(mallsDict) > 0:
# 	mallStr = max(mallsDict, key=mallsDict.get)


#########



# def remove_dots(data):
# 	for key in list(data.keys()):
# 		if type(data[key]) is dict: data[key] = remove_dots(data[key])
# 		if '.' in key:
# 			data[key.replace('.', '\uff0E')] = data[key]
# 			del data[key]
# 	return data


# data = {'icrMode': 'icr', 'ocrData': {'mallId': '6', 'store_name': 'inc.5', 'retailer_id': '', 'bill_time': '', 'time_errorCode': '66', 'bill_date': '2022-01-05', 'date_errorCode': '62', 'bill_number': '64032029', 'invoice_number_errorCode': '46', 'bill_total': '2490.00', 'total_errorCode': '18', 'mobile_number': '', 'mobile_errorCode': '150', 'errorCode': '146,4,66,62,46,18,150,141', 'final_errorCode': 905}, 'icrData': {'metaFile': {'filename': '24896262270-225924-2022-1-4.jpeg', 'extension': '.jpeg', 'visualizationFilePath': '/home/ritesh/OCR/icr-microservice/data/008_visualize_test_enrich_data/2022_01_05_14_51_39_716944.png'}, 'icr': {'vendor': {'name': {'objs': ['Date'], 'scores': {'inc.5': 1}}, 'address': {'objs': ['Inc.', 'Shoes', 'Unit', 'First', 'Floor', 'Phoenix', 'Palassio', 'Lucknow', 'Mall', 'situated']}, 'phone_number': {'objs': ['05226789069', 'A76P2122-0005939']}, 'gst_number': {'objs': []}, 'email': {'objs': ['customercare@inc5shoes.com']}}, 'total': {'objs': ['2490.00', '2490.00', '2490.00', '2490.00', '2490.00']}, 'invoice_number': {'objs': ['64032029', '75008']}, 'date': {'dateValue': ['2022-01-05']}, 'time': {'timeValue': []}, 'ocrTexts': 'Inc. 5 Shoes Pvt Ltd\nUnit No F-62 on the First Floor, Phoenix Palassio, Lucknow Mall,\nsituated in Sector -7Gomti Nagar Extension, Lucknow\nHelpline No: 05226789069\nE-Mail: customercare@inc5shoes.com\nGSTIN : 09AADC13682G1ZF\nPAN NO: AADC13682G\nCIN No: U19120MH2013PTC249172\nWebsite - www.inc5shoes.co.in\nTax Invoice\nCash Memo No : S/05939/Jan-22\nDate : 04-Jan-22 03:38:43 PM\nTax Invoice No: A76P2122-0005939\nCustomer Mobile: 8960791384\nCustomer Name: Ms. niharika\nSI Product Style No\nDisc.\nAmount\nHSN Code Salesman Qty Rate Disc. %\nNo.\n64032029 SM:75008 1.00 2490.00 0.00\n1. INC.5 LADIES 500101\n0.00\n2490.00\n1.00\n2490.00\nTotal:\nRs. Two Thousand Four Hundred Ninety Only\nCard - Pinelab\nCustomer Paid:\nBalance Refund:\n2490.00\n0.00\n0.00\nTotal Sale :\nItem Discount:\nBill Discount :\nNet Payable :\n2490.00\n0.00\n0.00\n2490.00\nGST Summary\nDescription\nGST 18%\nTotals:\nTaxable\n2110.16\n2110.16\nIGST\n0.00\n0.00\nCGST\n189.92\n189.92\nSGST\n189.92\n189.92\nCESS\n0.00\n0.00\n1)Exchange within 15 days for unused pairs with price tag Intact 2)Complaints will not be entertained without cash\nmemo. 3)Three months (90 days) Period warranty for pasting & stitching. 4) In case of minor defects such as pasting o\nstitching problem, the product will be repaired and returned to the Guest.5)We are not responsible for the delay and\ndelivery is not taken by the Guest within 45 days. 6) This memo is required to be produced for taking delivery. 7)No\nguarantee for fancy footwear. 8)No cash refund. 9)No Service / Exchange on EOSS (End of Season Sale) Goods.\n*S/05939/Jan-22\nThank You Please visit Again\n', 'mall': 'Phoenix Palassio Lucknow'}}}

# print("before data : ", data)

# data = remove_dots(data)

# print("\n\nafter data : ", data)

# mongo_uri = common_util.read_configuration()['models']['mongo_uri']
# db_name = common_util.read_configuration()['models']['db_name']
# dbCollection = common_util.read_configuration()['models']['collection_api']

# print (">>> : ", models.insert_one_mongodb(mongo_uri=mongo_uri, db_name=db_name, collection=dbCollection, data=data))



#########



# import os
# import sys
# import cv2
# import numpy as np
# from scipy.ndimage import interpolation as inter

# def correct_skew(imageFilePath, saveImageFilePath, delta=0.1, limit=10):
# 	image = cv2.imread(imageFilePath)
# 	def determine_score(arr, angle):
# 		data = inter.rotate(arr, angle, reshape=False, order=0)
# 		histogram = np.sum(data, axis=1)
# 		score = np.sum((histogram[1:] - histogram[:-1]) ** 2)
# 		return histogram, score
# 	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 	blur = cv2.medianBlur(gray, 3)
# 	thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# 	scores = []
# 	angles = np.arange(-limit, limit + delta, delta)
# 	for angle in angles:
# 		histogram, score = determine_score(thresh, angle)
# 		scores.append(score)
# 	bestAngle = angles[scores.index(max(scores))]
# 	(h, w) = image.shape[:2]
# 	center = (w // 2, h // 2)
# 	M = cv2.getRotationMatrix2D(center, bestAngle, 1.0)
# 	rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
# 	print("bestAngle : ", bestAngle)
# 	cv2.imwrite(saveImageFilePath, rotated)


# dirPath = "/home/ritesh/dataset/2022_01_03/wetransfer_invoices-brand-select-citywalk_2022-01-03_1200/Invoices/PVR/"
# imageFileNames = ["98100951260002.jpg","98912330570003.jpg","98912330570004.jpg","pvr food bill.jpg"]
# saveImageFileNames = ["98100951260002_1.jpg","98912330570003_1.jpg","98912330570004_1.jpg","pvr food bill_1.jpg"]

# for imageFileName, saveImageFileName in zip(imageFileNames, saveImageFileNames):
# 	imageFilePath = dirPath+imageFileName
# 	saveImageFilePath = dirPath+saveImageFileName
# 	correct_skew(imageFilePath, saveImageFilePath)



#########

# dirPath = "/home/ritesh/OCR/retailers_dump/2022_01_13/"
# filePath = dirPath+'mallsCollection.json'


# def get_vendorNames_from_mall(mallId):
# 	try:
# 		mallsCollection = common_util.read_configuration()['icrParams']['mallsCollection']

# 		vendorNamesArr = []
# 		if mallId != None:
# 			for mallCollection in mallsCollection:
# 				for mallKey, mallValue in mallCollection.items():
# 					if mallKey == 'mallid':
# 						if mallId == mallValue:
# 							vendorNamesArr = mallCollection['vendorNames']
# 		else:
# 			for mallCollection in mallsCollection:
# 				for mallKey, mallValue in mallCollection.items():
# 					vendorNamesArr = vendorNamesArr + mallCollection['vendorNames']
# 		return vendorNamesArr
# 	except Exception as e:
# 		common_util.error_logs(e, 'get_vendorNames_from_mall')
# 		raise e


# def get_trained_mall_vendorNames(vendorNamesArr):
# 	try:
# 		df = pd.DataFrame(vendorNamesArr)
# 		df = df[(df['trained'] == 1)]
# 		return df
# 	except Exception as e:
# 		common_util.error_logs(e, 'get_trained_mall_vendorNames')
# 		raise e


# def get_alias_data_of_trained_mall_vendorNames(df):
# 	try:
# 		aliasList = df['alias'].tolist()
# 		vendorNamesArr = [singleAlias for multiAlias in aliasList for singleAlias in multiAlias]
# 		return vendorNamesArr
# 	except Exception as e:
# 		common_util.error_logs(e, 'get_alias_data_of_trained_mall_vendorNames')
# 		raise e


# def get_mall_vendorName_details(df, vendorNames):
# 	try:
# 		vendorNameId = None
# 		retVendorName = ''

# 		if len(vendorNames) < 1:
# 			return vendorNameId, retVendorName

# 		df = pd.DataFrame([[vendorNameId, retVendorName, singleAlias, trained] for vendorNameId, retVendorName, alias, trained in df.itertuples(index=False) for singleAlias in alias], columns=df.columns)

# 		vendornamesGroup = df.groupby(['vendorNameId'])
# 		for vendornameId, vendornameDf in vendornamesGroup:
# 			vendornames = vendornameDf['alias'].tolist()
# 			if set(vendornames) == set(vendorNames):
# 				vendorNameId = int(vendornameDf['vendorNameId'].values[0])
# 				retVendorName = str(vendornameDf['retVendorName'].values[0])
# 		if vendorNameId != None and retVendorName != "":
# 			return vendorNameId, retVendorName

# 		if len(vendorNames) == 1:
# 			foundDf = df.loc[df['alias'].isin(vendorNames)]
# 			if len(foundDf) == 1:
# 				vendorNameId = int(foundDf['vendorNameId'].values[0])
# 				retVendorName = str(foundDf['retVendorName'].values[0])
# 			if vendorNameId != None and retVendorName != "":
# 				return vendorNameId, retVendorName
		
# 		if len(vendorNames) > 1:
# 			longestLengthVendorName = max(vendorNames, key=len)
# 			foundDf = df.loc[df['alias'].isin([longestLengthVendorName])]
# 			if len(foundDf) == 1:
# 				vendorNameId = int(foundDf['vendorNameId'].values[0])
# 				retVendorName = str(foundDf['retVendorName'].values[0])
# 			if vendorNameId != None and retVendorName != "":
# 				return vendorNameId, retVendorName
			
# 			shortestLengthVendorName = min(vendorNames, key=len)
# 			foundDf = df.loc[df['alias'].isin([shortestLengthVendorName])]
# 			if len(foundDf) == 1:
# 				vendorNameId = int(foundDf['vendorNameId'].values[0])
# 				retVendorName = str(foundDf['retVendorName'].values[0])
# 			if vendorNameId != None and retVendorName != "":
# 				return vendorNameId, retVendorName

# 		return vendorNameId, retVendorName
# 	except Exception as e:
# 		common_util.error_logs(e, 'get_mall_vendorName_details')
# 		raise e




# def find_malls_vendorNames(vendorNames):
# 	try:
# 		vendorNameId, retVendorName = None, ''
		
# 		# mainDict = find_malls(mainDict)
# 		# mallId = mainDict['mallid']
# 		mallId = None

# 		if mallId != None:
# 			vendorNamesArr = get_vendorNames_from_mall(mallId)
# 			df = get_trained_mall_vendorNames(vendorNamesArr)
# 			vendorNamesArr = get_alias_data_of_trained_mall_vendorNames(df)
# 			mainDict = find_vendorNames(mainDict, vendorNamesArr, top=5)
# 			vendorNames = mainDict['vendor']['name']['scores']
# 			vendorNameId, retVendorName = get_mall_vendorName_details(df, vendorNames)
# 			mainDict['vendor']['name']['retVendorName'] = retVendorName
# 		else:
# 			vendorNamesArr = get_vendorNames_from_mall(mallId)
# 			df = get_trained_mall_vendorNames(vendorNamesArr)
# 			vendorNamesArr = get_alias_data_of_trained_mall_vendorNames(df)
# 			vendorNamesArr = sorted(set(vendorNamesArr))
# 			print("vendorNamesArr : ", vendorNamesArr)
# 		# 	mainDict = find_vendorNames(mainDict, vendorNamesArr, top=5)
# 		# 	vendorNames = mainDict['vendor']['name']['scores']
# 		# 	vendorNameId, retVendorName = get_mall_vendorName_details(df, vendorNames)
# 		# 	mainDict['vendor']['name']['retVendorName'] = retVendorName
# 		# return mainDict
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_malls_vendorNames')
# 		raise e




# # vendorNames = {'lifestyle': 1}
# # vendorNames = {'lifestyle': 1, 'max': 1}
# # vendorNames = {'bath&body works':1}
# # vendorNames = {'mac': 1, 'marks and spencer': 1}
# # vendorNames = {'hamleys': 1, 'max': 1}
# # vendorNames = {'lifestyle': 1, 'uspa': 1}
# # vendorNames = {}
# # vendorNames = {'bata': 1, 'mac': 1}
# vendorNames = {'hazelnut factory': 1}


# find_malls_vendorNames(vendorNames)


#########


# _path = common_util._get_path_constants(_dir='data')
# print("_path : ", _path)

# inputMediaPath = _path['inputMediaPath']
# inputImagePath = _path['inputImagePath']
# ocrJsonPath = _path['ocrJsonPath']
# ocrDfPath = _path['ocrDfPath']
# ocrDfFormatPath = _path['ocrDfFormatPath']
# ocrDfFormatLabelPath = _path['ocrDfFormatLabelPath']


# # inputMediaPath = inputMediaPath
# # inputMediaPath = inputImagePath
# # inputMediaPath = ocrJsonPath
# # inputMediaPath = ocrDfPath
# # inputMediaPath = ocrDfFormatPath
# inputMediaPath = ocrDfFormatLabelPath

# print("inputMediaPath : ", inputMediaPath)

# mediaFilePaths = common_util.get_files_from_directory_subdirectory(dirPath=inputMediaPath)
# for i, filePath in enumerate(mediaFilePaths):
# 	print()
# 	print()
# 	# print("File {} : {}".format(i, filePath))
# 	directoryName, file, fileName, fileExtension = common_util.get_file_info(filePath)
# 	print("{} : {}, {}, {}, {}, {}".format(i, filePath, directoryName, file, fileName, fileExtension))

# 	oldFileName = fileName
# 	newFileName = '0'+fileName
# 	print("fileName : ", oldFileName, newFileName)

# 	oldFilePath = inputMediaPath+"/"+directoryName+"/"+oldFileName+fileExtension
# 	newFilePath = inputMediaPath+"/"+directoryName+"/"+newFileName+fileExtension
# 	print("oldFilePath : ", oldFilePath)
# 	print("newFilePath : ", newFilePath)
# 	os.rename(oldFilePath, newFilePath)



#########


# mongo_uri = "mongodb://localhost:27017/"
# db_name = "icr"
# dbCollection = "icr_api"


# icrOutputList = models.find_mongodb(mongo_uri=mongo_uri, db_name=db_name, collection=dbCollection)
# print("icrOutputList : ", icrOutputList, len(icrOutputList))


# for index, singleRecord in enumerate(icrOutputList):
# 	print()
# 	print("index : ", index)
# 	print("singleRecord : ", singleRecord, type(singleRecord))

# 	_id = singleRecord['_id']
# 	bill_number = ''
# 	if 'ocrData' in singleRecord.keys():
# 		if 'bill_number' in singleRecord['ocrData'].keys():
# 			bill_number = singleRecord['ocrData']['bill_number']

# 			new_bill_number = bill_number+str(index)
# 	print("_id : ", _id)
# 	print("bill_number : ", bill_number)
# 	print("new_bill_number : ", new_bill_number)

# 	mycollection.find_one_and_update({"_id": mongo_id}, {"$set": {"newfield": "abc"}})


#########

# inputMediaPath = "/home/ritesh/dataset/2022_01_28/SCW_all"

# inputMediaPath = inputMediaPath

# print("inputMediaPath : ", inputMediaPath)

# directoryNames = []

# mediaFilePaths = common_util.get_files_from_directory_subdirectory(dirPath=inputMediaPath)
# for i, filePath in enumerate(mediaFilePaths):
# 	print()
# 	print()
# 	# print("File {} : {}".format(i, filePath))
# 	directoryName, file, fileName, fileExtension = common_util.get_file_info(filePath)
# 	# print("{} : {}, {}, {}, {}, {}".format(i, filePath, directoryName, file, fileName, fileExtension))
# 	if directoryName not in directoryNames:
# 		directoryNames.append(directoryName)

# print("directoryNames : ", directoryNames)


# vendorImageFilePaths = {}

# for i, filePath in enumerate(mediaFilePaths):
# 	directoryName, file, fileName, fileExtension = common_util.get_file_info(filePath)
# 	if directoryName not in list(vendorImageFilePaths.keys()):
# 		vendorImageFilePaths[directoryName] = []
# 		if filePath not in vendorImageFilePaths[directoryName]:
# 			vendorImageFilePaths[directoryName].append(filePath)
# 	else:
# 		if filePath not in vendorImageFilePaths[directoryName]:
# 			vendorImageFilePaths[directoryName].append(filePath)

# for vendor, vendorImageFilePathList in vendorImageFilePaths.items():
# 	print()
# 	print()
# 	print(vendor, len(vendorImageFilePathList))
# 	for index, vendorImageFilePath in enumerate(vendorImageFilePathList):
# 		directoryName, file, fileName, fileExtension = common_util.get_file_info(vendorImageFilePath)
# 		oldFileName = fileName
# 		count = "%02d"%(index+1)
# 		newFileName = '16'+'000'+count
# 		oldFilePath = inputMediaPath+"/"+directoryName+"/"+oldFileName+fileExtension
# 		newFilePath = inputMediaPath+"/"+directoryName+"/"+newFileName+fileExtension
# 		print(oldFilePath, " to ", newFilePath)
# 		os.rename(oldFilePath, newFilePath)

#########

# vendorNamesArr = {'barista', 'tommy hilfiger', 'subway', 'the nut lounge', 'estee lauder', 'soch', 'shoppers stop', 'moti mahal', 'kakada ramprasad', 'rmkv silks', 'jack', 'luxe', 'one plus', 'mobitech creations', 'mad over donuts', 'xiaomi', 'puma', 'hp', 'nykaa', 'starbucks', 'bath&body works', 'senco gold', 'zara', 'united colors of benetton', 'max', 'miniso', 'timezone', 'asia seven express', 'jo malone london', 'inox', 'vero moda', 'pizza hut', 'tanishq', 'crocs', 'clinique', 'sephora', 'adidas', 'cafe coffee tree', 'kfc', 'tablez & toyz', 'lifestyle', 'show off', 'under armour', 'nautica', 'bobbi brown', 'vaango', 'bata', 'punjab grill', 'home centre', 'sunglass hut', 'raymond', 'the chocolate room', 'home stop', 'choco fountain', 'dosa planet', 'mohanlal sons', 'burger king', 'skechers', 'hazelnut factory', 'crossword', 'hp it world', 'house of candy', 'marks and spencer', 'the body shop', 'house of liquer', 'uspa', 'allen solly', 'inc.5', 'mothercare', 'malabar gold & diamonds', 'milkshake and co', 'westside', 'unicorn', 'hennes & mauritz', 'calvin klein', "kareem's", 'mac', 'starmark', 'hamleys', 'mochi', 'pantaloons', 'reliance digital', 'the big grill', 'hush puppies', 'dominos', 'wow momo', 'ni hao', 'shizusan', 'much more', 'louis philippe', 'market ninety nine', 'jones', 'heads up for tails', 'big bazaar', 'croma', 'reliance trends', 'funcity', 'jockey', 'go colors'}
# ocrTexts = "Tax Invoice ADITYA BIRLA FASHION AND RETAIL LIMITED Allen Solly Allen Solly Unit No. F 38A, Phoenix Market City No 142, Velacherry Main Road 600042 Chennai TN IN, India GSTIN No. 33AAECP2371C1ZW Company PAN: AAECP23710 Corporate Address: Aditya Birla Fashion and Retail Limited, Piramal Agastya Corporate park, Building A, 4th 5th Floor, Unit No. 401, 403, 501, 502, L.B.S Road, Kurla, Mumbai 400070 CIN: L18101 MH2007PLC233901 Customer Name: Praveen Customer No.: 9362626575 RECEIPT NO.: 3452601121000957 Store ID: 34526 Till: 34526001 03-10-2021 20:44 Cashier ID: 000011 Cashier Name: Manager 1 MRP DISC% DISC_AMT NET_AMT ITEM_NAME EAN_CODE HSN QTY TAX_RATE TAX ANTI FOGGING MASK 000 : : 000 8905376953337 61031100 1 CGST (2.50%) 16.64 SGST (2.50%) 16.64 MASK 010 : : 010 89053768 96924 62104090 1 CGST (2.50%) 9.50 SGST (2.50%) 9.50 699.00 699.00 399.00 399.00 Sub Total 1045.72 TAX RATE CGST SGST TAXABLE AMT 1045.71 1045.71 2.50% 2.50% TAX AMOUNT 26.14 26.14 Total 1098.00 Tender HDFC Reco Transaction ref. no. Item Purchased 1098.00 34526-34526001-21038 L: 1 2 For any queries, please call Customer Care 18004253050 This document is to be treated as tax invoice to the extent of supply of taxable goods and bill of supply to the extent of supply of exempted goods Sale is Ex-showroom This is a computer generated invoice & should be treated as signed by an authorized signatory Note : For any query / Suggestion, please refer to new registered office address mentioned on front side of the invoice. 3452601121000957 NAMASTE ! ! "
# ocrTexts = 'Solly\nAditya Birla Fashion and Retai\n(Formerly known as 744\nPantaloons Fashion & Retai Ltd.)\nAllen solly Unit No. F 38A, Phoenix Ma\nrket city No 142, Velacherry Main Road\nChennai-600042\nphone-044-48680169\nReg office: 701-704.8 7th Floor,\nSkyline Icon Business Park,\n86-92 off Andheri-Kurla Road,\nMaro? village, Andheri East,\nMumbai, Maharashtra-400059\nGSTIN NO: 33AAECP2371C1zw\nCIN NO: L18101MH2007 PLC233901\nPAN: AAECP23710\nTax Invoice\nCust. Name : sandya\nCust. PAN NO\nGST Bill No: 345260 1120001693\nDate:3/13/2021, 12 Time: 16.44\nPRODUCT DEL\nen Sony\n8905376101646 1 1,299.00 1,299400\nABSFESPFA65110 Est00414\nDENIM SNAP BUTTON SHIRT 004 :\n: 004\nHSNCODE 61091000\n8905209946550 1\n699.00 699.00\nABKCERGFA83919\n004\nBASIC CREW NECK HALF SLEEVE TSHIRT 004\nHSNCODE 61091000\nNo. of Products\nTotal MRP\nSub total (excl. of Tax)\nTax\nDiscounts\nTotal\n2.00\n1,998.00\n1,825.54\n172.46\n0.00\n1,998.00\nTender\nInnoviti Card\nTotal savings\n1,998.00\n0.00\nGST\nSummary\nTAXB\nTAXCOMPONENT\nCGST\na\nAnou\n1 159\n12:50 685.\n6.00 159482\n2.50% 665\n69512\n16.64\n69.59\n16.64\nSGST\nTotal GST\n172.46\n.\nSales Person\nPRAVEEN\n*3452601120001693\nsignature\nNo. of print : 1\n'

# ocrTexts = ocrTexts.replace("\n", " ")

# def count_occurrences(word, sentence):
# 	return sentence.count(word)

# vendorNameScores = {}
# # for index, row in enumerate(vendorNamesArr):
# # 	print()
# # 	print()
# # 	print("row : ", row)
# # 	# count = 0
# # 	if row in ocrTexts.lower():
# # 		print("hereee")
# # 	# 	count += 1
# # 	# 	vendorNameScores.update({row:count})


# for index, row in enumerate(vendorNamesArr):
# 	# print()
# 	# print()
# 	# print("row : ", row)
# 	counts = count_occurrences(row, ocrTexts.lower())
# 	if counts > 0:
# 		vendorNameScores.update({row:counts})
# print("vendorNameScores : ", vendorNameScores)

#########

# def find_malls(mallName, mainDict):
# 	try:
# 		mallStr = None
# 		mallId = None
# 		mallsDict = {}
# 		mainDict['mall'] = mallStr
# 		mainDict['mallid'] = mallId

# 		ocrTexts = mainDict['ocrTexts']
# 		ocrTexts = ocrTexts.replace("\n", " ")

# 		mallsAddressArr = common_util.read_configuration()['icrParams']['mallsCollection']

# 		for index, rows in enumerate(mallsAddressArr):
# 			mallAddressCount = 0
# 			mall = rows['mall']
# 			mallAddress = rows['address']
# 			for index, address in enumerate(mallAddress):
# 				count = count_occurrences(address, ocrTexts.lower())
# 				if count > 0:
# 					mallAddressCount += 1
# 					mallsDict.update({mall:mallAddressCount})

# 		if len(mallsDict) > 0:
# 			mallStr = max(mallsDict, key=mallsDict.get)

# 		for index, rows in enumerate(mallsAddressArr):
# 			for mallKey, mallValue in rows.items():
# 				if mallKey == 'mall':
# 					if mallValue == mallStr:
# 						mallId = rows['mallid']

# 		if mallStr != None:
# 			mainDict['mall'] = mallStr

# 		mallName = int(mallName)
# 		if mallName == mallId and mallId != None:
# 			mainDict['mallid'] = mallId

# 		return mainDict
# 	except Exception as e:
# 		common_util.error_logs(e, 'find_malls')
# 		raise e

# mallName = 1
# mainDict = {'vendor': {'name': {'index': [8, 9], 'objs': ['Allen', 'Solly'], 'pos': [[483, 139, 534, 154], [546, 140, 596, 155]], 'lineNumber': [3, 3]}, 'address': {'index': [12, 13, 18, 19, 20, 24, 25, 26, 27], 'objs': ['Solly', 'Unit', 'Phoenix', 'Market', 'City', 'Velacherry', 'Main', 'Road', 'Chennai'], 'pos': [[193, 182, 245, 201], [257, 182, 292, 201], [410, 182, 473, 201], [485, 182, 539, 201], [552, 182, 588, 201], [675, 182, 768, 201], [780, 182, 816, 201], [829, 182, 864, 201], [142, 218, 205, 233]], 'lineNumber': [4, 4, 4, 4, 4, 4, 4, 4, 5]}, 'phone_number': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}, 'gst_number': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}, 'email': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}}, 'total': {'index': [], 'objs': [], 'pos': [], 'lineNumber': []}, 'invoice_number': {'index': [95, 332], 'objs': ['3452601121000626', '3452601121000626'], 'pos': [[268, 506, 417, 520], [465, 1517, 614, 1532]], 'lineNumber': [14, 42]}, 'date': {'index': [103], 'objs': ['25-08-2021'], 'pos': [[144, 547, 234, 560]], 'lineNumber': [16], 'dateValue': ['2021-08-25']}, 'time': {'index': [], 'objs': [], 'pos': [], 'lineNumber': [], 'timeValue': []}, 'ocrTexts': 'Tax Invoice\nADITYA BIRLA FASHION AND RETAIL LIMITED\nAllen Solly\nAllen Solly Unit No. F 38A, Phoenix Market City No 142, Velacherry Main Road\n600042\nChennai\nTN\nIN, India\nGSTIN No. 33AAECP2371C1ZW\nCompany PAN: AAECP2371C\nCorporate Address:\nAditya Birla Fashion and Retail Limited, Piramal Agastya Corporate park, Building\nA, 4th - 5th Floor, Unit No. 401, 403, 501, 502, L.B.S Road, Kurla, Mumbai - 400070\nCIN: L18101MH2007PLC233901\nCustomer Name: Narayanan Ps\nCustomer No.: 9884950897\nRECEIPT NO.: 3452601121000626\nStore ID: 34526\nTill: 34526001\n25-08-2021 15:15\nCashier ID: 000011\nCashier Name: Manager 1\nHSN\nDISC%\nDISC_AMT\nNET_AMT\n46.51%\n1069.27\n1229.73\nITEM_NAME\nEAN_CODE\nQTY MRP\nTAX_RATE TAX\nSHIRT 040 F: : 040 : F\n8905209495959\n62059090 1 2299.00\nCGST (6.00%) 65.88 SGST (6.00%) 65.88\nbluff semi cuff away collar : : 042 : STF\n8905053850157\n62052000 1 1999.00\nCGST (6.00%) 57.28 SGST (6.00%) 57.28\nAS CARRY BAG 000 :: 000\n8905209513103\n48194000 1\n8.50\nCGST (6.00%) 0.00 SGST (6.00%) 0.00\n46.51%\n929.73\n1069.27\n100.00%\n8.50\n0.00\nSub Total\n2052.68\nTAX\nCGST\nSGST\nTotal\nTAXABLE AMT\n2052.68\n2052.68\nRATE\n6.00%\n6.00%\nTAX AMOUNT\n123.16\n123.16\n2299.00\nTender\nCash\nTransaction ref. no.\nItem Purchased\nTotal Savings\n2299.00\n34526-34526001 - 20352 L: 1\n3\n2007.50\nFor any queries, please call Customer Care - 18004253050\nThis document is to be treated as tax invoice to the extent of supply of taxable\ngoods and bill of supply to the extent of supply of exempted goods\nSale is Ex-Showroom\nThis is a computer generated invoice & should be treated as signed by an\nauthorized signatory\nNote : For any query / Suggestion, please refer to new registered office address\nmentioned on front side of the invoice.\n3452601121000626\nNAMASTE !!\n', 'icrModel': 'vendorModel'}
# mainDict = find_malls(mallName, mainDict)
# print("mainDict : ", mainDict)
#########


# def get_vendorNames_from_mall(mallId):
# 	try:
# 		mallsCollection = common_util.read_configuration()['icrParams']['mallsCollection']

# 		vendorNamesArr = []
# 		if mallId != None:
# 			for mallCollection in mallsCollection:
# 				for mallKey, mallValue in mallCollection.items():
# 					if mallKey == 'mallid':
# 						if mallId == mallValue:
# 							vendorNamesArr = mallCollection['vendorNames']
# 		else:
# 			for mallCollection in mallsCollection:
# 				for mallKey, mallValue in mallCollection.items():
# 					vendorNamesArr = vendorNamesArr + mallCollection['vendorNames']
# 		return vendorNamesArr
# 	except Exception as e:
# 		common_util.error_logs(e, 'get_vendorNames_from_mall')
# 		raise e

# def get_trained_mall_vendorNames(vendorNamesArr):
# 	try:
# 		df = pd.DataFrame(vendorNamesArr)
# 		df = df[(df['trained'] == 1)]
# 		return df
# 	except Exception as e:
# 		common_util.error_logs(e, 'get_trained_mall_vendorNames')
# 		raise e

# def get_alias_data_of_trained_mall_vendorNames(df):
# 	try:
# 		aliasList = df['alias'].tolist()
# 		vendorNamesArr = [singleAlias for multiAlias in aliasList for singleAlias in multiAlias]
# 		return vendorNamesArr
# 	except Exception as e:
# 		common_util.error_logs(e, 'get_alias_data_of_trained_mall_vendorNames')
# 		raise e

# mallId = None
# vendorNamesArr = get_vendorNames_from_mall(mallId)
# df = get_trained_mall_vendorNames(vendorNamesArr)
# vendorNamesArr = get_alias_data_of_trained_mall_vendorNames(df)
# vendorNamesArr = set(vendorNamesArr)
# vendorNamesArr = sorted(list(set(vendorNamesArr)))
# print("vendorNamesArr : ", vendorNamesArr, len(vendorNamesArr))

#########

# import shutil

# def rename_directory(sourceDir, destinationDir):
# 	try:
# 		if not os.path.exists(destinationDir):
# 			os.rename(sourceDir, destinationDir)
# 	except Exception as e:
# 		common_util.error_logs(e, 'rename_directory')
# 		raise e


# def copy_files_into_all(dirPath):
# 	try:
# 		mainDirPath = os.path.split((os.path.split(dirPath))[0])
# 		mainDir = mainDirPath[0]

# 		oldDirName = mainDirPath[1]
# 		newDirName = oldDirName+"_all"

# 		sourceDir = mainDir+"/"+oldDirName
# 		destinationDir = mainDir+"/"+newDirName

# 		rename_directory(sourceDir=sourceDir, destinationDir=destinationDir)
# 		return mainDir, oldDirName, newDirName
# 	except Exception as e:
# 		common_util.error_logs(e, 'copy_files_into_all')
# 		raise e


# def copy_files_from_all_to_origin(mainDir, newDirName, oldDirName):
# 	try:
# 		sourceDir = mainDir+"/"+newDirName
# 		destinationDir = mainDir+"/"+oldDirName

# 		files = common_util.get_files_from_directory_subdirectory(sourceDir, fileExtAllow=['.pt'])

# 		directoriesDict = {}
# 		for index, filePath in enumerate(files):
# 			fileDir, file = os.path.split(filePath)
# 			if fileDir not in list(directoriesDict.keys()):
# 				directoriesDict[fileDir] = [file]
# 			else:
# 				directoriesDict[fileDir].append(file)

# 		sourceFiles = []
# 		sourceDirFilePathDict = {}
# 		for pathDir, fileNames in directoriesDict.items():
# 			latestFile = common_util.get_latest_file_stored(pathDir)
# 			directoryName, file, fileName, fileExtension = common_util.get_file_info(latestFile)
# 			sourceDirFilePathDict.update({pathDir:file})
# 			sourceFiles.append(pathDir+"/"+file)

# 		destinationFiles = []
# 		destinationDirFilePathDict = {}
# 		for pathDir, fileName in sourceDirFilePathDict.items():
# 			key = destinationDir+pathDir.replace(sourceDir, "")
# 			destinationDirFilePathDict.update({key:fileName})
# 			destinationFiles.append(key+"/"+fileName)

# 		for pathDir, fileName in destinationDirFilePathDict.items():
# 			common_util.create_directory(pathDir)
# 		for sourceFile, destinationFile in zip(sourceFiles, destinationFiles):
# 			shutil.copyfile(sourceFile, destinationFile)


# 	except Exception as e:
# 		common_util.error_logs(e, 'copy_files_from_all_to_origin')
# 		raise e


# _path = common_util._get_path_constants(_dir='data')

# def default_model(_path):
# 	try:
# 		modelSavedPath = _path['modelSavedPath']
# 		mainDir, oldDirName, newDirName = copy_files_into_all(modelSavedPath)
# 		print("mainDir : ", mainDir)
# 		print("oldDirName : ", oldDirName)
# 		print("newDirName : ", newDirName)

# 		copy_files_from_all_to_origin(mainDir, newDirName, oldDirName)
# 	except Exception as e:
# 		common_util.error_logs(e, 'default_model')
# 		raise e

# def vendor_model(_path):
# 	try:
# 		modelVendorSavedPath = _path['modelVendorSavedPath']
# 		mainDir, oldDirName, newDirName = copy_files_into_all(modelVendorSavedPath)
# 		print("mainDir : ", mainDir)
# 		print("oldDirName : ", oldDirName)
# 		print("newDirName : ", newDirName)

# 		copy_files_from_all_to_origin(mainDir, newDirName, oldDirName)
# 	except Exception as e:
# 		common_util.error_logs(e, 'default_model')
# 		raise e

#########


# mainDict = {'23-02-2022': {'ocr': {1.0: {901: 57, 902: 17, 903: 1, 905: 64, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 1, 902: 0, 903: 0, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 24, 902: 45, 903: 1, 904: 2, 905: 15, 906: 82, 907: 0, 908: 0, 999: 0}}}, '24-02-2022': {'ocr': {1.0: {901: 78, 902: 19, 903: 2, 905: 58, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}}, 'icr': {1.0: {901: 37, 902: 53, 903: 1, 904: 1, 905: 32, 906: 55, 907: 0, 908: 0, 999: 0}}}, '25-02-2022': {'ocr': {1.0: {901: 66, 902: 26, 903: 1, 905: 54, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 41, 902: 51, 905: 20, 906: 68, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '26-02-2022': {'ocr': {1.0: {901: 146, 902: 82, 903: 6, 905: 82, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 1, 902: 0, 903: 0, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 62, 902: 102, 903: 3, 904: 3, 905: 29, 906: 153, 907: 0, 908: 0, 999: 0}}}, '27-02-2022': {'ocr': {1.0: {901: 186, 902: 75, 903: 3, 905: 92, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {902: 2, 901: 0, 903: 0, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 87, 902: 105, 905: 39, 906: 179, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '28-02-2022': {'ocr': {1.0: {901: 100, 902: 31, 903: 3, 905: 49, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 32, 903: 1, 905: 17, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 10, 902: 1, 903: 1, 905: 2, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 38, 902: 55, 903: 1, 905: 22, 906: 95, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 12, 902: 25, 903: 1, 904: 1, 905: 8, 906: 33, 907: 0, 908: 0, 999: 0}, 3.0: {901: 5, 902: 6, 903: 1, 904: 1, 905: 2, 906: 17, 907: 0, 908: 0, 999: 0}}}, '01-03-2022': {'ocr': {1.0: {901: 87, 902: 34, 903: 4, 905: 53, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 31, 902: 34, 903: 3, 905: 17, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 15, 902: 2, 905: 9, 999: 1, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}}, 'icr': {1.0: {901: 45, 902: 57, 903: 1, 904: 2, 905: 21, 906: 89, 907: 0, 908: 0, 999: 0}, 2.0: {901: 23, 902: 33, 904: 2, 905: 7, 906: 51, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 18, 902: 12, 905: 1, 906: 24, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '02-03-2022': {'ocr': {1.0: {901: 105, 902: 34, 903: 2, 905: 59, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 12, 903: 2, 905: 8, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 4, 905: 13, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 49, 902: 64, 903: 1, 904: 1, 905: 26, 906: 83, 907: 0, 908: 0, 999: 0}, 2.0: {901: 7, 902: 11, 905: 3, 906: 17, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 11, 902: 13, 905: 5, 906: 19, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '03-03-2022': {'ocr': {1.0: {901: 85, 902: 33, 903: 3, 905: 33, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 11, 902: 14, 905: 12, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 4, 905: 8, 902: 0, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 38, 902: 65, 903: 1, 905: 10, 906: 64, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 12, 905: 6, 906: 22, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 4, 902: 7, 905: 1, 906: 11, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '04-03-2022': {'ocr': {1.0: {901: 114, 902: 25, 903: 4, 905: 52, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 12, 902: 23, 903: 2, 905: 10, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 10, 902: 3, 903: 1, 905: 9, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 53, 902: 60, 903: 1, 904: 2, 905: 36, 906: 72, 907: 0, 908: 0, 999: 0}, 2.0: {901: 9, 902: 15, 905: 4, 906: 31, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 6, 902: 14, 904: 1, 905: 5, 906: 5, 903: 0, 907: 0, 908: 0, 999: 0}}}, '05-03-2022': {'ocr': {1.0: {901: 173, 902: 63, 903: 4, 905: 86, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 38, 905: 7, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 31, 902: 7, 903: 1, 905: 15, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 77, 902: 119, 903: 4, 904: 1, 905: 49, 906: 125, 907: 0, 908: 0, 999: 0}, 2.0: {901: 14, 902: 24, 905: 5, 906: 47, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 23, 903: 1, 904: 1, 905: 6, 906: 45, 907: 0, 908: 0, 999: 0}}}, '06-03-2022': {'ocr': {1.0: {901: 198, 902: 62, 903: 4, 905: 106, 999: 2, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 38, 902: 48, 903: 1, 905: 15, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 22, 902: 12, 905: 16, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 88, 902: 149, 903: 4, 904: 2, 905: 49, 906: 130, 907: 0, 908: 0, 999: 0}, 2.0: {901: 24, 902: 47, 904: 1, 905: 14, 906: 54, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 10, 902: 22, 903: 1, 905: 6, 906: 41, 904: 0, 907: 0, 908: 0, 999: 0}}}, '07-03-2022': {'ocr': {1.0: {901: 66, 902: 30, 905: 41, 999: 1, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 18, 902: 13, 903: 1, 905: 7, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 18, 902: 3, 905: 10, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 43, 902: 48, 905: 31, 906: 42, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 12, 905: 7, 906: 21, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 10, 902: 21, 905: 6, 906: 22, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '08-03-2022': {'ocr': {1.0: {901: 76, 902: 25, 903: 7, 905: 47, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 14, 902: 23, 905: 11, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 8, 902: 3, 905: 9, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 41, 902: 48, 903: 1, 905: 18, 906: 66, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 12, 902: 13, 905: 3, 906: 33, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 11, 902: 7, 905: 1, 906: 18, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '09-03-2022': {'ocr': {1.0: {901: 76, 902: 24, 903: 3, 905: 38, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 10, 902: 6, 905: 6, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 11, 902: 4, 905: 8, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 35, 902: 46, 903: 1, 905: 23, 906: 55, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 4, 902: 14, 904: 1, 905: 3, 906: 12, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 10, 902: 13, 905: 1, 906: 27, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '10-03-2022': {'ocr': {1.0: {901: 83, 902: 38, 903: 4, 905: 55, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 12, 902: 26, 903: 5, 905: 19, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 8, 902: 3, 905: 8, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 42, 902: 71, 903: 1, 904: 2, 905: 34, 906: 53, 907: 0, 908: 0, 999: 0}, 2.0: {901: 12, 902: 20, 904: 4, 905: 7, 906: 34, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 5, 902: 6, 905: 2, 906: 12, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '11-03-2022': {'ocr': {1.0: {901: 91, 902: 33, 903: 3, 905: 56, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 7, 902: 22, 903: 1, 905: 9, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 8, 905: 5, 902: 0, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 49, 902: 52, 903: 1, 904: 1, 905: 26, 906: 72, 907: 0, 908: 0, 999: 0}, 2.0: {901: 6, 902: 13, 905: 3, 906: 29, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 6, 902: 3, 905: 1, 906: 12, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '12-03-2022': {'ocr': {1.0: {901: 153, 902: 71, 903: 2, 905: 90, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 45, 902: 38, 903: 3, 905: 27, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 15, 902: 4, 903: 1, 905: 10, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 96, 902: 80, 903: 2, 905: 61, 906: 106, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 20, 902: 46, 903: 1, 905: 19, 906: 49, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 17, 904: 2, 905: 2, 906: 14, 903: 0, 907: 0, 908: 0, 999: 0}}}, '13-03-2022': {'ocr': {1.0: {901: 184, 902: 94, 903: 4, 905: 100, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 19, 902: 48, 905: 9, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 18, 902: 8, 905: 14, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 111, 902: 115, 903: 1, 904: 4, 905: 61, 906: 150, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 29, 904: 1, 905: 9, 906: 39, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 15, 902: 19, 904: 2, 905: 2, 906: 29, 903: 0, 907: 0, 908: 0, 999: 0}}}, '14-03-2022': {'ocr': {1.0: {901: 76, 902: 25, 903: 3, 905: 42, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 18, 902: 18, 903: 1, 905: 12, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 17, 902: 6, 905: 19, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 41, 902: 39, 903: 2, 904: 1, 905: 34, 906: 78, 907: 0, 908: 0, 999: 0}, 2.0: {901: 11, 902: 23, 903: 2, 905: 11, 906: 26, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 16, 902: 13, 905: 4, 906: 28, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '15-03-2022': {'ocr': {1.0: {901: 45, 902: 24, 905: 39, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 10, 902: 33, 903: 1, 905: 13, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 9, 902: 4, 905: 10, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 20, 902: 42, 903: 1, 904: 1, 905: 15, 906: 43, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 19, 904: 1, 905: 5, 906: 29, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 4, 902: 15, 906: 20, 903: 0, 904: 0, 905: 0, 907: 0, 908: 0, 999: 0}}}, '16-03-2022': {'ocr': {1.0: {901: 49, 902: 32, 903: 2, 905: 48, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 26, 903: 1, 905: 11, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 12, 902: 1, 905: 8, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 36, 902: 33, 903: 3, 904: 1, 905: 36, 906: 57, 907: 0, 908: 0, 999: 0}, 2.0: {901: 13, 902: 26, 903: 2, 905: 8, 906: 20, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 11, 902: 6, 904: 2, 905: 1, 906: 7, 903: 0, 907: 0, 908: 0, 999: 0}}}, '17-03-2022': {'ocr': {1.0: {901: 55, 902: 20, 903: 2, 905: 39, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 12, 902: 27, 905: 9, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 9, 902: 5, 905: 6, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 30, 902: 37, 903: 2, 905: 18, 906: 43, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 18, 903: 2, 905: 4, 906: 27, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 10, 902: 8, 904: 2, 905: 2, 906: 14, 903: 0, 907: 0, 908: 0, 999: 0}}}, '18-03-2022': {'ocr': {1.0: {901: 91, 902: 41, 905: 46, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 19, 902: 26, 905: 13, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 16, 902: 2, 905: 12, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 54, 902: 58, 903: 1, 904: 1, 905: 27, 906: 83, 907: 0, 908: 0, 999: 0}, 2.0: {901: 19, 902: 14, 905: 6, 906: 30, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 16, 903: 2, 905: 6, 906: 28, 904: 0, 907: 0, 908: 0, 999: 0}}}, '19-03-2022': {'ocr': {1.0: {901: 162, 902: 59, 903: 2, 905: 74, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 32, 902: 28, 903: 2, 905: 17, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 21, 902: 6, 905: 14, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 72, 902: 93, 903: 2, 904: 1, 905: 46, 906: 112, 907: 0, 908: 0, 999: 0}, 2.0: {901: 19, 902: 37, 904: 2, 905: 13, 906: 52, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 13, 902: 16, 905: 5, 906: 28, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '20-03-2022': {'ocr': {1.0: {901: 169, 902: 104, 903: 2, 905: 114, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 32, 902: 38, 903: 1, 905: 28, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 25, 902: 4, 905: 16, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 119, 902: 133, 903: 1, 904: 4, 905: 73, 906: 135, 907: 0, 908: 0, 999: 0}, 2.0: {901: 18, 902: 42, 905: 18, 906: 40, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 15, 904: 1, 905: 4, 906: 23, 903: 0, 907: 0, 908: 0, 999: 0}}}, '21-03-2022': {'ocr': {1.0: {901: 96, 902: 35, 903: 4, 905: 56, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 21, 902: 44, 905: 18, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 9, 905: 6, 902: 0, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 54, 902: 59, 903: 2, 904: 1, 905: 44, 906: 71, 907: 0, 908: 0, 999: 0}, 2.0: {901: 19, 902: 20, 905: 15, 906: 39, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 9, 902: 14, 904: 1, 905: 4, 906: 11, 903: 0, 907: 0, 908: 0, 999: 0}}}, '22-03-2022': {'ocr': {1.0: {901: 19, 902: 18, 905: 14, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 3, 902: 5, 905: 3, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 4, 905: 4, 902: 0, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 9, 902: 9, 905: 22, 906: 19, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 3, 902: 9, 905: 2, 906: 4, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 1, 902: 2, 905: 4, 906: 6, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '23-03-2022': {'ocr': {}, 'icr': {}}, '24-03-2022': {'ocr': {}, 'icr': {}}, '25-03-2022': {'ocr': {}, 'icr': {}}, '26-03-2022': {'ocr': {}, 'icr': {}}, '27-03-2022': {'ocr': {1.0: {901: 128, 902: 68, 903: 4, 905: 61, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 29, 902: 40, 903: 4, 905: 20, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 12, 902: 1, 905: 15, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 67, 902: 81, 903: 1, 904: 1, 905: 67, 906: 90, 907: 0, 908: 0, 999: 0}, 2.0: {901: 26, 902: 34, 903: 2, 905: 12, 906: 41, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 5, 903: 1, 905: 5, 906: 11, 904: 0, 907: 0, 908: 0, 999: 0}}}, '28-03-2022': {'ocr': {1.0: {901: 32, 902: 15, 905: 21, 999: 116, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 7, 902: 15, 903: 1, 905: 5, 999: 58, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 6, 902: 1, 905: 3, 999: 37, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}}, 'icr': {1.0: {901: 34, 902: 59, 904: 1, 905: 16, 906: 51, 903: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 31, 904: 1, 905: 7, 906: 16, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 21, 902: 16, 904: 1, 906: 20, 903: 0, 905: 0, 907: 0, 908: 0, 999: 0}}}, '29-03-2022': {'ocr': {1.0: {901: 49, 902: 30, 905: 26, 999: 66, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 9, 902: 10, 905: 8, 999: 20, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 4, 902: 1, 905: 3, 999: 9, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}}, 'icr': {1.0: {901: 58, 902: 31, 903: 1, 905: 25, 906: 63, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 9, 902: 23, 903: 1, 905: 9, 906: 19, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 6, 902: 6, 906: 10, 903: 0, 904: 0, 905: 0, 907: 0, 908: 0, 999: 0}}}, '30-03-2022': {'ocr': {1.0: {901: 71, 902: 36, 905: 44, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 20, 902: 14, 905: 11, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 6, 902: 3, 905: 3, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 45, 902: 35, 903: 4, 905: 25, 906: 60, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 11, 902: 17, 903: 3, 904: 2, 905: 8, 906: 24, 907: 0, 908: 0, 999: 0}, 3.0: {901: 2, 902: 3, 906: 13, 903: 0, 904: 0, 905: 0, 907: 0, 908: 0, 999: 0}}}, '31-03-2022': {'ocr': {1.0: {901: 63, 902: 35, 905: 47, 999: 27, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 13, 902: 32, 905: 7, 999: 3, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 9, 902: 1, 905: 8, 999: 5, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}}, 'icr': {1.0: {901: 51, 902: 43, 905: 40, 906: 46, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 6, 902: 23, 905: 8, 906: 26, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 9, 902: 8, 904: 1, 905: 4, 906: 5, 903: 0, 907: 0, 908: 0, 999: 0}}}, '01-04-2022': {'ocr': {1.0: {901: 66, 902: 31, 903: 1, 905: 36, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 11, 902: 23, 903: 1, 905: 8, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 13, 902: 2, 905: 18, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 40, 902: 45, 903: 4, 905: 25, 906: 44, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 14, 904: 1, 905: 9, 906: 14, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 10, 902: 15, 903: 1, 904: 1, 905: 5, 906: 19, 907: 0, 908: 0, 999: 0}}}, '02-04-2022': {'ocr': {1.0: {901: 136, 902: 73, 903: 2, 905: 76, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 28, 902: 31, 903: 1, 905: 14, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 11, 902: 3, 903: 1, 905: 18, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 76, 902: 91, 903: 3, 904: 1, 905: 65, 906: 101, 907: 0, 908: 0, 999: 0}, 2.0: {901: 21, 902: 28, 903: 4, 905: 10, 906: 28, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 8, 902: 15, 903: 2, 904: 1, 905: 18, 906: 22, 907: 0, 908: 0, 999: 0}}}, '03-04-2022': {'ocr': {1.0: {901: 105, 902: 64, 903: 6, 905: 74, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 32, 902: 40, 903: 4, 905: 21, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 17, 902: 2, 903: 1, 905: 22, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 70, 902: 70, 903: 3, 904: 2, 905: 50, 906: 111, 907: 0, 908: 0, 999: 0}, 2.0: {901: 31, 902: 40, 903: 1, 904: 1, 905: 21, 906: 54, 907: 0, 908: 0, 999: 0}, 3.0: {901: 17, 902: 17, 903: 3, 905: 11, 906: 17, 904: 0, 907: 0, 908: 0, 999: 0}}}, '04-04-2022': {'ocr': {1.0: {901: 52, 902: 27, 903: 4, 905: 46, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 8, 902: 21, 903: 1, 905: 2, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 5, 905: 11, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 29, 902: 46, 905: 27, 906: 58, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 10, 902: 12, 904: 1, 905: 8, 906: 23, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 13, 902: 10, 905: 5, 906: 12, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '05-04-2022': {'ocr': {1.0: {901: 65, 902: 38, 903: 1, 905: 38, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 22, 903: 1, 905: 9, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 7, 905: 3, 902: 0, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 36, 902: 42, 903: 1, 905: 33, 906: 79, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 4, 902: 11, 905: 9, 906: 44, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 2, 902: 6, 905: 3, 906: 2, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '06-04-2022': {'ocr': {1.0: {901: 37, 902: 53, 903: 3, 905: 36, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 10, 902: 43, 903: 1, 905: 3, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 7, 903: 2, 905: 4, 902: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 40, 902: 34, 903: 2, 905: 25, 906: 56, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 11, 902: 18, 904: 1, 905: 8, 906: 55, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 5, 902: 5, 903: 1, 905: 3, 906: 7, 904: 0, 907: 0, 908: 0, 999: 0}}}, '07-04-2022': {'ocr': {1.0: {901: 54, 902: 25, 903: 4, 905: 40, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 11, 902: 27, 903: 1, 905: 10, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 9, 902: 1, 905: 6, 999: 1, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}}, 'icr': {1.0: {901: 25, 902: 36, 903: 1, 905: 30, 906: 49, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 18, 905: 8, 906: 34, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 5, 902: 6, 905: 4, 906: 13, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '08-04-2022': {'ocr': {1.0: {901: 73, 902: 40, 905: 42, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 7, 902: 23, 903: 1, 905: 4, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 8, 905: 6, 902: 0, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 42, 902: 41, 903: 2, 905: 30, 906: 49, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 13, 902: 16, 903: 1, 905: 5, 906: 28, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 7, 902: 6, 905: 3, 906: 13, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '09-04-2022': {'ocr': {1.0: {901: 175, 902: 87, 903: 4, 905: 62, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 29, 902: 41, 903: 5, 905: 3, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 18, 902: 1, 903: 1, 905: 2, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 100, 902: 115, 903: 3, 904: 1, 905: 65, 906: 122, 907: 0, 908: 0, 999: 0}, 2.0: {901: 31, 902: 33, 903: 1, 905: 6, 906: 39, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 5, 902: 11, 903: 2, 904: 1, 905: 6, 906: 19, 907: 0, 908: 0, 999: 0}}}, '10-04-2022': {'ocr': {1.0: {901: 180, 902: 96, 905: 66, 999: 1, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 29, 902: 41, 903: 1, 905: 2, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 22, 902: 2, 903: 3, 905: 6, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 102, 902: 114, 903: 2, 905: 63, 906: 127, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 20, 902: 35, 903: 1, 905: 3, 906: 57, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 8, 902: 16, 904: 1, 905: 7, 906: 26, 903: 0, 907: 0, 908: 0, 999: 0}}}, '11-04-2022': {'ocr': {1.0: {901: 134, 902: 42, 903: 1, 905: 33, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 7, 902: 16, 905: 3, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 11, 902: 3, 903: 1, 905: 3, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 79, 902: 59, 905: 25, 906: 74, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 12, 902: 12, 903: 1, 905: 10, 906: 26, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 1, 902: 7, 905: 3, 906: 15, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '12-04-2022': {'ocr': {1.0: {901: 70, 902: 39, 903: 2, 905: 20, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 6, 902: 7, 905: 1, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 13, 902: 12, 903: 2, 905: 3, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 35, 902: 44, 903: 2, 905: 32, 906: 60, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 7, 902: 6, 905: 2, 906: 10, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 9, 902: 11, 903: 1, 904: 2, 905: 4, 906: 21, 907: 0, 908: 0, 999: 0}}}, '13-04-2022': {'ocr': {1.0: {901: 43, 902: 20, 903: 4, 905: 15, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 13, 902: 8, 903: 1, 999: 1, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 16, 902: 5, 905: 11, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 29, 902: 22, 903: 1, 905: 17, 906: 33, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 7, 902: 12, 906: 24, 903: 0, 904: 0, 905: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 7, 902: 12, 903: 1, 905: 7, 906: 26, 904: 0, 907: 0, 908: 0, 999: 0}}}, '14-04-2022': {'ocr': {1.0: {901: 129, 902: 56, 903: 1, 905: 32, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 22, 902: 18, 903: 1, 905: 5, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 17, 902: 4, 903: 2, 905: 5, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 63, 902: 69, 905: 51, 906: 89, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 12, 902: 21, 905: 8, 906: 29, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 13, 902: 9, 903: 1, 905: 4, 906: 20, 904: 0, 907: 0, 908: 0, 999: 0}}}, '15-04-2022': {'ocr': {1.0: {901: 132, 902: 60, 903: 5, 905: 55, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 14, 902: 23, 905: 3, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 19, 902: 2, 905: 5, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 69, 902: 95, 904: 1, 905: 55, 906: 82, 903: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 14, 902: 17, 903: 1, 905: 5, 906: 22, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 6, 902: 14, 903: 3, 905: 4, 906: 22, 904: 0, 907: 0, 908: 0, 999: 0}}}, '16-04-2022': {'ocr': {1.0: {901: 137, 902: 58, 903: 1, 905: 48, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 25, 902: 39, 905: 12, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 15, 902: 3, 905: 5, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 73, 902: 80, 903: 1, 904: 1, 905: 64, 906: 83, 907: 0, 908: 0, 999: 0}, 2.0: {901: 20, 902: 27, 903: 1, 905: 10, 906: 47, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 15, 902: 11, 905: 1, 906: 21, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '17-04-2022': {'ocr': {1.0: {901: 187, 902: 106, 903: 6, 905: 60, 999: 2, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 28, 902: 37, 903: 2, 905: 14, 999: 5, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 11, 902: 6, 903: 1, 905: 9, 999: 5, 904: 0, 906: 0, 907: 0, 908: 0}}, 'icr': {1.0: {901: 115, 902: 128, 903: 7, 905: 60, 906: 139, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 39, 902: 40, 904: 1, 905: 8, 906: 41, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 8, 902: 14, 904: 1, 905: 8, 906: 24, 903: 0, 907: 0, 908: 0, 999: 0}}}, '18-04-2022': {'ocr': {1.0: {901: 75, 902: 40, 903: 6, 905: 34, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 8, 902: 19, 903: 1, 905: 4, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 13, 902: 9, 903: 2, 905: 3, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 51, 902: 65, 904: 2, 905: 20, 906: 54, 903: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 10, 902: 19, 904: 1, 905: 7, 906: 26, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 6, 902: 21, 904: 1, 905: 4, 906: 24, 903: 0, 907: 0, 908: 0, 999: 0}}}, '19-04-2022': {'ocr': {1.0: {901: 44, 902: 33, 903: 4, 905: 20, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 12, 905: 3, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 17, 902: 2, 905: 4, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 33, 902: 56, 903: 1, 904: 1, 905: 18, 906: 5, 907: 0, 908: 0, 999: 0}, 2.0: {901: 15, 902: 23, 905: 5, 906: 24, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 9, 905: 5, 906: 10, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '20-04-2022': {'ocr': {1.0: {901: 43, 902: 16, 903: 1, 905: 12, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 3, 902: 8, 903: 0, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 5, 902: 0, 903: 0, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 25, 902: 42, 904: 1, 905: 17, 906: 16, 903: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 6, 902: 12, 905: 3, 906: 4, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 1, 902: 3, 903: 1, 905: 6, 906: 2, 904: 0, 907: 0, 908: 0, 999: 0}}}, '21-04-2022': {'ocr': {1.0: {901: 41, 902: 20, 903: 2, 905: 16, 999: 13, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 3, 902: 9, 903: 1, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 5, 902: 3, 905: 7, 999: 2, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}}, 'icr': {1.0: {901: 25, 902: 51, 904: 1, 905: 14, 906: 10, 903: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 6, 902: 16, 904: 2, 905: 3, 906: 8, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 4, 902: 9, 904: 1, 905: 3, 906: 6, 903: 0, 907: 0, 908: 0, 999: 0}}}, '22-04-2022': {'ocr': {1.0: {901: 47, 902: 29, 903: 3, 905: 16, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 13, 903: 0, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 15, 902: 1, 905: 4, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 33, 902: 36, 903: 1, 904: 1, 905: 24, 906: 13, 907: 0, 908: 0, 999: 0}, 2.0: {901: 10, 902: 23, 905: 9, 906: 6, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 13, 902: 4, 905: 1, 906: 8, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '23-04-2022': {'ocr': {1.0: {901: 120, 902: 59, 903: 5, 905: 35, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 14, 902: 31, 903: 2, 905: 4, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 16, 902: 6, 905: 6, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 75, 902: 102, 903: 1, 904: 1, 905: 50, 906: 33, 907: 0, 908: 0, 999: 0}, 2.0: {901: 22, 902: 54, 903: 1, 905: 9, 906: 24, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 16, 902: 10, 903: 1, 905: 2, 906: 12, 904: 0, 907: 0, 908: 0, 999: 0}}}, '24-04-2022': {'ocr': {1.0: {901: 169, 902: 68, 903: 8, 905: 53, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 32, 902: 39, 903: 3, 905: 10, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 23, 902: 5, 905: 4, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 88, 902: 157, 903: 2, 904: 1, 905: 64, 906: 34, 907: 0, 908: 0, 999: 0}, 2.0: {901: 37, 902: 77, 903: 1, 904: 2, 905: 20, 906: 30, 907: 0, 908: 0, 999: 0}, 3.0: {901: 3, 902: 11, 903: 1, 905: 3, 906: 34, 904: 0, 907: 0, 908: 0, 999: 0}}}, '25-04-2022': {'ocr': {1.0: {901: 69, 902: 28, 905: 33, 999: 14, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 27, 902: 30, 905: 1, 999: 1, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 3.0: {901: 7, 902: 2, 905: 6, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 38, 902: 56, 903: 3, 905: 39, 906: 21, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 26, 902: 60, 903: 1, 905: 10, 906: 25, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 4, 902: 7, 903: 1, 906: 13, 904: 0, 905: 0, 907: 0, 908: 0, 999: 0}}}, '26-04-2022': {'ocr': {1.0: {901: 69, 902: 39, 903: 4, 905: 21, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 5, 902: 9, 903: 1, 905: 1, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 8, 905: 5, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 47, 902: 64, 903: 1, 905: 42, 906: 24, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 20, 903: 2, 904: 1, 905: 5, 906: 9, 907: 0, 908: 0, 999: 0}, 3.0: {901: 14, 902: 11, 906: 8, 903: 0, 904: 0, 905: 0, 907: 0, 908: 0, 999: 0}}}, '27-04-2022': {'ocr': {1.0: {901: 58, 902: 21, 905: 21, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 6, 902: 15, 903: 0, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 19, 902: 4, 905: 4, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 40, 902: 46, 905: 34, 906: 10, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 5, 902: 14, 905: 6, 906: 7, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 6, 902: 8, 905: 4, 906: 9, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '28-04-2022': {'ocr': {1.0: {901: 42, 902: 30, 903: 1, 905: 9, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 9, 902: 12, 903: 1, 905: 1, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 9, 902: 2, 905: 10, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 31, 902: 42, 903: 3, 905: 18, 906: 8, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 13, 902: 24, 903: 1, 905: 5, 906: 11, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 7, 902: 3, 905: 5, 906: 14, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '29-04-2022': {'ocr': {1.0: {901: 43, 902: 57, 903: 5, 905: 28, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 19, 902: 24, 903: 0, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 10, 902: 5, 903: 1, 905: 2, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 35, 902: 61, 903: 1, 905: 52, 906: 16, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 17, 902: 45, 904: 1, 905: 9, 906: 15, 903: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 5, 902: 7, 906: 13, 903: 0, 904: 0, 905: 0, 907: 0, 908: 0, 999: 0}}}, '30-04-2022': {'ocr': {1.0: {901: 103, 902: 45, 903: 5, 905: 37, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 16, 902: 21, 903: 1, 904: 0, 905: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 23, 902: 3, 905: 13, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 67, 902: 86, 905: 50, 906: 29, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 19, 902: 33, 905: 9, 906: 16, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 13, 902: 12, 905: 4, 906: 11, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '01-05-2022': {'ocr': {1.0: {901: 160, 902: 79, 903: 6, 905: 57, 999: 1, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 18, 902: 47, 903: 2, 905: 5, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 23, 902: 7, 903: 1, 905: 10, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 101, 902: 128, 903: 4, 904: 1, 905: 94, 906: 46, 907: 0, 908: 0, 999: 0}, 2.0: {901: 35, 902: 63, 903: 2, 904: 3, 905: 27, 906: 23, 907: 0, 908: 0, 999: 0}, 3.0: {901: 16, 902: 5, 905: 4, 906: 18, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '02-05-2022': {'ocr': {1.0: {901: 75, 902: 25, 903: 4, 905: 28, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 12, 902: 20, 903: 1, 905: 1, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 10, 902: 8, 905: 3, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 37, 902: 65, 903: 1, 904: 1, 905: 40, 906: 26, 907: 0, 908: 0, 999: 0}, 2.0: {901: 11, 902: 26, 905: 9, 906: 13, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 12, 902: 7, 905: 3, 906: 10, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '03-05-2022': {'ocr': {1.0: {901: 92, 902: 45, 905: 34, 999: 1, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0}, 2.0: {901: 11, 902: 74, 903: 1, 905: 6, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 18, 902: 12, 905: 4, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 50, 902: 83, 905: 46, 906: 34, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 22, 902: 67, 903: 3, 904: 1, 905: 22, 906: 22, 907: 0, 908: 0, 999: 0}, 3.0: {901: 13, 902: 25, 903: 1, 904: 1, 905: 4, 906: 19, 907: 0, 908: 0, 999: 0}}}, '04-05-2022': {'ocr': {1.0: {901: 74, 902: 25, 903: 3, 905: 29, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 8, 902: 16, 905: 1, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 15, 902: 4, 903: 1, 905: 8, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 36, 902: 63, 903: 1, 905: 45, 906: 23, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 6, 902: 13, 905: 5, 906: 6, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 3.0: {901: 17, 902: 17, 905: 2, 906: 11, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '05-05-2022': {'ocr': {1.0: {901: 15, 902: 5, 905: 4, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 2, 902: 7, 905: 2, 903: 0, 904: 0, 906: 0, 907: 0, 908: 0, 999: 0}}, 'icr': {1.0: {901: 7, 902: 8, 905: 8, 906: 1, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}, 2.0: {901: 3, 902: 8, 905: 2, 906: 4, 903: 0, 904: 0, 907: 0, 908: 0, 999: 0}}}, '06-05-2022': {'ocr': {}, 'icr': {}}, '07-05-2022': {'ocr': {}, 'icr': {}}, '08-05-2022': {'ocr': {}, 'icr': {}}, '09-05-2022': {'ocr': {}, 'icr': {}}, '10-05-2022': {'ocr': {}, 'icr': {}}}


# for key,value in mainDict.items():
# 	print()
# 	print(key, value)

# folderWiseFiles = {}

# def get_files_from_directory_subdirectory(dirPath):       # Remove the 0th index before/after generating csv (uncomment till files.sort())
# 	# filePaths = []
# 	mall_1 = []
# 	mall_2 = []
# 	mall_3 = []
# 	mall_4 = []
# 	mall_5 = []
# 	mall_6 = []
# 	mall_16 = []
# 	countValList1 = []
	
# 	for root, ddirectories, files in sorted(os.walk(dirPath)):
# 		c1 = 0
# 		c2 = 0
# 		c3 = 0
# 		c4 = 0
# 		c5 = 0
# 		c6 = 0
# 		c16 = 0

# 		ddirectories.sort()
# 		files.sort()

# 	# for folderName in ddirectories:
# 		# print(folderName, len(os.listdir(os.path.join(root, folderName))))
# 		for file in files:                 #uncomment
# 			file = str(file)                 #uncomment
# 			if file.startswith("01000"):    #uncomment till above print(countValList1)
# 				c1 = c1 + 1                   
# 			if file.startswith("02000"):    
# 				c2 = c2 + 1                   
# 			if file.startswith("03000"):
# 				c3 = c3 + 1
# 			if file.startswith("04000"):
# 				c4 = c4 + 1
# 			if file.startswith("05000"):
# 				c5 = c5 + 1
# 			if file.startswith("06000"):
# 				c6 = c6 + 1
# 			if file.startswith("16000"):
# 				c16 = c16 + 1
     		
# 		mall_1.append(c1)     
# 		mall_2.append(c2)     
# 		mall_3.append(c3)     
# 		mall_4.append(c4)     
# 		mall_5.append(c5)     
# 		mall_6.append(c6)     
# 		mall_16.append(c16)   

# 	print(mall_1)
# 	for countVal in mall_1:
# 		if countVal > 0:
# 			countValList1.append("1")
# 		else:
# 			countValList1.append("0")
# 	print(countValList1)
	# 	df = pd.DataFrame({   
	# 		'mall1' : mall_1,   
	# 		'mall2' : mall_2,   
	# 		'mall3' : mall_3,   
	# 		'mall4' : mall_4,   
	# 		'mall5' : mall_5,   
	# 		'mall6' : mall_6,   
	# 		'mall16': mall_16   
	# 		})
	# print(df)

		# df.to_csv("mall_wise_invoice_count.csv")      #uncomment  end here


		# for file in sorted(files):
		# 	# for extension in fileExtAllow:
			# 	if file.endswith(extension):
				# filePaths.append(os.path.join(root, file))

				# for folder, files in filePaths:
					# [i.split('\t', 1)[0] for i in filePaths]

				# filePaths.append(os.path.join(root, file))
				# for files in filePaths:


	# print(len(filePaths))
	# return filePaths
# print(get_files_from_directory_subdirectory(dirPath = '/home/kartik/OCR/icr-microservice/data/001_image/'))  #uncomment



# common_util.read_configuration()['icrParams']['labels']
# def analysis_sheet(dirPath):
# 	for root, ddirectories, files in sorted(os.walk(dirPath)):
# 		ddirectories.sort()
# 		files.sort()

# analysis_sheet(dirPath = '/home/kartik/OCR/icr-microservice/data/001_image/')


# mallsCollection = common_util.read_configuration()['icrParams']['mallsCollection']['vendorModel'](vendorModel[0])
# print(mallsCollection)



def get_vendorNames_from_mall(mallId):
	try:
		mallsCollection = common_util.read_configuration()['icrParams']['mallsCollection']		# mallsCollection = mainDict['mallsCollection']
		# print(vendorModel)

		vendorNamesArr = []
		finalVendorNames = []
		# if mallId != None:
		if mallId == 1:
		# mallIds = [1,2,3,4,5,6,16]
			# for mallId in mallIds:
			for mallCollection in mallsCollection:
				for mallKey, mallValue in mallCollection.items():
					if mallKey == 'mallid':
						if mallId == mallValue:
							vendorNamesArr = mallCollection['vendorNames']
		else:
			for mallCollection in mallsCollection:
				for mallKey, mallValue in mallCollection.items():
					vendorNamesArr =  vendorNamesArr + mallCollection['vendorNames']
		for value in vendorNamesArr:
			if value['trained'] == 1:
				finalVendorNames.append(value)

			# print(vendorNamesArr)
		return finalVendorNames
	except Exception as e:
			# common_util.error_logs(e, 'get_vendorNames_from_mall')
		raise e

def map_vendornames_and_trained(finalVendorNames):

	totalVendors = common_util.read_configuration()['icrParams']['vendorModel']
	# print("vendorModel = totalVendors: ",totalVendors)

	vendorTrainDict = {}
	for key in totalVendors.keys():
		folderName = totalVendors[key]   #foldername
		# print(folderName)
		for finalVendorName in finalVendorNames:
			if key in finalVendorName['alias']:
				if folderName in vendorTrainDict.keys():
					vendorTrainDict[folderName].append(finalVendorName)  #check for duplicates
				else:
					vendorTrainDict[folderName] = []
					vendorTrainDict[folderName].append(finalVendorName)

	return vendorTrainDict


	# print(totalVendors)
	# print("len of vendorModel: ", len(set(totalVendors)))

# def get_trained_mall_vendorNames(vendorNamesArr):
# 	try:
# 		df = pd.DataFrame(vendorNamesArr)
# 		df = df[(df['trained'] == 1)]
# 		# df = df.get('retVendorName')
# 		# df.to_csv("mall_1_trained.csv")
# 		# print(df)
# 		return df
# 	except Exception as e:
# 		# common_util.error_logs(e, 'get_trained_mall_vendorNames')
# 		raise e

def get_vendorslist_and_noofdatapoints(dirPath):       # Remove the 0th index before/after generating csv (uncomment till files.sort())

	mall_1 = []
	mall_2 = []
	mall_3 = []
	mall_4 = []
	mall_5 = []
	mall_6 = []
	mall_16 = []
	mallsList = []
	vendorModelList = []
	
	for root, ddirectories, files in sorted(os.walk(dirPath)):
		c1 = 0
		c2 = 0
		c3 = 0
		c4 = 0
		c5 = 0
		c6 = 0
		c16 = 0

		ddirectories.sort()
		if ddirectories:

			# print("printing dirList/folderNames: ", ddirectories)
			vendorModelList.append(ddirectories)
		# print(ddirectories)
		files.sort()
		# print(files)
		
	# for folderName in ddirectories:
		# print(folderName, len(os.listdir(os.path.join(root, folderName))))
		for file in files:                 #uncomment
			file = str(file)                 #uncomment
			if file.startswith("01000"):    #uncomment till above df
				c1 = c1 + 1                   
			if file.startswith("02000"):    
				c2 = c2 + 1                   
			if file.startswith("03000"):
				c3 = c3 + 1
			if file.startswith("04000"):
				c4 = c4 + 1
			if file.startswith("05000"):
				c5 = c5 + 1
			if file.startswith("06000"):
				c6 = c6 + 1
			if file.startswith("16000"):
				c16 = c16 + 1
     		
		mall_1.append(c1)     
		mall_2.append(c2)     
		mall_3.append(c3)     
		mall_4.append(c4)     
		mall_5.append(c5)     
		mall_6.append(c6)     
		mall_16.append(c16)

	mall_1 = mall_1[1:]
	mall_2 = mall_2[1:]
	mall_3 = mall_3[1:]
	mall_4 = mall_4[1:]
	mall_5 = mall_5[1:]
	mall_6 = mall_6[1:]
	mall_16 = mall_16[1:]

	mallsList.append(mall_1)
	mallsList.append(mall_2)
	mallsList.append(mall_3)
	mallsList.append(mall_4)
	mallsList.append(mall_5)
	mallsList.append(mall_6)
	mallsList.append(mall_16)

	return vendorModelList, mallsList

def get_present_and_not_present_vendors(mallsList):

	presentList = []

	for malls in mallsList:
		tempMallList = []
		tempMallList.clear()
		for countVal in malls:
			if countVal > 0:
				tempMallList.append("1")
			else:
				tempMallList.append("0")

		presentList.append(tempMallList)
		
	return presentList

# def remove_duplicates_from_vendorTrainDict(vendorTrainDict):
# 	for key in vendorTrainDict:
# 		vendorModelValue = vendorTrainDict[key]
# 		vendorTrainDict[key] = set(vendorModelValue)

# 	return vendorTrainDict


def create_dataframe(vendorTrainDict, matchingDict, mallsList):
	dfList = []

	i = 0
	for key in matchingDict:
		# print("key: ", key)
		presentValue = int(matchingDict[key])
		# print("presentValue: ", matchingDict)
		# print("mallListValue: ", matchingDict)
		if presentValue == 1 and mallsList[0][i] > 0:
			# print("inside if: ", i)
			if str(key) in vendorTrainDict:
				tempVendorNameIdList = []

				vendorModelValue = vendorTrainDict[key]
				# print("vendorModelValue: ", vendorModelValue)
				for j in range(0, len(vendorModelValue)):
					if int(vendorModelValue[j]['vendorNameId']) not in tempVendorNameIdList:
						tempVendorNameIdList.append(int(vendorModelValue[j]['vendorNameId']))

						dfList.append({'present': presentValue,
								   'vendorNameId': int(vendorModelValue[j]['vendorNameId']),
								   'retVendorName': vendorModelValue[j]['retVendorName'],
								   'alias': vendorModelValue[j]['alias'],
								   'trained': int(vendorModelValue[j]['trained']),
								   'noOfDataPoints': mallsList[0][i]
								   })
				tempVendorNameIdList.clear()

		else:
			dfList.append({'present': presentValue,
						'vendorNameId': None,
						'retVendorName': None,
						'alias': None,
						'trained': None,
						'noOfDataPoints': 0

				})

		i = i + 1
	df = pd.DataFrame(dfList)
	# df = df.drop_duplicates(subset ="retVendorName",
                     # keep = False, inplace = True)

	return df

def map_vendorname_and_present(vendorModelList, presentList):

	matchingDict = dict(zip(vendorModelList[0], presentList[0]))
	
	return matchingDict


# if __name__== "__main__":

	# vendorNames = get_vendorNames_from_mall(mallId = 1)
	# # print(vendorNames)
	# # print("len of finalVendorNames: ", len(vendorNames))


	# # trained_mall_vendors = get_trained_mall_vendorNames(vendorNames)
	# # print(trained_mall_vendors)
	# # print("len of df: ",len(trained_mall_vendors))

	# vendorModelList, mallsList = get_vendorslist_and_noofdatapoints(dirPath = '/home/kartik/OCR/icr-microservice/data/001_image/')  #uncomment
	# # print(vendorModelList)
	# # print("len of vendorModelList: ", len(vendorModelList[0]))
	# # print(" ")
	# # print(mallsList[0][3])
	# # print(type(mallsList[0][3]))
	# # print("len of mallsList: ", len(mallsList[0]))

	# presentList = get_present_and_not_present_vendors(mallsList)
	# # print(presentList)
	# # print("len of presentList: ", len(presentList[0]))

	# mapPresentVendors = map_vendorname_and_present(vendorModelList, presentList)
	# # print("matchingDict: ",mapPresentVendors)
	# # print(len(mapPresentVendors))
	# # print(type(mapPresentVendors.keys()))
	# # print("matchingDict", matchingDict)

	# vendorTrainDict = map_vendornames_and_trained(vendorNames)
	# # print("Train DIct: ",vendorTrainDict)
	# # print(len(vendorTrainDict))
	# # print(vendorTrainDict['Clinique'])
	# # print("len of final train dict: ", len(vendorTrainDict))

	# # uniqueVendorTrainDict = remove_duplicates_from_vendorTrainDict(vendorTrainDict)



	# resultDataFrame = create_dataframe(vendorTrainDict, mapPresentVendors, mallsList)
	# print(resultDataFrame)
	# df = resultDataFrame.to_csv("mall_analysis_1.csv")
	# print("vendorModelValue", vendorModelValue)


def ocr_icr_final_errorcode_matrix():

	df = pd.read_csv(r'/home/kartik/OCR/ocrIcrProdLogs/2022_06_01/ocr_icr_response_malls_123_on_date_filter.csv')
	# print(df.columns)
	
	new_df = df[['ocr.mallId', 'ocr.final_errorCode', 'icr.final_errorCode']]
	# print(new_df)

	# new_df2=new_df.groupby(['ocr.mallId','ocr.final_errorCode', 'icr.final_errorCode'])['icr.final_errorCode'].count()
	new_df2=new_df.groupby(['ocr.final_errorCode', 'icr.final_errorCode'])['icr.final_errorCode'].count()

	# print(new_df2)
	new_df2 = new_df2.unstack()
	print(new_df2)
	new_df3 = new_df2.to_csv("matrix_all.csv")

if __name__== "__main__":
	ocr_icr_final_errorcode_matrix()



2022_04_13
2022_04_20
2022_04_27
2022_05_04
2022_05_11
2022_05_18
2022_05_25
2022_06_01
2022_06_08
