# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ngrams", help="some useful description.")
args = parser.parse_args()
if args.ngrams:
    ngrams = args.ngrams

spark = SparkSession.builder.getOrCreate()

savePath = dbutils.widgets.get("savePath").toString
animal = dbutils.widgets.get("animal").toString
food = dbutils.widgets.get("food").toString
rawPath = savePath + "/raw"
bronzePath = savePath + "/bronze"
enrichedPath = savePath + "/enriched"
silverPath = savePath + "/silver"
goldPath = savePath + "/gold"