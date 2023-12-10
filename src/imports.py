import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np
import time
import random

from multiprocessing import Pool, freeze_support, cpu_count
import os