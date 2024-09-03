from flask import Flask, render_template, send_file, request, Response , jsonify , send_from_directory
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource , reqparse , request
from flask_cors import CORS
from flask_migrate import Migrate

from datetime import datetime, timedelta

import os, time
from sqlalchemy import func
import requests

from jinja2 import Template

import csv
import os
import time
from httplib2 import Http
from json import dumps
import threading



from config.config import *
from models.database import *
from models.models import *
from config.security import *
from config.validation import *


from API.Authentication.LoginAPI import *
from API.Authentication.SignupAPI import *
from API.User.Availability import *
from API.User.BookAPI import *
from API.Admin.TrainsAPI import *
from API.Authentication.AdminAPI import AdminLoginAPI, SignupAdminAPI





def method_name():
    pass


